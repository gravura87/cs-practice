def read_rows(lines):
    rows = []
    header = None

    for line in lines:
        line = line.strip()

        if not line:
            continue

        values = [value.strip() for value in line.split(",")]

        if header is None:
            header = values
            continue

        if len(values) != len(header):
            continue

        row = dict(zip(header, values))
        rows.append(row)

    return rows


def count_types(rows):
    counts = {}

    for row in rows:
        kind = row["тип"]

        if kind not in counts:
            counts[kind] = 0

        counts[kind] += 1

    return counts


def total_minutes(rows, kind):
    total = 0.0

    for row in rows:
        if row["тип"] == kind:
            try:
                minutes = float(row["минуты"].replace(",", "."))
                total += minutes
            except ValueError:
                continue

    return round(total, 1)


def to_csv(counts):
    result = "тип,количество\n"

    for kind in sorted(counts):
        result += f"{kind},{counts[kind]}\n"

    return result