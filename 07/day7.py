########## PART 1 ##########
import sys
from typing import List

CMD = '$'
DIRECTORY = 'dir'
LIST = 'ls'
CHANGE = 'cd'


class FileSystemObject:

    def __init__(
            self,
            name: str = '',
            children=None,
            parent=None,
            size: int = 0
    ):
        if children is None:
            children = []
        self.name = name
        self.children = children
        self.parent = parent
        self.size = size


# find directories <= 10000
def find_directories_lte_10000(file_system_obj: FileSystemObject, result):
    if file_system_obj.size <= 100000 and file_system_obj.children != []:
        result.append(file_system_obj)

    for c in file_system_obj.children:
        if c not in result:
            find_directories_lte_10000(c, result)


def get_child(children: List, child):
    for c in children:
        if child == c.name:
            return c

    return None


def calculate_size(obj: FileSystemObject):
    if obj.size != 0:
        return obj.size

    total_size = 0
    for c in obj.children:
        total_size += calculate_size(c)
    obj.size = total_size
    return total_size


with open('day7-input.txt') as f:
    lines = f.readlines()

root = FileSystemObject(name='/')
current_directory = root
for i in range(len(lines)):

    if len(lines[i]) == 0:
        break

    tokens = lines[i].strip().split()

    if tokens[0] == CMD:
        command = tokens[1]

        if tokens[1] == CHANGE:
            if tokens[2] == '..':  # go up
                current_directory = current_directory.parent
            elif tokens[2] == '/':  # go back to root
                current_directory = root
            else:  # go to child directory
                child = get_child(current_directory.children, tokens[2])
                if not child:
                    print(f"Directory {tokens[2]} not found from previously listed directories, exiting...")
                    sys.exit(0)
                current_directory = child
        elif tokens[1] == LIST:
            for x in range(i + 1, len(lines)):
                if len(lines[x]) == 0:
                    break

                ls_output = lines[x].strip().split()
                if ls_output[0] == CMD:
                    break

                child = get_child(current_directory.children, ls_output[1])
                if child is None:
                    child = FileSystemObject(name=ls_output[1], parent=current_directory)
                    current_directory.children.append(child)

                if ls_output[0] == DIRECTORY:
                    continue
                else:
                    size = int(ls_output[0])
                    child.size = size
        else:
            print(f"Unknown command '{tokens[1]}' parsed, exiting")
            sys.exit(0)

# now we should be able to calculate the size of all of the directories contained within root
root.size = calculate_size(root)
# find the directories with a total size of at most 100000 for part 1, build up our result
res = []
find_directories_lte_10000(root, res)
total = 0
for x in res:
    total += x.size
print(f"part 1 total: {total}")




