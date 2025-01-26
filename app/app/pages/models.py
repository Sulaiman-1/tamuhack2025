import reflex as rx
from ..state import State
import dataclasses

@dataclasses.dataclass
class Vehicle:
    year: str
    model: str
    vehicle_type: str
    transmission: str
    cylinder: str


class TableSortingState(rx.State):
    _vehicles: list[Vehicle] = [
        Vehicle(
            year="2020",
            model="Camry",
            vehicle_type="Sedan",
            transmission="Automatic",
            cylinder="4",
        ),
        Vehicle(
            year="2022",
            model="RAV4",
            vehicle_type="SUV",
            transmission="Automatic",
            cylinder="6",
        ),
        Vehicle(
            year="2019",
            model="Tacoma",
            vehicle_type="Truck",
            transmission="Manual",
            cylinder="6",
        ),
    ]

    sort_value = ""
    search_value = ""

    @rx.var(cache=True)
    def current_vehicles(self) -> list[Vehicle]:
        vehicles = self._vehicles

        if self.sort_value != "":
            vehicles = sorted(
                vehicles,
                key=lambda vehicle: getattr(
                    vehicle, self.sort_value
                ).lower(),
            )

        if self.search_value != "":
            vehicles = [
                vehicle
                for vehicle in vehicles
                if any(
                    self.search_value
                    in getattr(vehicle, attr).lower()
                    for attr in [
                        "year",
                        "model",
                        "vehicle_type",
                        "transmission",
                        "cylinder",
                    ]
                )
            ]
        return vehicles


def show_vehicle(vehicle: list):
    """Show a vehicle in a table row."""
    return rx.table.row(
        rx.table.cell(vehicle.year),
        rx.table.cell(vehicle.model),
        rx.table.cell(vehicle.vehicle_type),
        rx.table.cell(vehicle.transmission),
        rx.table.cell(vehicle.cylinder),
    )


def sorting_table_example():
    return rx.vstack(
        rx.select(
            ["year", "model", "vehicle_type", "transmission", "cylinder"],
            placeholder="Sort By: year",
            on_change=TableSortingState.set_sort_value,
        ),
        rx.input(
            placeholder="Search here...",
            on_change=TableSortingState.set_search_value,
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Year"),
                    rx.table.column_header_cell("Model"),
                    rx.table.column_header_cell("Vehicle Type"),
                    rx.table.column_header_cell("Transmission"),
                    rx.table.column_header_cell("Cylinder"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    TableSortingState.current_vehicles,
                    show_vehicle,
                )
            ),
            width="100%",
        ),
        width="100%",
    )

@rx.page(route="/models")
def models_page() -> rx.Component:
    return sorting_table_example()
