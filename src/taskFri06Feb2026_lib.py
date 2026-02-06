class Lib1:
    def printList(self, list):
        # Тестване
        # if __name__ == "__main__":
        # print("Матрица:")
        for row in list:
            print(row)

class Node:
    """Възел в 2D свързан списък"""

    def __init__(self, value):
        self.value = value
        self.right = None  # връзка надясно
        self.down = None  # връзка надолу

    def __repr__(self):
        return f"Node({self.value})"


class LinkedMatrix2D:
    """2D матрица от свързан списък"""

    def __init__(self, matrix):
        """
        Конструктор - конвертира 2D списък в свързана матрица

        Args:
            matrix: списък от списъци (квадратна матрица)
        """
        if not matrix or not matrix[0]:
            self.head = None
            self.size = 0
            return

        self.size = len(matrix)

        # Създаваме матрица от Node обекти
        node_matrix = []
        for row in matrix:
            node_row = [Node(val) for val in row]
            node_matrix.append(node_row)

        # Свързваме възлите
        for i in range(self.size):
            for j in range(self.size):
                current = node_matrix[i][j]

                # Свързваме надясно (ако не е последна колона)
                if j < self.size - 1:
                    current.right = node_matrix[i][j + 1]

                # Свързваме надолу (ако не е последен ред)
                if i < self.size - 1:
                    current.down = node_matrix[i + 1][j]

        # Запазваме началото на матрицата
        self.head = node_matrix[0][0]

    def print_matrix(self):
        """Отпечатва матрицата във формат показващ връзките"""
        if not self.head:
            print("Empty matrix")
            return

        current_row = self.head

        while current_row:
            # Печатаме текущия ред
            current = current_row
            while current:
                print(f"{current.value}", end="")
                if current.right:
                    print(" -> ", end="")
                current = current.right
            print(" -> None")

            # Печатаме стрелките надолу
            if current_row.down:
                current = current_row
                while current:
                    print("|", end="")
                    if current.right:
                        print("       ", end="")
                    current = current.right
                print()

                current = current_row
                while current:
                    print("v", end="")
                    if current.right:
                        print("      ", end="")
                    current = current.right
                print()

            current_row = current_row.down

        # Печатаме последните None стойности
        print("|", end="")
        for _ in range(self.size - 1):
            print("       |", end="")
        print()
        print("v", end="")
        for _ in range(self.size - 1):
            print("      v", end="")
        print()
        for _ in range(self.size):
            print("None", end="")
            if _ < self.size - 1:
                print(" ", end="")
        print()

    def print_main_diagonal(self):
        """
        Отпечатва стойностите по главния диагонал,
        следвайки връзките в свързания списък
        """
        if not self.head:
            return

        diagonal_values = []
        current = self.head

        # Следваме диагонала: current -> current.down.right
        while current:
            diagonal_values.append(str(current.value))

            # Преминаваме към следващия диагонален елемент
            # Първо надолу, после надясно
            if current.down and current.down.right:
                current = current.down.right
            elif current.down:
                # Ако няма right, но има down (последна колона)
                current = current.down
            else:
                # Достигнахме края
                break

        print(" " + ", ".join(diagonal_values))

