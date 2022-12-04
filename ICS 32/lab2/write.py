import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")], [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    # TODO: Complete the function
    sep_sports = []     # outside list
    club : SportClub
    specific_sport : List[SportClub]
    for club in all_clubs:
        for specific_sport in sep_sports:    # current_sport is list of clubs of a specific sport
            if (club.getSport() == specific_sport[0].getSport()):
                sep_sports[sep_sports.index(specific_sport)].append(club)
                break
        else:
            # add list for specific sport if not found
            sep_sports.append([club])
    
    return sep_sports
            


def sortSport(sport: List[SportClub]) -> List[SportClub]:
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport

    Returns:
        A sorted list of the SportClubs  
    """
    # TODO: Complete the function
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )
    sport.sort(key=lambda x: x.name)
    sport.sort(key=lambda x: x.count, reverse=True)
    return sport


def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    # TODO: Complete the function
    with open("survey_database.csv", 'w') as survey_database:
        survey_csv = csv.writer(survey_database, delimiter=',')
        
        survey_csv.writerow(["City", "Team Name", "Sport", "Number of Times Picked"])
        
        for specific_sport in sorted_sports:
            team : SportClub
            for team in specific_sport:
                if (specific_sport.index(team) <= 2):
                    survey_csv.writerow([team.getCity(), team.getName(),
                                        team.getSport(), team.getCount()])