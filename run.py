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


def start():
    """
    User provided with introduction and input to start calculation.
    Try has if statement to check if user input is valid.
    The except captures any incorrect input the user entered.
    """
    print("Welcome to the Economics Data Analysis Tool\n")
    
    while True:
        print("Press Y to start\n")

        start_str = input("Enter here: \n")

        if start_str == "Y":
            print("Input is valid!\n")
            break
        else:
            print(f"Invalid input {start_str}, please try again.\n")

    return print("Starting calculations...\n")


def get_column_data():
    """
    Collects columns of data from project_data worksheet, collecting
    all entries for each category and returns the data
    as a list of lists.
    """
    project_data = SHEET.worksheet('project_data')

    columns = []
    for value in range(2, 8):
        column = project_data.col_values(value)
        columns.append(column[-11:])
    
    return columns


def calculate_sum(data):
    """
    Calculate the total sum for each column type.
    """
    print("Calculating total sum data...")
    total_sum_data = []

    for column in data:
        float_column = [float(num) for num in column]
        total_sum = sum(float_column)
        total_sum_data.append(round(total_sum, 2))

    print("Total sum calculated!\n")

    return total_sum_data


def calculate_average(data):
    """
    Calculate the average mean for each column type.
    """
    print("Calculating average for data...")
    average_data = []

    for value in data:
        average = value / 11
        average_data.append(round(average, 2))

    print("Average calculated!\n")

    return average_data


def calculate_estimate(data):
    """
    Calculate the estimate for 2021 for each column type.
    Using the average figures, decrease by 15% to calculate estimate.
    Insert 2021 at the beginning of the list for estimate_data,
    and return the estimate_data.
    """
    print("Calculating estimate for data...")
    estimate_data = []
    estimate_data.insert(0, 2021)

    for value in data:
        estimate = value * 0.85
        estimate_data.append(round(estimate, 2))

    print("Estimate calculated!\n")

    return estimate_data


def update_worksheet(data, worksheet):
    """
    Receives a list of floats to be inserted into a worksheet.
    Update the relevant worksheet with the data provided.
    """
    print(f"Updating {worksheet} worksheet...")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def create_data_frame():
    """
    Create DataFrame  for the project_data sheet,
    and convert to acceptable data type to allow for plotting.
    """
    project_data = SHEET.worksheet('project_data')
    all_data = project_data.get_all_values()
    headers = all_data.pop(0)
    df = pd.DataFrame(all_data, columns=headers)
    df = df.astype({
        'Unemployment': 'float',
        'Exports': 'float',
        'GDP growth': 'float',
        'GDP per capita growth': 'float',
        'Government expenditure': 'float',
        'Imports': 'float',
    })

    return df


def create_data_frame_est(data):
    """
    Create DataFrame for estimate 2021 data,
    which was previously calculated.
    """
    df_est = pd.DataFrame(data)

    return df_est


def select_y_plot():
    """
    Get column name input from the user to plot for y axis.
    Run while loop to collect valid string data from user.
    The loop will repeat until data input from user is valid.
    """
    while True:
        print("Please enter the column name for the y-axis plot.")
        print("The input should be exactly the same as from the data sheet.")
        print("Example: GDP growth\n")

        y_plot_str = input("Enter y-plot column here: \n")

        if validate_y_plot(y_plot_str):
            print("Input is valid!\n")
            break

    return y_plot_str


def validate_y_plot(value):
    """
    List defined of correct column names as per data sheet.
    Variable defined to check if input from user list matches
    to the correct values list.
    Inside the try, checks if input from user is valid.
    Raises ValueError if input does not match to the column name
    from data sheet or if any other invalid input is entered.
    """
    correct_values = [
        'Unemployment',
        'Exports',
        'GDP growth',
        'GDP per capita growth',
        'Government expenditure',
        'Imports'
    ]
    # check_value = any(value in values for value in correct_values)
    try:
        if value not in correct_values:
            raise ValueError(
                f"Incorrect column name entered, you entered {value}"
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
        print("bar, scatter, line")
        print("Example: bar\n")

        plot_type_str = input("Enter plot type here: \n")

        if validate_plot_type(plot_type_str):
            print("Input is valid!\n")
            break

    return plot_type_str


def validate_plot_type(value):
    """
    List defined of correct plot types. Variable defined to check if
    input from user list matches to the correct values list.
    Inside the try, checks if input from user is valid.
    Raises ValueError if input does not match to the correct type
    or if any other invalid input is entered.
    """
    correct_type = ['bar', 'scatter', 'line']
    try:
        if value not in correct_type:
            raise ValueError(
                f"Incorrect plot type, you entered {value}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False

    return True


def plot_output(data, value, plot):
    """
    Plot output as per user input.
    Image is saved of the plotted output.
    """
    print("Plotting data...")
    data.plot('Year', value, kind=plot)
    plt.savefig('assets/images/fig.png')
    plt.show()
    print("Data plotted successfully!")


def main():
    """
    Run all program functions
    """
    start()
    column_data = get_column_data()
    total_sum = calculate_sum(column_data)
    update_worksheet(total_sum, "sum")
    average = calculate_average(total_sum)
    update_worksheet(average, "average")
    estimate = calculate_estimate(average)
    update_worksheet(estimate, "estimate")
    data_frame = create_data_frame()
    est_df = create_data_frame_est(estimate)
    y_plot = select_y_plot()
    plot_type = select_plot_type()
    plot_output(data_frame, y_plot, plot_type)


main()