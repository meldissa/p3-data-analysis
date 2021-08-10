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

gdp_data = SHEET.worksheet('gdp_data')

data = gdp_data.get_all_values()

headers = data.pop(0)

df = pd.DataFrame(data, columns=headers)
print(df.head())

df_float = df.astype(float)

df_float.plot()

plt.show()

plt.savefig('fig.png')

