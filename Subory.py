import os


def numerate_files(filepath):
    for index, file in enumerate(os.listdir(filepath)):
        file_name, extension = file.split('.')
        os.rename(os.path.join(filepath, file), os.path.join(filepath, f'{file_name}_{index}.{extension}'))


print(numerate_files(MacintoshHD/Users/pm0702/Projects/SDA-PythonBasics))
