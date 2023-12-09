def get_game_record(filename: str) -> list:
    with open(filename) as file:
        lines: list = [line.rstrip() for line in file]

    return lines


def get_number_from_string(string: str) -> int:
    return int(string.replace('red', '').replace('green', '').replace('blue', ''))


def get_colour_from_string(string: str) -> str:
    if string.__contains__('red'):
        return 'red'
    elif string.__contains__('green'):
        return 'green'
    elif string.__contains__('blue'):
        return 'blue'
    else:
        raise RuntimeError('Invalid colour')


def main():
    game_record = get_game_record('game_record.txt')

    limits = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    invalid_games = []

    for line in game_record:
        line_without_game = line.removeprefix('Game ')
        game_id = int(line_without_game.split(':')[0])
        game_data_raw = line_without_game.split(':')[1]
        game_data = [selection.replace(' ', '') for selection in game_data_raw.split(';')]

        for collection in game_data:
            items = collection.split(',')

            for item in items:
                number = get_number_from_string(item)
                colour = get_colour_from_string(item)

                if number > limits.get(colour) and game_id not in invalid_games:
                    invalid_games.append(game_id)
                    break

    all_game_ids = [int(line.removeprefix('Game ').split(':')[0]) for line in game_record]

    possible_games = [game for game in all_game_ids if game not in invalid_games]

    print(sum(possible_games))


if __name__ == '__main__':
    main()
