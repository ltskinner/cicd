
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import logging
logger = logging.getLogger()


def get_unit_0():
    unit_0_link = 'https://cdn.vox-cdn.com/thumbor/q8z_oV3S33jSzgVdgRH-RY4KOh4=/0x0:1200x870/920x613/filters:focal(516x282:708x474):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/59535207/absolute_unit_sheep.0.jpg'
    unit_0 = html.Div(
        children=[
            html.Img(src=unit_0_link, className='single_img'),
            html.Button('Vote Unit 0', id='unit_0_button'),
            html.Div(id='unit_0_button_count', children='Unit 0 Votes: 0')
        ],
        className='unit_voter_div'
    )
    return unit_0


def get_unit_1():
    unit_1_link = 'https://gameplay.tips/uploads/posts/2018-09/thumbs/1537385272_montagne.jpg'

    unit_1 = html.Div(
        children=[
            html.Img(src=unit_1_link, className='single_img'),
            html.Button('Vote Unit 1', id='unit_1_button'),
            html.Div(id='unit_1_button_count', children='Unit 1 Votes: 0')
        ],
        className='unit_voter_div'
    )
    return unit_1


def get_unit_2():
    unit_2_link = 'https://cdn.wccftech.com/wp-content/uploads/2018/03/NVIDIA-DGX-2-2.png'

    unit_2 = html.Div(
        children=[
            html.Img(src=unit_2_link, className='single_img'),
            html.Button('Vote Unit 2', id='unit_2_button'),
            html.Div(id='unit_2_button_count', children='Unit 2 Votes: 0')
        ],
        className='unit_voter_div'
    )
    return unit_2


def make_unit_0_callback(app):
    app.callback(
        [Output('unit_0_button_count', 'children')],
        [Input('unit_0_button', 'n_clicks')]
    )(update_unit_count_0)


def update_unit_count_0(n_clicks):
    logger.info(f'[TELEM] [EVENT] Vote Unit 0: {n_clicks}')
    return [f'Unit 0 Votes: {n_clicks}']


def make_unit_1_callback(app):
    app.callback(
        [Output('unit_1_button_count', 'children')],
        [Input('unit_1_button', 'n_clicks')]
    )(update_unit_count_1)


def update_unit_count_1(n_clicks):
    logger.info(f'[TELEM] [EVENT] Vote Unit 1: {n_clicks}')
    return [f'Unit 1 Votes: {n_clicks}']


def make_unit_2_callback(app):
    app.callback(
        [Output('unit_2_button_count', 'children')],
        [Input('unit_2_button', 'n_clicks')]
    )(update_unit_count_2)


def update_unit_count_2(n_clicks):
    logger.info(f'[TELEM] [EVENT] Vote Unit 2: {n_clicks}')
    #int('deliberate error')
    return [f'Unit 2 Votes: {n_clicks}']
