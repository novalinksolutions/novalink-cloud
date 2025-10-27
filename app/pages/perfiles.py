import reflex as rx
from app.components.sidebar import sidebar


def perfiles_content() -> rx.Component:
    """Perfiles management content"""
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Gestión de Perfiles",
                class_name="text-3xl font-bold text-gray-800 mb-6",
            ),
            rx.el.div(
                rx.el.p(
                    "Administra los perfiles y permisos de los usuarios.",
                    class_name="text-gray-600 text-lg",
                ),
                class_name="bg-white p-6 rounded-xl shadow-lg border border-gray-100",
            ),
            class_name="max-w-7xl mx-auto",
        ),
        class_name="p-6",
    )


def perfiles() -> rx.Component:
    """Perfiles page with sidebar"""
    return rx.el.div(
        sidebar(),
        rx.el.main(perfiles_content(), class_name="flex-1 bg-gray-50"),
        class_name="flex min-h-screen",
    )