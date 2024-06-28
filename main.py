import flet as ft
import asyncio
import aiohttp

async def main(page: ft.Page):
    
    # Variable para controlar si se muestra o no el botón EMPEZAR
    show_button = True
    
    # Variable para rastrear si el botón EMPEZAR fue presionado
    button_pressed = False
    
    # Variable para rastrear si el botón REINICIO fue presionado
    buttonpressed = False
    
    #funcion para cerrar la pag 
    def close_page(e):
        page.clean()
        page.go("/")
        
    #Funcion de ejemplo pata mostrar el ID de los botones seleccionados
    def on__click(e):
        print(f"Botón con ID {e.control.data} presionado")
        
    def on_reinicio(e):
        nonlocal buttonpressed
        print(f"Botón con ID {e.control.data} presionado")
        buttonpressed = True
        #volver_inicio(page) <-- Funcion para volver todo a los valores predeterminados ya la pag principal
    
    #Funcion para el boton del comienzo
    def on_button_click(e):
        nonlocal show_button
        nonlocal button_pressed
            
        print(f"Botón con ID {e.control.data} presionado")
        show_button = False
        button.visible = False
        button_pressed = True
        update_screen(page)
        
        #funcion para que cambie la pantalla una vez inicad
        # Función para cambiar lo que se muestra en la pantalla según el valor de button_pressed
    def update_screen(page):
        print(button_pressed)
        print("Entro a la funcion")
        if button_pressed == True:
            print("Entro al if")
            pantallaCentral.content = ft.Image(
                src="Imagenes/tamagotchi_huevo.gif",
                scale=0.5,
            )
        else:
            print("Entro al else")
            pantallaCentral.content =ft.Image(
                src="Imagenes/tamagotchi.png",
                scale=0.5,
            )
        page.update()

    #Caracteristicas de la ventana
    page.window_width = 400
    page.window_height = 450
    page.window_resizable = False
    page.padding = 0

    # Colores del tamagotchi

    azul = '#00215E'
    cyan = '#2C4E80'
    amarillo = '#FFC55A'
    rosado = '#A91D3A'
    negro = '0xFF000000'
    blanco = '0xFFFFFFF'
    blanco24 = '0x3DFFFFFF'
    verdelima = '#00FF00'

    #Imagenes
    imagenLogo = ft.Image (
        src = "Imagenes/logo.png",
        width = 105,
        height = 60,
        fit = ft.ImageFit.CONTAIN,
    )
    
    #Boton de empezar se muestra al inicio unicamente
    button = ft.ElevatedButton(
        text="Empezar",
        height=50,
        width=150,
        data="BotonEmpezar",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        bgcolor= verdelima,
        color=ft.colors.BLACK,
        on_click=on_button_click,
        visible=show_button,
    )
    
    #boton de reinicio aparece a los 40 segundos de apretar el boton de empezar
    buttonReinicio = ft.ElevatedButton(
        content=ft.Icon(ft.icons.RESTART_ALT, color=ft.colors.WHITE),
        width = 50,
        height = 50,
        data="BotonReinicio",
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            bgcolor= ft.colors.BLUE,
            side=ft.BorderSide(width=2, color=blanco),
        ),
        on_click=on_reinicio,        
    )

    # Botones (Salir, Flechas, Circulo)
    botonSalida = ft.ElevatedButton(
        content=ft.Icon(ft.icons.CLOSE, color=ft.colors.WHITE),
        width=50,
        height=50,
        on_click=close_page,
        style = ft.ButtonStyle(
            bgcolor=ft.colors.RED,
            shape=ft.CircleBorder(),  
            side = ft.BorderSide(width=2, color=blanco),
        )
    )

    # Diseño de la parte superior, se agrega el boton y la imagen de logo
    disenoSuperior = [ 
        ft.Container(
            botonSalida,
            width = 80,
            height = 45 ,
            # border = ft.border.all()  <-- margen para la creacion del diseño
        ),
        ft.Container(
            imagenLogo,
            alignment=ft.alignment.center,
            expand= True # Permite que el contenedor de la imagen se expanda para centrar la imagen
        ),
        ft.Container(
            buttonReinicio,
            width = 80,
            height = 45,
        )
    ]

    pantallaCentral = ft.Stack ([
        ft.Container(
            width = 330,
            height = 250,
            bgcolor = blanco24,
            border_radius = 20,
            border = ft.border.all(4, blanco),
            content=ft.Image(
                src="Imagenes/tamagotchi.png",
                scale=0.5,
            ),
            alignment=ft.alignment.center,
        )
    ])

    # Cuadrantes de guia : Superior, Central e Inferior

    cuadroSuperior = ft.Container(
        content = ft.Row (
            disenoSuperior,
        ),
        width= 380,
        height= 45,
        margin= ft.margin.only(top=15),
        #border = ft.border.all() <-- margen para la creacion del diseño
    )

    cuadroCentral = ft.Container(
        content= pantallaCentral,
        width= 380,
        height= 250,
        margin= ft.margin.only(top=15),
        alignment= ft.alignment.center,
        #border = ft.border.all(), <-- margen para la creacion del diseño
    )
    
    cuadroInferior = ft.Container(#El data es el equivalente a un ID
        width = 380,
        height = 60,
        margin = ft.margin.only(top=15),
        alignment= ft.alignment.center,
        content = 
            ft.Row(      
                    alignment=ft.MainAxisAlignment.CENTER,  
                    controls=[
                        #Boton1
                        ft.ElevatedButton(text="<",height=50,width=50,data="BotonIzquierdo",style=ft.ButtonStyle(
                            shape=ft.CircleBorder(),  
                        ),bgcolor=ft.colors.AMBER,color=ft.colors.BLACK,on_click=on__click),
                        #Boton2
                        ft.ElevatedButton(height=50,width=50,data="BotonDelMedio",style=ft.ButtonStyle(
                            shape=ft.CircleBorder(),
                        ),bgcolor=ft.colors.AMBER,color=ft.colors.BLACK,on_click=on__click),
                        #Boton3
                        ft.ElevatedButton(text=">",height=50,width=50,data="BotonDerecho",style=ft.ButtonStyle(
                            shape=ft.CircleBorder(),  
                        ),bgcolor=ft.colors.AMBER,color=ft.colors.BLACK,on_click=on__click),
                        #boton que aparece una unica vez
                        button,
                    ]
            )
            #border = ft.border.all() <-- margen para la creacion del diseño
    )

    columna = ft.Column(
        spacing = 0,
        controls = [
            cuadroSuperior,
            cuadroCentral,
            cuadroInferior,
        ]
    )

    # Contenedor: Esta el color de fondo de toda la ventana, el tamaño, el centrado.
    # En este caso el tamaño de la ventana y contenedor coinciden, pero se podría modificar.
    contenedor = ft.Container(
        columna,
        width = 400,
        height = 500,
        bgcolor = cyan,
        gradient = ft.LinearGradient([
            azul,
            rosado,
            amarillo,
            ]),
        alignment = ft.alignment.top_center,
    )

    await page.add_async(contenedor)
    
    # Mostrar la pantalla inicial
    update_screen(page)
ft.app(target=main, port=5050)
