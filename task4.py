import json

def csv_to_list_dict(filename, delimiter = ",", new_line = "\n") -> list[dict]:
    with open(filename, 'r') as f:
        data = [line.replace(new_line, '').split(delimiter) for line in f]
        headers = data[0]
        num = len(data)
    list_ = []
    for i in range(1, num):
        result = dict(zip(headers, data[i]))
        list_.append(result)
    return list_

INPUT_FILE = "input.csv"

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
