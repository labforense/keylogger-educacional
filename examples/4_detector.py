"""
Exemplo 4: Detecção de ameaças e keyloggers
"""

from keylogger_edu import ThreatDetector

if __name__ == "__main__":
    print("🔍 DETECÇÃO DE AMEAÇAS\n")
    
    # Criar detector
    detector = ThreatDetector()
    
    # Fazer varredura
    print("Fazendo varredura do sistema...\n")
    resultado = detector.scan_system()
    
    # Imprimir relatório
    detector.print_scan_report()
    
    # Exportar relatório de segurança
    detector.export_security_report("exemplo4_seguranca.json")
    
    print("\n✅ Análise concluída!")
