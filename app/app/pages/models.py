import reflex as rx
from ..state import State

@rx.page(route="/models", on_load=State.on_models_page)
def models_page() -> rx.Component:
    return rx.hstack(
        
    )