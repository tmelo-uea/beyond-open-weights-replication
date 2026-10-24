#!/usr/bin/env python3
"""Concordância entre a codificação original (matriz-abertura-v1.csv) e a do segundo codificador (coding_sheet.csv preenchida).

Uso: python3 concordancia.py coding_sheet_preenchida.csv [matriz_de_referencia.csv] [saida.md]
Saídas no terminal e em concordancia.md: kappa de Cohen (A/N/ND, ignorando a marca (i)) sobre as 130 células
D1…S1 após herança; concordância percentual por critério; concordância do veredito OSAID; base declarada (S2);
lista de divergências para discussão.
"""
import csv
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CRIT = ["L1", "L2", "D1", "D2", "D3", "C1", "C2", "C3", "P1", "P2", "R1", "R2", "S1"]
OSAID = ["L1", "L2", "D1", "C1", "C2", "C3", "P1"]   # L2 incluído no veredito (revisão de 24/10/2026)


def norm(c):
    c = (c or "").strip().upper().replace("(I)", "")
    return c if c in ("A", "N", "ND") else None


CATS = ["A", "N", "ND"]


def ac1(pares):
    """AC1 de Gwet (2008): acaso estimado pela prevalência média de cada categoria."""
    n = len(pares)
    po = sum(a == b for a, b in pares) / n
    q = len(CATS)
    pi = {k: (sum(a == k for a, _ in pares) + sum(b == k for _, b in pares)) / (2 * n) for k in CATS}
    pe = sum(p * (1 - p) for p in pi.values()) / (q - 1)
    return (po - pe) / (1 - pe)


def bootstrap(pares, f, reps=2000, semente=20261024):
    import random
    rng = random.Random(semente)
    vals = sorted(f([pares[rng.randrange(len(pares))] for _ in pares]) for _ in range(reps))
    return vals[int(0.025 * reps)], vals[int(0.975 * reps) - 1]


def kappa(pares):
    n = len(pares)
    po = sum(a == b for a, b in pares) / n
    ca, cb = Counter(a for a, _ in pares), Counter(b for _, b in pares)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2
    return po, (po - pe) / (1 - pe) if pe < 1 else 1.0


def main(caminho, matriz=AQUI.parent / "matriz-abertura-v1.csv", saida=AQUI / "concordancia.md"):
    orig = {r["modelo"]: r for r in csv.DictReader(open(matriz, encoding="utf-8"))}
    seg = list(csv.DictReader(open(caminho, encoding="utf-8")))
    pares, por_crit, diverg, faltando = [], {c: [] for c in CRIT}, [], []
    osaid2, bases = {}, []
    for r in seg:
        m, c = r["model"], r["criterion"]
        if c == "S2":
            bases.append((m, orig[m]["modelo_base"], r["code_own"]))
            continue
        b = norm(r["code_final"])
        a = norm(orig[m][c])
        if b is None:
            faltando.append((m, c, r["code_final"]))
            continue
        pares.append((a, b))
        por_crit[c].append(a == b)
        osaid2.setdefault(m, {})[c] = b
        if a != b:
            diverg.append((m, c, orig[m][c], r["code_final"], r["interpretation"], r["source_url"], r["notes"]))
    po, k = kappa(pares)
    a1 = ac1(pares)
    k_ic = bootstrap(pares, lambda x: kappa(x)[1])
    a_ic = bootstrap(pares, ac1)
    po_ic = bootstrap(pares, lambda x: kappa(x)[0])
    conf = Counter(pares)
    linhas = [f"# Concordância entre codificadores", "",
              f"Células comparadas: {len(pares)} (inválidas ou vazias: {len(faltando)})",
              f"Concordância observada: {po:.1%} (IC 95% bootstrap: {po_ic[0]:.1%}–{po_ic[1]:.1%})",
              f"Kappa de Cohen (A/N/ND): {k:.3f} (IC 95%: {k_ic[0]:.3f}–{k_ic[1]:.3f})",
              f"AC1 de Gwet: {a1:.3f} (IC 95%: {a_ic[0]:.3f}–{a_ic[1]:.3f})",
              "IC por bootstrap de células (2.000 reamostragens, semente 20261024).", "",
              "Matriz de confusão (linhas: original; colunas: segundo codificador):", "",
              "| | A | N | ND | Total |", "|---|---|---|---|---|"]
    for x in CATS:
        linhas.append(f"| {x} | " + " | ".join(str(conf[(x, y)]) for y in CATS) + f" | {sum(conf[(x, y)] for y in CATS)} |")
    linhas.append("| Total | " + " | ".join(str(sum(conf[(x, y)] for x in CATS)) for y in CATS) + f" | {len(pares)} |")
    linhas += ["", "Concordância específica por categoria (2·n_kk / (linha_k + coluna_k)):"]
    for x in CATS:
        den = sum(conf[(x, y)] for y in CATS) + sum(conf[(y, x)] for y in CATS)
        linhas.append(f"- {x}: {2 * conf[(x, x)] / den:.1%}" if den else f"- {x}: sem ocorrências")
    linhas += ["",
              "| Critério | Concordância |", "|---|---|"]
    linhas += [f"| {c} | {sum(v)}/{len(v)} |" for c, v in por_crit.items() if v]
    concord_osaid = []
    for m, cods in osaid2.items():
        v2 = all(cods.get(c) == "A" for c in OSAID)
        v1 = orig[m]["osaid"] == "atende"
        concord_osaid.append((m, v1, v2))
    linhas += ["", f"Veredito OSAID igual em {sum(v1 == v2 for _, v1, v2 in concord_osaid)}/{len(concord_osaid)} modelos:"]
    linhas += [f"- {m}: original {'atende' if v1 else 'não atende'}; segundo {'atende' if v2 else 'não atende'}" for m, v1, v2 in concord_osaid]
    linhas += ["", "Base declarada (S2):"] + [f"- {m}: original «{o}»; segundo «{s}»" for m, o, s in bases]
    linhas += ["", "## Divergências", "", "| Modelo | Critério | Original | Segundo | (i) 2º | Fonte 2º | Notas 2º |", "|---|---|---|---|---|---|---|"]
    linhas += ["| " + " | ".join(str(x).replace("|", "/") for x in d) + " |" for d in diverg]
    if faltando:
        linhas += ["", "Células sem código válido: " + "; ".join(f"{m}/{c}={v!r}" for m, c, v in faltando)]
    texto = "\n".join(linhas)
    Path(saida).write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main(*sys.argv[1:]) if len(sys.argv) > 1 else main(AQUI / "coding_sheet.csv")
