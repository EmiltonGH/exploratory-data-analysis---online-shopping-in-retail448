import yaml
from sqlalchemy import create_engine
import pandas as pd

def load_credentials(filepath="credentials.yaml"):
    with open(filepath, "r") as file:
        credentials = yaml.safe_load(file)
    return credentials

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = self.create_engine()

    def create_engine(self):
        db_url = f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        return create_engine(db_url)

    def extract_data(self):
        query = "SELECT * FROM customer_activity;"
        return pd.read_sql(query, self.engine)

    def save_data_to_csv(self, dataframe, filename):
        dataframe.to_csv(filename, index=False)

    @staticmethod
    def load_data_from_csv(filename):
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
