import csv
import random

invalid_names    = ["", "1234", "???", "NULL"]
invalid_statuses = ["", "unknown", "NULL", "expired"]

# Automatically generate bad CSV using a loop
with open("bad_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "email", "status"])
    for i in range(1, 11):
        name   = random.choice(invalid_names)
        status = random.choice(invalid_statuses)
        writer.writerow([i, name, f"invalid_email_{i}", status])
        print(f"Row {i}: '{name}' | invalid_email_{i} | '{status}'")

print("\nbad_data.csv generated successfully")
