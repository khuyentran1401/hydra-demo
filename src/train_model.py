import hydra
import joblib
import pandas as pd
from omegaconf import DictConfig
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from helper import load_data


def create_pipeline() -> Pipeline:
    return Pipeline([("scaler", StandardScaler()), ("svm", SVC())])


def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    pipeline: Pipeline,
    hyperparameters: dict,
    grid_params: dict,
) -> GridSearchCV:
    """Train model using GridSearchCV"""
    grid_search = GridSearchCV(pipeline, dict(hyperparameters), **grid_params)
    grid_search.fit(X_train, y_train)
    return grid_search


def save_model(model, path: str):
    """Save model to path"""
    joblib.dump(model, f"{path}/svm.pkl")


@hydra.main(config_path="../conf", config_name="main", version_base=None)
def train(config: DictConfig) -> None:
    """Train model and save it"""
    X_train = load_data(f"{config.data.intermediate}/X_train.pkl")
    y_train = load_data(f"{config.data.intermediate}/y_train.pkl")
    pipeline = create_pipeline()
    grid_search = train_model(
        X_train,
        y_train,
        pipeline,
        config.train.hyperparameters,
        config.train.grid_search,
    )
    save_model(grid_search.best_estimator_, config.model)


if __name__ == "__main__":
    train()
