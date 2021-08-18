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


def select_y_plot():
    """
    Get column name input from the user to plot for y axis.
    Run while loop to collect valid string data from user.
    If multiple columns entered this must be separated by commas.
    The loop will repeat until data input from user is valid.
    """
    while True:
        print("Please enter the column name for the y-axis plot.")
        print("Column name should be exactly the same as from the data sheet.")
        print("To enter multiple columns, separate these by commas.")
        print("Example: GDP %,GDP per capita %\n")

        y_plot_str = input("Enter y-plot column here: \n")

        y_plot_column = y_plot_str.split(",")

        if validate_y_plot(y_plot_column):
            print("Input is valid!")
            break

    # print(y_plot_column)

    return y_plot_column


def validate_y_plot(values):
    """
    List defined of correct column names as per data sheet.
    Variable defined to check if input from user list matches
    to the correct values list.
    Inside the try, checks if input from user is valid.
    Raises ValueError if input does not match to the column name
    from data sheet or if any other invalid input is entered.
    """
    correct_values = ['GDP %', 'GDP per capita %']
    check_value = any(value in values for value in correct_values)
    try:
        if check_value is not True:
            raise ValueError(
                f"Incorrect column name entered, you entered {values}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False

    return True


def select_plot_type():
    """
    Get plot type input from the user to plot output.
    Run while loop to collect valid string data from user.
    The loop will repeat until data input from user is valid.
    """
    while True:
        print("Please enter the plot type from the options.")
        print("bar, scatter, pie, line")
        print("Example: bar\n")

        plot_type_str = input("Enter plot type here: \n")

        if validate_plot_type(plot_type_str):
            print("Input is valid!\n")
            break

    # print(plot_type_str)

    return plot_type_str


def validate_plot_type(values):
    """
    Validate plot type
    """
    correct_type = ['bar', 'scatter', 'pie', 'line']
    try:
        if values not in correct_type:
            raise ValueError(
                f"Incorrect plot type, you entered {values}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False

    return True


def plot_output(data, values, plot):
    """
    Plot output as per user input.
    """
    data.plot('Type', values, kind=plot)
    plt.show()
    plt.savefig('fig.png')


def main():
    """
    Run all program functions
    """
    print("Welcome to the Economics Data Plotting Tool\n")
    all_data = get_data()
    data_frame = create_data_frame(all_data)
    y_plot = select_y_plot()
    plot_type = select_plot_type()
    plot_output(data_frame, y_plot, plot_type)


main()