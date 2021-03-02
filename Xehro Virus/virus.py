#! /usr/bin/env python3
# # coding=utf-8
"""
Create an object-oriented virus.

The program will prompt the user for a letter input. With the
letter input, the program will open up a file named gandalf.txt
and locate all the occurances of the user input. It will then
replace that letter in the gandalf.txt file will a random
silly word, located in the file silly_words.txt. It will then
save the file in current working directory as infected_file.txt
The program will then create a copy of itself in the directory
and replicate itself onto the desktop.

Charlie Say
CS 162
10:00 AM

File Handle
    - Open new file infected_file.txt
    - Create list
    - User Input
    - Conditional statements for input
    - Error Handling
    - Open Gandalf.txt
        - Append lines to list

Recursive Cipher Function
    - Open & read silly_words.txt
    - Search for input letter in gandalf.txt
    - Replace letters for words
    - Write in file infected_file.txt
    - Close file

File Flood Function
    - Locate desktop directory
    - Copy infected_file.txt as foobar

"""


import random
import os
import shutil


def target_letter():
    """Get user input."""
    letter = input("Pick a letter: ")
    return letter


def open_silly():
    """Open silly_words.txt file."""
    with open("silly words.txt") as silly:
        silly_data = silly.readlines()
        ran_word = random.choice(silly_data)
        delete_line = ran_word.rstrip("\n")
    return delete_line


def payload(current_num, count):
    """Copy encrypted file and flood desktop using recursion."""
    shutil.copy("infected_file.txt", os.path.join(os.environ["HOMEPATH"], "Desktop", f"OMEGALUL-{current_num}.txt"))
    if current_num == 200:
        return count
    return payload(current_num + 1, count + current_num)


class XehroVirus():
    """Create class function and methods for virus."""

    def __init__(self, letter):
        """Initialize methods."""
        self.glist = []
        self.infected_file = open("infected_file.txt", "w+")
        with open("gandalf.txt", 'r') as gandalf:
            data = gandalf.read()
            self.glist.append(data)
        self.letter = letter

    def check_status(self, letter):
        """Check conditions of input."""
        letter_str = "aabcdefghijklmnopqrstuvwxyz"
        cap_str = "AABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if self.letter.isdigit() is True:
            print("No integers please.")
            return

        str_test = str(self.letter)
        if len(str_test) > 1:
            print("Needs to be a single letter.")
            return

        if self.letter not in letter_str and self.letter not in cap_str:
            print("Nice try. ;)")
            return

        silly_word = open_silly()
        xehro_me = XehroVirus(letter)
        xehro_me.cipher_func(silly_word)

    def cipher_func(self, delete_line):
        """Cipher the target text file."""
        join_me = "".join(self.glist)
        find_me = join_me.find(self.letter)
        rep_me = join_me.replace(join_me[find_me], delete_line)

        self.infected_file.write(rep_me)
        self.infected_file.close()
        print(f"Your random word is: {delete_line}\n")
        print(f"There should be a copy of the infected file in your directory "
              "& 200 copies on your desktop.\n")
        payload(1, 0)
        return "//## VIRUS REPLICATION SUCCESSFUL ##//"


if __name__ == "__main__":
    TARGET = target_letter()
    XEHRO = XehroVirus(TARGET)
    XEHRO.check_status(TARGET)
