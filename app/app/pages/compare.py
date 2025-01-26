import reflex as rx
from ..state import State
from ..components import navigation_bar

@rx.page(route="/compare", on_load=State.on_compare_page)
def compare_page() -> rx.Component:
    return rx.container(
        navigation_bar()
    )