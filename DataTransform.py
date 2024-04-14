import pandas as pd
from db_utils import RDSDatabaseConnector

class DataTransform:
    @staticmethod
    def convert_to_categorical(df, columns):
        """
        Convert specified columns in the DataFrame to categorical data type.

        Parameters:
        df (DataFrame): The pandas DataFrame.
        columns (list): A list of column names to be converted to categorical.

        Returns:
        DataFrame: The DataFrame with specified columns converted to categorical.
        """
        for col in columns:
            df[col] = df[col].astype('category')
        return df

    @staticmethod
    def convert_to_numeric(df, columns):
        """
        Convert specified columns in the DataFrame to numeric data type.

        Parameters:
        df (DataFrame): The pandas DataFrame.
        columns (list): A list of column names to be converted to numeric.

        Returns:
        DataFrame: The DataFrame with specified columns converted to numeric.
        """
        for col in columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        return df

    @staticmethod
    def convert_weekend_to_binary(df, weekend_column):
        """
        Convert the weekend column in the DataFrame to binary integer values.

        Parameters:
        df (DataFrame): The pandas DataFrame.
        weekend_column (str): The name of the column containing weekend information.

        Returns:
        DataFrame: The DataFrame with the weekend column converted to binary integer values.
        """
        df[weekend_column] = df[weekend_column].astype(int)  # Convert boolean to integer directly
        return df


df = pd.read_csv("customer_activity.csv")

transformed_df = DataTransform.convert_to_categorical(df, ['operating_systems', 'month', 'browser', 'region', 'traffic_type', 'visitor_type'])
transformed_df = DataTransform.convert_to_numeric(transformed_df, ['administrative_duration', 'informational_duration', 'product_related_duration', 'bounce_rates', 'exit_rates', 'page_values'])
transformed_df = DataTransform.convert_weekend_to_binary(transformed_df, 'weekend')
