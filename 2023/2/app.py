def get_game_record(filename: str) -> list:
    with open(filename) as file:
        lines: list = [line.rstrip() for line in file]

    return lines


def main():
    game_record = get_game_record('game_record.txt')
    game_record = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
    ]

    id_sum = 0

    limits = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    for line in game_record:
        line_without_game = line.removeprefix('Game ')
        game_id = int(line_without_game.split(':')[0])
        game_data_raw = line_without_game.split(':')[1]
        game_data = [selection.replace(' ', '') for selection in game_data_raw.split(';')]

        for collection in game_data:
            items = collection.split(',')
            print(items)


if __name__ == '__main__':
    main()
