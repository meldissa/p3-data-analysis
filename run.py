import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import plotext as plt

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
    Input is received from user to start application
    The if statement is to check if user input is valid
    The else statement captures any incorrect input the user entered

    Returns:
        Print statement returned to start calculations
    """
    print("Welcome to the Economics Data Analysis Tool!\n")
    while True:
        print("Enter Y to start\n")

        start_str = input("Enter here: \n")

        if start_str == "Y":
            print("Input is valid!\n")
            break
        else:
            print(f"Invalid input {start_str}, please try again.\n")

    return print("Starting calculations...\n")


def get_column_data():
    """
    Collects columns of data from project_data worksheet
    Collecting all entries for each category

    Returns:
    columns : list
        The data is returned as a list of lists
    """
    project_data = SHEET.worksheet('project_data')

    columns = []
    for value in range(2, 8):
        column = project_data.col_values(value)
        columns.append(column[-11:])
    return columns


def calculate_sum(data):
    """
    Calculates the total sum for each column of data from worksheet

    Parameters:
    data : float
        Takes the column data obtained from worksheet

    Returns:
    total_sum_data : float
        List of the total sum for each column of data
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
    Calculates the average for each column of data using the total sum
    figures previously calculated

    Parameters:
    data : float
        Takes the total sum data previously caluclated

    Returns:
    average_data : float
        List of the average for each column of data
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
    Calculates the estimate for year 2021 each column of data using the average
    figures previously calculated and appends 2021 at the beginning of the list

    Parameters:
    data : float
        Takes the average data previously caluclated

    Returns:
    estmate_data : float
        List of the estimate for each column of data for 2021
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
    Receives a list of floats to be inserted into a worksheet
    Update the relevant worksheet with the data provided

    Parameters:
    data : float
        Takes the data previously caluclated for sum, average and estimate
    worksheet : string
        Takes the name of selected worksheet
    """
    print(f"Updating {worksheet} worksheet...")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def create_data_frame(worksheet):
    """
    Creates DataFrame for the selected worksheet

    Parameters:
    worksheet : string
        Takes the name of selected worksheet

    Returns:
    df : DataFrame
        DataFrame created for selected worksheet
    """
    print(f"Creating DataFrame for {worksheet} worksheet...")
    worksheet_data = SHEET.worksheet(worksheet)
    all_data = worksheet_data.get_all_records()
    df = pd.DataFrame(all_data)
    print(f"DataFrame for {worksheet} worksheet created successfully!\n")

    return df


def append_data_frame(df1, df2):
    """
    Append both DataFrames
    Use only last row of data for second DataFrame
    Convert data types to float to allow for plotting

    Parameters:
    df1 : DataFrame
        Takes value of the first DataFrame
    df2 : DataFrame
        Takes value of the second DataFrame

    Returns:
    df_append : DataFrame
        Appended DataFrame created of df1 and df2
    """
    df_append = df1.append(df2.tail(1))
    df_append = df_append.astype({
        'Unemployment': 'float',
        'Exports': 'float',
        'GDP growth': 'float',
        'GDP per capita growth': 'float',
        'Government expenditure': 'float',
        'Imports': 'float',
    })

    return df_append


def select_y_plot():
    """
    Get column name input from the user to plot for y axis
    Run while loop to collect valid string data from user
    The loop will repeat until data input from user is valid

    Returns:
    y_plot_str : string
        String value returned from user input
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
    Validates the user string input
    Checks against the list defined of correct column names
    Inside the try checks if input from user is valid

    Parameters:
    value : string
        Takes value of string value from user input

    Raises:
    ValueError:
        Checks if user input does not match list of correct values
        Returns error message

    Returns:
    True : Boolean
        Boolean value returned of True if user input is correct
    """
    correct_values = [
        'Unemployment',
        'Exports',
        'GDP growth',
        'GDP per capita growth',
        'Government expenditure',
        'Imports'
    ]

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
    Get plot type input from the user to plot output
    Run while loop to collect valid string data from user
    The loop will repeat until data input from user is valid

    Returns:
    plot_type_str : string
        String value returned from user input
    """
    while True:
        print("Please enter the plot type from the options:")
        print("bar, scatter, line")
        print("Example: bar\n")

        plot_type_str = input("Enter plot type here: \n")

        if validate_plot_type(plot_type_str):
            print("Input is valid!\n")
            break

    return plot_type_str


def validate_plot_type(value):
    """
    Validates the user string input
    Checks against the list defined of correct column names
    Inside the try checks if input from user is valid

    Parameters:
    value : string
        Takes value of string value from user input

    Raises:
    ValueError:
        Checks if user input does not match list of correct values
        Returns error message

    Returns:
    True : Boolean
        Boolean value returned of True if user input is correct
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


def plot_output(data, value, kind):
    """
    Plots output based on user selection
    The if statement checks user input values and completes plotting
    Variable defined to select column from DataFrame based on user selection

    Parameters:
    data : string
        Takes value of the appended DataFrame
    value : string
        Takes value of the string input from user for column name
    kind : string
        Takes value of the string input from user for plot type

    Returns:
    print(output_selection)
        Prints statement for the column of data selected for plotting
    """
    print("Plotting data...\n")
    x = data['Year']
    y = data[value]
    plt.xlabel("Year")
    plt.ylabel(value)
    output_selection = data[['Year', value]]

    if kind == 'bar':
        plt.bar(x, y)
    elif kind == 'scatter':
        plt.scatter(x, y)
    elif kind == 'line':
        plt.plot(x, y)

    print(f"Data plotted successfully for {value} as {kind} plot!\n")
    print(f"Data selection for x-axis Year and y-axis {value}:\n")
    return print(output_selection)


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
    project_data_df = create_data_frame("project_data")
    estimate_df = create_data_frame("estimate")
    append_df = append_data_frame(project_data_df, estimate_df)
    y_plot = select_y_plot()
    plot_type = select_plot_type()
    plot_output(append_df, y_plot, plot_type)


main()
print("\nThank you for using the Economics Data Analysis Tool!\n")
print("Press RUN PROGRAM to start again.\n")
