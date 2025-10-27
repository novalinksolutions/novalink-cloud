import reflex as rx
from app.pages.index import index
from app.pages.usuarios import usuarios
from app.pages.roles import roles
from app.pages.tipos_justificacion import tipos_justificacion
from app.pages.feriados import feriados

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400..700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(usuarios, route="/usuarios")
app.add_page(roles, route="/roles")
app.add_page(tipos_justificacion, route="/tipos-justificacion")
app.add_page(feriados, route="/feriados")