import flet as ft

def main(page: ft.Page):
    page.title = "Criador de Perfil"
    page.bgcolor = ft.Colors.GREY_100  # fundo neutro
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campos do formulário
    campo_nome = ft.TextField(
        label="Nome completo",
        width=300,
        border_radius=10,
        border_color=ft.Colors.BLUE_700,
        focused_border_color=ft.Colors.BLUE_900,
        text_size=16
    )
    campo_idade = ft.TextField(
        label="Idade",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=10,
        border_color=ft.Colors.BLUE_700,
        focused_border_color=ft.Colors.BLUE_900,
        text_size=16
    )

    dropdown_hobby = ft.Dropdown(
        label="Hobby favorito",
        width=300,
        options=[
            ft.dropdown.Option("Leitura 📚"),
            ft.dropdown.Option("Esportes ⚽"),
            ft.dropdown.Option("Música 🎵"),
            ft.dropdown.Option("Jogos 🎮"),
            ft.dropdown.Option("Culinária 🍳"),
            ft.dropdown.Option("Arte 🎨"),
        ]
    )

    # Área do perfil criado (inicialmente oculta)
    cartao_perfil = ft.Container(
        content=ft.Text("Preencha os dados acima"),
        bgcolor=ft.Colors.GREY_100,
        padding=20,
        width=350,
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=10, spread_radius=1, color=ft.Colors.GREY_400),
        visible=False
    )

    def criar_perfil(evento):
        """Valida dados e cria o perfil visual"""
        if not campo_nome.value or len(campo_nome.value) < 2:
            mostrar_erro("Nome deve ter pelo menos 2 caracteres")
            return

        if not campo_idade.value:
            mostrar_erro("Idade é obrigatória")
            return

        try:
            idade = int(campo_idade.value)
            if idade < 1 or idade > 120:
                mostrar_erro("Idade deve estar entre 1 e 120 anos")
                return
        except ValueError:
            mostrar_erro("Idade deve ser um número")
            return

        if not dropdown_hobby.value:
            mostrar_erro("Selecione um hobby")
            return

        criar_cartao_perfil()

    def mostrar_erro(mensagem):
        """Mostra mensagem de erro"""
        cartao_perfil.content = ft.Column(
            [
                ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED_700, size=40),
                ft.Text(mensagem, color=ft.Colors.RED_700, text_align=ft.TextAlign.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        cartao_perfil.bgcolor = ft.Colors.RED_50
        cartao_perfil.visible = True
        page.update()

    def criar_cartao_perfil():
        """Cria o cartão visual do perfil"""
        idade = int(campo_idade.value)
        if idade < 18:
            categoria = "Jovem"
            cor_icone = ft.Colors.BLUE_700
        elif idade < 60:
            categoria = "Adulto"
            cor_icone = ft.Colors.BLUE_900
        else:
            categoria = "Experiente"
            cor_icone = ft.Colors.RED_700

        cartao_perfil.content = ft.Column([
            ft.Icon(ft.Icons.PERSON, size=60, color=cor_icone),
            ft.Text(campo_nome.value, size=20, weight=ft.FontWeight.BOLD),
            ft.Text(f"{idade} anos ({categoria})", size=14, color=ft.Colors.GREY_600),
            ft.Text(f"Hobby: {dropdown_hobby.value}", size=14),
            ft.Container(
                content=ft.Text("Perfil criado! 🎉", color=ft.Colors.WHITE),
                bgcolor=cor_icone,
                padding=10,
                border_radius=20
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)

        cartao_perfil.bgcolor = ft.Colors.WHITE
        cartao_perfil.visible = True
        page.update()

    def limpar_campos(evento):
        """Limpa todos os campos"""
        campo_nome.value = ""
        campo_idade.value = ""
        dropdown_hobby.value = None
        cartao_perfil.visible = False
        page.update()

    # Botões estilizados
    linha_botoes = ft.Row(
        [
            ft.ElevatedButton(
                "Criar Perfil",
                on_click=criar_perfil,
                bgcolor=ft.Colors.BLUE_700,
                color=ft.Colors.WHITE,
                width=150,
                height=50,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
            ),
            ft.ElevatedButton(
                "Limpar",
                on_click=limpar_campos,
                bgcolor=ft.Colors.RED_700,
                color=ft.Colors.WHITE,
                width=150,
                height=50,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER, spacing=20
    )

    # Layout principal com card centralizado
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("📝 Criador de Perfil", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                    ft.Text("Preencha seus dados para criar seu perfil personalizado!",
                            size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=20),
                    campo_nome,
                    campo_idade,
                    dropdown_hobby,
                    linha_botoes,
                    ft.Container(height=20),
                    cartao_perfil
                ],
                spacing=15,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=30,
            width=page.width * 0.9,
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
