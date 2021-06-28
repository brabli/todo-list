#!/usr/local/bin/python3
#export PATH="/Users/bradley/Desktop/Personal Projects/todo:${PATH}"

import os
import sys
from pathlib import Path

all_args = sys.argv[1:]


class TodoList:
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    path = "./todo_list.txt" if current_script_path == \
        "/Users/bradley/Desktop/Personal Projects/todo" else "/Users/bradley/bin/todo_list.txt"
    if not Path(path).exists():
        file = open(path, "w")
        file.close()

    @classmethod
    def execute_args(parsed_args):
        None

    @classmethod
    def show(cls):
        with open(cls.path, "r") as todo_list:
            print("\n#################\n### TODO LIST ###\n#################\n")
            all_items = todo_list.readlines()
            for i in range(len(all_items)):
                formatted_item = (str(i + 1) + ". " + all_items[i]).strip()
                print(formatted_item)
            print("\n")

    @classmethod
    def clean(cls):
        with open(cls.path, 'r') as todo_list:
            all_items = todo_list.readlines()
        with open(cls.path, "w") as todo_list:
            for line in all_items:
                if line.strip():
                    todo_list.write(line)

    @classmethod
    def add(cls, item):
        """
        :param item: String, line to add to list.
        """
        with open(cls.path, "a") as todo_list:
            todo_list.write(item + "\n")
            print("Item added to list: " + item + ".")

    @classmethod
    def remove(cls, item_numbers):
        """
        :param item_number: Int, number of line to be removed.
        """
        for item_number in item_numbers:
            item_index = item_number
            with open(cls.path, "r") as todo_list:
                all_items = todo_list.readlines()
            with open(cls.path, "w") as todo_list:
                for i, item in enumerate(all_items):
                    if i != item_index and item.strip() != "":
                        todo_list.write(item)


class Parser:
    @classmethod
    def parse_args(cls, args):
        """
        :param args: All args EXCEPT for first arg which is the filepath.
        """
        parsed_args = { "r": [], "i": [], "a": [] }
        # r: remove, i: item, a: apend
        for arg in args:
            if arg[0] == "-":
                option = arg[1]

                if option == "r":
                    lines_to_remove = arg[2:].split(",")
                    for line_num in lines_to_remove:
                        item_index = int(line_num) - 1
                        parsed_args["r"].append(item_index)

                elif option == "a":
                    line_to_amend = arg[2:]
                    index_to_amend = int(line_to_amend) - 1
                    parsed_args["a"].append(index_to_amend)

                elif option == "":
                    None

            else:
                parsed_args["i"].append(arg)

        parsed_args["r"].sort(reverse = True)
        parsed_args["i"] = cls.create_list_item(parsed_args["i"])

        return parsed_args

    @classmethod
    def create_list_item(cls, word_list):
        if len(word_list) != 0:
            word_list[0] = word_list[0].capitalize()
        todo_item = " ".join(word_list)
        return todo_item


if (len(all_args) == 0):
    TodoList.show()
    sys.exit()

args = Parser.parse_args(all_args)

TodoList.clean()

if args["i"] != "":
    TodoList.add(args["i"])

if len(args["r"]) > 0:
    TodoList.remove(args["r"])

TodoList.show()

sys.exit()
