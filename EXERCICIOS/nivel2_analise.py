"""
EXERCÍCIO NÍVEL 2 - INTERMEDIÁRIO
Análise de Dados - Encontrar Padrões

Objetivo: Aprender a analisar dados capturados.

Instruções:
1. Execute o keylogger normal e gere um keys.log
2. Use este script para analisar os dados
3. Identifique as teclas mais frequentes
"""

from collections import Counter
import json
from datetime import datetime


def analisar_arquivo_log(arquivo="keys.log"):
    """Analisa o arquivo de log e encontra padrões"""
    
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
    except FileNotFoundError:
        print(f"❌ Arquivo {arquivo} não encontrado")
        return
    
    # TODO: Implemente as análises abaixo:
    
    # 1. Téclas mais frequentes
    print("\n📊 ANÁLISE DE TECLAS")
    print("=" * 50)
    
    # Contar caracteres
    counter = Counter(conteudo)
    print("\nTeclas mais digitadas:")
    for tecla, freq in counter.most_common(10):
        if tecla != '\n':
            print(f"  '{tecla}': {freq}x")
    
    # 2. Estatísticas gerais
    print(f"\n📈 ESTATÍSTICAS")
    print("=" * 50)
    print(f"Total de caracteres: {len(conteudo)}")
    print(f"Linhas: {conteudo.count(chr(10))}")
    print(f"Espaços: {conteudo.count(' ')}")
    
    # 3. Detectar padrões suspeitos
    print(f"\n⚠️ DETECÇÃO DE PADRÕES")
    print("=" * 50)
    
    palavras_suspeitas = ["password", "senha", "pin", "admin", "login"]
    
    for palavra in palavras_suspeitas:
        if palavra.lower() in conteudo.lower():
            print(f"⚠️ Palavra suspeita encontrada: '{palavra}'")
    
    # 4. Salvar relatório em JSON
    relatorio = {
        "timestamp": datetime.now().isoformat(),
        "arquivo_analisado": arquivo,
        "total_caracteres": len(conteudo),
        "teclas_top_10": dict(counter.most_common(10)),
        "linhas": conteudo.count('\n'),
        "espacos": conteudo.count(' ')
    }
    
    with open("relatorio.json", "w") as f:
        json.dump(relatorio, f, indent=2, default=str)
    
    print(f"\n✅ Relatório salvo em relatorio.json")


if __name__ == "__main__":
    analisar_arquivo_log()


# DESAFIOS EXTRAS:
# 1. Encontre a palavra mais longa digitada
# 2. Calcule WPM (palavras por minuto)
# 3. Identifique padrões de URLs digitadas
# 4. Salve o relatório em diferentes formatos (CSV, Excel)
