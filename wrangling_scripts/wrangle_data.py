import plotly.graph_objs as go
from wrangling_scripts.stravaAPI import get_data
import plotly.graph_objs as go

# Prepare the plotly visualizations
data = get_data()



def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

# first chart plots total workouts by each member, of the last 60

    who_counts = data['who'].value_counts()
    who_vals = []
    for i in who_counts.items():
        who_vals.append(i[0])

    graph_one = []
    graph_one.append(
        go.Bar(
            x=who_vals,
            y=who_counts
        )
    )

    layout_one = dict(title="Who's done the most workouts overall?",
                      xaxis=dict(title='Who'),
                      yaxis=dict(title='Split of the past 60 workouts'),
                      )

# second chart plots total lengths of workouts by each member, of the last 60
    who_time = data.groupby(["who"]).sum()["moving_time"]

    who_vals = []
    for i in who_time.items():
        who_vals.append(i[0])

    who_time_clean = []
    for i in who_time.items():
        time =  i[1]/60
        who_time_clean.append(time)

    graph_two = []
    graph_two.append(
        go.Bar(
            x=who_vals,
            y=who_time_clean
        )
    )

    layout_two = dict(title="Who's worked out for the longest duration?",
                      xaxis=dict(title='Who'),
                      yaxis=dict(title='Total workout minutes'),
                          )

# third chart - whos been doing the most strength training ?
    type = ["WeightTraining", "Workout"]
    df_workouts = data[data.type.isin(type)]

    who_counts = df_workouts['who'].value_counts()
    who_vals = []
    for i in who_counts.items():
        who_vals.append(i[0])

    graph_three = []
    graph_three.append(
        go.Bar(
            x=who_vals,
            y=who_counts
        )
    )

    layout_three = dict(title="Who's done the most strength training?",
                        xaxis=dict(title='Who'),
                        yaxis=dict(title='Split of the past 60 workouts'),
                        )

# fourth chart - shows rural population vs arable land
    colors = ['lightcoral', 'darkturquoise', 'whitesmoke']

    trace1 = go.Scatter(
        y=[0, 4, 4, 4, 5, 5, 6, 6, 6],
        x=[0, 'wk1', 'wk2', 'wk3', 'wk4', 'wk5', 'wk6', 'wk7', 'wk8'],
        fill='tozeroy',
        name='Total',
        marker=dict(color=colors[0], line=dict(color='rgb(100,100,100)', width=1)))

    trace2 = go.Scatter(
        y=[0, 2, 2, 2, 3, 4, 4, 4, 4],
        x=[0, 'wk1', 'wk2', 'wk3', 'wk4', 'wk5', 'wk6', 'wk7', 'wk8'],
        fill='tozeroy',
        name='Toning Power',
        marker=dict(color=colors[2], line=dict(color='rgb(100,100,100)', width=1)))

    trace3 = go.Scatter(
        y=[0, 1, 1, 1, 2, 2, 2, 2, 2],
        x=[0, 'wk1', 'wk2', 'wk3', 'wk4', 'wk5', 'wk6', 'wk7', 'wk8'],
        fill='tozeroy',
        name='Sweaty Shredder',
        marker=dict(color=colors[1], line=dict(color='rgb(100,100,100)', width=1)))

    graph_four = [trace1, trace2, trace3]

    layout_four = dict(title='Workouts increase steadily per week',
                       xaxis=dict(title='Week'),
                       yaxis=dict(title='Total workouts, cumulative'),
                       )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures


