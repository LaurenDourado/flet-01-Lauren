import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro Botão"
    page.bgcolor = ft.Colors.GREY_100  # fundo neutro
    page.padding = 20
    page.scroll = "adaptive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Criando um texto estilizado
    mensagem = ft.Text(
        value="Clique no botão abaixo!👇",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_700,
        text_align=ft.TextAlign.CENTER
    )

    # Função que altera a mensagem ao clicar
    def botao_clicado(evento):
        mensagem.value = "🎉 Parabéns! Você clicou no botão!"
        mensagem.color = ft.Colors.RED_700
        page.update()

    # Botão estilizado
    meu_botao = ft.ElevatedButton(
        text="Clique em mim!",
        on_click=botao_clicado,
        width=250,
        height=60,
        bgcolor=ft.Colors.RED_600,
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15)
        )
    )

    # Card centralizado para organizar os elementos
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[mensagem, meu_botao],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
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

    # Adicionando o card à página
    page.add(
        ft.Column(
            controls=[card],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)
