import flet as ft
from funciones import Tamagotchi

# Función para crear la interfaz de usuario
async def create_ui(page: ft.Page):
    show_button = True
    button_pressed = False # Para controlar visibilidad y estado del botón
    
    # Se crea instancia (para el objeto)
    tamagotchi = Tamagotchi("Tama")
    # Para mostrar el estado del Tamagotchi
    estado_tamagotchi = ft.Text(
        value = "Estado del Tamagotchi",
        color = ft.colors.WHITE,
        weight = ft.FontWeight.BOLD, 
    )

    # Función para cerrar la página
    def close_page(e):
        page.clean()
        page.go("/")

    # Función para corroborar si el botón es presionado, se imprime por consola  
    def on_click(e):
        print(f"Botón con ID {e.control.data} presionado")

    # Función para reiniciar el estado del Tamagotchi   
    def on_reinicio(e):
        tamagotchi.reiniciar()
        estado_tamagotchi.value = "Estado del Tamagotchi reiniciado"
        page.update()
    
    # Función para el botón de Empezar 
    def on_button_click(e):
        nonlocal button_pressed
        nonlocal show_button
            
        print(f"Botón con ID {e.control.data} presionado")
        show_button = False
        button_pressed = True
        button.visible = False
        page.update()
    
    # Función para actualizar Tamagotchi según la acción
    def actualizar_estado(accion):
        if accion == "alimentar":
            mensaje = tamagotchi.alimentar()
        elif accion == "jugar":
            mensaje = tamagotchi.jugar()
        elif accion == "dormir":
            mensaje = tamagotchi.dormir()
        
        mensaje_tiempo = tamagotchi.tiempo_pasa(accion)
        estado_tamagotchi.value = f"{mensaje}\n{mensaje_tiempo}"
        page.update()
    
    # Configuración para la ventana 
    page.window_width = 500  # Ancho de la ventana
    page.window_height = 450  # Alto de la ventana
    page.window_resizable = False
    page.padding = 0

    # Colores declarados 
    azul = '#00215E'
    cyan = '#2C4E80'
    amarillo = '#FFC55A'
    rosado = '#A91D3A'
    blanco = '0xFFFFFFF'
    blanco24 = '0x3DFFFFFF'
    verdelima = '#00FF00'

    # Imagen ( Logo)
    imagenLogo = ft.Image(
        src = "Imagenes/logo.png",
        width = 105,
        height = 60,
        fit = ft.ImageFit.CONTAIN,
    )
    
    # Botón de Empezar
    button = ft.ElevatedButton(
        text = "Empezar",
        height = 50,
        width = 150,
        data = "BotonEmpezar",
        style = ft.ButtonStyle(
            shape = ft.RoundedRectangleBorder(radius=10),
        ),
        bgcolor = verdelima,
        color = ft.colors.BLACK,
        on_click = on_button_click,
        visible = show_button,
    )
    
    # Botón de Reinicio
    buttonReinicio = ft.ElevatedButton(
        content = ft.Icon(
            ft.icons.RESTART_ALT,
            color = ft.colors.WHITE),
        width = 50,
        height = 50,
        data = "BotonReinicio",
        style = ft.ButtonStyle(
            shape = ft.CircleBorder(),
            bgcolor = ft.colors.BLUE,
            side = ft.BorderSide(
                width = 2,
                color = blanco),
        ),
        on_click = on_reinicio,
    )

    #Botón de Salida
    botonSalida = ft.ElevatedButton(
        content = ft.Icon(
            ft.icons.CLOSE,
            color = ft.colors.WHITE),
        width = 50,
        height = 50,
        on_click = close_page,
        style = ft.ButtonStyle(
            bgcolor = ft.colors.RED,
            shape = ft.CircleBorder(),
            side = ft.BorderSide(width = 2, color = blanco),
        )
    )

    # Diseño para la parte superior de la interfaz
    disenoSuperior = [ 
        ft.Container(
            botonSalida,
            width = 80,
            height = 45,
        ),
        ft.Container(
            imagenLogo,
            alignment = ft.alignment.center,
            expand = True
        ),
        ft.Container(
            buttonReinicio,
            width = 80,
            height = 45,
        )
    ]

    # Donde se muestra la imagen y estado del Tamagotchi
    pantallaCentral = ft.Stack([
        ft.Container(
            width = 330,
            height = 250,
            bgcolor = blanco24,
            border_radius = 20,
            border = ft.border.all(4, blanco),
            content = ft.Stack([
                estado_tamagotchi,
                ft.Image(
                    src = "Imagenes/tamagotchi.png",
                    scale = 0.5,
                ),
            ]),
            alignment = ft.alignment.center,
        )
    ])

    # Contenedor de la parte superior
    cuadroSuperior = ft.Container(
        content = ft.Row(
            disenoSuperior,
        ),
        width = 380,
        height = 45,
        margin = ft.margin.only(top = 15),
    )

    # Contenedor de la parte central 
    cuadroCentral = ft.Container(
        content = pantallaCentral,
        width = 380,
        height = 250,
        margin = ft.margin.only(top = 15),
        alignment = ft.alignment.center,
    )

    # Contenedor inferior , junto con los botones de acciones
    cuadroInferior = ft.Container(
        width = 380,
        height = 60,
        margin = ft.margin.only(top = 15),
        alignment = ft.alignment.center,
        content = ft.Column(
            spacing = 5,
            alignment = ft.MainAxisAlignment.CENTER,
            controls = [
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton(text="<", height=50, width=50, data="alimentar", style=ft.ButtonStyle(
                            shape=ft.CircleBorder(),
                        ), bgcolor=ft.colors.AMBER, color=ft.colors.BLACK, on_click=lambda e: actualizar_estado("alimentar")),
                        ft.ElevatedButton(height=50, width=50, data="jugar", style=ft.ButtonStyle(
                            shape=ft.CircleBorder(),
                        ), bgcolor=ft.colors.AMBER, color=ft.colors.BLACK, on_click=lambda e: actualizar_estado("jugar")),
                        ft.ElevatedButton(text=">", height=50, width=50, data="dormir", style=ft.ButtonStyle(
                            shape=ft.CircleBorder(),
                        ), bgcolor=ft.colors.AMBER, color=ft.colors.BLACK, on_click=lambda e: actualizar_estado("dormir")),
                        button,
                    ]
                )
            ]
        )
    )

    # Columna para contener los 3 Cuadros
    columna = ft.Column(
        spacing = 0,
        controls = [
            cuadroSuperior,
            cuadroCentral,
            cuadroInferior,
        ]
    )

    # Contenedor principal para la configuración de ventana
    contenedor = ft.Container(
        columna,
        width = 500,  # Ancho de la ventana
        height = 450,  # Alto de la ventana
        bgcolor  =cyan,
        gradient = ft.LinearGradient([
            azul,
            rosado,
            amarillo,
        ]),
        alignment = ft.alignment.top_center,
    )

    # Se añade el contenedor principal a la página
    await page.add_async(contenedor)