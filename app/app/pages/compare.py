import reflex as rx
from ..state import State
from ..components import navigation_bar

from ..vehicle import Vehicle

def show_vehicle(vehicle: Vehicle):
    """Show a vehicle in a table row."""
    return rx.table.row(
        rx.table.cell(vehicle.vclass),
        rx.table.cell(vehicle.basemodel),
        rx.table.cell(vehicle.model),
        rx.table.cell(vehicle.year),
        rx.table.cell(vehicle.trany),
        rx.table.cell(vehicle.drive),
        rx.table.cell(vehicle.yousavespend),
        rx.table.cell(vehicle.cylinders),
        rx.table.cell(vehicle.displ)  # Fixed attribute name
    )


def sorting_table_example():
    """Render the table with vehicle details."""
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Vehicle Class"),
                    rx.table.column_header_cell("Base Model"),
                    rx.table.column_header_cell("Model"),
                    rx.table.column_header_cell("Year"),
                    rx.table.column_header_cell("Transmission"),
                    rx.table.column_header_cell("Drive"),
                    rx.table.column_header_cell("Save-Spend"),
                    rx.table.column_header_cell("Cylinders"),
                    rx.table.column_header_cell("Displ"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State.vehicles,  # Provide the list of vehicles to iterate over
                    show_vehicle,    # Render each vehicle using this function
                )
            ),
            width="100%",
        ),
        width="100%",
    )

@rx.page(route="/compare")
def compare_page() -> rx.Component:
    return rx.container(
        navigation_bar(),
        rx.hstack(
            rx.input(
                placeholder="Enter category...",
                on_change=State.set_category,
                value=State.category_entry,
                width="300px"
            ),
            rx.input(
                placeholder="Enter item...",
                on_change=State.set_item,
                value=State.item_entry,
                width="300px"
            ),
            rx.button(
                "search",
                background_color="maroon",
                color="white",
                on_click=State.filter_vehicles,
            ),
            justify_content="center",
            padding="20px"
        ),
        sorting_table_example()
    )
