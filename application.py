
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

application = app.server

unit_0_link = 'https://cdn.vox-cdn.com/thumbor/q8z_oV3S33jSzgVdgRH-RY4KOh4=/0x0:1200x870/920x613/filters:focal(516x282:708x474):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/59535207/absolute_unit_sheep.0.jpg'
unit_1_link = 'https://gameplay.tips/uploads/posts/2018-09/thumbs/1537385272_montagne.jpg'

app.title = 'Boneless Media Inc.'
app.layout = html.Div(
    children=[
        dcc.Markdown('# Absolute Units'),
        html.Img(src=unit_0_link),
        html.Img(src=unit_1_link)
    ]
)


if __name__ == '__main__':
    application.run()
