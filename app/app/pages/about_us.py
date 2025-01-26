import reflex as rx
from ..state import State
from ..components import navigation_bar

@rx.page(route="/about_us")
def about_us_page() -> rx.Component:
    return rx.container(
        navigation_bar(),
        rx.vstack(
            rx.heading("About us page!", size="9"),
        ),
        rx.logo(),
    )