__author__ = 'dugging'


class IOData():
    @staticmethod
    def save(folder, file, extension, data):
        export = open(folder+file+extension, 'w')
        if data.TYPE == 'PLAYER':
            export.write(data.TYPE)
            export.write('\n')
            export.write(data.Name)
            export.write('\n')
            export.write(str(data.Dex))
            export.write('\n')
            export.write(str(data.Int))
            export.write('\n')
            export.write(str(data.Str))
        if data.TYPE == 'MAGIC':
            export.write(data.TYPE)
            export.write('\n')
            export.write(data.Name)
            export.write('\n')
            export.write(data.Dam)
            export.write('\n')
            export.write(data.Lvl)
            export.write('\n')
            export.write(data.picPath)
        export.close()

    @staticmethod
    def load(folder, file, extension):
        importing = open(folder+file+extension, 'r')
        check = importing.readlines(0)
        if check[0].strip('\n') == 'PLAYER':
            ret = Player(check[1].strip('\n'), int(check[2].strip('\n')), int(check[3].strip('\n')), int(check[4]))
        elif check[0].strip('\n') == 'MAGIC':
            ret = Magic(check[1].strip('\n'), int(check[2].strip('\n')), int(check[3].strip('\n')))

        else:
            ret = None
        importing.close()
        return ret


class Player():
    TYPE = 'PLAYER'

    def __init__(self, name, dex, stre, inte):
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
