def get_column(file_name, query_column, query_value, result_column=1):
    results = []

    try:
        with open(file_name, "r") as f:
            for line in f:
                fields = line.strip().split(",")
                if fields[query_column] == query_value:
                    try:
                        results.append(int(fields[result_column]))
                    except ValueError:
                        print("Could not convert value to integer")

    except FileNotFoundError:
        print("Could not find file")
    return results
