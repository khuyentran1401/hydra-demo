import warnings
from typing import Tuple

import hydra
import pandas as pd
from omegaconf import DictConfig
from sklearn.model_selection import train_test_split

from helper import load_data, save_data

# Ignore all future warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


def drop_irrelevant_columns(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    print(f"\nDropping columns: {columns}")
    return data.drop(columns=columns)


def get_X_y(data: pd.DataFrame, feature: str) -> Tuple[pd.DataFrame, pd.Series]:
    """Split data into X and y"""
    print("\nSplitting data into X and y")
    print(f"Feature to predict: {feature}")
    X = data.drop(columns=feature)
    y = data[feature]
    return X, y


def split_train_test(X: pd.DataFrame, y: pd.Series, test_size: float) -> dict:
    """Split data into train and test sets"""
    print("\nSplitting data into train and test sets")
    print(f"Test size: {test_size}")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
    }


@hydra.main(config_path="../conf", config_name="main", version_base=None)
def process_data(config: DictConfig):
    df = load_data(config.data.raw)
    processed_df = drop_irrelevant_columns(df, config.process.cols_to_drop)
    X, y = get_X_y(processed_df, config.process.feature)
    splitted_datasets = split_train_test(X, y, config.process.test_size)
    for name, data in splitted_datasets.items():
        save_data(data, config.data.intermediate, name)


if __name__ == "__main__":
    process_data()
