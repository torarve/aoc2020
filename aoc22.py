import collections

def get_input():
    with open('input22.txt') as file:
        return [x.strip() for x in file]

def parse_deck(input):
    deck = collections.deque()
    for line in input:
        if line.startswith("Player"):
            continue
        if line=="":
            yield deck
            deck = collections.deque()
        else:
            deck.appendleft(int(line))
    if len(deck)>0:
        yield deck

input = [
    "Player 1:",
    "9",
    "2",
    "6",
    "3",
    "1",
    "",
    "Player 2:",
    "5",
    "8",
    "4",
    "7",
    "10",
    ""
]

input = get_input()
decks = [x for x in parse_deck(input)]
player1 = decks[0]
player2 = decks[1]

while len(player1)!=0 and len(player2)!=0:
    hand1 = player1.pop()
    hand2 = player2.pop()
    if hand1>hand2:
        player1.appendleft(hand1)
        player1.appendleft(hand2)
    else:
        player2.appendleft(hand2)
        player2.appendleft(hand1)

def calculate_points(player):
    return sum([(i+1)*x for i, x in enumerate(player)])

if len(player1)>0:
    print(f"Winner is player 1 with {calculate_points(player1)}")
else:
    print(f"Winner is player 2 with {calculate_points(player2)}")

# Recursive example
input2 = [
    "Player 1:",
    "43",
    "19",
    "",
    "Player 2:",
    "2",
    "29",
    "14",
]

decks = [x for x in parse_deck(input)]
decks = [x for x in parse_deck(get_input())]
player1 = decks[0]
player2 = decks[1]

def play_game(player1, player2):
    previous_configurations = set()
    while len(player1)!=0 and len(player2)!=0:
        hand1 = player1.pop()
        hand2 = player2.pop()
        tmp = [x for x in player1]
        tmp.extend([x for x in player2])
        current_configuration = tuple(tmp)
        if current_configuration in previous_configurations:
            return True

        previous_configurations.add(current_configuration)
        if len(player1)>=hand1 and len(player2)>=hand2:
            sub1 = collections.deque([x for x in player1][-hand1:])
            sub2 = collections.deque([x for x in player2][-hand2:])
            player1_won_round = play_game(sub1, sub2)
        else:
            player1_won_round = hand1>hand2
        
        if player1_won_round:
            player1.appendleft(hand1)
            player1.appendleft(hand2)
        else:
            player2.appendleft(hand2)
            player2.appendleft(hand1)

    return len(player1)>0

player1_won = play_game(player1, player2)

if player1_won:
    print(f"Winner is player 1 with {calculate_points(player1)}")
else:
    print(f"Winner is player 2 with {calculate_points(player2)}")
