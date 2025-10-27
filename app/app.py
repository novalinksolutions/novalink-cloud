import reflex as rx
from app.pages import index

app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(index.index)