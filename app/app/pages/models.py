import reflex as rx
from ..state import State
from ..vehicle import Vehicle

def show_vehicle(vehicle: Vehicle):
    """Show a vehicle in a table row."""
    return rx.table.row(
        rx.table.cell(vehicle.vclass),
        rx.table.cell(vehicle.basemodel),
        rx.table.cell(vehicle.model),
        rx.table.cell(vehicle.year),
        rx.table.cell(vehicle.trany),  # Fixed attribute name
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


@rx.page(route="/models")
def models_page() -> rx.Component:
    """Render the models page."""
    return sorting_table_example()
