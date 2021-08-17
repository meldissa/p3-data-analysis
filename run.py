import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import matplotlib.pyplot as plt

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_project_data')


def get_data():
    """
    Access the sheet with the data and receive all values.
    """
    gdp_data = SHEET.worksheet('gdp_data')
    all_data = gdp_data.get_all_values()

    return all_data


def create_data_frame(data):
    """
    Create DataFrame and convert to acceptable data type to allow for plotting.
    """
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    # print(df.head())
    df = df.astype({
        'GDP %': 'float',
        'GDP per capita %': 'float'
    })

    return df


def select_y_plot(data):
    """
    Get column name input from the user to plot for y axis.
    Run while loop to collect valid string data from user.
    If multiple columns entered this must be separated by commas.
    The loop will repeat until data input from user is valid.
    """
    print("Please enter the column name for the y-axis plot.\n")
    print("Column name should be exactly the same as from the data sheet.\n")
    print("To enter multiple columns for the plot, separate this by commas.\n")
    print("Example: GDP %,GDP per capita %\n")

    y_plot_str = input("Enter y-plot column here: \n")

    y_plot_column = []

    y_plot_column.append(y_plot_str)

    print(y_plot_column)

    return y_plot_column

    # data.plot('Type', ['GDP %', 'GDP per capita %'], kind='bar')
    # plt.show()
    # plt.savefig('fig.png')


def main():
    """
    Run all program functions
    """
    print("Welcome to the Economics Data Plotting Tool\n")
    all_data = get_data()
    data_frame = create_data_frame(all_data)
    select_y_plot(data_frame)


main()