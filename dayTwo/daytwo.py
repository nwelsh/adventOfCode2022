max_red = 12
max_green = 13
max_blue = 14
possible_games = set()

with open('test2.txt') as fp:
    lines = fp.readlines()
    for entry in lines:
        game_number = int(entry.partition(':')[0].split(' ')[1])
        games = entry.partition(':')[2].split(';')
        game_possible = True
        for game in games:
            red = 0
            blue = 0
            green = 0
            subsets = game.split(", ")
            for subset in subsets:
                cubes = subset.split()
                cube_color = cubes[-1]
                cube_count = int(cubes[0])
                if cube_color == 'red':
                    red += cube_count
                elif cube_color == 'blue':
                    blue += cube_count
                elif cube_color == 'green':
                    green += cube_count

            if red > max_red or green > max_green or blue > max_blue:
                game_possible = False
                break
        
        if game_possible:
            possible_games.add(game_number)

sum_of_possible_game_ids = sum(possible_games)
print(sum_of_possible_game_ids)
