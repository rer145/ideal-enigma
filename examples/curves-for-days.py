import pt_plot
import pt_data

pt = pt_plot.ProTracerPlot(add_extrapolation=True)

data = pt_data.load_file('C:\\Users\\ronri\\OneDrive\\Mercyhurst\\DATA 520 - Intro to Programming\\projects\\ideal-enigma\\data\\crappy-golfers.TXT')

shots = []
'''
shots.append({
        'Player Last First': 'Schniederjans, Ollie',
        'Tournament Name': 'AT&T Byron Nelson',
        'Round': 1,
        'Hole Number': 15
    })
'''
shots.append({
        'Player Last First': 'Pampling, Rod',
        'Tournament Name': 'AT&T Byron Nelson',
        'Round': 2,
        'Hole Number': 16
    })
for shot in shots:
    shot_data = pt_data.get_shot(data, shot["Player Last First"], shot["Tournament Name"],
                                 shot["Round"], shot["Hole Number"])

    # shot summary
    summary = pt_data.get_shot_summary(shot_data)
    pt.add_plot_data(shot_data, summary)


# pt.plot_2d()
pt.plot_3d(azim=96, title='Rod Pampling AT&T Byron Nelson - Round 2')
