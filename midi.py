import pygame
import time

def main():
    # Inicializar o Pygame
    pygame.init()
    pygame.mixer.init()

    # Configurar as notas MIDI correspondentes
    notes = [
        60,  # Dó (C4)
        62,  # Ré (D4)
        64,  # Mi (E4)
        65,  # Fá (F4)
        67,  # Sol (G4)
        69,  # Lá (A4)
        71   # Si (B4)
    ]

    # Adicionar sequência reversa para tocar de volta
    notes += notes[-2::-1]

    # Inicializar o mixer MIDI
    try:
        pygame.midi.init()
        player = pygame.midi.Output(0)
        player.set_instrument(0)  # Piano por padrão
    except pygame.midi.MidiException as e:
        print(f"Erro ao inicializar MIDI: {e}")
        pygame.midi.quit()
        return

    print("Tocando notas MIDI...")

    # Tocar cada nota
    for note in notes:
        player.note_on(note, 127)  # Iniciar a nota com a máxima intensidade (127)
        time.sleep(1)  # Esperar 1 segundo
        player.note_off(note, 127)  # Parar a nota

    print("Reprodução concluída. Saindo...")

    # Encerrar o player MIDI
    player.close()
    pygame.midi.quit()

if __name__ == "__main__":
    main()

