import reflex as rx
from ..state import State
from ..components import navigation_bar

@rx.page(route="/models")
def models_page() -> rx.Component:
    return rx.container(
        navigation_bar(),
        rx.vstack(
            rx.heading("This is the models page!", size="9"),
        ),
        rx.logo(),
    )
    
