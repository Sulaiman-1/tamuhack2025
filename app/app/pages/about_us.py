import reflex as rx
from ..state import State

@rx.page(route="/about_us", on_load=State.on_about_us_page)
def about_us_page() -> rx.Component:
    return rx.hstack(
        
    )