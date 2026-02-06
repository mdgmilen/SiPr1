# from .taskFri06Feb2026_lib import Lib1
from .lib import LinkedList


if __name__ == '__main__':
    print("Program start<<<<<<<<<<<<<<<<<<<<")
    ll =  LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_end(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.display()
    ll.insert_at_index(3, 100)
    ll.display()
    print("Program end>>>>>>>>>>>>>>>>>>>>>>>")