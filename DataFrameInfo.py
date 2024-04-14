import pandas as pd
from db_utils import RDSDatabaseConnector
from DataTransform import DataTransform

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

    transformed_df = DataTransform.convert_to_categorical(df, ['operating_systems', 'month', 'browser', 'region', 'traffic_type', 'visitor_type'])
    transformed_df = DataTransform.convert_to_numeric(transformed_df, ['administrative_duration', 'informational_duration', 'product_related_duration', 'bounce_rates', 'exit_rates', 'page_values'])
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
