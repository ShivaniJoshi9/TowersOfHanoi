import turtle

#Okay, so because I turned the auto update off, you need to call qwe.update() after you do anything.

qwe = turtle.Turtle()
screen = turtle.Screen()
qwe.tracer(0, 0)

a = 0
select = 0
blocksnum = 0
meses = [[-350, -150], [-100, 100], [150, 350]]
cents = [-250, 0, 250]

TempBlockHold = [[],[]] #Where I want to hold my block while I potentially move it from one tower to another



def drawDisk(l, r, t, b):
    qwe.ht()
    qwe.pu()
    qwe.setpos(l, b)
    qwe.pd()
    qwe.fillcolor("blue")
    qwe.fill(True)
    qwe.setpos(l, t)
    qwe.setpos(r, t)
    qwe.setpos(r, b)
    qwe.fill(False)
    qwe.pu()

'''def Win(self):
    screen.bgcolor("green")
    print("{{{{{2}}}}}")'''
# Setcol1


class Column:
    def __init__(self, colnm):
        self.disks = []
        self.temp = 0
        self.num = 0
        self.colnumber = colnm
    
    def retColumn(self):
        return(self.disks)
    
    def addDisk(self, disknum):
        print("dcba", self.colnumber, self.disks, disknum)
        if self.disks != []:
            self.temp = self.disks[-1]
            if self.temp[0] > disknum[0] :
                self.num += 1
                self.disks.append(disknum)
                return(True)
            elif self.temp[0] < disknum[0] :
                return(False)
            print("False", self.disks)
        elif self.disks == []:
            self.disks.append(disknum)
            self.num += 1
            return(True)
        
    def removeDisk(self):
        global TempBlockHold
        print("abcd", self.colnumber, self.disks)
        TempBlockHold[0] = self.disks.pop(-1)
        TempBlockHold[1] = self.colnumber
        self.num -= 1
        print("TempBlockHold", TempBlockHold)
        print(self.colnumber, self.disks)
    
    def resetCol(self):
        self.disks = []
        self.temp = 0
        self.num = 0
    
    def draw(self, colnum):
        if self.num == 0:
            print(0)
        else:
            print("draw", self.colnumber, self.disks)
            for i in range(self.num):
                b = self.disks[i][1]/2
                c = i + 1
                z = cents[colnum] - b
                y = cents[colnum] + b
                drawDisk(z, y, 15 * c, 15 * (c - 1))
                print("hi", self.colnumber, i, b, z, y)
    
    def checkWin(self):
        if self.disks == []:
            return True
        elif self.disks != []:
            return False



class Game :
    def __init__(self):
        self.col1 = Column(1)
        self.col2 = Column(2)
        self.col3 = Column(3)
        
        self.mes1 = [-350, -150]
        self.mes2 = [-100, 100]
        self.mes3 = [150, 350]
        
        self.towerBlocks = 0
        self.blocks = []
        self.bblocks = []
    
    def setBlocks(self):
        self.col1.resetCol()
        self.col2.resetCol()
        self.col3.resetCol()
        for i in range(self.towerBlocks):
            self.blocks.append([])
            self.blocks[i].append(i)
            self.blocks[i].append((i * 30) + 30)
        self.bblocks = self.blocks[::-1]
        for i in range(self.towerBlocks):
            self.col1.addDisk(self.bblocks[i])
        print("Setcol1", self.col1.retColumn())
    
    def setBlockNum(self, num):
        self.towerBlocks = num
    
    def blockPrint(self):
        print(self.blocks)
    
    def draw(self):
        qwe.reset()
        setScreen()
        self.col1.draw(0)
        self.col2.draw(1)
        self.col3.draw(2)
        self.checkW()
    
    def removeD(self, columnNum):
        if columnNum == 0:
            self.col1.removeDisk()
        if columnNum == 1:
            self.col2.removeDisk()
        if columnNum == 2:
            self.col3.removeDisk()
    
    def addD(self, columnNum):
        if columnNum == 0:
            m = self.col1.addDisk(TempBlockHold[0])
        elif columnNum == 1:
            m = self.col2.addDisk(TempBlockHold[0])
        elif columnNum == 2:
            m = self.col3.addDisk(TempBlockHold[0])
        if m == False: #Puts block back in its previous tower if it can't be moved
            if TempBlockHold[1] == 1:
                self.col1.addDisk(TempBlockHold[0])
            elif TempBlockHold[1] == 2:
                self.col2.addDisk(TempBlockHold[0])
            elif TempBlockHold[1] == 3:
                self.col3.addDisk(TempBlockHold[0])
        elif m == True:
            #check win
            pass
    
    def checkW(self):
        h = self.col1.checkWin()
        j = self.col2.checkWin()
        if h == True and j == True:
            self.Win()
    
    def Win(self):
        global a
        a = 2
        screen.bgcolor("green")
        qwe.reset()
        qwe.ht()
        qwe.pu()
        qwe.setpos(0, 50)
        qwe.pd()
        qwe.write("YOU WIN!!", align = "center", font = ("Arial", 25, "normal"))
        qwe.pu()
        qwe.setpos(0, 20)
        qwe.write("To play again, click on the screen", align = "center", font = ("Arial", 15, "normal"))
    
    



