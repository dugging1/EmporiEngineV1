__author__ = 'dugging'
import math
import random


class IOData():
    @staticmethod
    def save(folder, file, extension, data):
        export = open(folder+file+extension, 'w')
        if data.typ == 'MAP':
            export.write('typ:MAP\n')
            for x in range(data.width):
                for y in range(data.height):
                    export.write(data.map[x][y])
                export.write('\n')
        else:
            for i in data.__dict__:
                export.write(str(i) + ':' + str(data.__dict__[i]) + '\n')
        export.close()

    @staticmethod
    def load(folder, file, extension):
        #type, name, class, dex, str, int, Lvl, Expei, coe, exp,Dam(10), stat, slot, amount, cost, hp, mp, def
        info = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        importing = open(folder+file+extension, 'r')
        check = importing.readlines(0)
        importing.close()
        for x in check:
            if x[:3] == 'typ':
                info[0] = x[4:].strip('\n')
            elif x[:3] == 'Nam':
                info[1] = x[4:].strip('\n')
            elif x[:3] == 'cla':
                info[2] = x[4:].strip('\n')
            elif x[:3] == 'Dex':
                info[3] = int(x[4:].strip('\n'))
            elif x[:3] == 'Str':
                info[4] = int(x[4:].strip('\n'))
            elif x[:3] == 'Int':
                info[5] = int(x[4:].strip('\n'))
            elif x[:3] == 'Lvl':
                info[6] = int(x[4:].strip('\n'))
            elif x[:3] == 'Exp':
                info[7] = int(x[4:].strip('\n'))
            elif x[:3] == 'coe':
                info[8] = int(x[4:].strip('\n'))
            elif x[:3] == 'exp':
                info[9] = int(x[4:].strip('\n'))
            elif x[:3] == 'Dam':
                info[10] = int(x[4:].strip('\n'))
            elif x[:3] == 'Sta':
                info[11] = x[4:].strip('\n')
            elif x[:3] == 'Slo':
                info[12] = x[4:].strip('\n')
            elif x[:3] == 'Amo':
                info[13] = int(x[4:].strip('\n'))
            elif x[:3] == 'Cos':
                info[14] = int(x[4:].strip('\n'))
            elif x[:3] == 'Def':
                info[15] = int(x[4:].strip('\n'))
        if info[0] == 'PLAYER':
            ret = Player(info[1], info[3], info[4], info[5], info[2])
        elif info[0] == 'MAGIC':
            ret = Magic(info[1], info[10], info[6])
        elif info[0] == 'ITEM':
            ret = Item(info[1], info[11], info[12], info[13], info[14])
        elif info[0] == 'MOB':
            ret = Mob(info[1], info[15], info[16], info[10], info[17], info[7], ['WIP'], ['WIP'])
        elif info[0] == 'MAP':
            ret = Map(len(check[1].strip('\n')), len(check) - 1)
            ret.creategrid(ret.width, ret.height)
            for y in range(ret.height):
                for x in range(ret.width):
                    ret.map[x][y] = check[y+1][x]
        return ret


class Player():
    Lvl = 0
    Exp = 0
    coe = 0
    exp = 0

    def __init__(self, name='John', dex=0, stre=0, inte=0, clas='Unknown'):
        self.typ = 'PLAYER'
        self.cla = clas
        self.Nam = name
        self.Dex = dex
        self.Str = stre
        self.Int = inte
        self.Dam = int(self.Dex/2)+dex
        self.Def = int(self.Str/8)+int(self.Dex/4)
        self.MDe = int(self.Str/16)+int(self.Int/4)
        self.Hea = int(self.Str/4)+stre
        self.Man = int(self.Int/8)+inte
        self.Inv = []

    def createexpcurve(self, coefficient, exponent):
        self.coe = coefficient
        self.exp = exponent

    def checklvl(self):
        self.Lvl = math.floor(self.Exp**(1/self.exp)/self.coe)


class Magic():

    def __init__(self, name='Unknown', dam=0, lvl=0, pic=None, picpath=None):
        self.typ = 'MAGIC'
        self.Nam = name
        self.Dam = dam
        self.Lvl = lvl
        self.Pic = pic
        self.picpath = picpath


class Item():

    def __init__(self, name, stat, slot, amount, cost, pic=None):
        self.typ = 'ITEM'
        self.Nam = name
        self.Sta = stat
        self.Slo = slot
        self.Amo = amount
        self.Cos = cost
        self.pic = pic


class Mob():

    def __init__(self, name, hp, mp, dam, defe, exp, loot, magic, pic=None):
        self.typ = 'MOB'
        self.Nam = name
        self.Hea = hp
        self.Man = mp
        self.Dam = dam
        self.Def = defe
        self.Exp = exp
        self.Lot = loot
        self.Mag = magic
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


class Map():
    def __init__(self, width, height):
        self.typ = 'MAP'
        self.width = int(width)
        self.height = int(height)
        self.map = []

    def creategrid(self, width, height):
        for x in range(width):
            self.map.append([])
            for y in range(height):
                self.map[x].append([])

    def setdata(self, width, height, data):
        self.map[width][height] = data

    def fillfloor(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.map[x][y] == []:
                    self.map[x][y] = 'F'