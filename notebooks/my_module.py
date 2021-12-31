import numpy as np
import pandas as pd

def get_features_and_target(csv_file, target_col):
    '''Split a CSV into a DF of numeric features and a target column.'''
    
    adult_census = pd.read_csv(csv_file)
    
    raw_features = adult_census.drop(columns=target_col)
    numeric_features = raw_features.select_dtypes(np.number)
    feature_cols = numeric_features.columns.values

    features = adult_census[feature_cols]
    target = adult_census[target_col]
    
    return (features, target)