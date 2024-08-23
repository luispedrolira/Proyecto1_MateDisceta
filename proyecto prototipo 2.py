def mostrar_menu():
    print("\nMenúuuuuu Principal")
    print("1. Construir conjuntos")
    print("2. Operar conjuntos")
    print("3. Finalizar")
    opcion = input("Elige una opción: ")
    return opcion

def validar_elemento(elemento):
    return elemento.isalnum() and len(elemento) == 1

def construir_conjunto():
    conjuntos = []
    cantidad = int(input("¿Cuántos conjuntos deseas ingresar? "))
    
    for i in range(cantidad):
        conjunto = set()
        elementos = input(f"Ingresa los elementos del conjunto {i+1} separados por comas: ").upper().split(',')
        
        for elemento in elementos:
            elemento = elemento.strip()  # Elimina espacios en blanco alrededor del elemento
            if validar_elemento(elemento):
                conjunto.add(elemento)
            else:
                print(f"'{elemento}' no es un elemento válido y no se agregará.")
        
        conjuntos.append(conjunto)
        print(f"Conjunto {i+1} construido: {conjunto}")
    
    return conjuntos

def seleccionar_conjuntos(conjuntos):
    if len(conjuntos) < 2:
        print("Necesitas al menos dos conjuntos para operar.")
        return None, None
    
    print("\nConjuntos disponibles:")
    for idx, conjunto in enumerate(conjuntos):
        print(f"{idx+1}. {conjunto}")
    
    indice1 = int(input("Selecciona el número del primer conjunto: ")) - 1
    indice2 = int(input("Selecciona el número del segundo conjunto: ")) - 1
    
    if 0 <= indice1 < len(conjuntos) and 0 <= indice2 < len(conjuntos):
        return conjuntos[indice1], conjuntos[indice2]
    else:
        print("Selección inválida.")
        return None, None

def complemento(conjunto, universo):
    return universo - conjunto

def union(conjunto1, conjunto2):
    return conjunto1 | conjunto2

def interseccion(conjunto1, conjunto2):
    return conjunto1 & conjunto2

def diferencia(conjunto1, conjunto2):
    return conjunto1 - conjunto2

def diferencia_simetrica(conjunto1, conjunto2):
    return conjunto1 ^ conjunto2

def operar_conjuntos(conjunto1, conjunto2, universo):
    print("\nOperaciones disponibles:")
    print("1. Complemento del primer conjunto")
    print("2. Unión")
    print("3. Intersección")
    print("4. Diferencia (conjunto1 - conjunto2)")
    print("5. Diferencia Simétrica")
    operacion = input("Elige una operación: ")

    if operacion == "1":
        print(f"Complemento de conjunto1: {complemento(conjunto1, universo)}")
    elif operacion == "2":
        print(f"Unión: {union(conjunto1, conjunto2)}")
    elif operacion == "3":
        print(f"Intersección: {interseccion(conjunto1, conjunto2)}")
    elif operacion == "4":
        print(f"Diferencia (conjunto1 - conjunto2): {diferencia(conjunto1, conjunto2)}")
    elif operacion == "5":
        print(f"Diferencia Simétrica: {diferencia_simetrica(conjunto1, conjunto2)}")
    else:
        print("Operación no válida. Por favor, elige una opción correcta.")

def main():
    universo = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    conjuntos = []
    
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            nuevos_conjuntos = construir_conjunto()
            conjuntos.extend(nuevos_conjuntos)
        elif opcion == "2":
            if len(conjuntos) < 2:
                print("Debes construir al menos dos conjuntos antes de operar.")
            else:
                conjunto1, conjunto2 = seleccionar_conjuntos(conjuntos)
                if conjunto1 and conjunto2:
                    operar_conjuntos(conjunto1, conjunto2, universo)
        elif opcion == "3":
            print("Finalizando programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

if __name__ == "__main__":
    main()
