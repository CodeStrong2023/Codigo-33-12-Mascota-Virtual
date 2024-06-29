import flet as ft
import asyncio
from ui import create_ui

async def main(page: ft.Page):
    await create_ui(page)

ft.app(target=main, port=5050)