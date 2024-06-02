import tkinter
from PIL import Image, ImageTk

class Piece:
    def __init__(self, colour) -> None:
        self.colour = colour
        self.imgId = None
        self.hasMoved = False

    def pieceImg(self, imgSize):
        img = Image.open(self.path)
        img = img.resize((imgSize, imgSize))
        

        self.pieceImage = ImageTk.PhotoImage(img)
        return self.pieceImage
    
    def checkRange(self, row, col):
        # prevent getting out of range error
        if (row > 7 or row < 0):
            return False
        if (col > 7 or col < 0):
            return False
        return True

    def canMove(self, row, col, boardList):
        if (self.checkRange(row, col)):
            if (boardList[row][col] is None):
                return True
            if (boardList[row][col].colour != self.colour):
                return True
            else:
                return False
        else:
            return False

class Pawn(Piece):
    def __init__(self, colour) -> None:
        super().__init__(colour)
        self.path = f"./img/pawn{colour}.png"

    def validMoves(self, row, col, boardList) -> list[(int, int)]:
        moves = []
        if self.colour == "W":
            if boardList[row - 1][col] is None:
                moves.append((row - 1, col))
            if ((col - 1 > 0 and boardList[row - 1][col - 1] is not None) and 
                boardList[row - 1][col - 1].colour != self.colour):
                moves.append((row - 1, col - 1))
            if ((col + 1 < 8 and boardList[row - 1][col + 1] is not None) and
                boardList[row - 1][col + 1].colour != self.colour):
                moves.append((row - 1, col + 1))
            if (self.hasMoved == False and 
                (boardList[row - 1][col] is None and boardList[row - 2][col] is None)):
                moves.append((row - 2, col))
        else:
            if boardList[row + 1][col] is None:
                moves.append((row + 1, col))
            if ((col - 1 > 0 and boardList[row + 1][col - 1] is not None) and 
                boardList[row + 1][col - 1].colour != self.colour):
                moves.append((row + 1, col - 1))
            if ((col + 1 < 8 and boardList[row + 1][col + 1] is not None) and 
                boardList[row + 1][col + 1].colour != self.colour):
                moves.append((row + 1, col + 1))
            if (self.hasMoved == False and 
                (boardList[row + 1][col] is None and boardList[row + 2][col] is None)):
                moves.append((row + 2, col))
        return moves


class Rook(Piece):
    def __init__(self, colour) -> None:
        super().__init__(colour)
        self.path = f"./img/rook{colour}.png"

    # possibilities 
    def validMoves(self, row, col, boardList) -> list[(int, int)]: 
        moves = []
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for x, y in directions:
            for i in range(1,8):
                newRow = row + (i * x)
                newCol = col + (i * y)
                if (self.canMove(newRow, newCol, boardList)):
                    moves.append((newRow, newCol))
                    if (boardList[newRow][newCol] is not None and
                        boardList[newRow][newCol].colour != self.colour):
                        break
                else:
                    break
        return moves

class Knight(Piece):
    def __init__(self, colour) -> None:
        super().__init__(colour)
        self.path = f"./img/knight{colour}.png"
    
    def validMoves(self, row, col, boardList) -> list[(int, int)]: 
        moves = []
        directions = [(1, -2), (-1, -2), (2, -1), (-2, -1), (-1, 2), (1, 2), (2, 1), (-2, 1)]
        for x, y in directions:
            if (self.canMove(row + x, col + y, boardList)):
                moves.append((row + x, col + y))
        return moves


class Bishop(Piece):
    def __init__(self, colour) -> None:
        super().__init__(colour)
        self.path = f"./img/bishop{colour}.png"

    def validMoves(self, row, col, boardList) -> list[(int, int)]: 
        moves = []
        directions = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
        for x, y in directions:
            for i in range(1,8):
                newRow = row + (i * x)
                newCol = col + (i * y)
                if (self.canMove(newRow, newCol, boardList)):
                    moves.append((newRow, newCol))
                    if (boardList[newRow][newCol] is not None and
                        boardList[newRow][newCol].colour != self.colour):
                        break
                else:
                    break
        return moves

class King(Piece):
    def __init__(self, colour) -> None:
        super().__init__(colour)
        self.path = f"./img/king{colour}.png"
    
    def validMoves(self, row, col, boardList) -> list[(int, int)]: 
        moves = []
        directions = [(1, -1), (-1, -1), (-1, 1), (1, 1), (0, -1), (0, 1), (1, 0), (-1, 0)]
        for x, y in directions:
            if (self.canMove(row + x, col + y, boardList)):
                moves.append((row + x, col + y))
        return moves

class Queen(Piece):
    def __init__(self, colour) -> None:
        super().__init__(colour)
        self.path = f"./img/queen{colour}.png"

    def validMoves(self, row, col, boardList) -> list[(int, int)]: 
        moves = []
        directions = [(1, -1), (-1, -1), (-1, 1), (1, 1), (0, -1), (0, 1), (1, 0), (-1, 0)]
        for x, y in directions:
            for i in range(1,8):
                newRow = row + (i * x)
                newCol = col + (i * y)
                if (self.canMove(newRow, newCol, boardList)):
                    moves.append((newRow, newCol))
                    if (boardList[newRow][newCol] is not None and
                        boardList[newRow][newCol].colour != self.colour):
                        break
                else:
                    break
        return moves


