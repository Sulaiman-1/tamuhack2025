import reflex as rx


class State(rx.State):
    """The app state."""

    def on_home_page(self):
        return rx.redirect("/")
    
    def on_models_page(self):
        return rx.redirect("/models")
    
    def on_compare_page(self):
        return rx.redirect("/compare")
    
    def on_about_us_page(self):
        return rx.redirect("/about_us")
    ...