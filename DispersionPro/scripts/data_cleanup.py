# scripts/data_cleanup.py

import pandas as pd

def clean_data(df):
    """
    Cleans the input dataset by handling missing values and normalizing data.
    Parameters:
        df : pd.DataFrame : Input data
    Returns:
        pd.DataFrame : Cleaned data
    """
    # Fill missing values with mean
    df.fillna(df.mean(), inplace=True)
    
    # Normalize columns for uniform data distribution
    for column in df.select_dtypes(include=[float, int]).columns:
        df[column] = (df[column] - df[column].mean()) / df[column].std()
    
    return df

# Example usage
# df = pd.read_csv("data.csv")
# df_cleaned = clean_data(df)
# df_cleaned.to_csv("data_cleaned.csv", index=False)
