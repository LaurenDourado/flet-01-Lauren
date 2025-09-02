import flet as ft

def main(page: ft.Page):
    page.title = "Painel de Configuração"
    page.bgcolor = ft.Colors.GREY_100
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Área de preview dentro de um card
    area_preview = ft.Container(
        content=ft.Text("Texto de exemplo para configurar 🎨", size=16, color=ft.Colors.BLACK),
        bgcolor=ft.Colors.WHITE,
        padding=20,
        border_radius=15,
        border=ft.border.all(2, ft.Colors.GREY_300),
        width=350,
        height=150,
        alignment=ft.alignment.center
    )

    # Controles
    switch_negrito = ft.Switch(label="Negrito", value=False)
    switch_italico = ft.Switch(label="Itálico", value=False)
    checkbox_sublinhado = ft.Checkbox(label="Sublinhado", value=False)
    slider_tamanho = ft.Slider(min=12, max=32, value=16, divisions=4, label="Tamanho: {value}px")
    dropdown_cor = ft.Dropdown(
        label="Cor do texto",
        width=150,
        value="Preto",
        border_radius=10,
        options=[
            ft.dropdown.Option("Preto"),
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Roxo")
        ]
    )
    dropdown_fundo = ft.Dropdown(
        label="Cor do fundo",
        width=150,
        value="Branco",
        border_radius=10,
        options=[
            ft.dropdown.Option("Branco"),
            ft.dropdown.Option("Cinza Claro"),
            ft.dropdown.Option("Azul Claro"),
            ft.dropdown.Option("Verde Claro"),
            ft.dropdown.Option("Rosa Claro")
        ]
    )

    # Função para aplicar configuração
    def aplicar_config(e):
        texto = area_preview.content
        texto.size = slider_tamanho.value
        texto.weight = ft.FontWeight.BOLD if switch_negrito.value else ft.FontWeight.NORMAL
        texto.italic = switch_italico.value
        texto.style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE) if checkbox_sublinhado.value else None

        cores_texto = {
            "Preto": ft.Colors.BLACK,
            "Azul": ft.Colors.BLUE_700,
            "Verde": ft.Colors.GREEN_700,
            "Vermelho": ft.Colors.RED_700,
            "Roxo": ft.Colors.PURPLE_700
        }
        cores_fundo = {
            "Branco": ft.Colors.WHITE,
            "Cinza Claro": ft.Colors.GREY_200,
            "Azul Claro": ft.Colors.BLUE_100,
            "Verde Claro": ft.Colors.GREEN_100,
            "Rosa Claro": ft.Colors.PINK_100
        }

        texto.color = cores_texto[dropdown_cor.value]
        area_preview.bgcolor = cores_fundo[dropdown_fundo.value]
        page.update()

    # Conectar eventos
    for controle in [switch_negrito, switch_italico, checkbox_sublinhado, slider_tamanho, dropdown_cor, dropdown_fundo]:
        controle.on_change = aplicar_config

    # Card central para o painel
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("⚙️ Painel de Configuração", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                    ft.Text("Configure o texto abaixo:", size=14, color=ft.Colors.GREY_700),
                    area_preview,
                    ft.Divider(),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text("📝 Estilo", size=16, weight=ft.FontWeight.BOLD),
                                    switch_negrito,
                                    switch_italico,
                                    checkbox_sublinhado,
                                    ft.Text(f"Tamanho: {slider_tamanho.value}px"),
                                    slider_tamanho
                                ],
                                spacing=10
                            ),
                            ft.Column(
                                [
                                    ft.Text("🎨 Cores", size=16, weight=ft.FontWeight.BOLD),
                                    dropdown_cor,
                                    dropdown_fundo
                                ],
                                spacing=10
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        vertical_alignment=ft.CrossAxisAlignment.START
                    )
                ],
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

    page.add(
        ft.Column(
            controls=[card],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)
