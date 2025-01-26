#!/usr/bin/env python3

import os
import requests
import sqlite3

API_URL = "https://public.opendatasoft.com/api/records/1.0/search/"
PARAMS = {
    "dataset": "all-vehicles-model",
    "q": "",
    "rows": 300,
    "refine.make": "Toyota",
}


def populate_toyota_db(db_path="toyota.db"):
    """
    1. Delete the existing sqlite database file if present.
    2. Fetch Toyota data from OpenDataSoft.
    3. Insert records in the following column order:

       id, vclass, basemodel, model, year, fueltype1, trany,
       drive, yousavespend, engid, eng_dscr, cylinders, displ
    """

    # 1. Delete the DB file if it already exists
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Deleted existing DB file: {db_path}")

    # 2. Connect to/create the new SQLite DB
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 3. Create the toyota_cars table with the new column order
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS toyota_cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vclass TEXT,
            basemodel TEXT,
            model TEXT,
            year TEXT,
            fueltype1 TEXT,
            trany TEXT,
            drive TEXT,
            yousavespend TEXT,
            engid TEXT,
            eng_dscr TEXT,
            cylinders TEXT,
            displ TEXT
        );
    """)

    # 4. Fetch up to 300 Toyota records from OpenDataSoft
    response = requests.get(API_URL, params=PARAMS)
    response.raise_for_status()
    data = response.json()
    records = data.get("records", [])

    # 5. Parse each record for the specified columns
    entries = []
    for record in records:
        fields = record.get("fields", {})

        # We store each field in the new order
        vclass = fields.get("vclass", "")
        basemodel = fields.get("basemodel", "")
        model = fields.get("model", "Unknown")
        year = fields.get("year", "Unknown")
        fueltype1 = fields.get("fueltype1", "")
        trany = fields.get("trany", "")
        drive = fields.get("drive", "")
        yousavespend = str(fields.get("yousavespend", ""))

        engid = str(fields.get("engid", ""))

        # eng_dscr can be a list (e.g., ["FFS", "TRBO"]) so we'll join them
        eng_dscr_raw = fields.get("eng_dscr", [])
        if isinstance(eng_dscr_raw, list):
            eng_dscr = ", ".join(eng_dscr_raw)
        else:
            eng_dscr = str(eng_dscr_raw)

        cylinders = str(fields.get("cylinders", ""))
        displ = str(fields.get("displ", ""))

        # Append in the exact order matching the CREATE TABLE statement (minus 'id')
        entries.append((
            vclass,
            basemodel,
            model,
            year,
            fueltype1,
            trany,
            drive,
            yousavespend,
            engid,
            eng_dscr,
            cylinders,
            displ
        ))

    # 6. Insert the rows into the DB with the columns in that same order
    cursor.executemany(
        """
        INSERT INTO toyota_cars (
            vclass, basemodel, model, year, fueltype1, trany,
            drive, yousavespend, engid, eng_dscr, cylinders, displ
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        entries
    )

    conn.commit()
    conn.close()

    print(f"Inserted {len(entries)} Toyota records into '{db_path}'.")


if __name__ == "__main__":
    populate_toyota_db()
