__author__ = 'dugging'
import math
import random


class IOData():
    @staticmethod
    def save(folder, file, extension, data):
        export = open(folder+file+extension, 'w')
        if data.TYPE == 'PLAYER':
            for i in data.__dict__:
                export.write(str(i) + ':' + str(data.__dict__[i]) + '\n')
        export.close()

    @staticmethod
    def load(folder, file, extension):
        importing = open(folder+file+extension, 'r')
        check = importing.readlines(0)
        importing.close()
        for i in check:
            print(i[:3])
            if i[:3] == 'cla':
                clas = int(i.strip('\n')[4:])
            elif i[:3] == 'Nam':
                name = i.strip('\n')[4:]
            elif i[:3] == 'coe':
                coefficient = int(i.strip('\n')[4:])
            elif i[:3] == 'exp':
                exponent = int(i.strip('\n')[4:])
            elif i[:3] == 'Exp':
                experience = int(i.strip('\n')[4:])
            elif i[:3] == 'Str':
                strength = int(i.strip('\n')[4:])
            elif i[:3] == 'Int':
                inelegance = int(i.strip('\n')[4:])
            elif i[:3] == 'Dex':
                dexterity = int(i.strip('\n')[4:])
        ret = Player(name, dexterity, strength, inelegance, clas)
        ret.createexpcurve(coefficient, exponent)
        ret.Exp = experience
        ret.checklvl()
        return ret


class Player():
    TYPE = 'PLAYER'
    Lvl = 0
    Exp = 0
    coefficient = 0
    exponent = 0

    def __init__(self, name='John', dex=0, stre=0, inte=0, clas='Unknown'):
        self.clas = clas
        self.Name = name
        self.Dex = dex
        self.Str = stre
        self.Int = inte
        self.Dam = int(self.Dex/2)+dex
        self.Def = int(self.Str/8)+int(self.Dex/4)
        self.MDef = int(self.Str/16)+int(self.Int/4)
        self.Hp = int(self.Str/4)+stre
        self.Mp = int(self.Int/8)+inte
        self.Inv = []

    def createexpcurve(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent

    def checklvl(self):
        self.Lvl = math.floor(self.Exp**(1/self.exponent)/self.coefficient)


class Magic():
    TYPE = 'MAGIC'

    def __init__(self, name, dam, lvl, pic=None, picpath=None):
        self.Name = name
        self.Dam = dam
        self.Lvl = lvl
        self.Pic = pic
        self.picPath = picpath


class Item():
    TYPE = 'ITEM'

    def __init__(self, name, stat, slot, amount, cost, pic=None):
        self.Name = name
        self.Stat = stat
        self.Slot = slot
        self.Amount = amount
        self.Cost = cost
        self.pic = pic


class Mob():
    TYPE = 'MOB'

    def __init__(self, name, hp, mp, dam, defe, exp, loot, magic, pic=None):
        self.Name = name
        self.Hp = hp
        self.Mp = mp
        self.Dam = dam
        self.Def = defe
        self.Exp = exp
        self.Loot = loot
        self.Magic = magic
        self.pic = pic


class Battle():
    Victory = False
    Loss = False

    def __init__(self, player, monster):
        self.Player = player
        self.Monster = monster

    def playerpysatk(self):
        self.Monster.Hp -= (self.Player.Dam - self.Monster.Def)

    def monsterpysatk(self):
        self.Player.Hp -= (self.Monster.Dam - self.Player.Def)

    def playermatk(self, magic):
        self.Monster.Hp -= (magic.Dam - int(self.Monster.Def/2))

    def monstermatk(self, magic):
        self.Player.Hp -= (magic.Dam - int(self.Player.MDef))

    def checkstate(self):
        if self.Player.Hp == 0:
            self.Loss = True
        elif self.Monster.Hp == 0:
            self.Player.Inv.append(random.choice(self.Monster.Loot))
            self.Victory = True