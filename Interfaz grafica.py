import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CORAL_RED = (255, 64, 64)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
LIGHT_CYAN_SOFT = (176, 224, 230)
SLATE_GRAY = (112, 128, 144)


# Configurar la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piedra, Papel, Tijera, Spoke, Lizard")


# Fuente
font = pygame.font.Font(None, 36)

# Opciones del juego
opciones = ["piedra", "papel", "tijera", "spoke", "lizard"]

def obtener_eleccion_computadora():
    return random.choice(opciones)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel") or \
         (usuario == "piedra" and computadora == "lizard") or \
         (usuario == "lizard" and computadora == "spoke") or \
         (usuario == "spoke" and computadora == "tijera") or \
         (usuario == "tijera" and computadora == "lizard") or \
         (usuario == "lizard" and computadora == "papel") or \
         (usuario == "papel" and computadora == "spoke") or \
         (usuario == "spoke" and computadora == "piedra"):
        return "Ganaste"
    else:
        return "Perdiste"

def mostrar_texto(texto, x, y, color=SLATE_GRAY):
    render = font.render(texto, True, color)
    screen.blit(render, (x, y))


def main():
    running = True
    eleccion_usuario = None
    eleccion_computadora = None
    resultado = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    eleccion_usuario = "piedra"
                elif event.key == pygame.K_2:
                    eleccion_usuario = "papel"
                elif event.key == pygame.K_3:
                    eleccion_usuario = "tijera"
                elif event.key == pygame.K_4:
                    eleccion_usuario = "spoke"
                elif event.key == pygame.K_5:
                    eleccion_usuario = "lizard"

                if eleccion_usuario:
                    eleccion_computadora = obtener_eleccion_computadora()
                    resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)

        # Dibujar fondo
        screen.fill(WHITE)

        # Mostrar instrucciones
        mostrar_texto("Elige una opción:", 20, 20,PURPLE)
        mostrar_texto("1: Piedra", 20, 60,SLATE_GRAY)
        mostrar_texto("2: Papel", 20, 100,SLATE_GRAY)
        mostrar_texto("3: Tijera", 20, 140,SLATE_GRAY)
        mostrar_texto("4: Spoke", 20, 180,SLATE_GRAY)
        mostrar_texto("5: Lizard", 20, 220,SLATE_GRAY)

        if eleccion_usuario and eleccion_computadora:
            mostrar_texto(f"Tú elegiste: {eleccion_usuario}", 400, 60,)
            mostrar_texto(f"La computadora eligió: {eleccion_computadora}", 400, 100,)
            mostrar_texto(f"Resultado: {resultado}", 400, 140,)

        # Actualizar la pantalla
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
