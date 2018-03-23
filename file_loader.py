from os import listdir
from os.path import isfile, join
import random


def random_file(path_to_files):

    files_in_folder = [f for f in listdir(
        path_to_files) if isfile(join(path_to_files, f))]

    selected_file = (random.choice(files_in_folder))

    return path_to_files + selected_file
