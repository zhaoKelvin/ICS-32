from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    # TODO: Complete the function
    sports_list = []
    with file.open(mode='r') as open_file:
        csv_reader = csv.reader(open_file, delimiter=",")
        row = 0
        for sport_club in csv_reader:
            if (row == 0):
                row += 1
            
            else:
                
                if (len(sport_club) < 3 or len(sport_club) > 4 or "" in sport_club):
                    sports_list.clear()
                    raise ValueError

                sports_list.append((sport_club[0], sport_club[1], sport_club[2]))
            
        return sports_list
            


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    # TODO: Complete the function
    csv_files = Path.cwd().glob('*.csv')
    sportclubs_list = []
    files_read = 0
    lines_read = 0
    broken_files = []
    for file in csv_files:
        try:
            temp_list = readFile(file)
            for element in temp_list:
                # if there already exists a clubSport of the same attributes, then increment Count and skip iteration
                existing_club : SportClub
                loop_breaker = 0
                for existing_club in sportclubs_list:
                    
                    if (element[0] == existing_club.city and element[1] == existing_club.name 
                                                            and element[2] == existing_club.sport):
                        existing_club.incrementCount()
                        loop_breaker = existing_club.count
                        lines_read += 1
                        break
                
                if (loop_breaker == 0):
                    sportclubs_list.append(SportClub(element[0], element[1], element[2], 1))
                    lines_read += 1
            files_read += 1
        except ValueError:
            broken_files.append(file)
    
    # Creating the report.txt file
    with open("report.txt", 'w') as report_file:
        report_file.write(f"Number of files read: {files_read}\n")
        report_file.write(f"Number of lines read: {lines_read}\n")

    # Creating the error_log.txt file
    with open("error_log.txt", 'w') as error_text_file:
        for broken_csv in broken_files:    
            error_text_file.write(f"{Path(broken_csv).name}\n")
    
    return sportclubs_list

# Test readFile
#path = Path.cwd() / 'lab2' / 'junesurvey.csv'
#print(readFile(path))

# Test readAllFiles
#print(Path.cwd())
#print(readAllFiles())