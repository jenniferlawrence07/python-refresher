def get_column(file_name, query_column, query_value, result_column=1):
    results = []

    try:
        with open(file_name, "r") as f:
            for line in f:
                fields = line.strip().split(",")

                if fields[query_column] == query_value:
                    try:
                        results.append(int(float(fields[result_column])))
                    except ValueError:
                        print("Could not convert value to integer")

    except FileNotFoundError:
        print("Could not find file")

    return results


def find_mean(values):
    return sum(values) / len(values)


def find_median(values):
    sorted_values = sorted(values)
    middle = len(sorted_values) // 2

    if len(sorted_values) % 2 == 1:
        return sorted_values[middle]

    return (
        sorted_values[middle - 1] + sorted_values[middle]
    ) / 2


def find_std(values):
    mean = find_mean(values)

    squared_differences = [
        (value - mean) ** 2
        for value in values
    ]

    variance = sum(squared_differences) / len(values)

    return variance ** 0.5
