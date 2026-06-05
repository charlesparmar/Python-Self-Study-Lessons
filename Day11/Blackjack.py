import random

def deal_card():
    """This function deals a card randomly."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """This function is defined with a purpose to calculate the score of the cards that are dealt.
    Therefore, after this function will take arguments as card (which are dealt).
    This funciton will use the sum function on the list of cards.
    if anyone has got blackjack and second is if there is an 11 in one of the dealt cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(sample_u_score, sample_c_score):
    """This function will compare the scores for user and computer and decide on the outcome.
    The order in which the conditions are defined is important."""
    if sample_u_score == sample_c_score:
        return "It's a tie!"
    elif sample_u_score == 0:
        return "You got a BLACKJACK and You win!"
    elif sample_c_score == 0:
        return "Computer got a BLACKJACK and You Lose!"
    elif sample_u_score > 21:
        return "You went over and You lose!"
    elif sample_c_score > 21:
        return "Computer went over and You Win!"
    elif sample_u_score > sample_c_score:
        return "You win!"
    else:
        return "You Lose!"

def play_blackjack():
    user_score = -1
    computer_score = -11
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are {user_cards} and your score is {user_score}")
        print(f"                                                           Computer's first card is {computer_cards[0]}")

        if user_score > 21 or user_score == 0 or computer_score == 0:
            is_game_over = True
        else:
            should_user_deal = input(f"""Do you want to draw another card? y for yes of n for no  
            
            """).lower()
            if should_user_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
                if user_score > 21:
                    print(f"You went over and You lose!")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards are {user_cards} and your score is {user_score}")
    print(f"                                                                  Computer's final cards are {computer_cards} and Computer's score is {computer_score}")
    print(f"""{compare(user_score, computer_score)}
    
    
    """)

while input("Do you want to play the Blackjack game (y/n)? ").lower() == "y":
    print("\n" * 200)
    play_blackjack()
