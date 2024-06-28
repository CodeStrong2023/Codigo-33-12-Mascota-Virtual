#SE CREA CLASE - STATS EN CERO(INICIALIZACION EN CERO) - - ¿AGREGAR ALGO MAS?
class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.aburrimiento = 0
        self.sueno = 0

    def alimentar(self):
        if self.hambre > 0:
            self.hambre -= 1
            print(f"Alimentaste a {self.nombre}. Hambre: {self.hambre}")
        else:
            print(f"{self.nombre} no tiene hambre.")
            
    #Funcion para jugar con la mascota - Ezequiel Flores
    def jugar(self):
        if self.aburrimiento > 0:
            self.aburrimiento -= 1
            print(f"Jugaste con {self.nombre}. Aburrimiento: {self.aburrimiento}")
        else:
            print(f"{self.nombre} no está aburrido.")
            
    #Funcion Donde trasncurre el tiempo (Va sumando stats en 1 en 1) - Ezequiel Flores
    def tiempo_pasa(self):
        self.hambre += 1
        self.aburrimiento += 1
        self.sueno += 1
        print(f"El tiempo pasa... Hambre: {self.hambre}, Aburrimiento: {self.aburrimiento}, Sueño: {self.sueno}")
        
#Se crea un bucle que permitirá al usuario interactuar con el Tamagotchi.
#MENU INTERACTIVO EN DONDE EL USUARIO ELIGE QUE HACER
def main():
    nombre = input("¿Cómo se llama tu Tamagotchi? ")
    mascota = Tamagotchi(nombre)

    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Alimentar")
        print("2. Jugar")
        print("3. Dormir")
        print("4. Ver estado")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        # opciones del usario segun su eleccion -
        if opcion == "1":
            mascota.alimentar()
        elif opcion == "2":
            mascota.jugar()
        elif opcion == "3":
            mascota.dormir()
        elif opcion == "4":
            mascota.estado()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
            
        mascota.tiempo_pasa()      #Funcion donde pasa el tiempo

        # HASTA AQUI REALICE FUNCIONES DE MENU - ELECCION DE USUARIO
        # STATS - Y FUNCION ALIMENTAR - (JESSICA PAGANO)

if __name__ == "__main__":
    main()

# FUNCION PARA ALIMENTAR - - HACER DEMAS FUNCIONES - - FIJARSE LOS NOMBRES DE LOS STATS
# PARA CONTINUAR CON LAS DEMAS FUNCIONES
# ¿CAMBIAR ALGO MAS?