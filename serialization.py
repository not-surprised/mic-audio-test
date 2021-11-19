def serialize(data: list[list[float]]):
    lines = [','.join(map(repr, lst)) for lst in data]
    with open('data.csv', 'w') as f:
        f.write('\n'.join(lines))


def deserialize() -> list[list[float]]:
    with open('data.csv', 'r') as f:
        lines = f.readlines()
    data = [[float(x) for x in line.split(',')] for line in lines]
    return data


if __name__ == '__main__':
    a = [[1.,2.,3.],[4.,5.,6.],[1.23,4.56,7.89]]
    serialize(a)
    b = deserialize()
    print(a)
    print(b)
    print(a == b)
