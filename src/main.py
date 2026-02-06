from .taskFri06Feb2026_lib import Lib1
from .taskFri06Feb2026_lib import LinkedMatrix2D

if __name__ == '__main__':
    print("Program start<<<<<<<<<<<<<<<<<<<<")
    lib = Lib1()
    # list1 = [1, 2, 3]
    # Входна матрица, списък от списъци
    squareMatrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    #1 lib.printList(squareMatrix)
    # print()
    # lib.printList(list1)
    linkedList2dMatrix = LinkedMatrix2D(squareMatrix)
    # linkedList2dMatrix.print_matrix()
    # linkedList2dMatrix.print_main_diagonal()
    print("Program end>>>>>>>>>>>>>>>>>>>>>>>")