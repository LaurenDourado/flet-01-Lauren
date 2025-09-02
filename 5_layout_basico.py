import flet as ft

def main(page: ft.Page):
    page.title = "Layouts Básicos"
    page.bgcolor = ft.Colors.GREY_100  # fundo neutro
    page.padding = 20
    page.scroll = "adaptive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Título principal
    titulo = ft.Text(
        "Organizando Elementos na Tela 📐",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_800,
        text_align=ft.TextAlign.CENTER
    )

    # Linha horizontal de botões (azul e vermelho)
    linha_botoes = ft.Row(
        controls=[
            ft.ElevatedButton("Botão 1", bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE, width=100, height=50),
            ft.ElevatedButton("Botão 2", bgcolor=ft.Colors.RED_700, color=ft.Colors.WHITE, width=100, height=50),
            ft.ElevatedButton("Botão 3", bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE, width=100, height=50)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    # Caixas coloridas em coluna (azul e vermelho)
    caixa1 = ft.Container(
        content=ft.Text("Caixa 1", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
        bgcolor=ft.Colors.BLUE_700,
        width=200,
        height=60,
        alignment=ft.alignment.center,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=8, spread_radius=1, color=ft.Colors.GREY_400)
    )

    caixa2 = ft.Container(
        content=ft.Text("Caixa 2", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
        bgcolor=ft.Colors.RED_700,
        width=200,
        height=60,
        alignment=ft.alignment.center,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=8, spread_radius=1, color=ft.Colors.GREY_400)
    )

    # Coluna de caixas
    coluna_caixas = ft.Column(
        controls=[caixa1, caixa2],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    # Card principal para organizar todo o layout
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    titulo,
                    ft.Text("Linha horizontal de botões:", size=16, color=ft.Colors.BLUE_900),
                    linha_botoes,
                    ft.Text("Coluna de caixas:", size=16, color=ft.Colors.RED_900),
                    coluna_caixas,
                    ft.Text("Layout organizado! 🎉", size=14, color=ft.Colors.GREEN_700)
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
