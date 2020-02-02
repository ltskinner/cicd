
import dash
import dash_core_components as dcc
import dash_html_components as html

import logging
import logging.config

logging.config.fileConfig(fname="./logging.conf")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

application = app.server

badge_link = "https://codebuild.us-east-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiWmZFUU9ZS1NtM1JIdVFYOG0yejBucmFxR2JOYVN0YVZUcTBzSW9ZWjI1K2VCUk1mbXNWQ2NBdUZZWjBLclAxOGxnRnZBRUc4U1c4d0lJdkVreC83MXU0PSIsIml2UGFyYW1ldGVyU3BlYyI6ImR2endXajBObVptcWl3c28iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master"

unit_0_link = 'https://cdn.vox-cdn.com/thumbor/q8z_oV3S33jSzgVdgRH-RY4KOh4=/0x0:1200x870/920x613/filters:focal(516x282:708x474):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/59535207/absolute_unit_sheep.0.jpg'
unit_1_link = 'https://gameplay.tips/uploads/posts/2018-09/thumbs/1537385272_montagne.jpg'


app.title = 'Boneless Media Inc.'
app.layout = html.Div(
    children=[
        dcc.Markdown('# Absolute Units'),
        dcc.Markdown('## "eDiT tHe AbsOluTe UniTs oR sOmeThIng"'),
        dcc.Markdown('## "hAteD iT"'),
        html.Img(src=badge_link, className='single_img'),
        html.Img(src=unit_0_link, className='single_img'),
        html.Img(src=unit_1_link, className='single_img')
    ],
    className='layout_div'
)


if __name__ == '__main__':
    application.run()
