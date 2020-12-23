from collections import deque


def get_deck(player_data):
    return deque([int(x.strip()) for x in player_data.split("\n")[1:]])


with open("input.txt", 'r') as data:
    data = data.read().split("\n\n")
    deck_one = get_deck(data[0])
    deck_two = get_deck(data[1])

# part 1
winning_deck = None
while winning_deck is None:
    if len(deck_one) == 0:
        winning_deck = deck_two
        break
    if len(deck_two) == 0:
        winning_deck = deck_one
        break

    card_one, card_two = deck_one.popleft(), deck_two.popleft()
    if card_one > card_two:
        deck_one.append(card_one)
        deck_one.append(card_two)
    else:
        deck_two.append(card_two)
        deck_two.append(card_one)

print(sum([(i+1) * x for i, x in enumerate(reversed(winning_deck))]))
