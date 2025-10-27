import reflex as rx
from app.components.sidebar import sidebar
from app.states.sidebar_state import SidebarState


def feriados_content() -> rx.Component:
    """Holidays management content"""
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Definir Feriados", class_name="text-3xl font-bold text-gray-800 mb-6"
            ),
            rx.el.div(
                rx.el.p(
                    "Administra los feriados y días no laborales del sistema.",
                    class_name="text-gray-600 text-lg",
                ),
                class_name="bg-white p-6 rounded-xl shadow-lg border border-gray-100",
            ),
            class_name="max-w-7xl mx-auto",
        ),
        class_name="p-6",
    )


def feriados() -> rx.Component:
    """Holidays page with sidebar"""
    return rx.el.div(
        sidebar(),
        rx.el.main(feriados_content(), class_name="flex-1 bg-gray-50"),
        class_name="flex min-h-screen",
    )