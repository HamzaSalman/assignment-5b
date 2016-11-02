# Created by: Hamza Salman
# Course: ICS3U
# Created: October 2016
# This program is used to play 21 against the computer.

import ui
import random

player_total = 0
computer_total = 0
player_card_one = 0
player_card_two = 0
player_card_three = 0
computer_card_one = 0
computer_card_two = 0
computer_card_three = 0

def play_button_touch_up_inside(sender):
    # this function assigns two cards two the player and three to the computer.
    
    global player_card_one
    global player_card_two
    global player_total
    global computer_total
    
    player_card_one = random.randint(1,10)
    view['first_card_label'].text = str(player_card_one)
    player_card_two = random.randint(1,10)
    view['second_card_label'].text = str(player_card_two)
    
    
    player_total = int(player_card_one) + int(player_card_two)
    view['player_total_label'].text = 'Player Total: ' + str(player_total)
    #print int(player_total)
    
    #print int(computer_total)
    
def draw_button_touch_up_inside(sender):
    #this function checks if the player wants a third card and if so it assigns them one.
    
    global player_total
    global player_card_three
    
    player_card_three = random.randint(1,10)
    view['player_thirdcard_info_label'].text = 'Third card:'
    view['third_card_label'].text = str(player_card_three)
    player_total = int(player_total) + int(player_card_three)
    view['player_total_label'].text = 'Player Total: ' + str(player_total)
    
def check_button_touch_up_inside(sender):
    # this function compares the scores ans shows who wins.
    
    computer_card_one = random.randint(1,10)
    view['computer_first_card_label'].text = str(computer_card_one)
    computer_card_two = random.randint(1,10)
    view['computer_second_card_label'].text = str(computer_card_two)
    computer_card_three = random.randint(1,10)
    view['computer_third_card_label'].text = str(computer_card_three)
    
    computer_total = int(computer_card_one) + int(computer_card_two) + int(computer_card_three)
    view['computer_total_label'].text = 'Computer Total: ' + str(computer_total)
    
    if player_total <= 21:
        if computer_total > 21:
            view['result_label'].text = 'You Win!'
            view['result_label'].color = 'green'
        elif computer_total <= 21:
            if computer_total < player_total:
                view['result_label'].text = 'You Win!'
                view['result_label'].color = 'green'
            elif computer_total > player_total:
                view['result_label'].text = 'You Lose!'
                view['result_label'].color = 'red'
            elif computer_total == player_total:
                view['result_label'].text = 'It is a Tie!'
    if player_total > 21:
        view['result_label'].text = 'You Lose!'
        view['result_label'].color = 'red'
        if computer_total > 21:
            view['result_label'].text = 'You both Lose!'
            view['result_label'].color = 'red'
            
def reset_button_touch_up_inside(sender):
    # This function resets the game.
    
    global player_card_one
    global player_card_two
    global player_card_three
    global computer_card_one
    global computer_card_two
    global computer_card_three
    global player_total
    global computer_total
    
    player_card_one = 0
    player_card_two = 0
    player_card_three = 0
    computer_card_one = 0
    computer_card_two = 0
    computer_card_three = 0
    player_total = 0
    computer_total = 0
    
    view['first_card_label'].text = ''
    view['second_card_label'].text = ''
    view['third_card_label'].text = ''
    view['computer_first_card_label'].text = ''
    view['computer_second_card_label'].text = ''
    view['computer_third_card_label'].text = ''
    view['player_total_label'].text = ''
    view['computer_total_label'].text = ''
    view['result_label'].text = ''
    view['player_thirdcard_info_label'].text = ''
    view['third_card_label'].text = ''

view = ui.load_view()
view.present('fullscreen')
