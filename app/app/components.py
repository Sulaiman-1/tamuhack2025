
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
            },
            background_color = "maroon"
        ),
        rx.button(
            "Models",
            on_click=State.on_models_page,
                style={
                "padding": "27px",
            },
            background_color = "maroon"
        ),
        rx.button(
            "Compare",
            on_click=State.on_compare_page,
                style={
                "padding": "27px",
            },
            background_color = "maroon"
        ),
        rx.button(
            "About Us",
            on_click=State.on_about_us_page,
                style={
                "padding": "27px",
                
            },
            background_color = "maroon  "
        ),
        rx.button(
            "Populate Vehicles",
            on_click=State.populate_cars,
                style={
                "padding": "27px",
            },
            background_color = "lightgray",
            color = "black",
        ),

        style = {
            "display": "flex",
            "justify-content": "space-evenly",
            "background-color": "maroon",
            "padding": "13px",
            "border-radius": "6px",
        }
    ),