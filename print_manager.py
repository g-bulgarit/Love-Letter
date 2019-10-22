import subprocess
from time import sleep
import os
import glob

def _getfiles(path_to_dir):
    file_list = glob.glob(path_to_dir + "*.*")
    try:
        file_list.remove("/home/pi/LoveLetter/Images/whitelist.txt")
    except ValueError:
        pass
    return file_list


def _list_difference(list1, list2):
    """
    Return the difference between list1 and list2.
    :return: list that contains values that are only present in one of the lists.
    """

    output = [item for item in list2 if item not in list1]
    return output


def create_whitelist(path):
    """
    Function creates whitelist to prevent re-printing.
    """
    if not os.path.exists(path + "whitelist.txt"):
        with open(path + r"whitelist.txt", "w+") as whitelist:
            whitelist.close()


def update_whitelist(path, filename):
    """
    Function that adds the printed files to the whitelist to prevent re-printing.
    """
    with open(path + r"whitelist.txt", "a") as whitelist:
        try:
            whitelist.write(str(filename)+"\n")
        finally:
            whitelist.close()


def get_existing_whitelist(path):
    """
    Function that fetches all files from the whitelist.
    """
    current_whitelist = []
    with open(path + r"whitelist.txt", "r") as whitelist:
        try:
            for line in whitelist.readlines():
                current_whitelist.append(line.strip())
        finally:
            whitelist.close()

    return current_whitelist


def print_file(image_path):
    """
    Send a print request to the printer, fit to page.
    Afterwards, update the whitelist to prevent the file from printing again.
    :param image_path: path to file
    :return: Nothing
    """
    p = subprocess.Popen(["lp", "-o", "fit-to-page", image_path],
                         stdout=subprocess.PIPE,
                         shell=False)
    output, _ = p.communicate()


def remove_file(image_path):
    """
    Delete the file from the filesystem
    :param image_path: path to file
    :return: Nothing.
    """
    if os.path.exists(image_path):
        os.remove(image_path)


def queue_and_print(path, channel=None):
    create_whitelist(path)

    existing_whitelist = get_existing_whitelist(path)
    current_files = _getfiles(path)
    new_files = _list_difference(existing_whitelist, current_files)

    print("[!] Found " + str(len(new_files)) + " new files to print!")

    for file_to_print in new_files:
        print("[i] Printing file: " + str(file_to_print))
        print_file(file_to_print)

        print("[i] Adding " + str(file_to_print) + " to whitelist...")
        update_whitelist(path, file_to_print)


if __name__ == "__main__":
    whitelist_path = r"/home/pi/LoveLetter/Images/"
    while True:
        queue_and_print(whitelist_path)
        sleep(5)
