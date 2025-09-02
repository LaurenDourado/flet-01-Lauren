import flet as ft

def main(page: ft.Page):
    page.title = "Contador Animado"
    page.bgcolor = ft.Colors.GREY_100
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    valor_contador = 0

    # Display do contador com animação de tamanho
    display_contador = ft.Text(
        value="0",
        size=48,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_700,
        text_align=ft.TextAlign.CENTER
    )

    info_contador = ft.Text(
        value="Contador zerado",
        size=16,
        color=ft.Colors.GREY_600,
        text_align=ft.TextAlign.CENTER
    )

    def atualizar_display(crescer=False, diminuir=False):
        """Atualiza display, cor e animação baseado no valor"""
        display_contador.value = str(valor_contador)

        if valor_contador > 0:
            display_contador.color = ft.Colors.BLUE_700
            info_contador.value = "Valor positivo"
        elif valor_contador < 0:
            display_contador.color = ft.Colors.RED_700
            info_contador.value = "Valor negativo"
        else:
            display_contador.color = ft.Colors.BLUE_700
            info_contador.value = "Contador zerado"

        # Animação de crescimento ou diminuição
        if crescer:
            display_contador.size += 4
        elif diminuir:
            display_contador.size -= 4

        page.update()

    def incrementar(e):
        nonlocal valor_contador
        valor_contador += 1
        atualizar_display(crescer=True)

    def decrementar(e):
        nonlocal valor_contador
        valor_contador -= 1
        atualizar_display(diminuir=True)

    def resetar(e):
        nonlocal valor_contador
        valor_contador = 0
        display_contador.size = 48  # resetar tamanho
        atualizar_display()

    # Card centralizado com os controles
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("🧮 Contador Animado", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                    display_contador,
                    info_contador,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("➖", on_click=decrementar, width=100, height=100,
                                              bgcolor=ft.Colors.RED_700, color=ft.Colors.WHITE, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))),
                            ft.ElevatedButton("➕", on_click=incrementar, width=100, height=100,
                                              bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)))
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=40
                    ),
                    ft.ElevatedButton("🔄 Reset", on_click=resetar, width=150, height=50,
                                      bgcolor=ft.Colors.GREY_700, color=ft.Colors.WHITE,
                                      style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)))
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=30,
            width=page.width * 0.85,
            border_radius=15,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(blur_radius=12, spread_radius=1, color=ft.Colors.GREY_400)
        ),
        elevation=8
    )

    page.add(
        ft.Column(
            controls=[card],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)
