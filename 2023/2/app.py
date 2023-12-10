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

    sum_of_powers = 0

    all_game_ids = [int(line.removeprefix('Game ').split(':')[0]) for line in game_record]
    minimum_per_game = {game: 0 for game in all_game_ids}

    for line in game_record:
        line_without_game = line.removeprefix('Game ')
        game_id = int(line_without_game.split(':')[0])
        game_data_raw = line_without_game.split(':')[1]
        game_data = [selection.replace(' ', '') for selection in game_data_raw.split(';')]

        minimum_per_line = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

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

            if minimum_colour_count.get('red') > minimum_per_line.get('red'):
                minimum_per_line.update({
                    'red': minimum_colour_count.get('red')
                })

            if minimum_colour_count.get('green') > minimum_per_line.get('green'):
                minimum_per_line.update({
                    'green': minimum_colour_count.get('green')
                })

            if minimum_colour_count.get('blue') > minimum_per_line.get('blue'):
                minimum_per_line.update({
                    'blue': minimum_colour_count.get('blue')
                })

        power = minimum_per_line.get('red') * minimum_per_line.get('green') * minimum_per_line.get('blue')
        minimum_per_game.update({
            game_id: power
        })

        sum_of_powers += minimum_per_game.get(game_id)

    print(sum_of_powers)


if __name__ == '__main__':
    main()
