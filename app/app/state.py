import reflex as rx
import sqlite3
import os

from .vehicle import Vehicle

class State(rx.State):
    """The app state."""

    vehicles: list[Vehicle] = []

    def populate_cars(self):
        """
        Reads rows from toyota.db and populates self.vehicles.
        Be sure toyota.db was created/populated first by populate.py.
        """
        # Adjust the path as needed. If toyota.db is at the project root:
        db_path = os.path.join(os.path.dirname(__file__), "..", "..", "toyota.db")

        if not os.path.exists(db_path):
            print(f"Database not found at {db_path}. Did you run populate.py?")
            return

        # 1. Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 2. Query the columns
        query = """
        SELECT
            vclass,
            basemodel,
            model,
            year,
            fueltype1,
            trany,
            drive,
            yousavespend,
            cylinders,
            displ
        FROM toyota_cars
        """

        rows = cursor.execute(query).fetchall()
        conn.close()

        # 3. Clear any previously loaded vehicles (if desired)
        self.vehicles.clear()

        # 4. Convert each row into a Vehicle object
        for row in rows:
            (
                vclass,
                basemodel,
                model_name,
                year_str,
                fueltype1_str,
                trany,
                drive,
                yousavespend_str,
                cylinders_str,
                displ_str,
            ) = row

            # Safely parse numeric fields
            try:
                year_val = int(year_str)
            except:
                year_val = 0

            try:
                yousavespend_val = int(yousavespend_str)
            except:
                yousavespend_val = 0

            try:
                cylinders_val = int(cylinders_str)
            except:
                cylinders_val = 0

            try:
                displ_val = float(displ_str)
            except:
                displ_val = 0.0

            # Create a Vehicle object
            vehicle = Vehicle(
                vclass=vclass,
                basemodel=basemodel,
                model=model_name,
                year=year_val,
                fueltype1=fueltype1_str,
                trany=trany,
                drive=drive,
                yousavespend=yousavespend_val,
                cylinders=cylinders_val,
                displ=displ_val,
            )

            # 5. Append to the list
            self.vehicles.append(vehicle)

        print(f"Loaded {len(self.vehicles)} vehicles from {db_path}.")




    def on_home_page(self):
        return rx.redirect("/")
    
    def on_models_page(self):
        return rx.redirect("/models")
    
    def on_compare_page(self):
        return rx.redirect("/compare")
    
    def on_about_us_page(self):
        return rx.redirect("/about_us")
    ...
