
"""
Download this then run the file
Don't open this from discord!
"""

import time
import random

print("Before I can wish you Merry Christmas, I gotta first make sure that you're actually Grace.")
time.sleep(2)
print("To do so, complete this crossword. It should be simple if you're her.")
print()
time.sleep(2)
print("The first number indicates column, second is row, and the letter means down or across.")
time.sleep(2)
print("Answer in the format column, row, word, and if it's two words, don't put the space.")
time.sleep(2)
print("e.g. 11 DavidWu")
time.sleep(2)
print()
print("Good luck!")
print()
time.sleep(1)

def main(board):
    answers(board)
    end = False
    while not end:
        display(board)
        guess()
        answers(board)
        end = game_end()
    display(board)
    print()
    time.sleep(1)
    print("Ah, so it is you!")
    time.sleep(2)
    print("Tbh I don't have much to say that you don't already know...")
    time.sleep(2)
    print("So here's the long awaited MERRY CHIRTSMAS BABYYYY!!!")
    time.sleep(1000)
    print("Oh you're still here?")
    

def game_end():
    global answer_list
    game_end = True
    for answer in answer_list:
        if answer[3] == False:
            game_end = False
    return game_end

def questions():
    #Who is Grace and David's Godmother and made it all happen JUDY
    #What's Grace's favourite show to talk about FAMILYGUY
    #What beach did Grace and David spend their first day together at EASTERN
    #What's handsome guy in Chinese SHUAIGE
    #Which princess has a petite frame and small body that exudes something in men NOKIA
    #What can be used to pay Grace to swim HUGS
    #What has been pushed BOULDER
    #Which saiki character is Grace NENDOU
    #Which saiki character is David TERUHASHI

    #FINAL QUESTION
    #Out of Grace and David, who likes the other one more DAVID/GRACE both work
    question1 = "[4,9 a] What's our favourite author's first name"
    question2 = "[4,9 d] On tinder, what do people see you as (It rhymes with laddie)"
    question3 = "[1,5 a] What's the best show to watch while high"
    question4 = "[8,6 d] Who's the most wholeseome lecturer"
    question5 = "[3,2 a] What did you show me when we first met that changed my coding life forever"
    question6 = "[6,3 d] Who's the greatest story-teller of all time"
    question7 = "[4,7 a] What's a nickname for the coolest smartest guy in the world"
    question8 = "[2,6 d] What's the best school subject"
    questions = (question1, question2, question3, question4, question5, question6, question7, question8)
    global answer_list
    for idx in range(len(answer_list)):
        if answer_list[idx][3] == False:
            print(questions[idx])

def display(board):
    for i in range(9):
        string = str(9-i) + ' '
        for j in range(8,-1,-1):
            if board[j][i] == 0:
                string += "  "
            else:
                string += board[j][i] + " "
        print(string)
    print("  1 2 3 4 5 6 7 8 9")
    print()

def answers(board):
    global answer_list
    for idx in range(len(answer_list)):
        answer = answer_list[idx]
        if idx % 2 == 1:
            for letter_idx in range(len(answer[0])):
                if str(board[answer[1]][answer[2] + letter_idx]).isalpha() == True:
                    continue
                elif answer[3] == False:
                    board[answer[1]][answer[2] + letter_idx] = '▢'
                else:
                    board[answer[1]][answer[2] + letter_idx] = answer[0][letter_idx]
        else:
            for letter_idx in range(len(answer[0])):
                if str(board[answer[1] - letter_idx][answer[2]]).isalpha() == True:
                    continue
                if answer[3] == False:
                    board[answer[1] - letter_idx][answer[2]] = '▢'
                else:
                    board[answer[1] - letter_idx][answer[2]] = answer[0][letter_idx]

def guess():
    global answer_list
    check = True
    wrong_answers = ["Not quite...", "Try again!", "Hmm maybe something else", "Nope sorry", "No bruh", "Maybe you spelt it wrong?"]
    questions()
    while check:
        print()
        answer = input("Answer: ")
        answer = answer.strip().upper()
        try:
            row = 9 - int(answer[0])
            column = 9 - int(answer[1])
            word = answer[3:]
            for answer in answer_list:
                if word == answer[0] and row == answer[1] and column == answer[2]:
                    idx = answer_list.index(answer)
                    answer_list[idx][3] = True
                    check = False
            if check == True:
                time.sleep(1)
                print(wrong_answers[random.randrange(len(wrong_answers))])
                time.sleep(1)
        except ValueError:
            print("Answer in the format 'column row word', like '11 David'")
    print()

board = [[0] * 9 for i in range(9)]
answer1 = "BETH"
answer2 = "BADDIE"
answer3 = "FAMILYGUY"
answer4 = "SUDEEP"
answer5 = "VSCODE"
answer6 = "JO"
answer7 = "DAVE"
answer8 = "MATH"
global answer_list
answer_list = [[answer1, 5, 0, False], [answer2, 5, 0, False], [answer3, 8, 4, False], [answer4, 1, 3, False], [answer5, 6, 7, False], [answer6, 3, 6, False], [answer7, 5, 2, False], [answer8, 7, 3, False]]

main(board)