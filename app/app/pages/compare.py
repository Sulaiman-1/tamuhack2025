import reflex as rx
from ..state import State

@rx.page(route="/compare", on_load=State.on_compare_page)
def compare_page() -> rx.Component:
    return rx.hstack(
        
    )