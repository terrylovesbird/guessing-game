class GuessingGame():

    def __init__(self, answer):
        self.answer = answer
        self.is_correct = False

    def guess(self,guess):

        self.guess = guess
        if self.answer < self.guess:
            print('high')
        elif self.answer > self.guess:
            print('low')
        elif self.answer == self.guess:
            print('correct')
            self.is_correct = True


    def solved(self):
        print(self.is_correct)

   
game = GuessingGame(50)

game.guess(50)
game.solved()

