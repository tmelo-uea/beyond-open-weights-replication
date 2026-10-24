#!/usr/bin/env python3
"""Perfil de carga medido nos traces públicos de inferência de LLMs da Azure (CC-BY).

Fontes:
  2023: Patel et al., "Splitwise", ISCA 2024 — AzureLLMInferenceTrace_{conv,code}.csv (~1 h)
  2024: Stojkovic et al., "DynamoLLM", HPCA 2025 — AzureLLMInferenceTrace_{conv,code}_1week.csv

Para cada arquivo, calcula:
  - fração de tokens de entrada (contexto) no total
  - médias de tokens de contexto e gerados por requisição
  - fator de pico: maior volume horário de tokens / volume horário médio
    (só faz sentido no trace de 1 semana, que cobre o ciclo diário)

Uso: python3 traces.py ARQUIVO.csv [ARQUIVO.csv ...] > dados/perfil_carga.json
"""
import csv
import json
import sys
from collections import Counter


def perfil(caminho):
    ctx = gen = n = 0
    por_hora = Counter()
    for linha in csv.DictReader(open(caminho, newline="")):
        c, g = int(linha["ContextTokens"]), int(linha["GeneratedTokens"])
        ctx += c
        gen += g
        n += 1
        por_hora[linha["TIMESTAMP"][:13]] += c + g  # "AAAA-MM-DD HH"
    horas = sorted(por_hora)
    # descarta a primeira e a última hora, que podem estar incompletas
    completas = [por_hora[h] for h in horas[1:-1]] or list(por_hora.values())
    media = sum(completas) / len(completas)
    return {
        "arquivo": caminho.rsplit("/", 1)[-1],
        "requisicoes": n,
        "primeira_hora": horas[0],
        "ultima_hora": horas[-1],
        "horas_completas": len(completas),
        "fracao_entrada": ctx / (ctx + gen),
        "media_tokens_contexto": ctx / n,
        "media_tokens_gerados": gen / n,
        "fator_pico_horario": max(completas) / media,
    }


if __name__ == "__main__":
    print(json.dumps([perfil(a) for a in sys.argv[1:]], indent=2, ensure_ascii=False))
