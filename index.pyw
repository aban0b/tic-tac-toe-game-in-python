"""allam"""
"""high level"""
#################################################################################################################################
from math import inf as infinity
from random import choice
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
p1=[]
p2=[]
HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
def wineer():
    global p1
    global p2
    win = -1
    if (1 in p1 and 2 in p1 and 3 in p1) or (4 in p1 and 5 in p1 and 6 in p1) or (7 in p1 and 8 in p1 and 9 in p1) or ( 1 in p1 and 4 in p1 and 7 in p1) or (2 in p1 and 5 in p1 and 8 in p1) or ( 3 in p1 and 6 in p1 and 9 in p1) or (1 in p1 and 5 in p1 and 9 in p1) or (3 in p1 and 5 in p1 and 7 in p1):
        win = 1
    elif (1 in p2 and 2 in p2 and 3 in p2) or (4 in p2 and 5 in p2 and 6 in p2) or (7 in p2 and 8 in p2 and 9 in p2) or (1 in p2 and 4 in p2 and 7 in p2) or (2 in p2 and 5 in p2 and 8 in p2) or (3 in p2 and 6 in p2 and 9 in p2) or (1 in p2 and 5 in p2 and 9 in p2) or (3 in p2 and 5 in p2 and 7 in p2):
        win = 2
    elif len(p1) + len(p2) == 9:
        win=0
    return win
def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0
    return score
def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False
def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)
def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells
def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False
def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False
def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best
def ai_turn():
    global p2
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        move=[x,y]
        print("computer play ya human at : ",find_o_index(move))
        result = find_o_index(move)
        print("_______________________")
    else:
        move = minimax(board, depth, COMP)
        print("computer play : ", find_o_index(move))
        result = find_o_index(move)
        print("_______________________")
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    p2.append(result)
    return result

def find_o_index(move):
        move = move[:3]
        if move[0] == 0 and move[1] == 0:
            return 1
        elif move[0] == 0 and move[1] == 1:
            return 2
        elif move[0] == 0 and move[1] == 2:
            return 3
        elif move[0] == 1 and move[1] == 0:
            return 4
        elif move[0] == 1 and move[1] == 1:
            return 5
        elif move[0] == 1 and move[1] == 2:
            return 6
        elif move[0] == 2 and move[1] == 0:
            return 7
        elif move[0] == 2 and move[1] == 1:
            return 8
        elif move[0] == 2 and move[1] == 2:
            return 9
def human_turn():
    global a
    global p1
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }
    if move < 1 or move > 9:
        try:
            move = a
            p1.append(move)
            print("you play at : ",move)
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)
            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
    value=ai_turn()
    return value
