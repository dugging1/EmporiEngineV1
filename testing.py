__author__ = 'dugging'
import Engine

IO = Engine.IOData()
Dave = Engine.Player('Dave', 2, 3, 4)
IO.save('', 'Player', '.txt', Dave)
Bob = IO.load('', 'Player', '.txt')
print(Bob.Name + ' is amazing!')