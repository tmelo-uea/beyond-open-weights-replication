#!/usr/bin/env python3
"""Triagem dos contratos retornados pelas buscas no PNCP (protocolo em verificacoes.md V16–V18).

Fontes: (1) busca de 22/10/2026 — 8 consultas, 40 resultados mais recentes de cada, 82 contratos únicos, triados um a um
(índices abaixo); (2) consulta completa de "inteligência artificial generativa" em 24/10/2026 (226 resultados), da qual
entram os publicados até 22/10/2026 que não estavam em (1): 178 contratos, triados por regra escrita (abaixo) com
exceções lidas no texto integral.

Categorias (critério pelo objeto contratual, lido no texto integral da ficha do PNCP):
  BRK     intermediação (corretagem) de nuvens comerciais para IA/LLM — capacidade de LLM em nível de API/infraestrutura
  API     créditos diretos em nuvem estrangeira para IA/LLM (via revendedor)
  NAT-S   infraestrutura nacional de GPU em escala de servidor (on-premise ou data center no Brasil)
  NAT-W   GPU em escala de estação de trabalho (placas, workstations, notebooks)
  NAT-API API de LLM de fornecedor brasileiro
  SUITE   suíte de produtividade/colaboração com IA generativa como funcionalidade (valor não atribuível à IA)
  API-IND acesso a API de IA generativa por revendedor, sem provedor identificado
  SAAS    assinatura de aplicação de IA generativa (por usuário ou plataforma), inclusive suítes de produtividade com IA
  FORA    fora do escopo: capacitação, chatbot/omnichannel, projeto de pesquisa via fundação, segurança, outros serviços
Escopo da afirmação do artigo: BRK + API + NAT-S + NAT-API + API-IND (provisão de capacidade de LLM em nível de API ou infraestrutura).
Regra para a consulta completa: licença/assinatura/subscrição/SaaS/software/plataforma → SAAS; capacitação, eventos,
consultoria e demais → FORA; exceções lidas: Maritaca AI (NAT-API), HYTI/TSE (BRK, broker privado do Google Cloud com
plataforma de IA generativa), Município de Faina (API-IND).

Uso: python3 triagem.py → triagem_pncp.csv e resumo impresso
"""
import csv
import json
from pathlib import Path

AQUI = Path(__file__).parent
CAT = {}
for i in [1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13]: CAT[i] = "BRK"
for i in [56, 58, 59, 64, 67, 74]: CAT[i] = "API"
for i in [75, 77, 78]: CAT[i] = "NAT-S"
for i in [76, 79, 80, 81]: CAT[i] = "NAT-W"
for i in [14, 17, 18, 20, 21, 22, 23, 24, 27, 28, 30, 31, 32, 35, 36, 37, 38, 39, 40, 41, 42, 43, 46, 47, 48, 49, 50, 52,
          54, 55, 60, 61, 62, 63]: CAT[i] = "SAAS"
for i in [0, 2, 8, 15, 16, 19, 25, 26, 29, 33, 34, 44, 45, 51, 53, 57, 65, 66, 68, 69, 70, 71, 72, 73]: CAT[i] = "FORA"


def regra(v):
    import re
    f = (v.get("fornecedor_nome") or "").upper()
    o = (v.get("orgao_nome") or "").upper()
    t = (v.get("description") or "").lower()
    if "MARITACA" in f:
        return "NAT-API"
    if "HYTI" in f:
        return "BRK"
    if "FAINA" in o:
        return "API-IND"
    if re.search(r"curso|capacita|palestra|workshop|inscri|semin|evento|docên|docen|instrutor|oficina|congresso|forma[çc][ãa]o|encor|mentoria|consultoria", t) \
            and not re.search(r"licen[çc]|assinatura|subscri", t):
        return "FORA"
    if re.search(r"licen[çc]|assinatura|subscri|saas|software|plataforma|solu[çc][ãa]o tecnol", t):
        return "SAAS"
    return "FORA"


def main():
    itens = list(json.load(open(AQUI / "pncp_busca_2026-10-22.json", encoding="utf-8")).values())
    assert len(itens) == 82 and set(CAT) == set(range(82)), "triagem incompleta"
    vistos = {v["item_url"] for v in itens}
    completa = json.load(open(AQUI / "pncp_genai_completa_2026-10-24.json", encoding="utf-8"))
    extras = [v for v in completa if (v.get("data_publicacao_pncp") or "")[:10] <= "2026-10-22" and v["item_url"] not in vistos]
    origem = ["busca 22/10 (top 40 por consulta)"] * len(itens) + ["consulta completa 24/10 (corte 22/10)"] * len(extras)
    cats = [CAT[i] for i in range(len(itens))] + [regra(v) for v in extras]
    import re
    suite = re.compile(r"produtividade|office|microsoft 365|workspace|colabora[çc][ãa]o|correio eletr[ôo]nico|e-mail")
    nao_suite = re.compile(r"plataforma corporativa de intelig[êe]ncia artificial generativa|copilot|intelig[êe]ncia artificial generativa para o microsoft 365|relacionamento do setor p[úu]blico")
    bot = re.compile(r"contact center|chatbot|voicebot")
    novas = []
    for c, v in zip(cats, itens + extras):
        t = (v.get("description") or "").lower()
        if c == "SAAS" and bot.search(t):
            c = "FORA"
        elif c == "SAAS" and suite.search(t) and not nao_suite.search(t):
            c = "SUITE"
        novas.append(c)
    cats = novas
    linhas = []
    for i, v in enumerate(itens + extras):
        linhas.append(dict(n=i, origem=origem[i], categoria=cats[i], orgao=v.get("orgao_nome"), uf=v.get("uf"), fornecedor=v.get("fornecedor_nome"),
                           valor_global=v.get("valor_global"), data_assinatura=(v.get("data_assinatura") or "")[:10],
                           pncp=v.get("numero_controle_pncp"), url="https://pncp.gov.br/app" + v.get("item_url", ""),
                           objeto=(v.get("description") or "").replace("\n", " ").strip()))
    with open(AQUI / "triagem_pncp.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=linhas[0].keys())
        w.writeheader()
        w.writerows(linhas)
    print(f"{len(linhas)} contratos ({len(itens)} + {len(extras)})")
    for c in ["BRK", "API", "API-IND", "NAT-S", "NAT-API", "NAT-W", "SAAS", "SUITE", "FORA"]:
        g = [l for l in linhas if l["categoria"] == c]
        print(f"{c:6} n={len(g):2}  valor R$ {sum(float(l['valor_global'] or 0) for l in g):>14,.2f}")


if __name__ == "__main__":
    main()
