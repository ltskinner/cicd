
import dash
import dash_core_components as dcc
import dash_html_components as html

from boneless import (get_unit_0, make_unit_0_callback,
                      get_unit_1, make_unit_1_callback)

import logging
import logging.config

logging.config.fileConfig(fname="./logging.conf")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

application = app.server

badge_link = "https://codebuild.us-east-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiWmZFUU9ZS1NtM1JIdVFYOG0yejBucmFxR2JOYVN0YVZUcTBzSW9ZWjI1K2VCUk1mbXNWQ2NBdUZZWjBLclAxOGxnRnZBRUc4U1c4d0lJdkVreC83MXU0PSIsIml2UGFyYW1ldGVyU3BlYyI6ImR2endXajBObVptcWl3c28iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master"


app.title = 'Boneless Media Inc.'
app.layout = html.Div(
    children=[
        dcc.Markdown('# Absolute Units'),
        dcc.Markdown('## "eDiT tHe AbsOluTe UniTs oR sOmeThIng"'),
        dcc.Markdown('## "hAteD iT"'),
        html.Img(src=badge_link, className='single_img'),
        dcc.Markdown('#### Which is the best Unit:'),

        get_unit_0(),
        get_unit_1()

    ],
    className='layout_div'
)

make_unit_0_callback(app)
make_unit_1_callback(app)


if __name__ == '__main__':
    application.run()
