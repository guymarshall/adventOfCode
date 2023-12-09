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
    game_record = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
    ]

    sum_of_powers = 0

    all_game_ids = [int(line.removeprefix('Game ').split(':')[0]) for line in game_record]
    minimum_per_game = {game: 0 for game in all_game_ids}

    for line in game_record:
        line_without_game = line.removeprefix('Game ')
        game_id = int(line_without_game.split(':')[0])
        game_data_raw = line_without_game.split(':')[1]
        game_data = [selection.replace(' ', '') for selection in game_data_raw.split(';')]

        for collection in game_data:
            minimum_colour_count = {
                'red': 0,
                'green': 0,
                'blue': 0
            }

            items = collection.split(',')

            for item in items:
                number = get_number_from_string(item)
                colour = get_colour_from_string(item)

                if number > minimum_colour_count.get(colour):
                    minimum_colour_count.update({colour: number})

            power = minimum_colour_count.get('red') * minimum_colour_count.get('green') * minimum_colour_count.get('blue')
            minimum_per_game.update({
                game_id: power
            })

        sum_of_powers += minimum_per_game.get(game_id)

    print(sum_of_powers)


if __name__ == '__main__':
    main()
