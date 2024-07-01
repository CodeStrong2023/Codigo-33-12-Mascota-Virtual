class Tamagotchi:
    #FUNCION INICIALIZADORA
    #esta inicia los valores de las funciones y pide un valor para la variable de tipo String, nombre.
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.aburrimiento = 0
        self.sueno = 0
        
    #FUNCION ALIMENTAR:
    #Conciste en la variable que si hambre es mayor a cero se le restara uno de hambre
    def alimentar(self):
        if self.hambre > 0:
            self.hambre -= 1
        return f"Alimentaste a {self.nombre}. Hambre: {self.hambre}"

    #FUNCION JUGAR:
    #Conciste en la variable que si aburrimiento es mayor a cero se le restara uno de aburrimiento
    def jugar(self):
        if self.aburrimiento > 0:
            self.aburrimiento -= 1
        return f"Jugaste con {self.nombre}. Aburrimiento: {self.aburrimiento}"

    #FUNCION DORMIR:
    #Conciste en la variable que si sueno es mayor a cero se le restara uno de sueno
    def dormir(self):
        if self.sueno > 0:
            self.sueno -= 1
        return f"{self.nombre} durmió. Sueño: {self.sueno}"
    
    #FUNCION EL TIEMPO PASA
    #Agregara 1 valor a todas las variables y las mostrara 
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

    #Funcion reiniciar
    #Esta reinicia los valores de las vareables: HAMBRE, ABURRIMIENTO, SUENO en 0, para que vuelva a estar como antes 
    def reiniciar(self):
        self.hambre = 0
        self.aburrimiento = 0
        self.sueno = 0
        return f"{self.nombre} ha sido reiniciado. Hambre: {self.hambre}, Aburrimiento: {self.aburrimiento}, Sueño: {self.sueno}"
