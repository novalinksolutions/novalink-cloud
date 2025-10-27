import reflex as rx


def index_content() -> rx.Component:
    """Dashboard content."""
    return rx.el.main(
        rx.el.div(
            rx.el.h1("Dashboard", class_name="text-3xl font-bold text-gray-800"),
            rx.el.p(
                "Bienvenido al panel de administración.",
                class_name="mt-2 text-lg text-gray-600",
            ),
            class_name="mb-8",
        ),
        class_name="p-8 w-full",
    )