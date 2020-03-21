import random
from sty import fg, bg, ef, rs

def print_gold(gold):
    print(fg(45) + "Current amount of gold: " + str(gold) + "\n" + fg.rs)
    print()

def print_menu(gold):
    f = open("art.txt", "r")
    content = f.read()
    print(fg(209) + content + fg.rs)
    print_gold(gold)

def get_input(input):
    split_int = input.split(" ")
    if len(split_int) > 2:
        return False
    if split_int[0] != "/roll":
        return False
    gold = split_int[1]
    if gold.isdigit() == False :
        return False

    return int(gold)

def gold_check(gold):
    if gold == 0:
        return False
    return True

def game_start(gold):
    print_menu(gold)

def game_console():

    player_gold = 10
    turn = "Player"
    game = True
    bet_amount = 0
    game_start(player_gold)
    first_move = True

    while game:

        if turn == "Player":

            if first_move:
                command = input(">>>")
                if get_input(command) == False:
                    print(fg(124) + "Roll not valid !\n" + fg.rs)
                    turn = "Player"
                else:
                    amount = get_input(command)

                    if amount > player_gold * 10:
                        print(fg(124) + "Not enough gold !\n" + fg.rs)
                        turn = "Player"
                    else:
                        player_gold = player_gold - amount // 10
                        bet_amount = 2 * (amount // 10)
                        first_move = False
                        new_roll = random.randint(1, amount)
                        print(fg(220) + "You rolled: " + str(new_roll) + " out of " + str(amount) + fg.rs)
                        turn = "AI"

            else:
                command = input(">>>")
                if get_input(command) == False:
                    print(fg(124) + "Roll not valid !\n" + fg.rs)
                    turn = "Player"
                else:
                    amount = get_input(command)

                if amount != roll:
                    print(fg(124) + "Roll not in the right interval !\n" + fg.rs)
                    turn = "Player"
                else:
                    new_roll = random.randint(1, roll)
                    print(fg(220) + "You rolled: " + str(new_roll) + " out of " + str(roll) + fg.rs)
                    turn = "AI"

                    if new_roll == 1:
                        if roll - new_roll > 20:
                            print(fg(93) + "THAT'S ROUGH BUDDY\n" + fg.rs)
                        if gold_check(player_gold) == False:
                            print()
                            print(fg(201) + "You're out of gold  :'(" + fg.rs)
                            game = False
                        else:
                            print_gold(player_gold)
                            turn = "Player"
                            first_move = True

        elif turn == "AI":

            roll = random.randint(1, new_roll)
            print(fg(220) + "The A.I. rolled: " + str(roll) + " out of " + str(new_roll) + fg.rs)
            turn = "Player"
            if roll == 1:
                player_gold += bet_amount
                print_gold(player_gold)
                first_move = True

game_console()
