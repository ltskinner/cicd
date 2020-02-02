
import pandas as pd


def order_pizza():
    return "YA PIZZA WAT U WANT"


def get_drink_sizes(query):
    # For demo purposes, this is ok
    # For implementation, have you datalink class here
    # leverage the query to test over 'limit' statements
    drinks_df = pd.read_csv('./boneless/tests/integration/fixtures/drinks.csv')
    return drinks_df

def get_min_drink_size(drinks_df):
    return str(drinks_df['size'].min())

def do_pull_checks_work():
    # I think CL is too powerful
    return 'yes?'


if __name__ == '__main__':
    order_pizza()
    drinks_df = get_drink_sizes('')
