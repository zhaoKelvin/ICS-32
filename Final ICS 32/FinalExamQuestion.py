''' You are expected to comment your code. At a minimum if statements and for loops
 need at least 1 line of comment to explain what the loop does'''

#------------IMPORT ANY LIBRARIES YOU NEED HERE-----------
from pathlib import Path
#---------- CREATE YOUR CUSTOM EXCEPTION HERE-------------
class NotAValidDirectory(Exception):
  pass

class NoFilesFoundInDirectory(Exception):
  pass

'''Write a function called combineFiles that reads all the text
files (.txt extension) which takes the directory Name and the name of the combined file
it will create as input parameters.
located in the directory myPath and writes it to a new Combined
file created in the current directory. It returns the values
defined below. You will raise a custom exception called "NotAValidDirectory"
if the directory provided is not a directory. You will raise a custom
exception called "NoFilesFoundInDirectory" if the directly is empty
and contains no files. The function will return 3 variables.
(Ensure they are in the same order
I am specifying:
  - A variable that returns the total number of files in the directory provided
  - A variable that provides the number of text files found in the directory
  - A variable that provides the total number of lines in the final combined file
'''
#----------------YOUR FUNCTION CODE STARTS HERE--------------- 
def combineFiles(directory_name: str, new_file_name: str) -> list[int, int, int]:
  
  return_variables = []
  
  current_path = Path.cwd()
  directory_path = Path.cwd() / directory_name
  
  if (directory_path.exists() == False):
    raise NotAValidDirectory
  
  # get the total number of files in directory by looping through and counting files
  num_files = 0
  total_files = directory_path.iterdir()
  for file in total_files:
    if (file.is_dir()):
      continue
    num_files += 1
  return_variables.append(num_files)
  
  if (num_files == 0):
    raise NoFilesFoundInDirectory
  
  # make directory with inputted name
  #Path.mkdir(current_path / directory_name)
  
  # loop through each text file in the current directory and get total number of text files in directory
  num_text_files = 0
  total_file_text = []
  txt_files = directory_path.glob("*.txt")
  for file in txt_files:
    num_text_files += 1
    with file.open('r') as open_file:
      #total_file_text = total_file_text + open_file.readlines()
      for line in open_file:
        line.strip()
        line = line + '\n'
        total_file_text.append(line)
  return_variables.append(num_text_files)
  
  # write a new combined file
  with open(current_path / new_file_name, 'w') as combined_file:
    combined_file.writelines(total_file_text)
    
  return_variables.append(len(total_file_text))
  
  return return_variables


      
#------------------- YOUR FUNCTION CODE ENDS HERE------------------   

'''This will run your program. You should only add code to
handle exceptions that are raised. Any exceptions found will only
display "Exception Found" and end program execution. The program will
only run once.(Does not automatically restart)'''

if __name__ == "__main__":
  values = combineFiles("myPath", "combined_text")
  print(values)