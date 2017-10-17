#! python3


class Button:



    def __init__(self, name, size, position, win_siz):
        self.isPressed = False
        self.name = name
        self.bg_color = 'default'
        self.txt_color = 'default'
        self.width = size[0]
        self.height = size[1]
        self.x = max(min(position[0], win_siz[0]), 0)
        self.y = max(min(position[1], win_siz[1]), 0)

    def press(self):
        self.isPressed = True

        if self.name == '+':
            pass



class ScreenDisplay:

    def __init__(self, size, position, win_siz, text = ''):
        self.text = text
        self.bg_color = 'default'
        self.txt_color = 'default'
        self.width = size[0]
        self.height = size[1]
        self.x = max(min(position[0], win_siz[0]), 0)
        self.y = max(min(position[1], win_siz[1]), 0)





# TEST


plusButton = Button("+", [5, 5], [2, 3], [800, 600])
screen = ScreenDisplay([2,8], [0,0], [800,600])
input()
