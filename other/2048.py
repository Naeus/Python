#2048

import random

class Grid:

    def __init__(self):
        self.row_length = 4
        #defining standard row length in the game
        self.col_length = 4
        #defining standard column length in the game
        self.matrix = [[0 for x in range(self.row_length)] for y in range(self.col_length)]
        #creates a matrix that has the defined lengths and all elements 0

        self.random_fill()
        self.random_fill()


    def random_fill(self):

        #if 0 in self.matrix:
        index_random = random.randrange(0, self.row_length * self.col_length)
        #picks a rondom singular index number
        row_R = index_random // self.row_length
        col_R = index_random % self.row_length

        while self.matrix[row_R][col_R] != 0:

            index_random = random.randrange(0, self.row_length * self.col_length)
            #picks a rondom singular index number
            row_R = index_random // self.row_length
            col_R = index_random % self.row_length

        filler = self.random_number()
        self.matrix[row_R][col_R] = filler
        #fills matrice's from top left to bottom right, index_randomth element

    def random_number(self):
        odds = random.randrange(1, 11)
        number = -1
        if odds > 9:
            number = 4
        else:
            number = 2
        return number





#TESTER
a = Grid()

input()