ui,_ = loadUiType('main.ui')
a=0
class MainApp(QMainWindow , ui):
    global a
    global HUMAN
    global COMP
    global board
    global p1
    global p2
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.animation()

    def Handel_Buttons(self):
        self.pushButton_1.clicked.connect(self.tab1)
        self.pushButton_2.clicked.connect(self.tab2)
        self.pushButton_3.clicked.connect(self.tab3)
        self.pushButton_4.clicked.connect(self.tab4)
        self.pushButton_5.clicked.connect(self.tab5)
        self.pushButton_6.clicked.connect(self.tab6)
        self.pushButton_7.clicked.connect(self.tab7)
        self.pushButton_8.clicked.connect(self.tab8)
        self.pushButton_9.clicked.connect(self.tab9)

    def animation(self):
        box_animation1 = QPropertyAnimation(self.pushButton_1, b"geometry")
        box_animation1.setDuration(2500)
        box_animation1.setStartValue(QRect(0, 0, 0, 0))
        box_animation1.setEndValue(QRect(40, 9, 150, 121))
        box_animation1.start()
        self.box_animation1 = box_animation1
        box_animation2 = QPropertyAnimation(self.pushButton_2, b"geometry")
        box_animation2.setDuration(2500)
        box_animation2.setStartValue(QRect(0, 0, 0, 0))
        box_animation2.setEndValue(QRect(210, 9, 150, 121))
        box_animation2.start()
        self.box_animation2 = box_animation2
        #####
        box_animation3 = QPropertyAnimation(self.pushButton_3, b"geometry")
        box_animation3.setDuration(2500)
        box_animation3.setStartValue(QRect(0, 0, 0, 0))
        box_animation3.setEndValue(QRect(380, 9, 150, 121))
        box_animation3.start()
        self.box_animation3 = box_animation3
        #####
        box_animation4 = QPropertyAnimation(self.pushButton_4, b"geometry")
        box_animation4.setDuration(2500)
        box_animation4.setStartValue(QRect(0, 0, 0, 0))
        box_animation4.setEndValue(QRect(40, 149, 150, 121))
        box_animation4.start()
        self.box_animation4 = box_animation4
        #####
        box_animation5 = QPropertyAnimation(self.pushButton_5, b"geometry")
        box_animation5.setDuration(2500)
        box_animation5.setStartValue(QRect(0, 0, 0, 0))
        box_animation5.setEndValue(QRect(210, 149, 150, 121))
        box_animation5.start()
        self.box_animation5 = box_animation5
        #####
        box_animation6 = QPropertyAnimation(self.pushButton_6, b"geometry")
        box_animation6.setDuration(2500)
        box_animation6.setStartValue(QRect(0, 0, 0, 0))
        box_animation6.setEndValue(QRect(380, 149, 150, 121))
        box_animation6.start()
        self.box_animation6 = box_animation6
        #####
        box_animation7 = QPropertyAnimation(self.pushButton_7, b"geometry")
        box_animation7.setDuration(2500)
        box_animation7.setStartValue(QRect(0, 0, 0, 0))
        box_animation7.setEndValue(QRect(40, 290, 150, 121))
        box_animation7.start()
        self.box_animation7 = box_animation7
        #####
        box_animation8 = QPropertyAnimation(self.pushButton_8, b"geometry")
        box_animation8.setDuration(2500)
        box_animation8.setStartValue(QRect(0, 0, 0, 0))
        box_animation8.setEndValue(QRect(210, 290, 150, 121))
        box_animation8.start()
        self.box_animation8 = box_animation8
        #####
        box_animation9 = QPropertyAnimation(self.pushButton_9, b"geometry")
        box_animation9.setDuration(2500)
        box_animation9.setStartValue(QRect(0, 0, 0, 0))
        box_animation9.setEndValue(QRect(380, 290, 150, 121))
        box_animation9.start()
        self.box_animation9 = box_animation9
        #####
    def play_again(self):
        global  HUMAN
        global  COMP
        global  board
        global  p1
        global  p2
        buttonReply = QMessageBox.question(self, 'mydear', "Do you want play again?", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.close()
            HUMAN = -1
            COMP = +1
            board = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]
            p1=[]
            p2=[]
            self.open = MainApp()
            self.open.show()
            print('Yes clicked.')
        else:
            self.close()
            self.open = MainApp3()
            self.open.show()
            print('No clicked.')
    def check_case(self):
        a=wineer()
        if a==0 :
            QMessageBox.information(self,"result","you draw with computer")
            self.play_again()
        elif a==1:
            QMessageBox.information(self, "result", "you win computer")
            self.play_again()
        elif a==2:
            QMessageBox.information(self, "result", "you loose from computer")
            self.play_again()


    def draw_o(self, value):
        if value == 1:
            self.pushButton_1.setIcon(QIcon("o.jpg"))
        elif value == 2:
            self.pushButton_2.setIcon(QIcon("o.jpg"))
        elif value == 3:
            self.pushButton_3.setIcon(QIcon("o.jpg"))
        elif value == 4:
            self.pushButton_4.setIcon(QIcon("o.jpg"))
        elif value == 5:
            self.pushButton_5.setIcon(QIcon("o.jpg"))
        elif value == 6:
            self.pushButton_6.setIcon(QIcon("o.jpg"))
        elif value == 7:
            self.pushButton_7.setIcon(QIcon("o.jpg"))
        elif value == 8:
            self.pushButton_8.setIcon(QIcon("o.jpg"))
        elif value == 9:
            self.pushButton_9.setIcon(QIcon("o.jpg"))
    def tab1(self):
        global a
        self.pushButton_1.setIcon(QIcon("x.jpg"))
        a = 1
        self.draw_o(human_turn())
        self.check_case()

    def tab2(self):
        global a
        self.pushButton_2.setIcon(QIcon("x.jpg"))
        a = 2
        self.draw_o(human_turn())
        self.check_case()

    def tab3(self):
        global a
        self.pushButton_3.setIcon(QIcon("x.jpg"))
        a = 3
        self.draw_o(human_turn())
        self.check_case()

    def tab4(self):
        global a
        self.pushButton_4.setIcon(QIcon("x.jpg"))
        a = 4
        self.draw_o(human_turn())
        self.check_case()

    def tab5(self):
        global a
        self.pushButton_5.setIcon(QIcon("x.jpg"))
        a = 5
        self.draw_o(human_turn())
        self.check_case()

    def tab6(self):
        global a
        self.pushButton_6.setIcon(QIcon("x.jpg"))
        a = 6
        self.draw_o(human_turn())
        self.check_case()

    def tab7(self):
        global a
        self.pushButton_7.setIcon(QIcon("x.jpg"))
        a = 7
        self.draw_o(human_turn())
        self.check_case()

    def tab8(self):
        global a
        self.pushButton_8.setIcon(QIcon("x.jpg"))
        a = 8
        self.draw_o(human_turn())
        self.check_case()

    def tab9(self):
        global a
        self.pushButton_9.setIcon(QIcon("x.jpg"))
        a = 9
        self.draw_o(human_turn())
        self.check_case()
