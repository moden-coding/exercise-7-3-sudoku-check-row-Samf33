# Write your solution here
def row_correct(sudoku : list, row_index : int):
    count1 = 0
    count2 = 0
    for num in sudoku[row_index]:
        count1 += 1
        for nom in sudoku[row_index]:
            count2+=1
            if nom == num and nom != 0 and num != 0 and count1 != count2:
                return False
        count2 = 0
    return True



if __name__ == "__main__":

    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 6))