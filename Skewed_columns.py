import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class Plotter:
    @staticmethod
    def plot_null_values(df):
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
        plt.title('Missing Values Heatmap')
        plt.show()

    @staticmethod
    def visualize_skew(df, skewed_cols):
        for col in skewed_cols:
            plt.figure(figsize=(8, 5))
            sns.histplot(df[col], kde=True, bins=30, color='blue')
            plt.title(f'Skewness of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()

class DataFrameTransform:
    @staticmethod
    def check_null_values(df):
        return df.isnull().sum()

    @staticmethod
    def drop_columns_with_null(df, threshold=0.5):
        null_percentage = df.isnull().mean()
        columns_to_drop = null_percentage[null_percentage > threshold].index
        return df.drop(columns=columns_to_drop)

    @staticmethod
    def impute_null_values(df, strategy='mean'):
        numeric_cols = df.select_dtypes(include=['number']).columns
        if strategy == 'mean':
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        elif strategy == 'median':
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        else:
            raise ValueError("Invalid imputation strategy. Please choose 'mean' or 'median'.")
        return df

    @staticmethod
    def identify_skewed_columns(df, skew_threshold=1):
        numeric_cols = df.select_dtypes(include=np.number).columns
        skewed_cols = df[numeric_cols].skew().abs() > skew_threshold
        return skewed_cols.index[skewed_cols].tolist()


    @staticmethod
    def identify_best_transformation(df, skewed_cols):
        transformations = {}
        for col in skewed_cols:
            if df[col].min() > 0:
                transformations[col] = np.log1p
            else:
                transformations[col] = np.sqrt
        return transformations

    @staticmethod
    def apply_transformations(df, transformations):
        transformed_df = df.copy()
        for col, transform_func in transformations.items():
            transformed_df[col] = transform_func(df[col])
        return transformed_df

# Load your DataFrame
df = pd.read_csv("customer_activity.csv")

# Checking NULL values
null_counts = DataFrameTransform.check_null_values(df)
print("Null Value Counts:")
print(null_counts)

# Dropping columns with more than 50% missing values
cleaned_df = DataFrameTransform.drop_columns_with_null(df, threshold=0.5)
print("Cleaned DataFrame Shape after dropping columns with high NULL values:", cleaned_df.shape)

# Impute NULL values
cleaned_df_imputed = DataFrameTransform.impute_null_values(cleaned_df, strategy='mean')

# Check NULL values after imputation
null_counts_after_imputation = DataFrameTransform.check_null_values(cleaned_df_imputed)
print("Null Value Counts after imputation:")
print(null_counts_after_imputation)

# Plot null values
Plotter.plot_null_values(cleaned_df_imputed)

# Identify skewed columns
skewed_columns = DataFrameTransform.identify_skewed_columns(cleaned_df_imputed, skew_threshold=1)

# Visualize skewness
Plotter.visualize_skew(cleaned_df_imputed, skewed_columns)

# Identify best transformations
transformations = DataFrameTransform.identify_best_transformation(cleaned_df_imputed, skewed_columns)

# Apply transformations
transformed_df = DataFrameTransform.apply_transformations(cleaned_df_imputed, transformations)

# Visualize transformed data
Plotter.visualize_skew(transformed_df, skewed_columns)

# Save a separate copy of the transformed DataFrame
transformed_df.to_csv("transformed_customer_activity.csv", index=False)
