# Bibliotecas
from shiny import App, render, ui, run_app


# Interface do Usuário
app_ui = ui.page_navbar(
    title = "Título da Dashboard",
    bg = "blue",
    lang = "pt"
)


# Servidor
def server(input, output, session):
    ...


# Combinar objetos e rodar Shiny App
app = App(app_ui, server)

run_app(launch_browser = True)
