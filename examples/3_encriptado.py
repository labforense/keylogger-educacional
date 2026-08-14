"""
Exemplo 3: Keylogger com encriptação de dados
"""

from keylogger_edu import SecureKeyLogger, EncryptionManager

if __name__ == "__main__":
    print("🔐 KEYLOGGER COM ENCRIPTAÇÃO\n")
    
    # Criar keylogger seguro
    secure_logger = SecureKeyLogger(
        log_file="exemplo3_encriptado.enc",
        key_file="exemplo3_chave.key"
    )
    
    # Simular digitação de dados
    print("Registrando dados (simulado)...")
    for char in "teste123":
        secure_logger.register_key(char)
    
    print("✅ Dados encriptados e salvos")
    
    # Ler dados encriptados
    print("\n📖 Lendo dados encriptados:")
    secure_logger.read_log()
    
    # Mostrar estatísticas
    stats = secure_logger.get_statistics()
    print(f"\n📊 Estatísticas:")
    print(f"  Arquivo: {stats['log_file']}")
    print(f"  Teclas registradas: {stats['key_count']}")
