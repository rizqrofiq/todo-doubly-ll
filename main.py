import pyfiglet
import inquirer
import os
from todos import Todos


def main():
    todos = Todos()

    while True:
        os.system("clear")  # or "cls" on Windows
        print(pyfiglet.figlet_format("Todo App"))
        print("Welcome to the Todo App\n")

        print("Here are your options:")
        print("1. Add a new todo")
        print("2. View all todos")
        print("3. Search a todo")
        print("4. Update a todo")
        print("5. Delete a todo")
        print("6. Exit\n")

        option = inquirer.prompt([
            inquirer.Text("option", message="What would you like to do? [1-6]")
        ])

        option = int(option["option"])

        if option == 1:
            os.system("clear")  # or "cls" on Windows
            print("You chose to add a new todo")

            new_todo = inquirer.prompt([
                inquirer.Text("new_todo", message="What is the new todo?")
            ])

            todos.append({
                "id": todos.length + 1,
                "todo": new_todo["new_todo"],
                "completed": False
            })

            print("Todo added successfully")

        elif option == 2:
            os.system('clear')
            if todos.length == 0:
                print("You have no todos")
            else:
                todos.print_table()

        elif option == 3:
            os.system("clear")
            print("Search by ID")
            answer = inquirer.prompt([
                inquirer.Text("id", message="Enter the ID")
            ])

            todo = todos.getById(answer["id"])
            if todo is None:
                print("Todo not found")
                continue

            completed = ""
            if todo.data["completed"]:
                completed = "COMPLETED"
            else:
                completed = "NOT COMPLETED"

            print("\n==============================")
            print(f"ID: {todo.data['id']}")
            print(f"TODO: {todo.data['todo']}")
            print(f"COMPLETED: {completed}")
            print("============================== \n")

        elif option == 4:
            os.system("clear")
            print("Update by ID")
            answer = inquirer.prompt([
                inquirer.Text("id", message='Enter the ID')
            ])

            todo = todos.getById(answer['id'])

            if todo is None:
                print("Todo not found")
                continue

            answer = inquirer.prompt([
                inquirer.List(
                    "do",
                    message="What would you like to do?",
                    choices=[
                        ("Change todo", "todo"),
                        ("Update status", "status")
                    ]
                )
            ])

            if answer["do"] == "todo":
                answer = inquirer.prompt([
                    inquirer.Text("todo", message="New Todo")
                ])

                todo.data["todo"] = answer["todo"]
                todos.set_value((todo.data["id"] - 1), todo.data)
            else:
                answer = inquirer.prompt([
                    inquirer.List(
                        "status",
                        message="Status",
                        choices=[
                            ("Completed", True),
                            ("Not Completed", False)
                        ]
                    )
                ])

                todo.data["completed"] = answer["status"]
                todos.set_value((todo.data["id"] - 1), todo.data)

            print("Todo updated successfully")

        elif option == 5:
            os.system("clear")
            print("Delete by ID")
            answer = inquirer.prompt([
                inquirer.Text("id", message="Enter the ID")
            ])

            todo = todos.getById(answer["id"])

            if todo is None:
                print("Todo not found")
                continue

            todos.remove_at_index(todo.data["id"] - 1)
            print("Todo deleted successfully")

        input("Press any key to continue...")


if __name__ == "__main__":
    main()
