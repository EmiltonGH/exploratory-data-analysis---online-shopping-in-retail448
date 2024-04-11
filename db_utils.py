import yaml
from sqlalchemy import create_engine
import pandas as pd

def load_credentials(filepath="credentials.yaml"):
    """
    Load database credentials from a YAML file.

    Parameters:
        filepath (str): The file path to the YAML file containing database credentials.
                        Default is 'credentials.yaml'.

    Returns:
        dict: A dictionary containing database credentials.
    """
    with open(filepath, "r") as file:
        credentials = yaml.safe_load(file)
    return credentials

class RDSDatabaseConnector:
    """
    A class to connect to an Amazon RDS PostgreSQL database and perform data extraction and saving operations.

    Attributes:
        credentials (dict): A dictionary containing database connection credentials.
        engine (sqlalchemy.engine.base.Engine): A SQLAlchemy Engine object for database connection.
    """
    def __init__(self, credentials):
        """
        Initialize the RDSDatabaseConnector object with the provided credentials.

        Parameters:
            credentials (dict): A dictionary containing database connection credentials.
        """
        self.credentials = credentials
        self.engine = self.create_engine()

    def create_engine(self):
        """
        Create a SQLAlchemy Engine object for database connection.

        Returns:
            sqlalchemy.engine.base.Engine: A SQLAlchemy Engine object.
        """
        db_url = f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        return create_engine(db_url)

    def extract_data(self):
        """
        Extract data from the 'customer_activity' table in the connected database.

        Returns:
            pandas.DataFrame: A DataFrame containing the extracted data.
        """
        query = "SELECT * FROM customer_activity;"
        return pd.read_sql(query, self.engine)

    def save_data_to_csv(self, dataframe, filename):
        """
        Save data from a DataFrame to a CSV file.

        Parameters:
            dataframe (pandas.DataFrame): The DataFrame containing the data to be saved.
            filename (str): The name of the CSV file to save the data to.
        """
        dataframe.to_csv(filename, index=False)

    @staticmethod
    def load_data_from_csv(filename):
        """
        Load data from a CSV file into a DataFrame.

        Parameters:
            filename (str): The name of the CSV file containing the data to be loaded.

        Returns:
            pandas.DataFrame: A DataFrame containing the loaded data.
        """
        return pd.read_csv(filename)


if __name__ == "__main__":
    credentials = load_credentials()
    connector = RDSDatabaseConnector(credentials)
    data = connector.extract_data()
    connector.save_data_to_csv(data, "customer_activity.csv")
    data = RDSDatabaseConnector.load_data_from_csv("customer_activity.csv")
    print("Data shape:", data.shape)
    print("Sample of the data:")
    print(data.head())
    print(data.columns)
