from math import sqrt
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    mean_absolute_percentage_error,
    r2_score,
)

def get_csv_dataframe(file_path: str, index_col: str, format: str) -> pd.DataFrame:
    """Retrieves data from a CSV file.
    Args:
        file_path (str): The path to the CSV file.
    Returns:
        pd.DataFrame: The entries of the CSV file.
    """
    df = pd.read_csv(file_path)
    df[index_col] = pd.to_datetime(df[index_col], format=format)
    df.set_index(index_col, inplace=True)
    df.sort_index(inplace=True)
    return df


def train_test_split(ts_data: np.ndarray, train_test_split_ratio: float = 0.8) -> np.ndarray:
    """
    Performs train test split on a time series data.
    Parameters:
        ts_data (np.ndarray): The input time series data.
        train_test_split_ratio (float, optional): The ratio of training data to total data. Defaults to 0.8.
    Returns:
        np.ndarray: The train and test data.
    """
    train_index = int(train_test_split_ratio * len(ts_data))
    ts_train = ts_data[:train_index]
    ts_test = ts_data[train_index:]
    return ts_train, ts_test


def adf_test(ts_series: pd.Series) -> pd.Series:
    """
    Calculate the Augmented Dickey-Fuller test for stationarity of a time series.
    Parameters:
        ts_series (pandas.Series): The time series to be tested.
    Returns:
        pandas.Series: A series containing the test statistic, p-value, number of lags
        used, number of observations used, and critical values for different confidence levels.
    """
    result = adfuller(ts_series, autolag="AIC")
    output = pd.Series(
        result[0:4],
        index=[
            "Test Statistic",
            "p-value",
            "#Lags Used",
            "Number of Observations Used",
        ],
    )
    for key, value in result[4].items():
        output["Critical Value (%s)" % key] = value
    return output


def kpss_test(ts_series: pd.Series) -> pd.Series:
    """
    Calculate the Kwiatkowski-Phillips-Schmidt-Shin test for stationarity of a time series.
    Parameters:
        ts_series (pandas.Series): The time series to be tested.
    Returns:
        pandas.Series: A series containing the test statistic, p-value, number of lags
        used, and critical values for different confidence levels.
    """
    result = kpss(ts_series, regression="c")
    output = pd.Series(
        result[0:3],
        index=[
            "Test Statistic",
            "p-value",
            "Lags Used",
        ],
    )
    for key, value in result[3].items():
        output["Critical Value (%s)" % key] = value
    return output


def get_error_metrics(ts_test: np.ndarray, predictions: np.ndarray) -> dict:
    """Get error metrics for a time series data.
    Parameters:
        ts_test (np.ndarray): The test time series data.
        predictions (np.ndarray): The predicted values.
    Returns:
        dict: A dictionary containing the error metrics.
    """
    error_metrics = {}
    error_metrics["MSE"] = mean_squared_error(ts_test, predictions)
    error_metrics["RMSE"] = sqrt(mean_squared_error(ts_test, predictions))
    error_metrics["MAE"] = mean_absolute_error(ts_test, predictions)
    error_metrics["MAPE"] = mean_absolute_percentage_error(ts_test, predictions)
    error_metrics["R2"] = r2_score(ts_test, predictions)
    return error_metrics