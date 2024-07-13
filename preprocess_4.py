import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def load_and_preprocess_iris():
    iris = load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                      columns=iris['feature_names'] + ['target'])
    df.loc[1:5, 'sepal length (cm)'] = np.nan
    df.loc[10:15, 'petal width (cm)'] = np.nan
    numerical_columns = df.select_dtypes(include=['float64']).columns
    categorical_columns = ['target']  
    num_imputer = SimpleImputer(strategy='median')
    df[numerical_columns] = num_imputer.fit_transform(df[numerical_columns])
    scaler = StandardScaler()
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    df['target'] = pd.Categorical(df['target']).codes
    
    return df

if __name__ == "__main__":
    iris_df = load_and_preprocess_iris()
    
    print("Preprocessed Iris DataFrame:")
    print(iris_df.head(10))
    
    print("DataFrame Info:")
    print(iris_df.info())
    
    print("Summary Statistics:")
    print(iris_df.describe())
