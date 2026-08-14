"""
Módulo Detector - Detecção de keyloggers e ameaças

Classes:
    ThreatDetector: Detecta ameaças no sistema
"""

from typing import List, Dict
import os


class ThreatDetector:
    """
    Detecta presença de keyloggers e ameaças.
    
    Example:
        >>> detector = ThreatDetector()
        >>> detector.scan_system()
    """
    
    def __init__(self):
        """Inicializa o detector."""
        self.threats = []
        self.warnings = []
    
    def check_suspicious_files(self) -> List[str]:
        """
        Verifica arquivos suspeitos.
        
        Returns:
            Lista de arquivos encontrados
        """
        suspicious = [
            "keys.log", "log.txt", "log.enc",
            "keylogger.py", "chave.key",
            "monitor.exe", "hook.sys"
        ]
        
        found = []
        for arquivo in suspicious:
            if os.path.exists(arquivo):
                found.append(arquivo)
                self.threats.append(f"Arquivo suspeito: {arquivo}")
        
        return found
    
    def check_network_connections(self) -> Dict[str, str]:
        """
        Verifica conexões de rede suspeitas.
        
        Returns:
            Dicionário com conexões
        """
        # TODO: Implementar com psutil
        suspicious_ips = {}
        return suspicious_ips
    
    def check_processes(self) -> List[str]:
        """
        Verifica processos suspeitos.
        
        Returns:
            Lista de processos
        """
        # TODO: Implementar com psutil
        suspicious_processes = []
        return suspicious_processes
    
    def scan_system(self) -> Dict:
        """
        Faz varredura completa do sistema.
        
        Returns:
            Dicionário com resultados
        """
        return {
            "suspicious_files": self.check_suspicious_files(),
            "suspicious_processes": self.check_processes(),
            "network_connections": self.check_network_connections(),
            "threats_found": len(self.threats) > 0,
            "threat_count": len(self.threats)
        }
    
    def print_scan_report(self) -> None:
        """Imprime relatório de varredura."""
        print("\n" + "="*60)
        print("🔍 RELATÓRIO DE VARREDURA DO SISTEMA")
        print("="*60)
        
        suspicious_files = self.check_suspicious_files()
        
        if suspicious_files:
            print(f"\n⚠️ ARQUIVOS SUSPEITOS ENCONTRADOS:")
            for arquivo in suspicious_files:
                print(f"  🚨 {arquivo}")
        else:
            print(f"\n✅ Nenhum arquivo suspeito encontrado")
        
        if self.threats:
            print(f"\n⚠️ AMEAÇAS DETECTADAS ({len(self.threats)}):")
            for threat in self.threats:
                print(f"  🚨 {threat}")
        else:
            print(f"\n✅ Nenhuma ameaça detectada")
        
        print("\n" + "="*60)
