import reflex as rx
from app.components.sidebar import sidebar
from app.states.sidebar_state import SidebarState


def tipos_justificacion_content() -> rx.Component:
    """Justification types management content"""
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Tipos de Justificaciones",
                class_name="text-3xl font-bold text-gray-800 mb-6",
            ),
            rx.el.div(
                rx.el.p(
                    "Configura los diferentes tipos de justificaciones disponibles en el sistema.",
                    class_name="text-gray-600 text-lg",
                ),
                class_name="bg-white p-6 rounded-xl shadow-lg border border-gray-100",
            ),
            class_name="max-w-7xl mx-auto",
        ),
        class_name="p-6",
    )


def tipos_justificacion() -> rx.Component:
    """Justification types page with sidebar"""
    return rx.el.div(
        sidebar(),
        rx.el.main(tipos_justificacion_content(), class_name="flex-1 bg-gray-50"),
        class_name="flex min-h-screen",
    )