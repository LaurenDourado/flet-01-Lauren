import flet as ft

def main(page: ft.Page):
    """
    App mobile-friendly usando Flet
    """
    # Configurações básicas da página
    page.title = "Meu Primeiro App Flet"
    page.bgcolor = ft.Colors.GREY_100  # fundo neutro
    page.padding = 20
    page.scroll = "adaptive"  # permite rolagem em telas pequenas
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Título principal
    titulo = ft.Text(
        "🫰🏽Hello world! (Primeiro app com Flet!)",
        size=28,
        color=ft.Colors.BLUE_700,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    # Função para alternar a cor do título
    def mudar_cor(e):
        titulo.color = ft.Colors.RED_700 if titulo.color == ft.Colors.BLUE_700 else ft.Colors.BLUE_700
        page.update()

    # Botão para mudar a cor
    botao_mudar_cor = ft.ElevatedButton(
        "Mudar cor do título 🎨",
        bgcolor=ft.Colors.RED_600,
        color=ft.Colors.WHITE,
        on_click=mudar_cor,
        expand=True  # ocupa toda a largura do card (mobile-friendly)
    )

    # Card centralizado
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    titulo,
                    ft.Text(
                        "Bem-vindo ao mundo do desenvolvimento mobile!",
                        size=18,
                        color=ft.Colors.BLUE_900,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Com Flet, você pode criar apps incríveis 🪄📱",
                        size=18,
                        color=ft.Colors.RED_700,
                        text_align=ft.TextAlign.CENTER
                    ),
                    botao_mudar_cor
                ],
                spacing=15,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            padding=20,
            width=page.width * 0.9,  # card ocupa 90% da largura da tela
            border_radius=15,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(blur_radius=12, spread_radius=1, color=ft.Colors.GREY_400)
        ),
        elevation=8
    )

    # Adicionando o card à página centralizada
    page.add(
        ft.Column(
            controls=[card],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)
