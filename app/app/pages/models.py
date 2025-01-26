import reflex as rx
from ..state import State
from ..components import navigation_bar

@rx.page(route="/models")
def models_page() -> rx.Component:
    return rx.container(
        navigation_bar(),
        rx.vstack(
            # First heading with margin and text styling
            rx.heading(
                "Sedans", 
                size="7",
                font_weight="bold",  
                text_decoration="underline", 
                margin_top="30px",  # Add some space between the navigation bar and the heading
            ),
            # Section for Toyota Camry
            rx.text("Toyota Camry", 
                    size="3",
                    font_weight="bold", 
                    margin_top="20px"),
            rx.container(
                rx.hstack(
                    # Description on the left
                    rx.text(
                        "The base Toyota Camry offers a comfortable ride with a 2.5-liter four-cylinder engine that delivers a balance of power and fuel efficiency. It comes equipped with essential features such as a touchscreen infotainment system, advanced safety technologies, and a spacious interior, making it an excellent choice for those seeking value and reliability.", 
                        size="1",
                        margin_top="1px",
                        width="50%",  # Set width to 50% to allocate space for the image on the right
                    ),
                    # Image of the Toyota Camry on the right
                    rx.image(
                        src="https://www.motortrend.com/uploads/2023/11/2025-Toyota-Camry-hybrid-sedan-13.png?w=768&width=768&q=75&format=webp",  # Replace this with the image URL
                        width="50%",  # Set width to 50% for equal distribution of space
                        height="auto",
                        margin_top="5px",  # Adjust margin if necessary
                    ),
                ),
            ),
            rx.text("MSRP: $28,700", 
                    size="3",
                    font_weight="bold", 
                    text_decoration="underline",
                    margin_top="1px"),
            # Section for Toyota Corolla
            rx.text("Toyota Corolla", 
                    size="3",
                    font_weight="bold", 
                    margin_top="40px"),  # Additional margin to separate from Camry
            rx.container(
                rx.hstack(
                    # Description on the left
                    rx.text(
                        "The Toyota Corolla combines efficiency and reliability with its 1.8-liter four-cylinder engine. It features modern technology such as a user-friendly infotainment system, advanced safety features, and a stylish design, making it a favorite for commuters and families alike.", 
                        size="1",
                        margin_top="10px",
                        width="50%",  # Set width to 50% to allocate space for the image on the right
                    ),
                    # Image of the Toyota Corolla on the right
                    rx.image(
                        src="https://scout.customerscout.net/Gallery/IMAGES/2025/Toyota/GR-Corolla/2025-Toyota-GR-Corolla-800x.jpg",  # Replace this with the image URL
                        width="50%",  # Set width to 50% for equal distribution of space
                        height="auto",
                        margin_top="5px",  # Adjust margin if necessary
                    ),
                ),
            ),
            rx.text("MSRP: $22,325", 
                    size="3",
                    font_weight="bold", 
                    text_decoration="underline",
                    margin_top="1px"),




            # Heading for Trucks
            rx.heading(
                "Trucks", 
                size="7",
                font_weight="bold",  
                text_decoration="underline", 
                margin_top="50px",  # Add some space between the sedans and the trucks section
            ),
            # Section for Toyota Tacoma
            rx.text("Toyota Tacoma", 
                    size="3",
                    font_weight="bold", 
                    margin_top="20px"),
            rx.container(
                rx.hstack(
                    # Description on the left
                    rx.text(
                        "The Toyota Tacoma is a versatile mid-size truck known for its off-road capabilities and rugged design. It features a 3.5-liter V6 engine option, modern technology, and excellent durability, making it a popular choice for adventurers and work purposes alike.", 
                        size="1",
                        margin_top="1px",
                        width="50%",  # Set width to 50% to allocate space for the image on the right
                    ),
                    # Placeholder image for the Toyota Tacoma (replace with actual image URL)
                    rx.image(
                        src="https://di-uploads-pod10.dealerinspire.com/toyotaofnewnan/uploads/2019/12/2020-toyota-tacoma-driving-down-sand-dune.png",  # Replace this with the image URL
                        width="50%",  # Set width to 50% for equal distribution of space
                        height="auto",
                        margin_top="1px",  # Adjust margin if necessary
                    ),
                ),
            ),
            rx.text("MSRP: $31,590", 
                    size="3",
                    font_weight="bold", 
                    text_decoration="underline",
                    margin_top="1px"),
            # Section for Toyota Tundra
            rx.text("Toyota Tundra", 
                    size="3",
                    font_weight="bold", 
                    margin_top="40px"),  # Additional margin to separate from Tacoma
            rx.container(
                rx.hstack(
                    # Description on the left
                    rx.text(
                        "The Toyota Tundra is a full-size pickup truck offering exceptional towing capacity and a robust 3.5-liter twin-turbo V6 engine. With a spacious interior, advanced safety features, and impressive durability, it is designed for both heavy-duty work and family comfort.", 
                        size="1",
                        margin_top="1px",
                        width="50%",  # Set width to 50% to allocate space for the image on the right
                    ),
                    # Placeholder image for the Toyota Tundra (replace with actual image URL)
                    rx.image(
                        src="https://www.cnet.com/a/img/resize/4d9413e2e1ead1d0403a7055ff608ac16b48c6cc/hub/2021/10/11/42950137-b68f-499b-9951-e2e948dd144c/2022-toyota-tundra-trd-pro-001.jpg?auto=webp&fit=crop&height=675&width=1200",  # Replace this with the image URL
                        width="50%",  # Set width to 50% for equal distribution of space
                        height="auto",
                        margin_top="1px",  # Adjust margin if necessary
                    ),
                ),
            ),
            rx.text("MSRP: $40,090", 
                    size="3",
                    font_weight="bold", 
                    text_decoration="underline",
                    margin_top="1px"),
            # Heading for SUVs
            rx.heading(
                "SUVs", 
                size="7",
                font_weight="bold",  
                text_decoration="underline", 
                margin_top="30px",  # Add some space between the navigation bar and the heading
            ),
            # Section for Toyota Highlander
            rx.text("Toyota Highlander", 
                    size="3",
                    font_weight="bold", 
                    margin_top="20px"),
            rx.container(
                rx.hstack(
                    # Description on the left
                    rx.text(
                        "The Toyota Highlander is a versatile midsize SUV offering a comfortable ride, ample cargo space, and advanced safety features. It comes with a 2.5-liter hybrid powertrain or a 3.5-liter V6 engine, making it a great choice for families and adventurers.", 
                        size="1",
                        margin_top="1px",
                        width="50%",  # Set width to 50% to allocate space for the image on the right
                    ),
                    # Placeholder image for the Toyota Highlander (replace with actual image URL)
                    rx.image(
                        src="https://www.clickheretesting.com/ToyotaNewBern/research/2024/highlander/images/mlp-img-hero.jpg",  # Replace this with the image URL
                        width="50%",  # Set width to 50% for equal distribution of space
                        height="auto",
                        margin_top="1px",  # Adjust margin if necessary
                    ),
                ),
            ),
            rx.text("MSRP: $39,520", 
                    size="3",
                    font_weight="bold", 
                    text_decoration="underline",
                    margin_top="1px"),
            # Section for Toyota 4Runner
            rx.text("Toyota 4Runner", 
                    size="3",
                    font_weight="bold", 
                    margin_top="40px"),  # Additional margin to separate from Highlander
            rx.container(
                rx.hstack(
                    # Description on the left
                    rx.text(
                        "The Toyota 4Runner is a rugged SUV designed for off-road adventures and family outings. It features a durable body-on-frame construction, a 4.0-liter V6 engine, and advanced off-road capabilities, making it a favorite among outdoor enthusiasts.", 
                        size="1",
                        margin_top="1px",
                        width="50%",  # Set width to 50% to allocate space for the image on the right
                    ),
                    # Placeholder image for the Toyota 4Runner (replace with actual image URL)
                    rx.image(
                        src="https://hips.hearstapps.com/hmg-prod/images/2025-toyota-4runner-trdpro-mudbath-010-jpg-6615909a9e592.jpg",  # Replace this with the image URL
                        width="50%",  # Set width to 50% for equal distribution of space
                        height="auto",
                        margin_top="1px",  # Adjust margin if necessary
                    ),
                ),
            ),
            rx.text("MSRP: $40,770", 
                    size="3",
                    font_weight="bold", 
                    text_decoration="underline",
                    margin_top="1px"),
            # Section for Toyota Sequoia
            rx.text("Toyota Sequoia", 
                    size="3",
                    font_weight="bold", 
                    margin_top="40px"),  # Additional margin to separate from 4Runner
            rx.container(
                rx.hstack(
                    # Description on the left
                    rx.text(
                        "The Toyota Sequoia is a full-size SUV that combines power and luxury. With a robust twin-turbo V6 hybrid engine, spacious seating for up to eight passengers, and premium features, it is designed for both families and heavy-duty performance.", 
                        size="1",
                        margin_top="1px",
                        width="50%",  # Set width to 50% to allocate space for the image on the right
                    ),
                    # Placeholder image for the Toyota Sequoia (replace with actual image URL)
                    rx.image(
                        src="https://di-uploads-pod6.dealerinspire.com/maticktoyota/uploads/2024/11/Untitled-design-2024-11-30T061609.955.png",  # Replace this with the image URL
                        width="50%",  # Set width to 50% for equal distribution of space
                        height="auto",
                        margin_top="1px",  # Adjust margin if necessary
                    ),
                ),
            ),
            rx.text("MSRP: $62,425", 
                    size="3",
                    font_weight="bold", 
                    text_decoration="underline",
                    margin_top="1px"),

            # Heading for Vans/Crossovers
            rx.heading(
                "Vans/Crossovers", 
                size="7",
                font_weight="bold",  
                text_decoration="underline", 
                margin_top="30px",  # Add some space between the navigation bar and the heading
            ),
            # Section for Toyota Sienna
            rx.text("Toyota Sienna", 
                    size="3",
                    font_weight="bold", 
                    margin_top="20px"),
            rx.container(
                rx.hstack(
                    # Description on the left
                    rx.text(
                        "The Toyota Sienna is a premium minivan offering a hybrid powertrain for excellent fuel efficiency. With a spacious interior, advanced safety features, and modern technology, it is perfect for families seeking comfort and convenience.", 
                        size="1",
                        margin_top="1px",
                        width="50%",  # Set width to 50% to allocate space for the image on the right
                    ),
                    # Placeholder image for the Toyota Sienna (replace with actual image URL)
                    rx.image(
                        src="https://media.ed.edmunds-media.com/toyota/sienna/2023/oem/2023_toyota_sienna_passenger-minivan_le-8-passenger_fq_oem_1_1600.jpg",  # Replace this with the image URL
                        width="50%",  # Set width to 50% for equal distribution of space
                        height="auto",
                        margin_top="1px",  # Adjust margin if necessary
                    ),
                ),
            ),
            rx.text("MSRP: $39,185", 
                    size="3",
                    font_weight="bold", 
                    text_decoration="underline",
                    margin_top="1px"),
            # Section for Toyota RAV4
            rx.text("Toyota RAV4", 
                    size="3",
                    font_weight="bold", 
                    margin_top="40px"),  # Additional margin to separate from Sienna
            rx.container(
                rx.hstack(
                    # Description on the left
                    rx.text(
                        "The Toyota RAV4 is a compact crossover SUV that offers a balance of performance, efficiency, and practicality. With a range of powertrain options, including a hybrid, and advanced safety features, it is an excellent choice for urban and outdoor adventures alike.", 
                        size="1",
                        margin_top="1px",
                        width="50%",  # Set width to 50% to allocate space for the image on the right
                    ),
                    # Placeholder image for the Toyota RAV4 (replace with actual image URL)
                    rx.image(
                        src="https://www.motortrend.com/files/65a462062936a70008a96cbc/001-2024-toyota-rav4-prime-plug-in-hybrid-front-three-quarters-in-motion.jpg?w=768&width=768&q=75&format=webp",  # Replace this with the image URL
                        width="50%",  # Set width to 50% for equal distribution of space
                        height="auto",
                        margin_top="1px",  # Adjust margin if necessary
                    ),
                ),
            ),
            rx.text("MSRP: $29,250", 
                    size="3",
                    font_weight="bold", 
                    text_decoration="underline",
                    margin_top="1px"),
            # Section for Toyota Corolla Cross
            rx.text("Toyota Corolla Cross", 
                    size="3",
                    font_weight="bold", 
                    margin_top="40px"),  # Additional margin to separate from RAV4
            rx.container(
                rx.hstack(
                    # Description on the left
                    rx.text(
                        "The Toyota Corolla Cross combines the reliability of the Corolla with the versatility of an SUV. Featuring a 2.0-liter engine, ample cargo space, and advanced safety technologies, it is an ideal choice for those seeking an efficient and stylish crossover.", 
                        size="1",
                        margin_top="1px",
                        width="50%",  # Set width to 50% to allocate space for the image on the right
                    ),
                    # Placeholder image for the Toyota Corolla Cross (replace with actual image URL)
                    rx.image(
                        src="https://di-uploads-pod19.dealerinspire.com/hendricktoyotaconcord/uploads/2024/12/mlp-img-perf-2025-corolla-cross.jpg",  # Replace this with the image URL
                        width="50%",  # Set width to 50% for equal distribution of space
                        height="auto",
                        margin_top="1px",  # Adjust margin if necessary
                    ),
                ),
            ),
            rx.text("MSRP: $24,035", 
                    size="3",
                    font_weight="bold", 
                    text_decoration="underline",
                    margin_top="1px"),
        ),
    )