import flet as ft


def main(page: ft.Page):
    page.title = "Улучшенная история с лимитом"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []

    name_input = ft.TextField(label="Введите имя")

    result_text = ft.Text("")
    history_column = ft.Column()

    def update_history():
        history_column.controls.clear()

        for name in greeting_history:
            history_column.controls.append(ft.Text(name))

        page.update()

    def add_name(e):
        name = name_input.value.strip()

        if not name:
            result_text.value = "Введите имя!"
            result_text.color = ft.Colors.RED

        elif len(name) < 2:
            result_text.value = "Имя должно быть не короче 2 символов!"
            result_text.color = ft.Colors.RED

        elif name.isdigit():
            result_text.value = "Имя не может состоять из цифр!"
            result_text.color = ft.Colors.RED

        elif name in greeting_history:
            result_text.value = "Это имя уже в истории!"
            result_text.color = ft.Colors.RED

        else:
            greeting_history.insert(0, name)

            if len(greeting_history) > 5:
                greeting_history.pop()

            result_text.value = f"Имя {name} добавлено!"
            result_text.color = ft.Colors.GREEN

            update_history()

        name_input.value = ""
        page.update()

    def clear_history(e):
        greeting_history.clear()
        result_text.value = "История очищена!"
        result_text.color = ft.Colors.BLUE
        update_history()

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    top_buttons = ft.Row(
        controls=[
            ft.ElevatedButton("Сменить тему", on_click=toggle_theme),
            ft.ElevatedButton("Очистить историю", on_click=clear_history),
        ]
    )

    add_button = ft.ElevatedButton("Добавить имя", on_click=add_name)

    main_column = ft.Column(
        controls=[
            top_buttons,
            name_input,
            add_button,
            result_text,
            ft.Text("История имен:"),
            history_column,
        ]
    )

    page.add(main_column)


ft.app(target=main)