"""
Exemplo 2: Análise de dados capturados
"""

from keylogger_edu import LogAnalyzer

if __name__ == "__main__":
    # Analisar arquivo de log existente
    try:
        analyzer = LogAnalyzer("keys.log")
        
        # Imprimir resumo
        analyzer.print_summary()
        
        # Exportar relatório
        analyzer.export_report("exemplo2_relatorio.json")
        
    except FileNotFoundError as e:
        print(f"❌ Erro: {e}")
        print("Execute primeiro o exemplo 1_basico.py para gerar um log")
