import os.path
from constants import *
from collections import defaultdict
from shutil import move


# list all the files and items that exist under PATH
def create_new_file_name(fname: str, extension: str):
    return os.path.join(PATH,extension,fname)


def get_extension(full_path: str):
    return '' if full_path.rfind('.') == -1 \
        else full_path[full_path.rfind('.')+1:]


def drop_no_extension_files(all_items):
    all_items_with_extension = []
    for i in range(len(all_items)):
        if all_items[i].__contains__('.'):
            all_items_with_extension.append(all_items[i])
    return all_items_with_extension


def drop_script_files(all_items):
    all_items.remove('constants.py')
    all_items.remove('main.py')


def get_items_in_bins():
    all_items = os.listdir(PATH)
    all_items = drop_hidden_files(all_items)
    all_items = drop_no_extension_files(all_items)
    drop_script_files(all_items)
    extension_bins = defaultdict(list)
    for item_name in all_items:
        extension_bins[get_extension(item_name)].append(item_name)
    return extension_bins


def drop_hidden_files(all_items):
    all_items_no_hidden_files = []
    for i in range(len(all_items)):
        if not all_items[i].startswith('.'):
            all_items_no_hidden_files.append(all_items[i])
    return all_items_no_hidden_files


def main():
    bins = get_items_in_bins()
    for extension in bins.keys():
        new_path = os.path.join(PATH, extension)
        if not os.path.exists(new_path):
            os.mkdir(new_path)
        for item in bins[extension]:
            move(item, create_new_file_name(item, extension))



if __name__ == '__main__':
    main()
