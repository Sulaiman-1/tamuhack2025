import reflex as rx
from ..state import State
from ..components import navigation_bar

@rx.page(route="/about_us", on_load=State.on_about_us_page)
def about_us_page() -> rx.Component:
    return rx.container(
        navigation_bar()
    )