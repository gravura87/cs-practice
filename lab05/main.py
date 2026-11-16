from pathlib import Path
from tablestats import read_rows, count_types, total_minutes, to_csv

folder = Path(__file__).parent

filename = input().strip()

with open(folder / filename, encoding="utf-8") as table:
    rows = read_rows(table)

counts = count_types(rows)

print(len(rows))
print(len(counts))
print(total_minutes(rows, "ошибка"))

with open(folder / "summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))