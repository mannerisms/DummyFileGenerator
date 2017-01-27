import os
import random
from faker import Faker


class Runner():
    """starts a new application instance"""
    def __init__(self):
        self.location = self.input_location()
        self.directory = self.input_directory()
        self.folder_range = self.input_range(1)
        self.file_range = self.input_range(2)
        self.fake = Faker()

    # Get a location and check if it exists
    def input_location(self):
        while True:
            location = str(raw_input('Please specify a location: ')).strip()
            if(os.path.isdir(location)):
                return location
                break

    # Create a new top level folder if folder does not exist
    def input_directory(self):
        directory = str(raw_input('Please specify a top directory name: ')).strip()
        directory = os.path.join(self.location, directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    def input_range(self, type):
        while True:
            if type == 1:
                max = raw_input('Please specify a maximum number of subfolders: ')
            elif type == 2:
                max = raw_input('Please specify a maximum number of files per folder: ')

            if max.isdigit():
                return int(max)
                break
            else:
                print "Please enter a valid number greater than 0"

    def run(self):

        if self.folder_range > 0:
            num_sub_folder = random.randint(1, self.folder_range)
            for folder in range(num_sub_folder):
                self.create_new_folders(self.directory, random.randint(0, 6))

    def create_new_folders(self, dir_name, num_subs):
        if num_subs > 0:
            directory = str(self.fake.word())
            cur_dir = os.path.join(dir_name, directory)
            if not os.path.exists(cur_dir):
                os.makedirs(cur_dir)
                self.create_new_folders(cur_dir, random.randint(0, num_subs))
            num_subs = num_subs - 1
            if num_subs == 0:
                num_sub_files = random.randint(1, self.file_range)
                for folder in range(num_sub_files):
                    file = str(self.fake.file_name())
                    file_path = os.path.join(cur_dir, file)
                    open(file_path, 'a').close()
            self.create_new_folders(cur_dir, num_subs)

    def get_directory(self):
        return self.directory

    def get_folder_range(self):
        return int(self.folder_range)

    def get_file_range(self):
        return self.file_range
