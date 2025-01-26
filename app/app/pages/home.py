import reflex as rx
from rxconfig import config
from ..state import State

def ribbon():
    return rx.hstack(
        rx.color_mode.button(position="top-right"),
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

@rx.page(route="/", on_load=State.on_home_page)
def home_page() -> rx.Component:
    return rx.container(
        ribbon(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )