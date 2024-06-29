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

    def jugar(self):
        if self.aburrimiento > 0:
            self.aburrimiento -= 1
            print(f"Jugaste con {self.nombre}. Aburrimiento: {self.aburrimiento}")
        else:
            print(f"{self.nombre} no está aburrido.")

    def dormir(self):
        if self.cansancio > 0:
            self.cansancio -= 1
            print(f"{self.nombre} ha dormido. Cansancio: {self.cansancio}")
        else:
           print(f"{self.nombre} no está cansado.")

    def tiempo_pasa(self):
        self.hambre += 1
        self.aburrimiento += 1
        self.sueno += 1
        print(f"El tiempo pasa... Hambre: {self.hambre}, Aburrimiento: {self.aburrimiento}, Sueño: {self.sueno}")

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

        mascota.tiempo_pasa()

if __name__ == "__main__":
    main()
