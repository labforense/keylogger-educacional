"""
Exemplo 1: Uso básico do keylogger
"""

from keylogger_edu import KeyLogger

if __name__ == "__main__":
    # Criar keylogger simples
    logger = KeyLogger(
        log_file="exemplo1_basico.log",
        stop_key=__import__('pynput').keyboard.Key.esc
    )
    
    # Iniciar captura
    logger.start()
