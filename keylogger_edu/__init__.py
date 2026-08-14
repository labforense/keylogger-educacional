"""
KeyLogger Educational Library
============================

Biblioteca educacional para aprendizado de segurança ofensiva.
Contém modelos, ferramentas e exemplos didáticos.

Uso básico:
    from keylogger_edu import KeyLogger
    
    logger = KeyLogger()
    logger.start()
"""

__version__ = "1.0.0"
__author__ = "Educational Team"
__license__ = "CC BY-SA 4.0"

from .core import KeyLogger
from .analyzer import LogAnalyzer
from .security import SecureKeyLogger, EncryptionManager
from .detector import ThreatDetector

__all__ = [
    'KeyLogger',
    'LogAnalyzer',
    'SecureKeyLogger',
    'EncryptionManager',
    'ThreatDetector'
]
