import flet as ft
from funciones import Tamagotchi

# Variables globales
show_button = True
button_pressed = False
buttonpressed = False
mascota = Tamagotchi("Tamagotchi")

def close_page(e):
    e.page.clean()
    e.page.go("/")

def on__click(e):
    print(f"Botón con ID {e.control.data} presionado")

def on_reinicio(e):
    global buttonpressed
    print(f"Botón con ID {e.control.data} presionado")
    buttonpressed = True

def on_button_click(e):
    global show_button, button_pressed, button
    print(f"Botón con ID {e.control.data} presionado")
    show_button = False
    button.visible = False
    button_pressed = True
    update_screen(e.page)

def update_screen(page):
    global button_pressed, pantallaCentral
    if button_pressed:
        pantallaCentral.content = ft.Image(
            src="Imagenes/tamagotchi_huevo.gif",
            scale=0.5,
        )
    else:
        pantallaCentral.content = ft.Image(
            src="Imagenes/tamagotchi.png",
            scale=0.5,
        )
    page.update()

# Función para crear la interfaz de usuario
async def create_ui(page: ft.Page):
    global pantallaCentral, button

    # Características de la ventana
    page.window_width = 400
    page.window_height = 450
    page.window_resizable = False
    page.padding = 0

    # Colores del Tamagotchi
    azul = '#00215E'
    cyan = '#2C4E80'
    amarillo = '#FFC55A'
    rosado = '#A91D3A'
    blanco = '0xFFFFFFF'
    blanco24 = '0x3DFFFFFF'
    verdelima = '#00FF00'

    # Imágenes
    imagenLogo = ft.Image(
        src="Imagenes/logo.png",
        width=105,
        height=60,
        fit=ft.ImageFit.CONTAIN,
    )

    # Botón de empezar
    button = ft.ElevatedButton(
        text="Empezar",
        height=50,
        width=150,
        data="BotonEmpezar",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        bgcolor=verdelima,
        color=ft.colors.BLACK,
        on_click=on_button_click,
        visible=show_button,
    )

    # Botón de reinicio
    buttonReinicio = ft.ElevatedButton(
        content=ft.Icon(ft.icons.RESTART_ALT, color=ft.colors.WHITE),
        width=50,
        height=50,
        data="BotonReinicio",
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            bgcolor=ft.colors.BLUE,
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
        style=ft.ButtonStyle(
            bgcolor=ft.colors.RED,
            shape=ft.CircleBorder(),
            side=ft.BorderSide(width=2, color=blanco),
        )
    )

    # Diseño de la parte superior
    disenoSuperior = [
        ft.Container(
            botonSalida,
            width=80,
            height=45,
        ),
        ft.Container(
            imagenLogo,
            alignment=ft.alignment.center,
            expand=True
        ),
        ft.Container(
            buttonReinicio,
            width=80,
            height=45,
        )
    ]

    pantallaCentral = ft.Stack([
        ft.Container(
            width=330,
            height=250,
            bgcolor=blanco24,
            border_radius=20,
            border=ft.border.all(4, blanco),
            content=ft.Image(
                src="Imagenes/tamagotchi.png",
                scale=0.5,
            ),
            alignment=ft.alignment.center,
        )
    ])

    # Cuadrantes de guía: Superior, Central e Inferior
    cuadroSuperior = ft.Container(
        content=ft.Row(disenoSuperior),
        width=380,
        height=45,
        margin=ft.margin.only(top=15),
    )

    cuadroCentral = ft.Container(
        content=pantallaCentral,
        width=380,
        height=250,
        margin=ft.margin.only(top=15),
        alignment=ft.alignment.center,
    )

    cuadroInferior = ft.Container(
        width=380,
        height=60,
        margin=ft.margin.only(top=15),
        alignment=ft.alignment.center,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ElevatedButton(text="<", height=50, width=50, data="BotonIzquierdo", style=ft.ButtonStyle(
                    shape=ft.CircleBorder(),
                ), bgcolor=ft.colors.AMBER, color=ft.colors.BLACK, on_click=on__click),
                ft.ElevatedButton(height=50, width=50, data="BotonDelMedio", style=ft.ButtonStyle(
                    shape=ft.CircleBorder(),
                ), bgcolor=ft.colors.AMBER, color=ft.colors.BLACK, on_click=on__click),
                ft.ElevatedButton(text=">", height=50, width=50, data="BotonDerecho", style=ft.ButtonStyle(
                    shape=ft.CircleBorder(),
                ), bgcolor=ft.colors.AMBER, color=ft.colors.BLACK, on_click=on__click),
                button,
            ]
        )
    )

    columna = ft.Column(
        spacing=0,
        controls=[
            cuadroSuperior,
            cuadroCentral,
            cuadroInferior,
        ]
    )

    contenedor = ft.Container(
        columna,
        width=400,
        height=500,
        bgcolor=cyan,
        gradient=ft.LinearGradient([azul, rosado, amarillo]),
        alignment=ft.alignment.top_center,
    )

    await page.add_async(contenedor)
    update_screen(page)
