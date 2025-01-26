import reflex as rx


class State(rx.State):
    """The app state."""


    def on_home_page(self):
        return rx.redirect("/home")
    ...