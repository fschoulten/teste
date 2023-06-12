from shiny import ui, App

# Interface do usuário (UI)
app_ui = ui.page_navbar(
    # Cria uma "página interna" na dashboard
    ui.nav(
        # Título da página
        "Página 1",
        ui.layout_sidebar(
            ui.panel_sidebar("Contúdo da barra lateral"),
            ui.panel_main(
                ui.row(
                    ui.column(6, "Bloco A", {"style": "background-color: yellow;"}),
                    ui.column(6, "Bloco B", {"style": "background-color: red;"})
                ),
                ui.row(
                    ui.column(4, "Bloco C", {"style": "background-color: blue;"}),
                    ui.column(4, "Bloco D", {"style": "background-color: orange;"}),
                    ui.column(4, "Bloco E", {"style": "background-color: purple;"})
                )
            )
        )
    ),
    ui.nav(
        # Título da página
        "Página 2"
    ),
    #ui.nav_spacer(),
    # Links barra de navegação
    ui.nav_control(ui.a("Análise Macro", href = "https://analisemacro.com.br/")),
    ui.nav_menu(
        "Mais",
        ui.nav_control(
            ui.a("LinkedIn", href = "https://br.linkedin.com/company/an%C3%A1lise-macro"),
            ui.a("Blog", href = "https://analisemacro.com.br/blog/")
        ),
        align="left"
    ),
    # Título e estilos barra de navegação
    title = ui.row(
        ui.column(3, ui.img(src = "https://aluno.analisemacro.com.br/download/49491/?tmstv=1685386850")),
        ui.column(9, "Título da dashboard")
        ),
    bg = "blue",
    inverse = True
)

# Servidor (backend)
def server (input, output, session):
    ...

# Construir Shiny App
app = App(app_ui, server)