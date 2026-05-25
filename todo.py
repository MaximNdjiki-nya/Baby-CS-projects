"""a simple to do list"""
import typing
import json
from pathlib import Path

def show_menu() -> None:
    """ Prints out menu options for to do list"""
    print("Show to do list")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Quit ")

tasks: list[dict[str, typing.Any]] = []

def add_tasks(task: list[dict[str, typing.Any]]) -> list[str]:
    """Stores users entered tasks"""
    add_todo = input("\n Please enter the task you would like to store: ")
    new_task = {"Name": add_todo, "done": False}
    task.append(new_task)

def show_tasks(view_list: list[dict[str, typing.Any]]) -> None:
    """Prints out the tasks stored in tasks """
    for index, item in enumerate(view_list, start=1):
        if not item["done"]:
            print(str(index) + ".)", item["Name"]+"[]")
        else:
            print(str(index) + ".)", item["Name"]+"[X]")
    print("\n")

def delete_tasks(view_list: list[dict[str, typing.Any]]) -> None:
    """Deletes tasks from the tasks list"""
    show_tasks(view_list)
    user_del = int(input("Which tasks would you like to delete? "))
    while user_del > len(view_list) or user_del < 1:
        user_del = int(input("\n Please try again? "))
    del view_list[user_del -1]
    show_tasks(view_list)

def complete_tasks(view_lists: list[dict[str, typing.Any]]) -> None:
    """Shows the completed tasks"""
    show_tasks(tasks)
    user_choice = int(input("\nWhat tasks have you completed? "))
    while user_choice > len(view_lists) or user_choice < 1:
        user_choice = int(input("\n Please try again? "))
    view_lists[user_choice -1]["done"] = True

def todo_save(task_list: list[dict[str, typing.Any]])-> None:
    """saves tasks as a json file"""
    with open("task_list.json", "w", encoding="utf-8") as f:
        json.dump(task_list, f)

def todo_load() -> list[dict[str, typing.Any]]:
    "loads the to do list when the app is opened"
    file_path = Path("tasks.json")
    if file_path.is_file():
        with open("tasks.json", "r", encoding="utf-8") as f:
            data: list[dict[str, typing.Any]] = json.load(f)
        return data
    else:
        return []


def main()-> None:
    "Demonstrates the logic for to do list and calls functuions"
    while True:
        show_menu()
        choice = input("\n \nEnter choice (1-5): ")

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_tasks(tasks)
        elif choice == "4":
            delete_tasks(tasks)
        elif choice == "5":
            todo_save(tasks)
            print("Saving file now....Goodbye!")
            break
    else:
        print("invalid choice, try again!")


main()
print(tasks)
