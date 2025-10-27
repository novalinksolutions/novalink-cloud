import reflex as rx


class SidebarState(rx.State):
    """State for sidebar navigation"""

    current_page: str = "dashboard"
    security_expanded: bool = False
    parameters_expanded: bool = False
    menu_items: list[dict[str, str]] = [
        {
            "id": "dashboard",
            "name": "Dashboard",
            "icon": "home",
            "route": "/",
            "type": "page",
        },
        {"id": "security", "name": "Seguridad", "icon": "shield", "type": "menu"},
        {
            "id": "users",
            "name": "Usuarios",
            "icon": "users",
            "route": "/usuarios",
            "parent": "security",
            "type": "page",
        },
        {
            "id": "roles",
            "name": "Roles",
            "icon": "user-check",
            "route": "/roles",
            "parent": "security",
            "type": "page",
        },
        {"id": "parameters", "name": "Parámetros", "icon": "settings", "type": "menu"},
        {
            "id": "justification_types",
            "name": "Tipo de Justificaciones",
            "icon": "file-text",
            "route": "/tipos-justificacion",
            "parent": "parameters",
            "type": "page",
        },
        {
            "id": "holidays",
            "name": "Definir Feriados",
            "icon": "calendar",
            "route": "/feriados",
            "parent": "parameters",
            "type": "page",
        },
    ]

    @rx.event
    def set_current_page(self, page_id: str):
        """Set the current active page"""
        self.current_page = page_id

    @rx.event
    def toggle_security_menu(self):
        """Toggle security submenu"""
        self.security_expanded = not self.security_expanded

    @rx.event
    def toggle_parameters_menu(self):
        """Toggle parameters submenu"""
        self.parameters_expanded = not self.parameters_expanded