import plotly.offline as py
import plotly.graph_objs as go
from plotly import tools


def create_bar_chart(df, top_x=None, candidate=None):
    data = [go.Bar(
        x=df.index,
        y=df.values)]

    title_str = 'Contributions for {}'.format(candidate)

    layout = go.Layout(title=title_str,
                       yaxis=dict(title='$ Contributions'),
                       xaxis=dict(title='Contributor'))

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='{}.html'.format(title_str.replace(' ', '_')))

    return


def create_histogram(df, candidate=None):
    data = [go.Bar(
        x=df.index,
        y=df.values)]

    title_str = 'Contributions for {}'.format(candidate)

    layout = go.Layout(title=title_str,
                       yaxis=dict(title='$ Contributions'),
                       xaxis=dict(title='Contributor'))

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='{}.html'.format(title_str.replace(' ', '_')))

    return


# def non_comparative_bar(dataframe,xlabel,ylabel,title,width=0.05):
# 	"""
# 	Method for creating a bar plot with no comparative features.
# 	"""
# 	return

# 	data = [go.Bar(
# 	            x=dataframe[xlabel],
# 	            y=dataframe[ylabel]
# 	    )]

# 	layout = go.Layout(title=title,
# 					   yaxis=dict(
# 					   	title=ylabel)
# 					   )

# 	fig = go.Figure(data=data,layout = layout)
# 	py.plot(fig,filename='{}.html'.format(title))
