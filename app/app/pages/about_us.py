import reflex as rx
from ..state import State
from ..components import navigation_bar

@rx.page(route="/about_us")
def about_us_page() -> rx.Component:
    return rx.container(
        navigation_bar(),
        rx.vstack(
            # Hero Image
            rx.image(
                src="https://blogmedia.dealerfire.com/wp-content/uploads/sites/767/2022/03/2021-Toyota-Tacoma_o.jpg",
                width="1280px",
                height="auto",
            ),
            
            # About Us Content
            rx.heading("About Toyota", size="1", margin_top="20px"),  # Adjusted size to a valid value
            rx.text("🚗🌍 Driven by Innovation, Built for the Future", size="2", font_weight="bold"),  # Adjusted size to a valid value
            
            rx.text(
                "Founded in 1937 by Kiichiro Toyoda, Toyota Motor Corporation has grown from a small Japanese automaker "
                "into a global leader in mobility and innovation. Headquartered in Toyota City, Japan, we are committed "
                "to producing high-quality, reliable, and sustainable vehicles that redefine driving experiences.",
                text_align="justify",
            ),

            rx.heading("What We’re Known For", size="2", margin_top="15px"),  # Adjusted size to a valid value
            rx.unordered_list(
                rx.list_item("✅ Reliability & Quality: Our legendary models, including the Toyota Corolla, Camry, and Land Cruiser, "
                             "have set industry standards for durability and performance."),
                rx.list_item("✅ Hybrid & Electric Innovation: Toyota revolutionized the automotive world with the Prius, the first mass-produced "
                             "hybrid vehicle, and continues to lead in hydrogen fuel-cell and electric vehicle (EV) technologies with models like "
                             "the Toyota Mirai and bZ4X."),
                rx.list_item("✅ Safety & Sustainability: Our Toyota Safety Sense (TSS) technology ensures advanced driver assistance, while our commitment "
                             "to a carbon-neutral future drives innovations in green mobility."),
            ),

            rx.heading("Awards & Recognitions 🏆", size="2", margin_top="15px"),  # Adjusted size to a valid value
            rx.unordered_list(
                rx.list_item("🌟 J.D. Power Awards – Recognized for vehicle dependability and customer satisfaction."),
                rx.list_item("🌟 Green Car of the Year – Honored for our commitment to sustainability and fuel efficiency."),
                rx.list_item("🌟 IIHS & NHTSA Top Safety Ratings – Awarded for excellence in vehicle safety."),
                rx.list_item("🌟 Fortune’s Most Admired Companies – Ranked among the world's most respected brands."),
            ),

            rx.heading("The Road Ahead 🚀", size="2", margin_top="15px"),  # Adjusted size to a valid value
            rx.text(
                "At Toyota, we are shaping the future of mobility with autonomous driving, AI-driven transportation, and "
                "next-generation vehicle technology. Our mission is to create a better, more connected, and environmentally "
                "conscious world—one innovation at a time.",
                text_align="justify",
            ),
        ),
        padding="40px",
    )