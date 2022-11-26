import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as f:
        t = []
        for ind, line in enumerate(f):
            fields = line.strip(new_line).split(delimiter)
            if ind == 0:
                heads = fields
                continue

            t.append({})

            for i, _ in enumerate(heads):
                t[-1][heads[i]] = fields[i]
    return t


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


