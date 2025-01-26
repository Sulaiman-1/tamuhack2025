from .pages.home import home_page
from .pages.compare import compare_page
from .pages.models import models_page
from .pages.about_us import about_us_page
import reflex as rx



app = rx.App()
app.add_page(home_page)
app.add_page(models_page)
app.add_page(compare_page)
app.add_page(about_us_page)
