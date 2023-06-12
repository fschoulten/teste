from shiny import ui, App

# INTERFACE DO USUÁRIO
app_ui = ui.page_navbar(
    ui.nav(
        "Página 1",
        ui.layout_sidebar(
            ui.panel_sidebar("Barra lateral"),
            ui.panel_main(
                "Painel principal",
                ui.row(
                    ui.column(6, "Linha 1, Coluna A", style = "background-color: red;"),
                    ui.column(6, "Linha 1, Coluna B", style = "background-color: yellow;")
                    ),
                ui.row(
                    ui.column(4, "Linha 2, Coluna C", style = "background-color: green;"),
                    ui.column(4, "Linha 2, Coluna D", style = "background-color: purple;"),
                    ui.column(4, "Linha 2, Coluna E", style = "background-color: pink;")
                    )
                )
        )
        ),
    ui.nav("Página 2"),
    ui.nav_control(ui.a("Análise Macro", href = "https://analisemacro.com.br/")),
    ui.nav_spacer(),
    ui.nav_menu(
        "Mais",
        ui.nav_control(ui.a("Blog", href = "https://analisemacro.com.br/blog/")),
        ui.nav_control(ui.a("LinkedIn", href = "https://br.linkedin.com/company/an%C3%A1lise-macro")),
        align = "right"
    ),
    title = ui.row(
        ui.column(3, ui.img(src = "https://aluno.analisemacro.com.br/download/49491/?tmstv=1685386850")),
        ui.column(9, "Título da dashboard")
    ),
    bg = "blue",
    inverse = True
)


# SERVIDOR
def server(input, output, session):
    ...


# SHINY APP
app = App(app_ui, server)