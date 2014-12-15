__author__ = 'dugging'
import Engine

IO = Engine.IOData()
Dave = Engine.Player('Dave', 2, 3, 4, 'Hunter')
Dave.Exp = 5
Dave.Lvl = 0
Dave.createexpcurve(2, 1)
IO.save('', 'Player', '.txt', Dave)
Bob = IO.load('', 'Player', '.txt')