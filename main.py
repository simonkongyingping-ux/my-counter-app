import flet as ft

def main(page: ft.Page):
    # Setup the page
    page.title = "Counter App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT  # Optional: forces light mode

    # Create the text field that shows the number
    number_text = ft.Text(value="0", size=40)

    # Function: What happens when you click MINUS
    def minus_click(e):
        current_value = int(number_text.value)
        number_text.value = str(current_value - 1)
        page.update() # Crucial: tells the phone to refresh the screen

    # Function: What happens when you click PLUS
    def plus_click(e):
        current_value = int(number_text.value)
        number_text.value = str(current_value + 1)
        page.update()

    # Add everything to the page in a Row (side by side)
    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click, icon_size=30),
                number_text,
                ft.IconButton(ft.icons.ADD, on_click=plus_click, icon_size=30),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)