def setScreen():
    screen.bgcolor("white")
    for i in range(3):
        qwe.ht()
        qwe.penup()
        qwe.setpos(meses[i][0], 0)
        qwe.pendown()
        qwe.forward(100)
        qwe.setpos(meses[i][1], 0)
        qwe.penup()
    qwe.update()



def CheckClick(x, y):
    global a
    global TempBlockHold
    global game
    if a == 0 :
        print("")
        #When you select a block
        col = 3
        for i in range(3):
            if x >= meses[i][0] and x <= meses[i][1]: #Checks which column you clicked in
                col = i
        if col != 3:
            print("Column " + str(col + 1))
            game.removeD(col)
            a = 1
        else:
            print("NOT A COLUMN")
        print("...")
    elif a == 1:
        #where you place block
        col = 3
        for i in range(3):
            if x >= meses[i][0] and x <= meses[i][1]: #Checks which column you clicked in
                col = i
        if col != 3:
            print("Column " + str(col + 1))
            game.addD(col)
            a = 0
            game.draw()
            qwe.update()
            print("\n-----------------")
        else:
            print("NOT A COLUMN")
    elif a == 2:
        #win screen
        a = 0
        turtle.reset()
        qwe.update()
        startScreen()
    
    
    #print("click")
    #print(x, y)

def lol():
    print("subhd")

def press3():
    global blocksnum
    blocksnum = 3
    newGame()

def press4():
    global blocksnum
    blocksnum = 4
    newGame()

def press5():
    global blocksnum
    blocksnum = 5
    newGame()

def press6():
    global blocksnum
    blocksnum = 6
    newGame()

def press7():
    global blocksnum
    blocksnum = 7
    newGame()

def press8():
    global blocksnum
    blocksnum = 8
    newGame()

def press9():
    global blocksnum
    blocksnum = 9
    newGame()

def start():
    screen.onkey(press3, "3")
    screen.onkey(press4, "4")
    screen.onkey(press5, "5")
    screen.onkey(press6, "6")
    screen.onkey(press7, "7")
    screen.onkey(press8, "8")
    screen.onkey(press9, "9")
    screen.listen()

def runGame():
    screen.onclick(CheckClick)
    screen.listen()

def newGame():
    global game
    game = Game()
    game.setBlockNum(blocksnum)
    ###USE USER INPUT IN LINE ABOVE###
    game.setBlocks()
    #game.blockPrint()
    game.draw()
    runGame()
    setScreen()
    


def startScreen():
    screen.bgcolor("blue")
    qwe.ht()
    qwe.penup()
    qwe.setpos(0, -50)
    qwe.write("To start,", align = "center", font = ("Arial", 20, "normal"))
    qwe.setpos(0, -75)
    qwe.write("Choose the number of desired", align = "center", font = ("Arial", 20, "normal"))
    qwe.setpos(0, -100)
    qwe.write("blocks on your keyboard", align = "center", font = ("Arial", 20, "normal"))
    qwe.pendown()
    qwe.penup()
    qwe.update()
    start()
startScreen()

#newGame()
#setScreen()



#while True:
    #runGame()


#cents[x] - blocks[z][1]/2
#cents[x] + blocks[z][1]/2

#### in order to move:
####    setScreen()


