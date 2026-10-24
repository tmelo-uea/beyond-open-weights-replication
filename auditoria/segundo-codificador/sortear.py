#!/usr/bin/env python3
"""Sorteio estratificado da subamostra para o segundo codificador (semente fixa, reproduzível)."""
import csv
import random
from pathlib import Path

SEMENTE = 20261023
AQUI = Path(__file__).resolve().parent
matriz = list(csv.DictReader(open(AQUI.parent / "matriz-abertura-v1.csv", encoding="utf-8")))
EXCLUIR = {"Amazonia-IA", "Fronteira proprietaria (GPT/Claude/Gemini)"}   # sem fonte primária / linha representativa
grupos = {
    "global": [r["modelo"] for r in matriz if r["estrato"] == "1"],
    "lusofono_latam": [r["modelo"] for r in matriz if r["estrato"] == "2" and r["modelo"] not in EXCLUIR],
    "referencia_continuidade": [r["modelo"] for r in matriz if r["estrato"] in ("3", "continuidade") and r["modelo"] not in EXCLUIR],
}
TAMANHO = {"global": 4, "lusofono_latam": 4, "referencia_continuidade": 2}
rng = random.Random(SEMENTE)
with open(AQUI / "subamostra.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["grupo", "modelo"])
    for g, ms in grupos.items():
        for m in sorted(rng.sample(sorted(ms), TAMANHO[g])):
            w.writerow([g, m])
print(open(AQUI / "subamostra.csv").read())
