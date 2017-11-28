import pt_plot
import pt_data

pt = pt_plot.ProTracerPlot()

data = pt_data.load_file('C:\\Users\\ronri\\OneDrive\\Mercyhurst\\DATA 520 - Intro to Programming\\projects\\ideal-enigma\\data\\traj-detail-2017771908.TXT')

shots = []
'''
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
'''

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
    summary = pt_data.get_shot_summary(shot_data)
    pt.add_plot_data(shot_data, summary)


# pt.plot_2d()
pt.plot_3d(azim=100)
