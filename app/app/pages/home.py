import reflex as rx
from rxconfig import config
from ..state import State

def ribbon():
    return rx.hstack(
        rx.color_mode.button(position="top-right"),
        rx.button("Models"),
        rx.button("Compare"),
        rx.button("About Us"),
        bg="gray.100",
        p="2",
        border_bottom="1px solid gray.200",
    ),

@rx.page(route="/home", on_load=State.on_home_page)
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