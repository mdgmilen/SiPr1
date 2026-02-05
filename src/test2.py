# file's first line
from .lib import LinkedList
# Main block begin. Example Usage:
print("Program start<<<<<<<<<<<<<<<<<<<<")
ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_end(5)
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_end(6)
ll.insert_at_end(7)
ll.display()  
# 20 -> 10 -> 1 -> 5 -> 6 -> 7 -> None
print("Without 'is not None'")
current = ll.head
while current:
  #elements.append(str(current.data))
  print(current.data)
  current = current.next
#
print("With 'is not None'")
current = ll.head
while current is not None:
  print(current.data)
  current = current.next
#
print("CurrentList is list")
currentList = LinkedList()
# the following fails
#currentList = ll
# populate CurrentList by copying ll
llCurrent = ll.head
while llCurrent is not None:
  currentList.insert_at_end(llCurrent.data)
  llCurrent = llCurrent.next
# print the correctly populated CurrentList
currentListCurrent = currentList.head
while currentListCurrent is not None:
  print(currentListCurrent.data)
  currentListCurrent = currentListCurrent.next
# display both lists
ll.display()
currentList.display()
print("Program end>>>>>>>>>>>>>>>>>>>>>>>")
# Main block end
# file's last line