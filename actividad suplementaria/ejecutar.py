from coliseo import ColiseoDeportivo

def iniciar_programa():
    lista_coliseos = []
    print("--- SISTEMA DE GESTION DE COLISEOS ---")
    
    while True:
        print("\nIngrese datos del Coliseo:")
        nom = input("Nombre: ")
        ciu = input("Ciudad: ")
        cap = input("Capacidad: ")
        dep = input("Deporte: ")
        
        obj = ColiseoDeportivo(nom, ciu, cap, dep)
        lista_coliseos.append(obj)
        
        if input("¿Agregar otro? (s/n): ").lower() != 's':
            break

    print("\n--- LISTA FINAL ---")
    for c in lista_coliseos:
        print(c)

if __name__ == "__main__":
    iniciar_programa()
    