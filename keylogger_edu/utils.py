"""
Módulo Utils - Funções auxiliares

Funções:
    setup_logging: Configura logging
    load_config: Carrega configuração
"""

import logging
import json
from datetime import datetime
from typing import Dict, Any


def setup_logging(
    log_file: str = "keylogger_edu.log",
    level: int = logging.INFO
) -> logging.Logger:
    """
    Configura logging da biblioteca.
    
    Args:
        log_file: Arquivo de log
        level: Nível de logging
        
    Returns:
        Logger configurado
    """
    logger = logging.getLogger("keylogger_edu")
    
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    
    return logger


def load_config(config_file: str = "config.json") -> Dict[str, Any]:
    """
    Carrega configuração de arquivo JSON.
    
    Args:
        config_file: Arquivo de configuração
        
    Returns:
        Dicionário com configurações
    """
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_config(config: Dict[str, Any], config_file: str = "config.json") -> None:
    """
    Salva configuração em arquivo JSON.
    
    Args:
        config: Dicionário de configuração
        config_file: Arquivo de saída
    """
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)


def format_timestamp(dt: datetime = None, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Formata timestamp.
    
    Args:
        dt: Objeto datetime (padrão: agora)
        fmt: Formato de saída
        
    Returns:
        String formatada
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime(fmt)


def get_default_config() -> Dict[str, Any]:
    """
    Retorna configuração padrão.
    
    Returns:
        Dicionário com valores padrão
    """
    return {
        "log_file": "keys.log",
        "stop_key": "esc",
        "ignore_keys": [
            "shift",
            "shift_r",
            "ctrl_l",
            "ctrl_r",
            "alt_l",
            "alt_r",
            "caps_lock",
            "cmd"
        ],
        "encrypt_data": False,
        "key_file": "chave.key",
        "auto_upload": False
    }
