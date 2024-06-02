import tkinter
from Piece import * 
from BoardState import BoardState

class BoardGraphic:
    def __init__(self) -> None:
        # board sizes
        self.sqrSize = 70
        self.labelSize = (self.sqrSize // 10) * 2
        self.offset = self.labelSize * 2
        self.boardSize =  self.sqrSize * 8
        self.canWidth = self.boardSize + self.offset * 2 + self.sqrSize * 5
        self.canHeight = self.boardSize + self.offset * 2
        # canvas setup
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=self.canWidth, height=self.canHeight)
        self.canvas.pack()
        # colours 
        self.white = "#F7E6E1"
        self.whiteStats = "#F28268"
        self.lightWhite = "#66D8B9"
        self.black = "#871EFA"
        self.lightBlack = "#05EB14"
        # BoardState
        self.boardState = BoardState(self.canvas, self)
        self.boardList = self.boardState.boardList
        # initial methods 
        self.initDraw()
    
    def lightsOn(self, validSqr):
        for row, col in validSqr:
            colour = self.canvas.itemcget(f"{row},{col}", "fill")
            if (colour == self.white):
                self.canvas.itemconfig(tagOrId=f"{row},{col}", fill=self.lightWhite)
            else:
                self.canvas.itemconfig(tagOrId=f"{row},{col}", fill=self.lightBlack)
    
    def lightsOff(self, validSqr):
        for row, col in validSqr:
            colour = self.canvas.itemcget(f"{row},{col}", "fill")
            if (colour == self.lightWhite):
                self.canvas.itemconfig(tagOrId=f"{row},{col}", fill=self.white)
            else:
                self.canvas.itemconfig(tagOrId=f"{row},{col}", fill=self.black)

    def drawStats(self, x1, y1, x2, y2):
        # create border
        self.canvas.create_rectangle(x1, y1, x2, y2)
        # texts
        self.canvas.create_text(x1 + self.labelSize * 2.5, self.offset, fill=self.black,
                                font=("Aptos", self.labelSize), tags="black", text="Black")
        self.canvas.create_text(x1 + self.labelSize * 2.5, y2 - self.offset + self.offset * 0.4, fill=self.whiteStats,
                                font=("Aptos", self.labelSize, "bold"), tags="white", text="White")


    def initDraw(self):
        # board border
        boardBottom = self.boardSize + self.labelSize * 3
        self.canvas.create_rectangle((self.labelSize, self.labelSize), (boardBottom, boardBottom))
        self.canvas.create_rectangle((self.offset - 1, self.offset - 1), (boardBottom - self.labelSize, boardBottom - self.labelSize))
        
        # squares 
        colour = self.black
        for row in range(8):
            colour = self.white if colour == self.black else self.black
               
            for col in range(8):
               x = self.offset + (col * self.sqrSize)
               y = self.offset + (row * self.sqrSize)
               self.canvas.create_rectangle((x, y), (x + self.sqrSize, y + self.sqrSize), 
                                            tags=f"{row},{col}", outline="", fill=colour)
               colour = self.white if colour == self.black else self.black

        # coordinates into label
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
        for i in range(8):
            step = self.offset + self.sqrSize//2 + self.sqrSize * i
            # up
            self.canvas.create_text((step, self.offset - self.labelSize//2), 
                                    text=letters[i])
            # bottom
            self.canvas.create_text((step, self.boardSize + self.offset + self.labelSize//2), 
                                    text=letters[i])
            # left
            self.canvas.create_text((self.offset - self.labelSize//2, step),
                                    text=numbers[i])
            # right 
            self.canvas.create_text((self.boardSize + self.offset + self.labelSize//2, step), 
                                    text=numbers[i])
            
        # put pieces
        for row in range(8):
            for col in range(8):
                piece: Piece = self.boardList[row][col]
                if (piece is not None):
                    image = piece.pieceImg(int(self.sqrSize - self.sqrSize * 0.1))

                    pieceImage = self.canvas.create_image(self.offset + (col * self.sqrSize) + self.sqrSize//2,
                                                          self.offset + (row * self.sqrSize) + self.sqrSize//2,
                                                          image=image)
                    self.boardList[row][col].imgId = pieceImage

        # draw stats
        self.drawStats(self.boardSize + self.offset * 2, self.labelSize,
                       self.boardSize + self.labelSize * 3 + self.sqrSize * 5, self.boardSize + self.labelSize * 3)
        
    def setNewGame(self):
        self.canvas.delete("all")
        self.boardState.isPicking = True
        self.boardState.turn = "W"
        self.boardList = self.boardState.initBoard()
        self.boardState.boardList = self.boardList
        self.initDraw()
        
        self.boardState.takenPieces = {
            "W": [],
            "B": []
        }
        self.boardState.playAgain.destroy()
  
class Program:
    def __init__(self):
        self.b = BoardGraphic()
        self.b.canvas.bind("<Button-1>", self.b.boardState.handleClick)
        tkinter.mainloop()
Program()