from core import DoublyLinkedList
from prettytable import PrettyTable


class Todos(DoublyLinkedList):

    def getAll(self) -> list:
        todos = []
        temp = self.head
        iterate = 0
        while temp is not None:
            iterate += 1
            status = temp.data["completed"]
            completed = ""

            if not status:
                completed = "NOT COMPLETED"
            else:
                completed = "COMPLETED"

            todos.append([
                iterate,
                temp.data["id"],
                temp.data["todo"],
                completed
            ])

            temp = temp.next_node

        return todos

    def getById(self, id):
        temp = self.head
        id = int(id)
        while temp is not None:
            if temp.data["id"] == id:
                return temp

            temp = temp.next_node

        return None

    def print_table(self):
        table = PrettyTable()
        table.field_names = ["no", "id", "todo", "completed"]
        table.align = "l"

        todos = self.getAll()
        table.add_rows(todos)
        print(table)
