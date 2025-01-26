import reflex as rx
from rxconfig import config
from ..state import State
from ..components import navigation_bar

@rx.page(route="/")
def home_page() -> rx.Component:
    return rx.container(
        navigation_bar(),
        rx.vstack(
            rx.image(
                src="https://lp-auto-assets.s3.us-east-1.amazonaws.com/20/Toyota/model-lineups/sedans/header.jpg",  # Path to your image file
                alt="Toyota Vehicles",  # Alt text for the image
                width="100%",  # Adjust the width as needed (optional)
            ),
            rx.link(
                rx.button("Join the Toyota Family!"),
                href="http://localhost:3000/models/",
                is_external=True,
            ),
            # Commented out section
            # rx.heading("Join the Toyota Family!", size="9"),
            # rx.text(
            #     "Get started by editing ",
            #     rx.code(f"{config.app_name}/{config.app_name}.py"),
            #     size="5",
            # ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",  # Horizontal centering
            align="center",  # Vertical centering
            min_height="85vh",
        ),
        rx.logo(),
    )
