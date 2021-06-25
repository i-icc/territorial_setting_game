class Player():
    def __init__(self,num):
        self.num = num
        self.pl = 9
        self.x = num
        self.y = num
        if num == 1:
            self.pl = 8
            self.x = 21
            self.y = 12

class Game():
    def __init__(self):
        self.players = [Player(1), Player(2)]
        self.field = [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5],
            [5, 0, 9, 0, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 5, 0, 0, 0, 5, 0, 5],
            [5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 5], 
            [5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 5], 
            [5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5], 
            [5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 5],
            [5, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5],
            [5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 5, 0, 0, 5],
            [5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 5], 
            [5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 5], 
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        ]
    
    def move(self,num,command):
        p = self.players[num]
        self.field[p.y][p.x] = p.num
        flag = True
        if command == "u":
            if self.field[p.y - 1][p.x] in (5,8,9):
                flag = False
            else:
                self.players[num].y += -1
        elif command == "d":
            if self.field[p.y + 1][p.x] in (5,8,9):
                flag = False
            else:
                self.players[num].y += 1
        elif command == "l":
            if self.field[p.y][p.x - 1] in (5,8,9):
                flag = False
            else:
                self.players[num].x += -1
        elif command == "r":
            if self.field[p.y][p.x + 1] in (5,8,9):
                flag = False
            else:
                self.players[num].x += 1
        if flag:
            self.move(num,command)
        else:
            self.field[p.y][p.x] = p.pl
        
    

    def dump(self):
        r = ""
        r += f"{len(self.field):02}"
        r += f"{len(self.field[0]):02}"
        for y in self.field:
            for x in y:
                r += str(x)
        return r
    
    def load(r):
        h = int(r[:2])
        w = int(r[2:4])
        f = list(map(int,list(r[4:])))
        fie = []
        for y in range(h):
            fie.append([])
            for x in range(w):
                fie[y].append(f[y * w + x])
        
        for y in fie:
            for x in y:
                a = "⬜"
                if x == 1:
                    a = "🟥"
                elif x == 2:
                    a = "🟦"
                elif x == 5:
                    a = "⛔"
                elif x == 8:
                    a = "🥵"
                elif x == 9:
                    a = "🥶"
                print(a,end="")
            print()

    

if __name__=="__main__":
    game = Game()
    d = game.dump()
    Game.load(d)
