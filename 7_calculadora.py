import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Simples"
    page.bgcolor = ft.Colors.GREY_100  # fundo neutro
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campos e elementos
    numero1 = ft.TextField(
        label="Primeiro número",
        width=250,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=10,
        border_color=ft.Colors.BLUE_700,
        focused_border_color=ft.Colors.BLUE_900,
        text_size=16
    )
    numero2 = ft.TextField(
        label="Segundo número",
        width=250,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=10,
        border_color=ft.Colors.BLUE_700,
        focused_border_color=ft.Colors.BLUE_900,
        text_size=16
    )

    operacao = ft.Dropdown(
        label="Operação",
        width=250,
        border_radius=10,
        options=[
            ft.dropdown.Option("Soma"),
            ft.dropdown.Option("Subtração"),
            ft.dropdown.Option("Multiplicação"),
            ft.dropdown.Option("Divisão")
        ]
    )

    resultado = ft.Text(
        "Resultado aparecerá aqui",
        size=20,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREY_600
    )

    def calcular(e):
        try:
            num1, num2, op = float(numero1.value), float(numero2.value), operacao.value

            if not op:
                resultado.value, resultado.color = "⚠️ Selecione uma operação!", ft.Colors.ORANGE
            elif op == "Divisão" and num2 == 0:
                resultado.value, resultado.color = "❌ Erro: Divisão por zero!", ft.Colors.RED_700
            else:
                simbolos = {
                    "Soma": ("+", num1 + num2),
                    "Subtração": ("-", num1 - num2),
                    "Multiplicação": ("×", num1 * num2),
                    "Divisão": ("÷", num1 / num2)
                }
                simbolo, res = simbolos[op]
                resultado.value, resultado.color = f"{num1} {simbolo} {num2} = {res:.2f}", ft.Colors.GREEN_700
        except ValueError:
            resultado.value, resultado.color = "❌ Digite números válidos!", ft.Colors.RED_700
        page.update()

    def limpar(e):
        numero1.value = numero2.value = operacao.value = ""
        resultado.value, resultado.color = "Campos limpos! ✨", ft.Colors.BLUE_700
        page.update()

    # Botões estilizados
    botoes = ft.Row(
        [
            ft.ElevatedButton(
                "✔ Calcular",
                on_click=calcular,
                width=150,
                height=50,
                bgcolor=ft.Colors.GREEN_700,
                color=ft.Colors.WHITE,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
            ),
            ft.ElevatedButton(
                "✖ Limpar",
                on_click=limpar,
                width=150,
                height=50,
                bgcolor=ft.Colors.BLUE_700,
                color=ft.Colors.WHITE,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Card centralizado
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("🧮 Calculadora Simples", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=20),
                    numero1,
                    numero2,
                    operacao,
                    botoes,
                    ft.Divider(),
                    resultado
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

    page.add(
        ft.Column(
            controls=[card],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)
