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
        if self.sueno > 0:
            self.sueno -= 1
            print(f"{self.nombre} ha dormido. sueno: {self.sueno}")
        else:
           print(f"{self.nombre} no está cansado.")

    
    def tiempo_pasa(self, accion): 
        if accion == "alimentar":
            self.hambre = max(0, self.hambre)
            self.aburrimiento = max(0, self.aburrimiento + 1)
            self.sueno = max(0, self.sueno + 1)
        elif accion == "jugar":
            self.hambre = max(0, self.hambre + 1)
            self.aburrimiento = max(0, self.aburrimiento)
            self.sueno = max(0, self.sueno + 1)
        elif accion == "dormir":
            self.hambre = max(0, self.hambre + 1)
            self.aburrimiento = max(0, self.aburrimiento + 1)
            self.sueno = max(0, self.sueno)

        print(f"El tiempo pasa... Hambre: {self.hambre}, Aburrimiento: {self.aburrimiento}, Sueño: {self.sueno}")

def main():
    nombre = input("¿Cómo se llama tu Tamagotchi? ")
    mascota = Tamagotchi(nombre)

    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Alimentar")
        print("2. Jugar")
        print("3. Dormir")
        

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mascota.alimentar()
            mascota.tiempo_pasa("alimentar")
        elif opcion == "2":
            mascota.jugar()
            mascota.tiempo_pasa("jugar")
        elif opcion == "3":
            mascota.dormir()
            mascota.tiempo_pasa("dormir")
        else:
            print("Opción no válida.")
        
        

if __name__ == "__main__":
    main()
