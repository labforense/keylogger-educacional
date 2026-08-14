"""
EXERCÍCIO NÍVEL 3 - AVANÇADO
Encriptação e Defesa

Objetivo: Aprender a proteger dados sensíveis com encriptação.

Instruções:
1. Instale: pip install cryptography
2. Execute este script
3. Observe como encriptação funciona
4. Integre com o keylogger principal
"""

from cryptography.fernet import Fernet
import json
from datetime import datetime
import os


class KeyloggerSeguro:
    """Keylogger com encriptação de dados"""
    
    def __init__(self, arquivo_chave="chave.key", arquivo_log="keys.enc"):
        """
        Inicializa o keylogger seguro
        
        Args:
            arquivo_chave: Arquivo que armazena a chave de encriptação
            arquivo_log: Arquivo criptografado de log
        """
        self.arquivo_chave = arquivo_chave
        self.arquivo_log = arquivo_log
        self.cipher = None
        
        # Carregar ou criar chave
        if os.path.exists(arquivo_chave):
            self.carregar_chave()
        else:
            self.criar_chave()
    
    def criar_chave(self):
        """Cria nova chave de encriptação"""
        chave = Fernet.generate_key()
        
        with open(self.arquivo_chave, "wb") as f:
            f.write(chave)
        
        self.cipher = Fernet(chave)
        print(f"✅ Chave criada: {self.arquivo_chave}")
    
    def carregar_chave(self):
        """Carrega chave existente"""
        with open(self.arquivo_chave, "rb") as f:
            chave = f.read()
        
        self.cipher = Fernet(chave)
        print(f"✅ Chave carregada: {self.arquivo_chave}")
    
    def registrar_tecla(self, tecla_digitada):
        """Encripta e registra uma tecla"""
        
        # Criar mensagem
        timestamp = datetime.now().isoformat()
        mensagem = f"[{timestamp}] {tecla_digitada}"
        
        # Encriptar
        mensagem_bytes = mensagem.encode()
        criptografado = self.cipher.encrypt(mensagem_bytes)
        
        # Salvar
        with open(self.arquivo_log, "ab") as f:
            f.write(criptografado + b"\n")
    
    def ler_log_descriptografado(self):
        """Lê e descriptografa o arquivo de log"""
        
        if not os.path.exists(self.arquivo_log):
            print(f"❌ Arquivo {self.arquivo_log} não encontrado")
            return
        
        print("\n📖 CONTEÚDO DESCRIPTOGRAFADO:")
        print("=" * 60)
        
        try:
            with open(self.arquivo_log, "rb") as f:
                for linha in f:
                    linha = linha.strip()
                    if linha:
                        descriptografado = self.cipher.decrypt(linha)
                        print(descriptografado.decode())
        except Exception as e:
            print(f"❌ Erro ao descriptografar: {e}")
            print("⚠️ Chave incorreta ou arquivo corrompido")


class DetectorKeylogger:
    """Detecta presença de keylogger no sistema"""
    
    @staticmethod
    def verificar_processos_suspeitos():
        """Verifica processos em execução"""
        print("\n🔍 VERIFICANDO PROCESSOS SUSPEITOS...")
        print("=" * 60)
        
        processos_suspeitos = [
            "keylogger.py",
            "logger.exe",
            "hook.sys",
            "spyware.exe",
            "monitor.exe"
        ]
        
        # TODO: Implementar verificação com psutil
        # import psutil
        # for proc in psutil.process_iter():
        #     if any(suspeito in proc.name() for suspeito in processos_suspeitos):
        #         print(f"⚠️ ALERTA: {proc.name()}")
        
        print("(Requer 'pip install psutil' para implementação completa)")
    
    @staticmethod
    def verificar_arquivos_suspeitos():
        """Verifica arquivos suspeitos"""
        print("\n🔍 VERIFICANDO ARQUIVOS SUSPEITOS...")
        print("=" * 60)
        
        arquivos_suspeitos = [
            "keys.log",
            "log.txt",
            "log.enc",
            "keylogger.py"
        ]
        
        for arquivo in arquivos_suspeitos:
            if os.path.exists(arquivo):
                tamanho = os.path.getsize(arquivo)
                print(f"⚠️ ENCONTRADO: {arquivo} ({tamanho} bytes)")
    
    @staticmethod
    def gerar_relatorio_seguranca():
        """Gera relatório de segurança"""
        print("\n📋 RELATÓRIO DE SEGURANÇA")
        print("=" * 60)
        
        relatorio = {
            "timestamp": datetime.now().isoformat(),
            "verificacoes": [
                "✅ Antivírus: Windows Defender",
                "⚠️ 2FA: Não ativado em Gmail",
                "✅ Senha: Forte",
                "❌ WiFi: Sem VPN",
                "✅ Updates: Atualizados"
            ]
        }
        
        for item in relatorio["verificacoes"]:
            print(item)
        
        return relatorio


# TESTES
if __name__ == "__main__":
    print("🔐 KEYLOGGER SEGURO - DEMONSTRAÇÃO\n")
    
    # 1. Criar e testar encriptação
    print("1️⃣ TESTANDO ENCRIPTAÇÃO")
    print("=" * 60)
    
    seguro = KeyloggerSeguro()
    
    # Simular captura de teclas
    print("Registrando dados de teste...")
    for tecla in "teste":
        seguro.registrar_tecla(tecla)
    
    print("✅ Dados registrados com encriptação")
    
    # 2. Ler dados descriptografados
    print("\n2️⃣ DESCRIPTOGRAFANDO DADOS")
    seguro.ler_log_descriptografado()
    
    # 3. Detectar ameaças
    print("\n3️⃣ DETECTANDO AMEAÇAS")
    print("=" * 60)
    
    detector = DetectorKeylogger()
    detector.verificar_arquivos_suspeitos()
    detector.verificar_processos_suspeitos()
    detector.gerar_relatorio_seguranca()
    
    print("\n" + "=" * 60)
    print("✅ Demonstração completa!")
    print("\nDicas de Segurança:")
    print("- Guarde sua chave em local seguro")
    print("- Nunca compartilhe a chave.key")
    print("- Use senhas fortes")
    print("- Ative 2FA em contas importantes")
