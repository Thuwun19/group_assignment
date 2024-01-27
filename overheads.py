import csv
from pathlib import Path

filepath = Path.cwd()/"csv_reports"/"overheads-day-90.csv"
with filepath.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    overheads_data = list(reader)


def overheads():
    highest_overhead_category = max(overheads_data)
    output = (f"[HIGHEST OVERHEAD] {highest_overhead_category[0]}:{highest_overhead_category[1]}%\n")
    return output

# overheads()
# print(type(overheads()))

# print(type(overheads()))