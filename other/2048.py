#2048

import random

class Grid:
    row_length = 4
    #defining standard row length in the game
    col_length = 4
    #defining standard column length in the game
    matrix = [[0 for x in range(row_length)] for y in range(col_length)]
    #creates a matrix that has the defined lengths and all elements 0

    random_fill(random_number)


    def random_fill(filler):

        index_random = random.randrange(0, row_length * col_length - 1)
        #picks a rondom singular index number
        row_R = index_random / row_length
        col_R = index_random % row_length

        while matrix[row_R][col_R] != 0:

            index_random = random.randrange(0, row_length * col_length - 1)
            #picks a rondom singular index number
            row_R = index_random / row_length
            col_R = index_random % row_length

        matrix[row_R][col_R] = filler
        #fills matrice's from top left to bottom right, index_randomth element

    def random_number():
        odds = random.randrange(1, 10)
        number = -1
        if odds > 9:
            number = 4
        else:
            number = 2
        return number
