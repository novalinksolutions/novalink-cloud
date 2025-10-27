import reflex as rx


class SidebarState(rx.State):
    """State for sidebar navigation"""

    collapsed: bool = False
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
            "parent": "",
        },
        {
            "id": "security",
            "name": "Seguridad",
            "icon": "shield",
            "type": "menu",
            "parent": "",
        },
        {
            "id": "users",
            "name": "Usuarios",
            "icon": "users",
            "route": "/usuarios",
            "parent": "security",
            "type": "page",
        },
        {
            "id": "perfiles",
            "name": "Perfiles",
            "icon": "user-check",
            "route": "/perfiles",
            "parent": "security",
            "type": "page",
        },
        {
            "id": "parameters",
            "name": "Parámetros",
            "icon": "settings",
            "type": "menu",
            "parent": "",
        },
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

    @rx.event
    def toggle_sidebar(self):
        """Toggle the sidebar collapsed state"""
        self.collapsed = not self.collapsed