






# solution for the homework task fo Fri06Feb2026
print("Program start<<<<<<<<<<<<<<<<<<<<")
lib = Lib1()
ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_end(5)
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_end(6)
ll.insert_at_end(7)
ll.display()
print("Please, enter the index of the element you want to see: ")
elemIndex = input()
try:
    elemIndex = int(elemIndex)
    print(f"Element at index {elemIndex} is: {ll.get_element_at_index(elemIndex)}")
except ValueError:
    print("Invalid input. Please enter a valid integer index.")
print("Program end>>>>>>>>>>>>>>>>>>>>>>>")



# list1 = [1, 2, 3]
# Входна матрица, списък от списъци
squareMatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# lib.printList(squareMatrix)
# print()
# lib.printList(list1)
# linkedList2dMatrix = LinkedMatrix2D(squareMatrix)
# linkedList2dMatrix.print_matrix()
# linkedList2dMatrix.print_main_diagonal()


# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
#def print_hi(name):
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#  print_hi('PyCharm2')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/