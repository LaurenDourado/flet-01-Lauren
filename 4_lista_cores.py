import flet as ft

def main(page: ft.Page):
    page.title = "Seletor de Cores"
    page.bgcolor = ft.Colors.GREY_100  # fundo neutro
    page.padding = 20
    page.scroll = "adaptive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Caixa que mudará de cor
    caixa_colorida = ft.Container(
        content=ft.Text(
            "Escolha uma cor! 🎨",
            color=ft.Colors.WHITE,
            size=18,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
        ),
        bgcolor=ft.Colors.GREY_500,
        width=300,
        height=120,
        border_radius=15,
        alignment=ft.alignment.center
    )

    # Função para mudar a cor da caixa
    def cor_selecionada(evento):
        cor_escolhida = evento.control.value
        cores_disponiveis = {
            "Azul": ft.Colors.BLUE_700,
            "Verde": ft.Colors.GREEN_700,
            "Vermelho": ft.Colors.RED_700,
            "Roxo": ft.Colors.PURPLE_700,
            "Laranja": ft.Colors.ORANGE_700,
            "Rosa": ft.Colors.PINK_400
        }
        caixa_colorida.bgcolor = cores_disponiveis[cor_escolhida]
        caixa_colorida.content.value = f"Cor selecionada: {cor_escolhida} ✨"
        page.update()

    # Dropdown estilizado
    seletor_cor = ft.Dropdown(
        label="Escolha uma cor",
        width=220,
        options=[
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Roxo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Rosa")
        ],
        on_change=cor_selecionada
    )

    # Card centralizado para organizar o layout
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Seletor de Cores Mágico! ✨", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                    seletor_cor,
                    caixa_colorida
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
