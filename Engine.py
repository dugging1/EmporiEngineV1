__author__ = 'dugging'


class IOData():
    @staticmethod
    def save(folder, file, extension, Data):
        Export = open(folder+file+extension, 'w')
        if Data.TYPE == 'PLAYER':
            Export.write(Data.TYPE)
            Export.write('\n')
            Export.write(Data.Name)
            Export.write('\n')
            Export.write(str(Data.Dex))
            Export.write('\n')
            Export.write(str(Data.Int))
            Export.write('\n')
            Export.write(str(Data.Str))
        Export.close()

    def load(self, folder, file, extension):
        Import = open(folder+file+extension, 'r')
        Check = Import.readlines(0)
        if Check[0].strip('\n') == 'PLAYER':
            ret = Player(Check[1].strip('\n'), int(Check[2].strip('\n')), int(Check[3].strip('\n')), int(Check[4]))
        Import.close()
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

    def __init__(self, name, dam, lvl, pic=None):
        self.Name = name
        self.Dam = dam
        self.Lvl = lvl
        self.pic = pic


class Item():
    TYPE = 'ITEM'
    def __init__(self, name, stat, amount, cost, pic=None):
        self.Name = name
        self.Stat = stat
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
    def __init__(self, Player, Monster):
        self.Player = Player
        self.Monster = Monster

    def PlayerPysAtk(self):
        self.Monster.Hp -= (self.Player.Dam - self.Monster.Def)

    def MonsterPysAtk(self):
        self.Player.Hp -= (self.Monster.Dam - self.Player.Def)

    def PlayerMAtk(self, Magic):
        self.Monster.Hp -= (Magic.Dam - int(self.Monster.Def/2))

    def MonsterMAtk(self, Magic):
        self.Player.Hp -= (Magic.Dam - int(self.Player.MDef))
