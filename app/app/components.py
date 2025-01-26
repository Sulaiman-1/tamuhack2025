
import reflex as rx
from .state import State

def navigation_bar():
    return rx.hstack(
        rx.color_mode.button(position="top-right"),
        rx.button(
            "Home",
            on_click=State.on_home_page,
            style={
                "padding": "27px",
            }
        ),
        rx.button(
            "Models",
            on_click=State.on_models_page,
                style={
                "padding": "27px",
            }
        ),
        rx.button(
            "Compare",
            on_click=State.on_compare_page,
                style={
                "padding": "27px",
            }
        ),
        rx.button(
            "About Us",
            on_click=State.on_about_us_page,
                style={
                "padding": "27px",
            }
        ),

        style = {
            "display": "flex",
            "justify-content": "space-evenly",
            "background-color": "#003366",
            "padding": "13px",
            "border-radius": "6px",


        }
    ),