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
                src="https://media.discordapp.net/attachments/1332821505415053434/1333034767423111218/DALLE_2025-01-26_01.31.16_-_A_lineup_of_flagship_Toyota_vehicles_including_SUVs_sedans_and_hybrids_displayed_in_a_dramatic_and_elegant_dark_scene_slightly_more_zoomed_in_to_.png?ex=67976cdf&is=67961b5f&hm=776aea40c05466fb64668f9d69b6203ce5fbca56df3840ac1c25217142b4d830&=&format=webp&quality=lossless&width=1591&height=909",  # Path to your image file
                alt="Toyota Vehicles", 
                width="100%", 
                height="500px",  # Set a specific height to ensure it works with object_fit
                object_fit="cover",  # Ensures the image covers the container fully
                border_radius="15px",
                margin_top="20px",
                margin_bottom="10px",
            ),
            rx.container(rx.heading("Find Your Dream Car Today With Toyotapedia",
                       size="9",
                       color="black",
                       text_align="center",
                       font_weight="bold",
                       font_family="Helvetica, Arial, sans-serif"
            ),
            style = {
                "background-color": "white",
                "border-radius": "25px"
            },
            ),
            # Use an HStack to arrange images side by side
            rx.hstack(
                # Camry Section
                rx.vstack(
                    rx.image(
                        src="https://hips.hearstapps.com/hmg-prod/images/2025-toyota-camry-xse-awd-123-66993cc94cc40.jpg?crop=0.676xw:0.506xh;0.101xw,0.399xh&resize=1200:*",  # Path to your image file
                        alt="Toyota Camry", 
                        width="100%",  # Same width for both images
                        height="340px",
                        object_fit = "cover",  # Let the height adjust based on aspect ratio
                        border_radius="15px",
                        border="solid black 3px"
                    ),
                    rx.text(
                        "Toyota Camry: A refined sedan that blends unparalleled comfort, sophisticated performance, and cutting-edge safety features. Elevate your driving experience with the iconic Toyota Camry.",
                        font_size="18px",  # Slightly larger text for readability
                        text_align="center",
                        color="black",
                        padding="20px",  # More padding for a more spacious, professional look
                        background_color="lightgray",  # Subtle background color for description
                        border_radius="10px",
                        box_shadow="none",  # Minimalistic with no box shadow
                        font_weight="400",  # Normal weight for a professional, clean look
                        font_family="Georgia, serif",  # A formal serif font for a professional feel
                        line_height="1.5",  # Increase line height for readability
                        margin="0 10px",
                        height = "200px",  # Adding a margin to space out the text from container edges
                    ),
                    spacing="4",
                    align="center",  # Ensure both the image and text are centered
                    width="100%",  # Make sure each side takes the same width
                ),
                # Tundra Section
                rx.vstack(
                    rx.image(
                        src="https://media.ed.edmunds-media.com/toyota/tacoma/2024/oem/2024_toyota_tacoma_crew-cab-pickup_limited_fq_oem_1_1280.jpg",  # Path to your image file
                        alt="Toyota Tundra", 
                        width="100%",  # Same width for both images
                        height="340px",
                        object_fit = "cover",  # Let the height adjust based on aspect ratio
                        border_radius="15px",
                        border="solid black 3px",
                    ),
                    rx.text(
                        "Toyota Tundra: Built for strength and versatility, the Toyota Tundra delivers exceptional towing capacity, rugged off-road performance, and the latest in innovative technology. A pickup truck designed to exceed your expectations.",
                        font_size="18px",  # Slightly larger text for readability
                        text_align="center",
                        color="black",
                        padding="20px",  # More padding for a more spacious, professional look
                        background_color="lightgray",  # Subtle background color for description
                        border_radius="10px",
                        box_shadow="none",  # Minimalistic with no box shadow
                        font_weight="400",  # Normal weight for a professional, clean look
                        font_family="Georgia, serif",  # A formal serif font for a professional feel
                        line_height="1.5",  # Increase line height for readability
                        margin="0 10px",
                        height = "200px"  # Adding a margin to space out the text from container edges
                    ),
                    spacing="4",
                    align="center",  # Ensure both the image and text are centered
                    width="100%",  # Make sure each side takes the same width
                ),
                spacing="5",
                style = {
                    "display": "flex", 
                    "justify-content": "space-between",  # Equal space between images
                    "align-items": "stretch",  # Stretch the images and text equally
                    "width": "100%",  # Ensure the hstack takes up the full width
                },
            ),
            rx.link(
                rx.button("View all available models",
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
                href="http://localhost:3000/models/",
                is_external=True,
            ),
            spacing="8",
            justify="center",  # Horizontal centering for button
            align="center",  # Vertical centering
            min_height="85vh",
        ),
        style={
            "height": "100%",
            "background-color": "white",
            "background-image": "url(https://wallpaperaccess.com/full/11110568.jpg)",
            "background-size": "cover",
            "background-position": "center",
            "background-attachment": "fixed",
              # Clean white background for a minimalist look
        }
    )
