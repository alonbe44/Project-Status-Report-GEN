#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
import pandas as pd

from data_Visualization import mp


def Data_Cleaning(data_dict=mp):
    """
    Cleans the given data dictionary by performing various cleaning steps.

    Args:
        data_dict (dict): A dictionary containing the data to be cleaned. Defaults to an empty dictionary.

    Returns:
        pandas.DataFrame: A cleaned DataFrame.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_dict)

    # Handle missing values (if any)
    df.fillna('', inplace=True)  # Replace NaN values with empty strings

    # Convert relevant columns to the appropriate data types
    # (e.g., 'Date' column to datetime)
    if 'Date' in df:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert 'Date' to datetime

    # Ensure consistency in column names (convert to lowercase)
    df.columns = df.columns.str.lower()

    # Clean and preprocess text columns (e.g., remove leading/trailing whitespace)
    text_columns = ['project name', 'engineer name', 'details']
    for col in text_columns:
        df[col] = df[col].str.strip()

    # Perform any other cleaning steps as needed

    # Set display options to show all rows and columns
    pd.set_option('display.max_rows', None)  # Show all rows
    pd.set_option('display.max_columns', None)  # Show all columns

    return df

    # Usage example:
    # Clean your data using the clean_data function

