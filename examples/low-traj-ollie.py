import pt_plot
import pt_data

pt = pt_plot.ProTracerPlot(add_extrapolation=False)

data = pt_data.load_file('C:\\Users\\ronri\\OneDrive\\Mercyhurst\\DATA 520 - Intro to Programming\\projects\\ideal-enigma\\data\\crappy-golfers.TXT')

shots = []
shots.append({
        'Player Last First': 'Schniederjans, Ollie',
        'Tournament Name': 'Sony Open in Hawaii',
        'Round': 4,
        'Hole Number': 9
    })
shots.append({
        'Player Last First': 'Schniederjans, Ollie',
        'Tournament Name': 'Wyndham Championship',
        'Round': 3,
        'Hole Number': 14
    })
shots.append({
        'Player Last First': 'Kaufman, Smylie',
        'Tournament Name': 'FedEx St. Jude Classic',
        'Round': 1,
        'Hole Number': 13
    })
'''
shots.append({
        'Player Last First': 'Schniederjans, Ollie',
        'Tournament Name': 'RBC Heritage',
        'Round': 1,
        'Hole Number': 3
    })

shots.append({
        'Player Last First': 'Schniederjans, Ollie',
        'Tournament Name': 'AT&T Byron Nelson',
        'Round': 1,
        'Hole Number': 15
    })
'''

for shot in shots:
    shot_data = pt_data.get_shot(data, shot["Player Last First"], shot["Tournament Name"],
                                 shot["Round"], shot["Hole Number"])

    # shot summary
    summary = pt_data.get_shot_summary(shot_data)
    pt.add_plot_data(shot_data, summary)


pt.plot_2d(title="Low Ball Ollie")
# pt.plot_3d()
