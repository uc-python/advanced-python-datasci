import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def get_features_and_target(csv_file, target_col):
    '''Split a CSV into a DF of numeric features and a target column.'''
    
    adult_census = pd.read_csv(csv_file)
    
    raw_features = adult_census.drop(columns=target_col)
    numeric_features = raw_features.select_dtypes(np.number)
    feature_cols = numeric_features.columns.values

    features = adult_census[feature_cols]
    target = adult_census[target_col]
    
    return (features, target)

def make_preprocessor(features, categorical_preprocessor=None, numeric_preprocessor=None):
    '''Create a column transformer that applies sensible preprocessing procedures.'''
    
    if categorical_preprocessor is None:
        categorical_preprocessor = OneHotEncoder(handle_unknown='ignore')
    if numeric_preprocessor is None:
        numeric_preprocessor = StandardScaler()
        
    numeric_columns = features.select_dtypes(exclude=object).columns
    categorical_columns = features.select_dtypes(include=object).columns
    preprocessor = ColumnTransformer([
        ('one-hot-encoder', categorical_preprocessor, categorical_columns),
        ('standard_scaler', numeric_preprocessor, numeric_columns)
    ])
    return preprocessor