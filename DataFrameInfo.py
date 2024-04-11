import pandas as pd
from db_utils import RDSDatabaseConnector

class DataTransform:
    """A class containing static methods for data transformation."""

    @staticmethod
    def convert_to_categorical(df, columns):
        """
        Convert specified columns in the DataFrame to categorical data type.

        Parameters:
        df (DataFrame): The pandas DataFrame.
        columns (list): A list of column names to convert to categorical.

        Returns:
        DataFrame: The DataFrame with specified columns converted to categorical data type.
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
        columns (list): A list of column names to convert to numeric.

        Returns:
        DataFrame: The DataFrame with specified columns converted to numeric data type.
        """
        for col in columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        return df

    @staticmethod
    def convert_month_to_categorical(df, month_column):
        """
        Convert the month column in the DataFrame to categorical data type.

        Parameters:
        df (DataFrame): The pandas DataFrame.
        month_column (str): The name of the column representing months.

        Returns:
        DataFrame: The DataFrame with the month column converted to categorical data type.
        """
        df[month_column] = df[month_column].astype('category')
        return df

    @staticmethod
    def convert_weekend_to_binary(df, weekend_column):
        """
        Convert the weekend column in the DataFrame to binary integers.

        Parameters:
        df (DataFrame): The pandas DataFrame.
        weekend_column (str): The name of the column representing weekends.

        Returns:
        DataFrame: The DataFrame with the weekend column converted to binary integers.
        """
        df[weekend_column] = df[weekend_column].astype(int)  
        return df


class DataFrameInfo:
    """A class for extracting information about a pandas DataFrame."""

    def __init__(self, df):
        """
        Initialize the DataFrameInfo object with a DataFrame.

        Parameters:
        df (DataFrame): The pandas DataFrame.
        """
        self.df = df

    def describe_columns(self):
        """
        Describe the data types of columns in the DataFrame.

        Returns:
        Series: A Series containing the data types of DataFrame columns.
        """
        return self.df.dtypes

    def extract_statistics(self):
        """
        Extract descriptive statistics for numeric columns in the DataFrame.

        Returns:
        DataFrame: A DataFrame containing descriptive statistics.
        """
        return self.df.describe()

    def count_distinct_values(self):
        """
        Count distinct values for categorical and object columns in the DataFrame.

        Returns:
        dict: A dictionary containing the count of distinct values for each categorical or object column.
        """
        distinct_counts = {}
        for col in self.df.select_dtypes(include=['category', 'object']):
            distinct_counts[col] = self.df[col].nunique()
        return distinct_counts

    def print_shape(self):
        """Print the shape of the DataFrame."""
        print("DataFrame shape:", self.df.shape)

    def count_null_values(self):
        """
        Count null values in each column of the DataFrame.

        Returns:
        DataFrame: A DataFrame containing the count and percentage of null values for each column.
        """
        null_counts = self.df.isnull().sum()
        null_percentage = (null_counts / len(self.df)) * 100
        return pd.DataFrame({'Null Count': null_counts, 'Null Percentage': null_percentage}, index=self.df.columns)


if __name__ == "__main__":
    df = pd.read_csv("customer_activity.csv")

    transformed_df = DataTransform.convert_to_categorical(df, ['operating_systems', 'browser', 'region', 'traffic_type', 'visitor_type'])
    transformed_df = DataTransform.convert_to_numeric(transformed_df, ['administrative_duration', 'informational_duration', 'product_related_duration', 'bounce_rates', 'exit_rates', 'page_values'])
    transformed_df = DataTransform.convert_month_to_categorical(transformed_df, 'month')
    transformed_df = DataTransform.convert_weekend_to_binary(transformed_df, 'weekend')

    info = DataFrameInfo(transformed_df)
    print("Column Data Types:")
    print(info.describe_columns())
    print("\nStatistics:")
    print(info.extract_statistics())
    print("\nDistinct Value Counts:")
    print(info.count_distinct_values())
    print("\nDataFrame Shape:")
    info.print_shape()
    print("\nNull Value Counts:")
    print(info.count_null_values())
