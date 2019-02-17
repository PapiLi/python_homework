from graphics import *
from button import Button

class ruleswin:
    def __init__(self):
        self.win = GraphWin("rules", 800, 240)
        self.win.setBackground("green3")

        banner = Text(Point(400, 30), "Rules")
        banner.setSize(25)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)

        self.msg1 = Text(Point(400, 60), "1 The player starts with $100. ")
        self.msg1.setSize(15)
        self.msg1.draw(self.win)

        self.msg2 = Text(Point(400, 90), "2 Each round costs $10 to play. This amount is subtracted from the player's ")
        self.msg2.setSize(15)
        self.msg2.draw(self.win)

        self.msg3 = Text(Point(400, 120), "money at the start of the round.  ")
        self.msg3.setSize(15)
        self.msg3.draw(self.win)

        self.msg4 = Text(Point(400, 150), "3 The player initially rolls a completely random hand (i.e., all five dice are rolled). ")
        self.msg4.setSize(15)
        self.msg4.draw(self.win)

        self.msg5 = Text(Point(400, 180), "4 The player gets two chances to enhance the hand by rerolling some or all of the dice. ")
        self.msg5.setSize(15)
        self.msg5.draw(self.win)

        self.buttons = []
        b = Button(self.win, Point(400, 215), 40, 30, "Exit")
        b.activate()
        self.buttons.append(b)

    def choose(self, choices):
        buttons = self.buttons
        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here.

    def select(self):
        ans = self.choose(["Exit"])
        while ans != "Exit":
            ans = self.choose(["Exit"])
        self.close()

    def close(self):
        self.win.close()