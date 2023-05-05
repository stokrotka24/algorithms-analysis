def parse_file(filename: str):
    with open(filename, 'r') as f:
        lines = f.readlines()
    title = lines[0]
    data = dict()
    for line in lines[1:]:
        (key, val) = line.split()
        data[int(key)] = int(val)
    return title, data
