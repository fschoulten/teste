from shiny import ui, App

# Interface do usuário (UI)
app_ui = ui.page_navbar(
    ui.nav_control(ui.a("Análise Macro", href = "https://analisemacro.com.br/")),
    ui.nav_menu(
        "Mais",
        ui.nav_control(
            ui.a("LinkedIn", href = "https://br.linkedin.com/company/an%C3%A1lise-macro"),
            ui.a("Blog", href = "https://analisemacro.com.br/blog/")
            )
        ),
    title = "Título da dashboard",
    bg = "blue",
    inverse = True
)

# Servidor (backend)
def server (input, output, session):
    ...

# Construir Shiny App
app = App(app_ui, server)