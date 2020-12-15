class MemoryGame:
    def __init__(self):
        self.last_seen_at = {}
        self.turn = 0
        self.previous = None

    def find_next(self):
        value = self.previous
        result = self.last_seen_at.get(value, 0)
        if result > 0:
            return self.turn - result - 1
        
        return result

    def next(self, value=None):
        self.turn = self.turn + 1
        if value is None:
            value = self.find_next()

        self.last_seen_at[self.previous] = self.turn-1
        self.previous = value

    def __repr__(self):
        return f"turn {self.turn}: {self.previous}"

game = MemoryGame()

starting_numbers = [7,12,1,0,16,2]
for i in starting_numbers:
    game.next(i)

while game.turn<2020:
    game.next()

print(game)

while game.turn<30000000:
    game.next()

print(game)