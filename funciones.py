class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.aburrimiento = 0
        self.sueno = 0

    def alimentar(self):
        if self.hambre > 0:
            self.hambre -= 1
        return f"Alimentaste a {self.nombre}. Hambre: {self.hambre}"

    def jugar(self):
        if self.aburrimiento > 0:
            self.aburrimiento -= 1
        return f"Jugaste con {self.nombre}. Aburrimiento: {self.aburrimiento}"

    def dormir(self):
        if self.sueno > 0:
            self.sueno -= 1
        return f"{self.nombre} durmió. Sueño: {self.sueno}"

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

        return f"El tiempo pasa... Hambre: {self.hambre}, Aburrimiento: {self.aburrimiento}, Sueño: {self.sueno}"

    def reiniciar(self):
        self.hambre = 0
        self.aburrimiento = 0
        self.sueno = 0
        return f"{self.nombre} ha sido reiniciado. Hambre: {self.hambre}, Aburrimiento: {self.aburrimiento}, Sueño: {self.sueno}"
