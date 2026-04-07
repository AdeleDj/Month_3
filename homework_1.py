import flet as ft

def main(page: ft.Page):
    count = 0

    text_hello = ft.Text(value="Нажато: 0 раз", size=20)

    def on_click(e):
        nonlocal count
        count += 1
        text_hello.value = f"Нажато: {count} раз"
        page.update()

    button = ft.ElevatedButton(
        content=ft.Text("Нажми меня"),
        on_click=on_click
    )

    page.add(text_hello, button)

ft.app(target=main)