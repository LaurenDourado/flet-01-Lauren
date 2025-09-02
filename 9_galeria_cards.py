import flet as ft

def criar_card_animal(nome, emoji, descricao, cor):
    """Cria um card estilizado para cada animal"""
    return ft.Container(
        content=ft.Column([
            ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
            ft.Text(nome, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Text(descricao, size=12, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=6
        ),
        bgcolor=cor,
        padding=15,
        border_radius=15,
        width=160,
        height=140,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=12,
            color=ft.Colors.with_opacity(0.25, ft.Colors.BLACK)
        )
    )

def main(page: ft.Page):
    page.title = "Galeria de Animais"
    page.bgcolor = ft.Colors.GREY_100
    page.padding = ft.padding.all(20)
    page.scroll = ft.ScrollMode.AUTO

    animais = [
        {"nome":"Gato","emoji":"🐱","descricao":"Felino carinhoso","cor":ft.Colors.ORANGE_400,"categoria":"Doméstico","tamanho":"Médio"},
        {"nome":"Cachorro","emoji":"🐶","descricao":"Melhor amigo","cor":ft.Colors.BROWN_400,"categoria":"Doméstico","tamanho":"Grande"},
        {"nome":"Peixe","emoji":"🐟","descricao":"Animal aquático","cor":ft.Colors.BLUE_400,"categoria":"Aquático","tamanho":"Pequeno"},
        {"nome":"Pássaro","emoji":"🐦","descricao":"Voa livremente","cor":ft.Colors.GREEN_400,"categoria":"Selvagem","tamanho":"Pequeno"},
        {"nome":"Coelho","emoji":"🐰","descricao":"Saltita pelos campos","cor":ft.Colors.PINK_400,"categoria":"Doméstico","tamanho":"Pequeno"},
        {"nome":"Leão","emoji":"🦁","descricao":"Rei da selva","cor":ft.Colors.YELLOW_700,"categoria":"Selvagem","tamanho":"Grande"},
        {"nome":"Elefante","emoji":"🐘","descricao":"Gigante gentil","cor":ft.Colors.GREY_600,"categoria":"Selvagem","tamanho":"Grande"},
        {"nome":"Golfinho","emoji":"🐬","descricao":"Mamífero marinho","cor":ft.Colors.CYAN_400,"categoria":"Aquático","tamanho":"Grande"}
    ]

    area_cards = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=180,
        child_aspect_ratio=1.0,
        spacing=15,
        run_spacing=15
    )

    filtro_categoria = ft.Dropdown(
        label="Categoria",
        width=160,
        value="Todos",
        border_radius=10,
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Doméstico"),
            ft.dropdown.Option("Selvagem"),
            ft.dropdown.Option("Aquático")
        ]
    )

    filtro_tamanho = ft.Dropdown(
        label="Tamanho",
        width=160,
        value="Todos",
        border_radius=10,
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Pequeno"),
            ft.dropdown.Option("Médio"),
            ft.dropdown.Option("Grande")
        ]
    )

    campo_busca = ft.TextField(
        label="Buscar",
        width=160,
        prefix_icon=ft.Icons.SEARCH,
        border_radius=10
    )

    contador = ft.Text("", size=14, color=ft.Colors.GREY_700, text_align=ft.TextAlign.CENTER)

    def carregar_cards(e=None):
        area_cards.controls.clear()
        categoria = filtro_categoria.value
        tamanho = filtro_tamanho.value
        busca = (campo_busca.value or "").lower()
        filtrados = [a for a in animais
                     if (categoria=="Todos" or a["categoria"]==categoria)
                     and (tamanho=="Todos" or a["tamanho"]==tamanho)
                     and (not busca or busca in a["nome"].lower())]
        for animal in filtrados:
            area_cards.controls.append(criar_card_animal(animal["nome"], animal["emoji"], animal["descricao"], animal["cor"]))
        total_filtrados = len(filtrados)
        total_geral = len(animais)
        contador.value = f"Mostrando {total_filtrados} de {total_geral} animais" if total_filtrados != total_geral else f"Mostrando todos os {total_geral} animais"
        page.update()

    def limpar_filtros(e):
        filtro_categoria.value = "Todos"
        filtro_tamanho.value = "Todos"
        campo_busca.value = ""
        carregar_cards()

    for controle in [filtro_categoria, filtro_tamanho, campo_busca]:
        controle.on_change = carregar_cards

    carregar_cards()

    page.add(
        ft.Column([
            ft.Text("🦁 Zoológico Virtual", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
            ft.Text("Explore diferentes categorias de animais", size=14, color=ft.Colors.GREY_700, text_align=ft.TextAlign.CENTER),
            ft.Row([filtro_categoria, filtro_tamanho], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Row([campo_busca, ft.ElevatedButton("🧹 Limpar", on_click=limpar_filtros, bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            contador,
            ft.Container(content=area_cards, height=400, padding=10, border=ft.border.all(1, ft.Colors.GREY_300), border_radius=15, bgcolor=ft.Colors.WHITE, shadow=ft.BoxShadow(blur_radius=10, spread_radius=1, color=ft.Colors.with_opacity(0.15, ft.Colors.BLACK)))
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
    )

ft.app(target=main)
