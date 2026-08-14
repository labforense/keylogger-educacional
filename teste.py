from pynput import keyboard

def ao_pressionar(tecla):
    print(f"Tecla pressionada: {tecla}")

# Configura o listener para escutar o teclado
with keyboard.Listener(on_press=ao_pressionar) as listener:
    listener.join()