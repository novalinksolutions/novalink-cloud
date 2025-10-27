import reflex as rx
from app.states.sidebar_state import SidebarState
from app.states.database import DatabaseState


def menu_item(item: dict) -> rx.Component:
    """Render a menu item"""
    return rx.cond(
        item["type"] == "menu",
        rx.el.button(
            rx.icon(item["icon"], class_name="h-5 w-5 mr-3 text-gray-600"),
            rx.el.span(item["name"], class_name="font-medium text-gray-700"),
            rx.icon(
                rx.cond(
                    (item["id"] == "security") & SidebarState.security_expanded,
                    "chevron-down",
                    rx.cond(
                        (item["id"] == "parameters") & SidebarState.parameters_expanded,
                        "chevron-down",
                        "chevron-right",
                    ),
                ),
                class_name="h-4 w-4 ml-auto text-gray-400",
            ),
            on_click=rx.cond(
                item["id"] == "security",
                SidebarState.toggle_security_menu,
                rx.cond(
                    item["id"] == "parameters",
                    SidebarState.toggle_parameters_menu,
                    rx.noop(),
                ),
            ),
            class_name="flex items-center w-full p-3 rounded-xl hover:bg-blue-50 transition-all duration-200 text-left group",
        ),
        rx.el.a(
            rx.icon(
                item["icon"],
                class_name="h-5 w-5 mr-3 text-gray-600 group-hover:text-blue-600",
            ),
            rx.el.span(
                item["name"],
                class_name="font-medium text-gray-700 group-hover:text-blue-700",
            ),
            href=item.get("route", "#"),
            on_click=lambda: SidebarState.set_current_page(item["id"]),
            class_name=rx.cond(
                SidebarState.current_page == item["id"],
                "flex items-center w-full p-3 rounded-xl bg-blue-100 text-blue-700 font-semibold shadow-sm group",
                "flex items-center w-full p-3 rounded-xl hover:bg-blue-50 transition-all duration-200 group",
            ),
        ),
    )


def submenu_item(item: dict) -> rx.Component:
    """Render a submenu item"""
    return rx.el.a(
        rx.icon(
            item["icon"],
            class_name="h-4 w-4 mr-3 text-gray-500 group-hover:text-blue-600",
        ),
        rx.el.span(
            item["name"],
            class_name="text-sm font-medium text-gray-600 group-hover:text-blue-700",
        ),
        href=item.get("route", "#"),
        on_click=lambda: SidebarState.set_current_page(item["id"]),
        class_name=rx.cond(
            SidebarState.current_page == item["id"],
            "flex items-center w-full p-2 pl-8 rounded-lg bg-blue-50 text-blue-700 font-semibold group ml-4",
            "flex items-center w-full p-2 pl-8 rounded-lg hover:bg-blue-50 transition-all duration-200 group ml-4",
        ),
    )


def database_status() -> rx.Component:
    """Database connection status indicator"""
    return rx.el.div(
        rx.el.div(
            rx.icon(
                rx.cond(DatabaseState.db_connected, "database", "database-x"),
                class_name=rx.cond(
                    DatabaseState.db_connected,
                    "h-4 w-4 text-green-600",
                    "h-4 w-4 text-red-600",
                ),
            ),
            rx.el.span("Base de Datos", class_name="text-xs font-medium text-gray-600"),
            class_name="flex items-center gap-2 mb-1",
        ),
        rx.el.p(
            DatabaseState.connection_status,
            class_name=rx.cond(
                DatabaseState.db_connected,
                "text-xs text-green-600 font-medium",
                "text-xs text-red-600 font-medium",
            ),
        ),
        rx.el.button(
            "Verificar",
            on_click=DatabaseState.check_database_connection,
            class_name="text-xs px-2 py-1 bg-blue-100 text-blue-700 rounded-md hover:bg-blue-200 transition-colors mt-1",
        ),
        class_name="p-3 bg-gray-50 rounded-xl border",
    )


def sidebar() -> rx.Component:
    """Main sidebar component"""
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon("shield-check", class_name="h-8 w-8 text-blue-600"),
                rx.el.div(
                    rx.el.h1("Sistema", class_name="text-lg font-bold text-gray-800"),
                    rx.el.p("Gestión", class_name="text-sm text-gray-600"),
                    class_name="ml-3",
                ),
                class_name="flex items-center p-4 border-b border-gray-200",
            ),
            rx.el.nav(
                rx.foreach(
                    SidebarState.menu_items,
                    lambda item: rx.cond(
                        item.get("parent") == "",
                        rx.el.div(
                            menu_item(item),
                            rx.cond(
                                (item["id"] == "security")
                                & SidebarState.security_expanded,
                                rx.el.div(
                                    rx.foreach(
                                        SidebarState.menu_items,
                                        lambda subitem: rx.cond(
                                            subitem.get("parent") == "security",
                                            submenu_item(subitem),
                                            rx.fragment(),
                                        ),
                                    ),
                                    class_name="mt-1 mb-2",
                                ),
                                rx.fragment(),
                            ),
                            rx.cond(
                                (item["id"] == "parameters")
                                & SidebarState.parameters_expanded,
                                rx.el.div(
                                    rx.foreach(
                                        SidebarState.menu_items,
                                        lambda subitem: rx.cond(
                                            subitem.get("parent") == "parameters",
                                            submenu_item(subitem),
                                            rx.fragment(),
                                        ),
                                    ),
                                    class_name="mt-1 mb-2",
                                ),
                                rx.fragment(),
                            ),
                            class_name="mb-1",
                        ),
                        rx.fragment(),
                    ),
                ),
                class_name="flex flex-col gap-1 p-4 flex-1 overflow-y-auto",
            ),
            rx.el.div(database_status(), class_name="p-4 border-t border-gray-200"),
            class_name="flex flex-col h-full",
        ),
        class_name="w-72 bg-white border-r border-gray-200 shadow-sm h-screen flex-shrink-0",
    )