import flet as ft

def main(page: ft.Page):
    page.title = "Проверка возраста"

    age_input = ft.TextField(label="Введите возраст")

    result_text = ft.Text("")

    def check_age(e):
        age = age_input.value

        if not age or not age.isdigit():
            result_text.value = "Введите корректный возраст"
            result_text.color = ft.Colors.YELLOW

        else:
            age = int(age)

            if age >= 18:
                result_text.value = "Доступ разрешен"
                result_text.color = ft.Colors.GREEN
            else:
                result_text.value = "Доступ запрещен"
                result_text.color = ft.Colors.RED

        page.update()

    check_button = ft.ElevatedButton(
        content=ft.Text("Проверить"),
        on_click=check_age
    )

    page.add(age_input, check_button, result_text)

ft.app(target=main)