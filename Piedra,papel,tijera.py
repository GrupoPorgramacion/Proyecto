import random

def obtener_eleccion_usuario():
    eleccion = input("Elige una opcion (piedra, papel, tijera): ").lower()
    while eleccion not in ["piedra", "papel", "tijera"]:
        eleccion = input("Opcion no valida. Elige piedra, papel o tijera: ").lower()
    return eleccion

def obtener_eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    usuario = obtener_eleccion_usuario()
    computadora = obtener_eleccion_computadora()
    
    print(f"Tu elegiste: {usuario}")
    print(f"La computadora eligio: {computadora}")
    
    resultado = determinar_ganador(usuario, computadora)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    jugar()