#La clase Tamagotchi es la representación básica de una mascota virtual.
#Estos atributos se inician en cero y representan el estado de la mascota en cuanto a su necesidad de comer, jugar o dormir. 
class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.aburrimiento = 0
        self.sueno = 0
        
# 1- Definición de la función main():
#Aqui se pide al usuario que introduzca el nombre de su Tamagotchi y Se crea un objeto Tamagotchi con ese nombre.
def main():
    nombre = input("¿Cómo se llama tu Tamagotchi? ")
    mascota = Tamagotchi(nombre)

#2- Bucle while infinito que presenta un menú de opciones al usuario, las Opciones disponibles son:
#Alimentar
#Jugar
#Dormir 
#Selección de opción:
#En donde el usuario elige una opción ingresando un número. Según la opción elegida, se llama a un método correspondiente del objeto MASCOTA(alimentar, jugar, dormir).
#Después de cada acción, se llama al método "tiempo_pasa" con el argumento de la acción realizada para actualizar el estado del Tamagotchi.

    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Alimentar")
        print("2. Jugar")
        print("3. Dormir")
        
#Aqui la Validación de la opción:
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
#Si la opción no es válida, se muestra un mensaje de error.
        else:
            print("Opción no válida.")

#3- Ejecución del programa: Donde se asegura que la función main() se ejecute solo si el script se ejecuta directamente.
if __name__ == "__main__":
    main()
