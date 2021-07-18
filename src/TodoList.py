import os
from pathlib import Path
from .HistoryList import HistoryList

class TodoList:
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    dev_script_path = "/Users/bradley/Desktop/Personal Projects/todo/src"
    dev_todo_list_path = "./resources/todo_list.txt"
    live_todo_list_path = "/Users/bradley/bin/todo_list.txt"

    if current_script_path == dev_script_path:
        todo_list_path = dev_todo_list_path
    else:
        todo_list_path = live_todo_list_path

    if not Path(todo_list_path).exists():
        file = open(todo_list_path, "w")
        file.close()

    @classmethod
    def execute_args(cls, parsed_args):
        if len(parsed_args["r"]) > 0:
            cls.remove(parsed_args["r"])

        if len(parsed_args["a"]) != 0:
            cls.amend(parsed_args["a"][0], parsed_args["i"])
            return

        if parsed_args["i"] != "" and len(parsed_args["a"]) == 0:
            cls.add(parsed_args["i"])

    @classmethod
    def show(cls):
        with open(cls.todo_list_path, "r") as todo_list:
            print("\n#################\n### TODO LIST ###\n#################\n")
            all_items = todo_list.readlines()
            for i in range(len(all_items)):
                formatted_item = (str(i + 1) + ". " + all_items[i]).strip()
                print(formatted_item)
            print("\n")

    @classmethod
    def clean(cls):
        with open(cls.todo_list_path, 'r') as todo_list:
            all_items = todo_list.readlines()
        with open(cls.todo_list_path, "w") as todo_list:
            for line in all_items:
                if line.strip():
                    todo_list.write(line)

    @classmethod
    def add(cls, item):
        """
        :param item: String, line to add to list.
        """
        with open(cls.todo_list_path, "a") as todo_list:
            todo_list.write(item + "\n")
            print("Item added to list: " + item + ".")
            HistoryList.add(item, "ADDED")

    @classmethod
    def amend(cls, item_index, amended_item):
        """
        :param item_index: Int, item index to add to list.
        :param amended_item: String, string to replace the current item.
        """
        with open(cls.todo_list_path, "r") as todo_list:
            all_items = todo_list.readlines()

        with open(cls.todo_list_path, "w") as todo_list:
            for i, current_item in enumerate(all_items):
                if (i != item_index):
                    item = current_item
                else:
                    item = amended_item + "\n"
                    HistoryList.add(amended_item, "AMENDED")
                todo_list.write(item)


    @classmethod
    def remove(cls, item_numbers):
        """
        :param item_number: Int, number of line to be removed.
        """
        for item_number in item_numbers:
            item_index = item_number
            with open(cls.todo_list_path, "r") as todo_list:
                all_items = todo_list.readlines()

            with open(cls.todo_list_path, "w") as todo_list:
                for i, item in enumerate(all_items):
                    if i != item_index and item.strip() != "":
                        todo_list.write(item)
                    else:
                        print(f"\nRemoved item {i + 1}: {item.strip()}")
                        HistoryList.add(item.strip(), "REMOVED")
