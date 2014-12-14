__author__ = 'dugging'
import Engine

IO = Engine.IOData()
Dave = Engine.Player('Dave', 2, 3, 4, 'Hunter')
Dave.Exp = 5
IO.save('', 'Player', '.txt', Dave)
Bob = IO.load('', 'Player', '.txt')
Bob.createexpcurve(1.5, 1)
Bob.checklvl()
print(Bob.Lvl)