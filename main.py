import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainWin.ui', self)

        self.buttons = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8,
                        self.btn_9]

        self.x_sign = '✗'
        self.o_sign = '◯'
        self.x_turn = False
        self.current_motion = 0
        self.field = [" "] * 9
        self.count_btn = 0

        self.start_btn.clicked.connect(self.start_game)

        for i, btn in enumerate(self.buttons):
            btn.clicked.connect(lambda _, btn=btn, cur_mot=i: self.btn_realize(btn, cur_mot))

    def win_check(self, field, sign):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(field[i] == sign for i in combo) for combo in winning_combinations)

    def btn_realize(self, btn, cur_mot):
        self.x_turn = not self.x_turn
        sign = self.x_sign if self.x_turn else self.o_sign
        btn.setText(sign)

        self.current_motion = cur_mot
        self.field[self.current_motion] = sign

        if self.win_check(self.field, self.x_sign):
            self.res_txt.setText(self.x_sign)
        elif self.win_check(self.field, self.o_sign):
            self.res_txt.setText(self.o_sign)
        elif self.count_btn == 8:
            self.res_txt.setText('TIE')

        self.count_btn += 1
    


    def start_game(self):
        self.res_txt.setText(' ')
        self.count_btn = 0

        self.x_turn = False
        for btn in self.buttons:
            btn.setText('')

        self.field = [" "] * 9

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