###########################################################################################
class MainApp1(QMainWindow , ui):
    global a
    global HUMAN
    global COMP
    global board
    global p1
    global p2
    def __init__(self , parent=None):
        super(MainApp1 , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

########################################################################

"""easy leval"""
from random import *
Active_Player = 1
pp1 = list()
pp2 = list()
y=-1
def select_random(mylist):
    x = choice(mylist)
    return x
def Autoplay():
    global Active_Player
    global pp1
    global pp2
    global y
    if len(pp1)+len(pp2)==9 :
        return
    else :
      emp=[]
      for i in range(1,10):
          if (not ((i in pp1)or(  i in pp2))):
              emp.append(i)
      y=select_random(emp)
      Buclick(y)
def Buclick(x):
    global Active_Player
    global pp1
    global pp2
    global y
    if Active_Player == 1:
        print("you play ",x)
        pp1.append(x)
        g=wineerr()
        Active_Player = 2
        Autoplay()
    elif Active_Player == 2:
        print("computer play ", x)
        pp2.append(x)
        g=wineerr()
        Active_Player = 1
    return y , g
def wineerr():

    win = -1
    if (1 in pp1 and 2 in pp1 and 3 in pp1) or (4 in pp1 and 5 in pp1 and 6 in pp1) or (7 in pp1 and 8 in pp1 and 9 in pp1) or (1 in pp1 and 4 in pp1 and 7 in pp1) or (2 in pp1 and 5 in pp1 and 8 in pp1) or (3 in pp1 and 6 in pp1 and 9 in pp1) or (1 in pp1 and 5 in pp1 and 9 in pp1) or (3 in pp1 and 5 in pp1 and 7 in pp1): win = 1
    elif (1 in pp2 and 2 in pp2 and 3 in pp2) or (4 in pp2 and 5 in pp2 and 6 in pp2) or (7 in pp2 and 8 in pp2 and 9 in pp2) or (1 in pp2 and 4 in pp2 and 7 in pp2) or (2 in pp2 and 5 in pp2 and 8 in pp2) or (3 in pp2 and 6 in pp2 and 9 in pp2) or (1 in pp2 and 5 in pp2 and 9 in pp2) or (3 in pp2 and 5 in pp2 and 7 in pp2): win = 2
    elif len(pp1) + len(pp2)==9 :
        win=0
        print("no winner")
        pp1.clear()
        pp2.clear()
        Active_Player == 1
    if win == 1:
        print(" winner")
        pp1.clear()
        pp2.clear()
        Active_Player == 1
    if win == 2:
        print("losser")
        pp2.clear()
        pp1.clear()
        Active_Player == 1
    return win
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
ui,_ = loadUiType('main.ui')
class MainApp1(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp1 , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.animation()
        self.Handel_Buttons()

    def animation(self):
        box_animation1 = QPropertyAnimation(self.pushButton_1, b"geometry")
        box_animation1.setDuration(2500)
        box_animation1.setStartValue(QRect(0, 0, 0, 0))
        box_animation1.setEndValue(QRect(40, 9, 150, 121))
        box_animation1.start()
        self.box_animation1 = box_animation1
        box_animation2 = QPropertyAnimation(self.pushButton_2, b"geometry")
        box_animation2.setDuration(2500)
        box_animation2.setStartValue(QRect(0, 0, 0, 0))
        box_animation2.setEndValue(QRect(210, 9, 150, 121))
        box_animation2.start()
        self.box_animation2 = box_animation2
        #####
        box_animation3 = QPropertyAnimation(self.pushButton_3, b"geometry")
        box_animation3.setDuration(2500)
        box_animation3.setStartValue(QRect(0, 0, 0, 0))
        box_animation3.setEndValue(QRect(380, 9, 150, 121))
        box_animation3.start()
        self.box_animation3 = box_animation3
        #####
        box_animation4 = QPropertyAnimation(self.pushButton_4, b"geometry")
        box_animation4.setDuration(2500)
        box_animation4.setStartValue(QRect(0, 0, 0, 0))
        box_animation4.setEndValue(QRect(40, 149, 150, 121))
        box_animation4.start()
        self.box_animation4 = box_animation4
        #####
        box_animation5 = QPropertyAnimation(self.pushButton_5, b"geometry")
        box_animation5.setDuration(2500)
        box_animation5.setStartValue(QRect(0, 0, 0, 0))
        box_animation5.setEndValue(QRect(210, 149, 150, 121))
        box_animation5.start()
        self.box_animation5 = box_animation5
        #####
        box_animation6 = QPropertyAnimation(self.pushButton_6, b"geometry")
        box_animation6.setDuration(2500)
        box_animation6.setStartValue(QRect(0, 0, 0, 0))
        box_animation6.setEndValue(QRect(380, 149, 150, 121))
        box_animation6.start()
        self.box_animation6 = box_animation6
        #####
        box_animation7 = QPropertyAnimation(self.pushButton_7, b"geometry")
        box_animation7.setDuration(2500)
        box_animation7.setStartValue(QRect(0, 0, 0, 0))
        box_animation7.setEndValue(QRect(40, 290, 150, 121))
        box_animation7.start()
        self.box_animation7 = box_animation7
        #####
        box_animation8 = QPropertyAnimation(self.pushButton_8, b"geometry")
        box_animation8.setDuration(2500)
        box_animation8.setStartValue(QRect(0, 0, 0, 0))
        box_animation8.setEndValue(QRect(210, 290, 150, 121))
        box_animation8.start()
        self.box_animation8 = box_animation8
        #####
        box_animation9 = QPropertyAnimation(self.pushButton_9, b"geometry")
        box_animation9.setDuration(2500)
        box_animation9.setStartValue(QRect(0, 0, 0, 0))
        box_animation9.setEndValue(QRect(380, 290, 150, 121))
        box_animation9.start()
        self.box_animation9 = box_animation9
        #####
    def Handel_Buttons(self):
        self.pushButton_1.clicked.connect(self.tab1)
        self.pushButton_2.clicked.connect(self.tab2)
        self.pushButton_3.clicked.connect(self.tab3)
        self.pushButton_4.clicked.connect(self.tab4)
        self.pushButton_5.clicked.connect(self.tab5)
        self.pushButton_6.clicked.connect(self.tab6)
        self.pushButton_7.clicked.connect(self.tab7)
        self.pushButton_8.clicked.connect(self.tab8)
        self.pushButton_9.clicked.connect(self.tab9)

    def draw_o(self, value):
        if value == 1:
            self.pushButton_1.setIcon(QIcon("o.jpg"))
        elif value == 2:
            self.pushButton_2.setIcon(QIcon("o.jpg"))
        elif value == 3:
            self.pushButton_3.setIcon(QIcon("o.jpg"))
        elif value == 4:
            self.pushButton_4.setIcon(QIcon("o.jpg"))
        elif value == 5:
            self.pushButton_5.setIcon(QIcon("o.jpg"))
        elif value == 6:
            self.pushButton_6.setIcon(QIcon("o.jpg"))
        elif value == 7:
            self.pushButton_7.setIcon(QIcon("o.jpg"))
        elif value == 8:
            self.pushButton_8.setIcon(QIcon("o.jpg"))
        elif value == 9:
            self.pushButton_9.setIcon(QIcon("o.jpg"))
    def check_case(self,v,vv):
        if vv==0 :
            QMessageBox.information(self,"my dear","you draw with computer")
            self.play_again()
        elif vv==1:
            QMessageBox.information(self, "my dear", "youwin with computer")
            self.play_again()
        elif vv==2:
            QMessageBox.information(self, "my dear", "you lose from computer")
            self.play_again()
        else :
            self.draw_o(v)

    def play_again(self):
        global pp1
        global pp2
        global Active_Player
        global y
        buttonReply = QMessageBox.question(self, 'mydear', "Do you want play again?", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.close()
            pp1=[]
            pp2=[]
            Active_Player=1
            y=-1
            self.open = MainApp1()
            self.open.show()
            print('Yes clicked.')
        else:
            self.close()
            self.open = MainApp3()
            self.open.show()
            print('No clicked.')
    def tab1(self):
        self.pushButton_1.setIcon(QIcon("x.jpg"))
        v,vv=Buclick(1)
        self.check_case(v,vv)

    def tab2(self):
        self.pushButton_2.setIcon(QIcon("x.jpg"))
        v,vv = Buclick(2)
        self.check_case(v,vv)

    def tab3(self):
        self.pushButton_3.setIcon(QIcon("x.jpg"))
        v,vv = Buclick(3)
        self.check_case(v,vv)

    def tab4(self):
        self.pushButton_4.setIcon(QIcon("x.jpg"))
        v,vv = Buclick(4)
        self.check_case(v,vv)

    def tab5(self):
        self.pushButton_5.setIcon(QIcon("x.jpg"))
        v,vv = Buclick(5)
        self.check_case(v,vv)

    def tab6(self):
        self.pushButton_6.setIcon(QIcon("x.jpg"))
        v,vv = Buclick(6)
        self.check_case(v,vv)
    def tab7(self):
        self.pushButton_7.setIcon(QIcon("x.jpg"))
        v,vv = Buclick(7)
        self.check_case(v,vv)

    def tab8(self):
        self.pushButton_8.setIcon(QIcon("x.jpg"))
        v,vv = Buclick(8)
        self.check_case(v,vv)

    def tab9(self):
        self.pushButton_9.setIcon(QIcon("x.jpg"))
        v,vv = Buclick(9)
        self.check_case(v,vv)


##########################################################################3

#########################################################################
"""play with a friend """
def Buclickk(x):
    global Active_Player
    global pp1
    global pp2
    global y
    if Active_Player == 1:
        print("you play ",x)
        pp1.append(x)
        g=wineerrr()
        Active_Player = 2
    elif Active_Player == 2:
        print("computer play ", x)
        pp2.append(x)
        g=wineerrr()
        Active_Player = 1
    return y , g
def wineerrr():

    win = -1
    if (1 in pp1 and 2 in pp1 and 3 in pp1) or (4 in pp1 and 5 in pp1 and 6 in pp1) or (7 in pp1 and 8 in pp1 and 9 in pp1) or (1 in pp1 and 4 in pp1 and 7 in pp1) or (2 in pp1 and 5 in pp1 and 8 in pp1) or (3 in pp1 and 6 in pp1 and 9 in pp1) or (1 in pp1 and 5 in pp1 and 9 in pp1) or (3 in pp1 and 5 in pp1 and 7 in pp1): win = 1
    elif (1 in pp2 and 2 in pp2 and 3 in pp2) or (4 in pp2 and 5 in pp2 and 6 in pp2) or (7 in pp2 and 8 in pp2 and 9 in pp2) or (1 in pp2 and 4 in pp2 and 7 in pp2) or (2 in pp2 and 5 in pp2 and 8 in pp2) or (3 in pp2 and 6 in pp2 and 9 in pp2) or (1 in pp2 and 5 in pp2 and 9 in pp2) or (3 in pp2 and 5 in pp2 and 7 in pp2): win = 2
    elif len(pp1) + len(pp2)==9 :
        win=0
        print("no winner")
        pp1.clear()
        pp2.clear()
        Active_Player == 1
    if win == 1:
        print(" winner")
        pp1.clear()
        pp2.clear()
        Active_Player == 1
    if win == 2:
        print("losser")
        pp2.clear()
        pp1.clear()
        Active_Player == 1
    return win

class MainApp2(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp2 , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.animation()
        self.Handel_Buttons()

    def animation(self):
        box_animation1 = QPropertyAnimation(self.pushButton_1, b"geometry")
        box_animation1.setDuration(2500)
        box_animation1.setStartValue(QRect(0, 0, 0, 0))
        box_animation1.setEndValue(QRect(40, 9, 150, 121))
        box_animation1.start()
        self.box_animation1 = box_animation1
        box_animation2 = QPropertyAnimation(self.pushButton_2, b"geometry")
        box_animation2.setDuration(2500)
        box_animation2.setStartValue(QRect(0, 0, 0, 0))
        box_animation2.setEndValue(QRect(210, 9, 150, 121))
        box_animation2.start()
        self.box_animation2 = box_animation2
        #####
        box_animation3 = QPropertyAnimation(self.pushButton_3, b"geometry")
        box_animation3.setDuration(2500)
        box_animation3.setStartValue(QRect(0, 0, 0, 0))
        box_animation3.setEndValue(QRect(380, 9, 150, 121))
        box_animation3.start()
        self.box_animation3 = box_animation3
        #####
        box_animation4 = QPropertyAnimation(self.pushButton_4, b"geometry")
        box_animation4.setDuration(2500)
        box_animation4.setStartValue(QRect(0, 0, 0, 0))
        box_animation4.setEndValue(QRect(40, 149, 150, 121))
        box_animation4.start()
        self.box_animation4 = box_animation4
        #####
        box_animation5 = QPropertyAnimation(self.pushButton_5, b"geometry")
        box_animation5.setDuration(2500)
        box_animation5.setStartValue(QRect(0, 0, 0, 0))
        box_animation5.setEndValue(QRect(210, 149, 150, 121))
        box_animation5.start()
        self.box_animation5 = box_animation5
        #####
        box_animation6 = QPropertyAnimation(self.pushButton_6, b"geometry")
        box_animation6.setDuration(2500)
        box_animation6.setStartValue(QRect(0, 0, 0, 0))
        box_animation6.setEndValue(QRect(380, 149, 150, 121))
        box_animation6.start()
        self.box_animation6 = box_animation6
        #####
        box_animation7 = QPropertyAnimation(self.pushButton_7, b"geometry")
        box_animation7.setDuration(2500)
        box_animation7.setStartValue(QRect(0, 0, 0, 0))
        box_animation7.setEndValue(QRect(40, 290, 150, 121))
        box_animation7.start()
        self.box_animation7 = box_animation7
        #####
        box_animation8 = QPropertyAnimation(self.pushButton_8, b"geometry")
        box_animation8.setDuration(2500)
        box_animation8.setStartValue(QRect(0, 0, 0, 0))
        box_animation8.setEndValue(QRect(210, 290, 150, 121))
        box_animation8.start()
        self.box_animation8 = box_animation8
        #####
        box_animation9 = QPropertyAnimation(self.pushButton_9, b"geometry")
        box_animation9.setDuration(2500)
        box_animation9.setStartValue(QRect(0, 0, 0, 0))
        box_animation9.setEndValue(QRect(380, 290, 150, 121))
        box_animation9.start()
        self.box_animation9 = box_animation9
        #####
    def Handel_Buttons(self):
        self.pushButton_1.clicked.connect(self.tab1)
        self.pushButton_2.clicked.connect(self.tab2)
        self.pushButton_3.clicked.connect(self.tab3)
        self.pushButton_4.clicked.connect(self.tab4)
        self.pushButton_5.clicked.connect(self.tab5)
        self.pushButton_6.clicked.connect(self.tab6)
        self.pushButton_7.clicked.connect(self.tab7)
        self.pushButton_8.clicked.connect(self.tab8)
        self.pushButton_9.clicked.connect(self.tab9)

    def check_case(self,v,vv):
        if vv==0 :
            QMessageBox.information(self,"my dear","draw between 2 players")
            self.play_again()
        elif vv==1:
            QMessageBox.information(self, "my dear", "player 1 is winner")
            self.play_again()
        elif vv==2:
            QMessageBox.information(self, "my dear", "player 2 is winner")
            self.play_again()


    def play_again(self):
        global pp1
        global pp2
        global Active_Player
        global y
        buttonReply = QMessageBox.question(self, 'mydear', "Do you want play again?", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.close()
            pp1=[]
            pp2=[]
            Active_Player=1
            y=-1
            self.open = MainApp2()
            self.open.show()
            print('Yes clicked.')
        else:
            self.close()
            self.open = MainApp3()
            self.open.show()
            print('No clicked.')
    def tab1(self):
        if Active_Player ==1 :
          self.pushButton_1.setIcon(QIcon("x.jpg"))
        else :
            self.pushButton_1.setIcon(QIcon("o.jpg"))
        v,vv=Buclickk(1)
        self.check_case(v,vv)

    def tab2(self):
        if Active_Player == 1:
            self.pushButton_2.setIcon(QIcon("x.jpg"))
        else:
            self.pushButton_2.setIcon(QIcon("o.jpg"))
        v,vv = Buclickk(2)
        self.check_case(v,vv)

    def tab3(self):
        if Active_Player == 1:
            self.pushButton_3.setIcon(QIcon("x.jpg"))
        else:
            self.pushButton_3.setIcon(QIcon("o.jpg"))
        v,vv = Buclickk(3)
        self.check_case(v,vv)

    def tab4(self):
        if Active_Player == 1:
            self.pushButton_4.setIcon(QIcon("x.jpg"))
        else:
            self.pushButton_4.setIcon(QIcon("o.jpg"))
        v,vv = Buclickk(4)
        self.check_case(v,vv)

    def tab5(self):
        if Active_Player == 1:
            self.pushButton_5.setIcon(QIcon("x.jpg"))
        else:
            self.pushButton_5.setIcon(QIcon("o.jpg"))
        v,vv = Buclickk(5)
        self.check_case(v,vv)

    def tab6(self):
        if Active_Player == 1:
            self.pushButton_6.setIcon(QIcon("x.jpg"))
        else:
            self.pushButton_6.setIcon(QIcon("o.jpg"))
        v,vv = Buclickk(6)
        self.check_case(v,vv)
    def tab7(self):
        if Active_Player == 1:
            self.pushButton_7.setIcon(QIcon("x.jpg"))
        else:
            self.pushButton_7.setIcon(QIcon("o.jpg"))
        v,vv = Buclickk(7)
        self.check_case(v,vv)

    def tab8(self):
        if Active_Player == 1:
            self.pushButton_8.setIcon(QIcon("x.jpg"))
        else:
            self.pushButton_8.setIcon(QIcon("o.jpg"))
        v,vv = Buclickk(8)
        self.check_case(v,vv)

    def tab9(self):
        if Active_Player == 1:
            self.pushButton_9.setIcon(QIcon("x.jpg"))
        else:
            self.pushButton_9.setIcon(QIcon("o.jpg"))
        v,vv = Buclickk(9)
        self.check_case(v,vv)

##########################################################################
#########################
"""welcome page"""
uii,_ = loadUiType('main0.ui')
class MainApp3(QMainWindow , uii):

    def __init__(self , parent=None):
        super(MainApp3 , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
    def Handel_Buttons(self):
        self.pushButton_2.clicked.connect(self.hard)
        self.pushButton_3.clicked.connect(self.easy)
        self.pushButton.clicked.connect(self.friend)
    def easy(self):
        self.close()
        self.open = MainApp()
        self.open.show()
    def hard(self):
        self.close()
        self.open = MainApp1()
        self.open.show()
    def friend(self):
        self.close()
        self.open = MainApp2()
        self.open.show()



######################
def main():
    app = QApplication(sys.argv)
    window = MainApp3()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()