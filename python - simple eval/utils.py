import eval7
import numpy as np

ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
suits = ('c', 'd', 'h', 's')


def get_full_deck():
    cards = []
    for rank in ranks:
        for suit in suits:
            card = rank + suit
            cards.append(card)
    return cards


def get_deck_with_exceptions(exceptions):
    cards = []
    for rank in ranks:
        for suit in suits:
            card = rank + suit
            if card in exceptions:
                continue
            cards.append(card)
    return cards


def simulate_full_board(deck, current_board):
    if len(current_board) < 5:
        return simulate_full_board(deck[1:], current_board + [deck[1]])
    else:
        last_card = current_board[-1]
        if last_card[1] in "hd":
            return current_board
        else:
            return simulate_full_board(deck[1:], current_board + [deck[1]])


def get_hand_vs_everything_winning_odds(hand, board, num_iterations=10):
    num_wins = 0
    for _ in range(num_iterations):
        deck_cards = np.asarray(get_deck_with_exceptions(hand + board))
        np.random.shuffle(deck_cards)
        deck_cards = deck_cards.tolist()

        villain_hand = deck_cards[:2]
        deck_cards = deck_cards[2:]
        deck_cards = deck_cards[2:]

        full_board = simulate_full_board(deck_cards, board)

        hand_value = eval7.evaluate(
            [
                eval7.Card(temp)
                for temp in hand + full_board
            ]
        )

        villain_hand_value = eval7.evaluate(
            [
                eval7.Card(temp)
                for temp in villain_hand + full_board
            ]
        )
        if hand_value > villain_hand_value:
            num_wins += 1
    return num_wins / num_iterations
