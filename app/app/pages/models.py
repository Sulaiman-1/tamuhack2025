import reflex as rx
from ..state import State
from ..components import navigation_bar

@rx.page(route="/models", on_load=State.on_models_page)
def models_page() -> rx.Component:
    return rx.container(
        navigation_bar()
    )