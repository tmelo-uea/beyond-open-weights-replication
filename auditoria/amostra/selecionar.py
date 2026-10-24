#!/usr/bin/env python3
"""Seleção reproduzível da amostra da auditoria.

Estrato 1 (quadro global): Epoch AI, "Notable AI models" (CSV baixado em 23/10/2026, atualização de 19/10/2026, CC BY 4.0).
  Critério: Domain contém "Language" e não contém "Robotics"; Task contém "Language modeling" ou "Chat"; "Model accessibility"
  começa com "Open weights"; publicação de 01/01/2025 até a data do snapshot; um modelo por organização (a primeira listada):
  o mais recente e, no empate, o de mais parâmetros.
Estrato 2 (propositivo, lusófono e latino-americano): todos os LLMs com pesos ou relatórios públicos identificados na
  pesquisa (verificacoes.md e evidencias/). A Epoch não tem nenhum modelo do Brasil, de Portugal ou do Chile; este estrato corrige o viés.
Estrato 3 (referência): modelos validados como abertos pela OSI (Pythia, OLMo) e os "fully open" mais citados (Apertus, SmolLM3, BLOOM).
"""
import csv
from pathlib import Path

AQUI = Path(__file__).parent
SNAPSHOT = AQUI / "epoch_notable_ai_models_2026-10-23.csv"

ESTRATO2 = ["Tucano2-0.6B-Base", "Tucano2-qwen-3.7B", "GAIA-4B", "Jurema-7B", "Soberano-1", "Sabia-4", "Sabia-7B",
            "Curio-1.1b", "Manaca-1B", "Amazonia IA (WideLabs)", "LatamGPT-70B", "AMALIA-9B", "Gervasio-8B-PTPT"]
ESTRATO3 = ["Pythia-12B", "Olmo-3-32B-Think", "Apertus-70B-2509", "SmolLM3-3B", "BLOOM-176B"]
# Continuidade com o artigo original e casos de open-washing já auditados (fora do quadro da Epoch, que não lista a Mistral
# com pesos abertos em 2025–26 nem o Muse Glimmer): reportados à parte.
CONTINUIDADE = ["Llama-3.1-70B", "Mixtral-8x22B", "Mistral-Large-3-675B", "DeepSeek-R1", "Muse-Glimmer-30B",
                "OpenEuroLLM-Prelude-9B", "Fronteira proprietaria (GPT/Claude/Gemini)"]


def estrato1():
    linhas = list(csv.DictReader(open(SNAPSHOT, encoding="utf-8")))
    sel = [x for x in linhas if x["Publication date"] >= "2025-01-01" and "Language" in x["Domain"]
           and "Robotics" not in x["Domain"] and ("Language modeling" in x["Task"] or "Chat" in x["Task"])
           and x["Model accessibility"].startswith("Open weights")]
    por_org = {}
    for x in sel:
        org = x["Organization"].split(",")[0].strip()
        chave = (x["Publication date"], float(x["Parameters"] or 0))
        atual = por_org.get(org)
        if atual is None or chave > (atual["Publication date"], float(atual["Parameters"] or 0)):
            por_org[org] = x
    return sorted(por_org.values(), key=lambda x: x["Organization"])


def main():
    e1 = estrato1()
    with open(AQUI / "amostra.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["estrato", "modelo", "organizacao", "pais", "data", "acessibilidade_epoch", "link"])
        for x in e1:
            w.writerow([1, x["Model"], x["Organization"], x["Country (of organization)"].split(",")[0],
                        x["Publication date"], x["Model accessibility"], x["Link"]])
        for m in ESTRATO2:
            w.writerow([2, m, "", "", "", "", ""])
        for m in ESTRATO3:
            w.writerow([3, m, "", "", "", "", ""])
        for m in CONTINUIDADE:
            w.writerow(["continuidade", m, "", "", "", "", ""])
    print(f"Estrato 1: {len(e1)} | Estrato 2: {len(ESTRATO2)} | Estrato 3: {len(ESTRATO3)} | continuidade: {len(CONTINUIDADE)}")
    for x in e1:
        print(f"  {x['Organization'].split(',')[0][:28]:28} {x['Model'][:42]:42} {x['Publication date']} {x['Model accessibility']}")


if __name__ == "__main__":
    main()
