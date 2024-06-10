import time

answers = ["FISHING", "MONSTERS", "YOGA", "DAVID", "AMY", "TERUHASHI", "KUBZ", "PENGUIN", "GRACE", "BOULDER", "FAMILYGUY", "NENDOU", "EASON", "SPRAINED", "JUDY", "MINESWEEPER", "HARDING", "KAIDO", "DUDE", "HUGS", "PIE", "NAP", "CAT"]

questions_down = ["[1,3] Grace's favourite show to talk about", "[3,5] Which Saiki character is Grace", "[3,8] Grace's guy best friend", "[3,10] What happened to Judy's ankle during badminton", "[4,12] Who is Grace and David's Godmother and made it all happen", "[5,15] What did Grace ask David about as a pretext to get ins", "[8,1] Grace's favourite cryptid", "[7,17] Which Saiki character is Riley", "[9,6] What Grace says where David would say 'Bro'", "[9,13] What can be used to pay Grace to swim", "[12,5] What was the first thing David bought Grace", "[12,7] What Grace does after she gets home from work", "[13,3] Grace's favourite animal"]
questions_across = ["[1,3] A genre of video John watches", "[3,3] My Singing", "[6,7] If you rearrange the letters in The Killer or Clyde you lowkey get ____ Master...", "[6,12] Who's the coolest smartest handsomest guy in the world", "[9,1] Grace's girl best friend", "[9,9] Which Saiki character is David", "[10,5] Which scout is Grace's favourite Youtuber", "[12,5] Club _______", "[14,1] Who's the cutest funniest most interesting girl in the world that deserves more than this life can offer", "[15,9] What has been pushed"]

NUM_QS_ACROSS = len(questions_across)
NUM_QS_DOWN = len(questions_down)

NUM_QS = NUM_QS_DOWN + NUM_QS_ACROSS

answer_information = [[int(questions_across[i][1 : questions_across[i].index(",")]), int(questions_across[i][questions_across[i].index(",") + 1 : questions_across[i].index("]")]), False] for i in range(NUM_QS_ACROSS)]
answer_information += [[int(questions_down[i][1 : questions_down[i].index(",")]), int(questions_down[i][questions_down[i].index(",") + 1 : questions_down[i].index("]")]), False] for i in range(NUM_QS_DOWN)]

COLUMNS = 17
ROWS = 15
board = [[" "] * COLUMNS for i in range(ROWS)]

hollow_square = "\u25A2"


def main():
    intro()
    game_on = True
    correct_across_answers = [0]
    correct_down_answers = [0]

    wrong_answer_index = [0]
    right_answer_index = [0]

    while game_on:
        generate_board()
        display_board()
        display_questions(correct_across_answers, correct_down_answers)
        game_on = guess_input(correct_across_answers, correct_down_answers, wrong_answer_index, right_answer_index)
    
    end()

def intro():
    print("Before I can wish you a happy valentine's day, I gotta first make sure that you're actually Grace.")
    time.sleep(3)
    print("To do so, complete this crossword. It should be simple if you're her.")
    print()
    time.sleep(3)
    print("The first number indicates row, and the second is column")
    time.sleep(2)
    print("Answer in the format 'row, column word', and if it's two words, don't put the space.")
    time.sleep(3)
    print("e.g. 3, 10 DavidWu")
    time.sleep(2)
    print()
    print("Good luck!")
    print()
    time.sleep(2) 

def end():
    time.sleep(1)
    print("Ah, so it is you!")
    time.sleep(2)
    print("Tbh I don't have much to say that you don't already know...")
    time.sleep(2)
    print("So here's the long awaited HAPPY VALENTINE'S DAY BABYYYY!!!")
    time.sleep(1000)
    print("Oh you're still here?")


def generate_board():
    for i in range(NUM_QS):
        answer = answers[i]
        start_pos = [answer_information[i][0] - 1, answer_information[i][1] - 1]

        for letter_idx in range(len(answer)):
            if i < NUM_QS_ACROSS:
                current_board_pos = (start_pos[0], start_pos[1] + letter_idx)
            else:
                current_board_pos = (start_pos[0] + letter_idx, start_pos[1])

            if answer_information[i][2] == True or board[current_board_pos[0]][current_board_pos[1]] != " " and board[current_board_pos[0]][current_board_pos[1]] != hollow_square:
                board[current_board_pos[0]][current_board_pos[1]] = answer[letter_idx]
            else:
                board[current_board_pos[0]][current_board_pos[1]] = hollow_square

def display_board():
    for row in range(1, ROWS + 1):
        string = str(row) + ' '
        if row < 10:
            string += ' '
        for column in range(COLUMNS):
                string += board[row - 1][column] + "  "
        
        print(string)
        print()

    print("   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17\n")

def display_questions(correct_across_answers, correct_down_answers):
    if correct_across_answers[0] < NUM_QS_ACROSS:
        print("ACROSS:")
        for i in range(NUM_QS_ACROSS):
            if answer_information[i][2] == False:
                print(questions_across[i])
    
        print()
    if correct_down_answers[0] < NUM_QS_DOWN:
        print("DOWN:")
        for i in range(NUM_QS_DOWN):
            if answer_information[i + NUM_QS_ACROSS][2] == False:
                print(questions_down[i])

def guess_input(correct_across_answers, correct_down_answers, wrong_answer_index, right_answer_index):
    guessing = True

    wrong_answer_replies = ["Not quite...", "Try again!", "Hmm maybe something else", "Nope sorry", "No bruh", "Maybe you spelt it wrong?", "1 IQ response", "You weren't supposed to get this many wrong...", "That's wrong, but just a typo right? Haha...", "How do you not know this :("]
    right_answer_replies = ["Okay so you know that, but I'm still not convinced", "YAY NICE", "You're so smart", "That's correct!", "Put that on bible", "GOOD JOB!!!", "Right answer, baby!", "You're on fire!", "You're killing it!!!", "YAYAYAYAYAYY", "NICE! I'm starting to believe you...", "Awww you remembered that?", "Sweet angel baby princess got it right!", "ANOTHER ONE CORRECT!", "Indeed.", "1 trillion IQ response", "Ofc my baby would know that :)", "Holy, nice", "I'm impressed", "BRAVO EVERYBODY, BRAVO", "Wonderful answer, fabulous work", "CORRECT, now just one more..."]

    while guessing:
        print()
        answer = input("Answer: ")
        answer = answer.strip().upper()
        try:
            row = int(answer[:answer.index(",")].strip())
            column = int(answer[answer.index(",") + 1 : answer.rfind(" ")].strip())
            word = answer[answer.rfind(" "):].strip()
            if word in answers:
                answer_idx = answers.index(word)
                if row == answer_information[answer_idx][0] and column == answer_information[answer_idx][1]:
                    answer_information[answer_idx][2] = True
                    guessing = False
                    if answer_idx < NUM_QS_ACROSS:
                        correct_across_answers[0] += 1
                    else:
                        correct_down_answers[0] += 1

            if correct_across_answers[0] + correct_down_answers[0] == NUM_QS:
                return False
            
            time.sleep(1)
            if guessing == True:
                print(wrong_answer_replies[wrong_answer_index[0] % len(wrong_answer_replies)])
                wrong_answer_index[0] += 1
            else:
                print(right_answer_replies[right_answer_index[0] % len(right_answer_replies)])
                right_answer_index[0] += 1
            time.sleep(1)

        except ValueError:
            print("Answer in the format 'row, column word', like '1, 12 Hi'")
    print()
    return True

main()