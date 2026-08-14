"""
Exemplo 5: Integração completa da biblioteca
"""

from keylogger_edu import (
    KeyLogger,
    LogAnalyzer,
    SecureKeyLogger,
    ThreatDetector
)

if __name__ == "__main__":
    print("="*60)
    print("🎓 EXEMPLO COMPLETO - KEYLOGGER EDU")
    print("="*60)
    
    # 1. Capturar dados
    print("\n1️⃣ CAPTURA DE DADOS")
    print("-"*60)
    logger = KeyLogger(log_file="exemplo5_dados.log")
    print("Execute: logger.start()")
    print("(Comentado para não interromper o script)")
    # logger.start()
    
    # 2. Analisar dados (se existirem)
    print("\n2️⃣ ANÁLISE DE DADOS")
    print("-"*60)
    try:
        analyzer = LogAnalyzer("keys.log")
        analyzer.print_summary()
    except FileNotFoundError:
        print("❌ Arquivo keys.log não encontrado")
        print("Execute o exemplo 1_basico.py primeiro")
    
    # 3. Detectar ameaças
    print("\n3️⃣ DETECÇÃO DE AMEAÇAS")
    print("-"*60)
    detector = ThreatDetector()
    detector.print_scan_report()
    
    # 4. Resumo de segurança
    print("\n4️⃣ CHECKLIST DE SEGURANÇA")
    print("-"*60)
    checklist = detector.generate_security_checklist()
    print("Análise de segurança:")
    for check, status in checklist['checks'].items():
        print(f"  • {check}: {status}")
    
    print("\n" + "="*60)
    print("✅ Exemplo completo concluído!")
    print("="*60)
