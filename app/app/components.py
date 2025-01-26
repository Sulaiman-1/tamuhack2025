
import reflex as rx
from .state import State

def navigation_bar():
    return rx.hstack(
        rx.color_mode.button(position="top-right"),
        rx.button(
            "Home",
            on_click=State.on_home_page,
        ),
        rx.button(
            "Models",
            on_click=State.on_models_page,
        ),
        rx.button(
            "Compare",
            on_click=State.on_compare_page,
        ),
        rx.button(
            "About Us",
            on_click=State.on_about_us_page,
        ),
    ),