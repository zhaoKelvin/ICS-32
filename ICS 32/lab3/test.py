import pathlib

path_object = pathlib.Path().cwd()

path_object.open("textfile.txt", "w")

with open(path_object/pathlib.Path("newfile.txt"), "w") as new_file:
    new_file.write("hi")