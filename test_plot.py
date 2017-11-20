import numpy as np
import pandas as pd
import pt_plot
import pt_data

pt = pt_plot.ProTracerPlot()

data = pt_data.load_file('C:\\Users\\ronri\\OneDrive\\Mercyhurst\\DATA 520 - Intro to Programming\\projects\\ideal-enigma\\data\\traj-detail-2017771908.TXT')

shots = []
shots.append({
        'Player Last First': 'Mickelson, Phil',
        'Tournament Name': 'Safeway Open',
        'Round': 1,
        'Hole Number': 5
    })
shots.append({
        'Player Last First': 'Mickelson, Phil',
        'Tournament Name': 'Safeway Open',
        'Round': 2,
        'Hole Number': 5
    })
shots.append({
        'Player Last First': 'Mickelson, Phil',
        'Tournament Name': 'Safeway Open',
        'Round': 3,
        'Hole Number': 5
    })
shots.append({
        'Player Last First': 'Mickelson, Phil',
        'Tournament Name': 'Safeway Open',
        'Round': 4,
        'Hole Number': 5
    })

shots.append({
        'Player Last First': 'Thomas, Justin',
        'Tournament Name': 'Safeway Open',
        'Round': 1,
        'Hole Number': 5
    })
shots.append({
        'Player Last First': 'Thomas, Justin',
        'Tournament Name': 'Safeway Open',
        'Round': 2,
        'Hole Number': 5
    })
shots.append({
        'Player Last First': 'Thomas, Justin',
        'Tournament Name': 'Safeway Open',
        'Round': 3,
        'Hole Number': 5
    })
shots.append({
        'Player Last First': 'Thomas, Justin',
        'Tournament Name': 'Safeway Open',
        'Round': 4,
        'Hole Number': 5
    })

for shot in shots:
    shot_data = pt_data.get_shot(data, shot["Player Last First"], shot["Tournament Name"],
                                 shot["Round"], shot["Hole Number"])

    # shot summary
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

    pt.add_plot_data(shot_data, summary)


# pt.plot_2d()
pt.plot_3d()


#import widget_mpl
#x = widget_mpl.ProTracerDialog()
#x.show()
