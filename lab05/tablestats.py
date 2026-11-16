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