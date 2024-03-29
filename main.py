if __name__ == "__main__":
    length = int(input().split()[0])
    middle = length // 2
    coordinates = {'x': 0, 'y': 0}
    while coordinates['y'] < length:
        while coordinates['x'] < length:
            if coordinates['y'] == middle and coordinates['x'] == middle - 1:
                print("-WELCOME-", end="")
                coordinates['x'] += 2
            elif (coordinates['y'] != middle and
                  abs(coordinates['x'] - middle) + abs(coordinates['y'] - middle) <= middle):
                print(".|.", end="")
            else:
                print("---", end="")
            coordinates['x'] += 1
        print("")
        coordinates['y'] += 1
        coordinates['x'] = 0
