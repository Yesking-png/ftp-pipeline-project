import csv
import random

valid_names    = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
valid_statuses = ["active", "inactive", "pending"]

# Automatically generate good CSV using a loop
with open("good_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "email", "status"])
    for i in range(1, 11):
        name   = random.choice(valid_names)
        status = random.choice(valid_statuses)
        writer.writerow([i, name, f"{name.lower()}{i}@company.com", status])
        print(f"Row {i}: {name} | {name.lower()}{i}@company.com | {status}")

print("\ngood_data.csv generated successfully")
