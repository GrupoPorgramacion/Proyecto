import random

def obtener_eleccion_usuario():
    eleccion = input("Elige una opción (piedra, papel, tijera, spoke, lizard): ").lower()
    while eleccion not in ["piedra", "papel", "tijera","spoke","lizard"]:
        eleccion = input("Opción no válida. Elige piedra, papel, tijera, spoke, lizard: ").lower()
    return eleccion

def obtener_eleccion_computadora():
    opciones = ["piedra", "papel", "tijera","spoke","lizard"]
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

def jugar():
    usuario = obtener_eleccion_usuario()
    computadora = obtener_eleccion_computadora()
    
    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")
    
    resultado = determinar_ganador(usuario, computadora)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    jugar()