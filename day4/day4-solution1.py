import day4.BingoGame as bg
import day4.BingoTable as bt

input_location: str = "day4-input.txt"


def solution():
    my_game = bg.BingoGame(input_location)

    for game_number in my_game.game_numbers:
        my_game.play_number(game_number)

    first_winner = my_game.game_winners[0]
    first_winner_score = solution1_1_calculate_score(first_winner)

    last_winner = my_game.game_winners[-1]
    last_winner_score = solution1_1_calculate_score(last_winner)

    print("FIRST Winner!!!!\n")
    print(first_winner)
    print(f" - Table score = {first_winner_score}")

    print("LAST Winner!!!!\n")
    print(last_winner)
    print(f" - Table score = {last_winner_score}")


def solution1_1_calculate_score(game_board: bt.BingoTable) -> int:
    total_non_marked = 0
    for i in range(len(game_board.positions_marked)):
        for j in range(len(game_board.positions_marked[i])):
            if game_board.positions_marked[i][j] == 0:
                total_non_marked += game_board.table_numbers[i][j]

    last_number_played = game_board.numbers_played[-1]
    final_score = total_non_marked * last_number_played

    return final_score


solution()
