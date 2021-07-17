#!/usr/local/bin/python3
#export PATH="/Users/bradley/Desktop/Personal Projects/todo:${PATH}"
# file todo/__main__.py

import sys
from src.Parser import Parser
from src.TodoList import TodoList

def main():
    args = Parser.parse_args(sys.argv[1:])
    TodoList.execute_args(args)
    TodoList.clean()
    TodoList.show()
    sys.exit()


if __name__ == '__main__':
  main()
