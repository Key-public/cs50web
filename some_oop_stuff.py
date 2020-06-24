class First():
    def __init__ (self, one, two):
        self.catch = one
        self.throw = two
    
    def printScore(self, player, catch, throw):
        try:
            print(f"The {player} is catch {catch} times and throw {throw} times. Total score is {int(catch) + 2 * int(throw)}")
            return None
        except ValueError:
            print(f"We can't print result. Seems like you've typed non-int value")

player = input("Baseball player's name: ")
baseball = First(input("He catch (1pt): "), input("He throw (2pt): "))

baseball.printScore(player, baseball.catch, baseball.throw)

