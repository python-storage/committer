from dir_check import dir_init, in_doc_search
from file_maker import generate_file
from file_types import Formatter
from part_time import Set
from options import Option


# This method checks the directories status for existence
# Returns a new Set instance
def initialize():
    dir_init()
    temp = Set()
    in_doc_search(temp.get_dir_string())
    return temp


# This method creates the files for user
def make_files(total_number, time_setter, formatter, file_type):
    for i in range(total_number):
        file_path = "./Documents/"+time_setter.get_dir_string()+"/"
        generate_file(file_path, formatter, file_type)
    print(f"{time_setter.get_time_string()}\nNew files added")


# This method creates a view and returns it
def present_view(formatter):
    option_view = Option()
    option_view.files = formatter.get_files_list()
    option_view.format_init()
    return option_view


# In this method we split the use command line input to takeout the indexes
def input_line_break(string_line, option_view):
    numbers = [int(num.strip()) for num in string_line.split(" ")]
    files_list = [option_view.get_file(num-1) for num in numbers]
    return files_list


# Script execute method
def execute():
    number = input("Number >> ")
    type_formatter = Formatter()
    # Creating viewer
    option_viewer = present_view(type_formatter)
    option_viewer.view_list()
    # Input command line
    file_format = input("Enter the numbers >> ")
    format_list = input_line_break(file_format, option_viewer)
    # Program setter
    setter = initialize()
    # File creating
    for type_file in format_list:
        make_files(int(number), setter, type_formatter, type_file)


if __name__ == "__main__":
    execute()
