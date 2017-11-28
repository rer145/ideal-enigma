import pandas as pd
import numpy as np


def load_file(filename, sep=';'):
    """ (string) -> DataFrame

    Returns a pandas DataFrame with all the contents of the file specified.
    """

    data = pd.read_csv(filename, sep=sep)

    # Create helper columns
    data["Player Full Name"] = data["Player First Name"] + " " + data["Player Last Name"]
    data["Player Last First"] = data["Player Last Name"] + ", " + data["Player First Name"]
    data["Index"] = range(data.shape[0])

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
    """ (DataFrame, string, string, bool) -> DataFrame
    
    Returns a DataFrame of all shots by a golfer for a tournament.
    """

    # TODO: put into helper function
    if last_name_first:
        col = "Player Last First"
    else:
        col = "Player Full Name"

    return data.loc[
        (data[col] == golfer) &
        (data["Tournament Name"] == tournament) &
        (data['Trajectory Sequence'] == 1)
    ]


def get_all_shots(data):
    """ (DataFrame) -> DataFrame

    Returns a DataFrame of all unique shots in the data file.
    """

    return data.loc[
        (data["Trajectory Sequence"] == 1)
    ].sort_values(by=['Player Last Name', 'Player First Name', 'Tournament Name', 'Round', 'Hole Number'])


def get_shot(data, golfer, tournament, round, hole, last_name_first=True):
    """ (DataFrame, string, string, int, int, bool) -> DataFrame

    Returns the full trajectory data for a shot.
    """

    if last_name_first:
        col = "Player Last First"
    else:
        col = "Player Full Name"

    return data.loc[
        (data[col] == golfer) &
        (data["Tournament Name"] == tournament) &
        (data["Round"] == int(round)) &
        (data["Hole Number"] == int(hole))
    ].sort_values(by=['Trajectory Sequence'])


def get_shot_summary(shot_data):
    """ (DataFrame) -> dictionary

    Returns a dictionary of summary data.
    """

    summary = {}
    summary["Player First Name"] = shot_data.iloc[0]["Player First Name"]
    summary["Player Last Name"] = shot_data.iloc[0]["Player Last Name"]
    summary["Player Full Name"] = shot_data.iloc[0]["Player Full Name"]
    summary["Tournament Name"] = shot_data.iloc[0]["Tournament Name"]
    summary["Round"] = shot_data.iloc[0]["Round"]
    summary["Hole Number"] = shot_data.iloc[0]["Hole Number"]
    summary["Club Head Speed"] = shot_data.iloc[0]["Club Head Speed"]
    summary["Ball Speed"] = shot_data.iloc[0]["Ball Speed"]
    summary["Smash Factor"] = shot_data.iloc[0]["Smash Factor"]
    summary["Vertical Launch Angle"] = shot_data.iloc[0]["Vertical Launch Angle"]
    summary["Apex Height"] = shot_data.iloc[0]["Apex Height"]
    summary["Actual Flight Time"] = shot_data.iloc[0]["Actual Flight Time"]
    summary["Actual Range"] = shot_data.iloc[0]["Actual Range"]
    summary["Actual Height"] = shot_data.iloc[0]["Actual Height"]
    summary["Distance of Impact"] = shot_data.iloc[0]["Distance of Impact"]
    summary["Club"] = shot_data.iloc[0]["Club"]
    summary["Total Distance"] = shot_data.iloc[0]["Total Distance"]
    summary["Ending Location Description"] = shot_data.iloc[0]["Ending Location Description"]
    summary["Weather"] = shot_data.iloc[0]["Weather"]

    return summary
