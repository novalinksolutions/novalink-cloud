import reflex as rx
from app.components.sidebar import sidebar
from app.pages.index import index_content


def dashboard() -> rx.Component:
    """Dashboard page with sidebar"""
    return rx.el.div(
        sidebar(),
        rx.el.main(index_content(), class_name="flex-1 bg-gray-50"),
        class_name="flex min-h-screen font-['Inter']",
    )