import reflex as rx
from app.components.sidebar import sidebar
from app.states.sidebar_state import SidebarState
from app.states.database import DatabaseState


def dashboard_content() -> rx.Component:
    """Main dashboard content"""
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Dashboard Principal",
                class_name="text-3xl font-bold text-gray-800 mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("users", class_name="h-12 w-12 text-blue-600 mb-4"),
                    rx.el.h3(
                        "Usuarios",
                        class_name="text-xl font-semibold text-gray-700 mb-2",
                    ),
                    rx.el.p(
                        "Gestionar usuarios del sistema",
                        class_name="text-gray-600 mb-4",
                    ),
                    rx.el.a(
                        "Ver Usuarios",
                        href="/usuarios",
                        class_name="inline-block px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors",
                    ),
                    class_name="bg-white p-6 rounded-xl shadow-lg border border-gray-100 text-center",
                ),
                rx.el.div(
                    rx.icon("shield", class_name="h-12 w-12 text-green-600 mb-4"),
                    rx.el.h3(
                        "Roles", class_name="text-xl font-semibold text-gray-700 mb-2"
                    ),
                    rx.el.p(
                        "Administrar roles y permisos", class_name="text-gray-600 mb-4"
                    ),
                    rx.el.a(
                        "Ver Roles",
                        href="/roles",
                        class_name="inline-block px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors",
                    ),
                    class_name="bg-white p-6 rounded-xl shadow-lg border border-gray-100 text-center",
                ),
                rx.el.div(
                    rx.icon("file-text", class_name="h-12 w-12 text-purple-600 mb-4"),
                    rx.el.h3(
                        "Justificaciones",
                        class_name="text-xl font-semibold text-gray-700 mb-2",
                    ),
                    rx.el.p(
                        "Tipos de justificaciones", class_name="text-gray-600 mb-4"
                    ),
                    rx.el.a(
                        "Configurar",
                        href="/tipos-justificacion",
                        class_name="inline-block px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors",
                    ),
                    class_name="bg-white p-6 rounded-xl shadow-lg border border-gray-100 text-center",
                ),
                rx.el.div(
                    rx.icon("calendar", class_name="h-12 w-12 text-orange-600 mb-4"),
                    rx.el.h3(
                        "Feriados",
                        class_name="text-xl font-semibold text-gray-700 mb-2",
                    ),
                    rx.el.p(
                        "Definir feriados del sistema", class_name="text-gray-600 mb-4"
                    ),
                    rx.el.a(
                        "Gestionar",
                        href="/feriados",
                        class_name="inline-block px-4 py-2 bg-orange-600 text-white rounded-lg hover:bg-orange-700 transition-colors",
                    ),
                    class_name="bg-white p-6 rounded-xl shadow-lg border border-gray-100 text-center",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6",
            ),
            class_name="max-w-7xl mx-auto",
        ),
        class_name="p-6",
    )


def index() -> rx.Component:
    """Main page with sidebar and content"""
    return rx.el.div(
        sidebar(),
        rx.el.main(dashboard_content(), class_name="flex-1 bg-gray-50"),
        on_mount=DatabaseState.check_database_connection,
        class_name="flex min-h-screen",
    )