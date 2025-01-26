import reflex as rx
from ..state import State
from ..components import navigation_bar

@rx.page(route="/compare")
def compare_page() -> rx.Component:
    return rx.container(
        navigation_bar(),
        rx.vstack(
            rx.heading("This is the compare page!", size="9"),
        ),
        rx.logo(),
    )