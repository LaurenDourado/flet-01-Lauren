import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.bgcolor = ft.Colors.GREY_100  # fundo neutro
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = "adaptive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campo de texto estilizado
    campo_nome = ft.TextField(
        label="Digite seu nome aqui",
        width=300,
        border_color=ft.Colors.BLUE_700,
        focused_border_color=ft.Colors.BLUE_900,
        border_radius=10,
        text_size=18,
        text_align=ft.TextAlign.CENTER
    )

    # Texto para mostrar a resposta
    resposta = ft.Text(
        value="",
        size=18,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD
    )

    # Função que processa o nome digitado
    def processar_nome(evento):
        nome_digitado = campo_nome.value.strip()
        if not nome_digitado:
            resposta.value = "⚠️ Por favor, digite seu nome!"
            resposta.color = ft.Colors.RED_700
        elif len(nome_digitado) < 2:
            resposta.value = "⚠️ Nome muito curto!"
            resposta.color = ft.Colors.ORANGE_700
        else:
            resposta.value = f"✅ Olá, {nome_digitado}! Prazer em conhecê-lo(a)"
            resposta.color = ft.Colors.GREEN_700
        page.update()

    # Botão estilizado
    botao_ok = ft.ElevatedButton(
        text="Confirmar",
        on_click=processar_nome,
        width=180,
        height=50,
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15)
        )
    )

    # Card centralizado para organizar o layout
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Vamos nos conhecer!🤗", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                    campo_nome,
                    botao_ok,
                    resposta
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
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
