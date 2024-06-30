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
            print(f"{self.nombre} durmió. Sueño: {self.sueno}")
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
