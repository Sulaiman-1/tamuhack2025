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
                style={
                    "width": "100%",
                }
            )
        ),
        rx.vstack(
            rx.image(
                src="https://lp-auto-assets.s3.us-east-1.amazonaws.com/20/Toyota/model-lineups/sedans/header.jpg",  # Path to your image file
                alt="Toyota Vehicles", 
                width="100%", 
                height="400px",  # Set a specific height to ensure it works with object_fit
                object_fit="cover",  # Ensures the image covers the container fully
                border_radius="15px",
                border="solid black 3px",
                margin_top="10px",
            ),
            rx.heading("Join the Toyota Family!",
                       size="9",
                       color="black",
                       text_align="center",
                       font_weight="bold",
                       font_family="Helvetica, Arial, sans-serif"
            ),
            # Use an HStack to arrange images side by side
            rx.hstack(
                rx.image(
                    src="https://hips.hearstapps.com/hmg-prod/images/2025-toyota-camry-xse-awd-123-66993cc94cc40.jpg?crop=0.676xw:0.506xh;0.101xw,0.399xh&resize=1200:*",  # Path to your image file
                    alt="Toyota Vehicles", 
                    width="45%",
                    align="left",
                    border_radius="15px",
                    border="solid black 3px"
                ),
                rx.image(
                    src="https://media.ed.edmunds-media.com/toyota/tacoma/2024/oem/2024_toyota_tacoma_crew-cab-pickup_limited_fq_oem_1_1280.jpg",  # Add your second image here
                    alt="Toyota Vehicle 2", 
                    width="45%",
                    height="200px",
                    align="left",
                    border_radius="15px",
                    border="solid black 3px",
                ),
                spacing="5",
                style = {
                    "display": "flex", 
                    "justify-content": "space-evenly",
                },
            ),
            rx.link(
                rx.button("View all models",
                          font_size="35px",
                          padding="25px 30px",
                          background_color="#600000",
                          color="white",
                          opacity=1,
                          hover_style={
                              "opacity": 0.1,
                          },
                          transition="opacity 0.3s ease in-out",
                          ),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="8",
            justify="center",  # Horizontal centering for button
            align="center",  # Vertical centering
            min_height="85vh",
        ),
        style={
            "height": "100%",
            "background-color": "lightg"
        }
    )
