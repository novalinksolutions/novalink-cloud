import reflex as rx
from app.states.state import State


def index() -> rx.Component:
    return rx.el.div(rx.el.p("Welcome to Reflex!"))