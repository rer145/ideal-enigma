import pandas as pd
import numpy as np


def load_file(filename):
    """ (string) -> DataFrame

    Returns a pandas DataFrame with all the contents of the file specified.
    """

    data = pd.read_csv(filename, sep=';')

    # Create helper columns
    data["Player Full Name"] = data["Player First Name"] + " " + data["Player Last Name"]
    data["Player Last First"] = data["Player Last Name"] + ", " + data["Player First Name"]

    return data


def get_all_golfers(data, last_name_first=True):
    """ (DataFrame, bool) -> list

    Returns a list of all unique golfers in the data.
    """

    if last_name_first:
        return sorted(data["Player Last First"].unique().tolist())
    else:
        return sorted(data['Player Full Name'].unique().tolist())


def get_golfers_by_tournament(data, tournament, last_name_first=True):
    """ (DataFrame, string) -> list

    Returns a list of unique golfers for a certain tournament.
    """
    if last_name_first:
        return data.loc[(data["Tournament Name"] == tournament)]["Player Last First"].unique().tolist()
    else:
        return data.loc[(data["Tournament Name"] == tournament)]["Player Full Name"].unique().tolist()


def get_all_tournaments(data):
    """ (DataFrame) -> list

    Returns a list of all unique tournaments in the data.
    """

    return data['Tournament Name'].unique().tolist()


def get_tournaments_by_golfer(data, golfer, last_name_first=True):
    """ (DataFrame, string, bool) -> list

    Returns a list of all the unique tournaments for a certain golfer.
    """

    if last_name_first:
        return data.loc[(data["Player Last First"] == golfer)]["Tournament Name"].unique().tolist()
    else:
        return data.loc[(data["Player Full Name"] == golfer)]["Tournament Name"].unique().tolist()


def get_shots_by_golfer_tournament(data, golfer, tournament, last_name_first=True):
    """ (DataFrame, stirng, string, bool) -> list
    
    Returns a list of all shots by a golfer for a tournament.
    """

    if last_name_first:
        col = "Player Last First"
    else:
        col = "Player Full Name"

    return data.loc[
        (data[col] == golfer) &
        (data["Tournament Name"] == tournament) &
        (data['Trajectory Sequence'] == 1)
    ].values.tolist()
