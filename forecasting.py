import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
)
import numpy as np

def prepare_forecast_data(df):
    """
    Prepares monthly sales data for Prophet forecasting.
    """

    monthly_sales = (
        df.groupby(
            pd.Grouper(
                key="Order Date",
                freq="MS"
            )
        )["Sales"]
        .sum()
        .reset_index()
    )

    monthly_sales.columns = ["ds", "y"]

    return monthly_sales

def split_time_series(forecast_df, train_size=0.8):
    """
    Split time-series data into training and testing sets.
    """

    split_index = int(len(forecast_df) * train_size)

    train = forecast_df.iloc[:split_index]

    test = forecast_df.iloc[split_index:]

    return train, test

def train_prophet_model(forecast_df):
    """
    Trains a Prophet model on the monthly sales data.
    """

    model = Prophet()

    model.fit(forecast_df)

    return model

def generate_forecast(model, periods):
    """
    Generates future forecast.
    """

    future = model.make_future_dataframe(
        periods=periods,
        freq="MS"
    )

    forecast = model.predict(future)

    return forecast

def forecast_chart(forecast_df, forecast):
    """
    Creates an interactive forecast visualization.
    """

    fig = go.Figure()
    last_date = forecast_df["ds"].max()

    future_forecast = forecast[forecast["ds"] > last_date]

    # Historical Sales
    fig.add_trace(
        go.Scatter(
            x=future_forecast["ds"],
            y=future_forecast["yhat"],  
            mode="lines+markers",
            name="Historical Sales",
        )
    )

    # Forecast
    fig.add_trace(
        go.Scatter(
            x=future_forecast["ds"],
            y=future_forecast["yhat"],
            mode="lines",
            name="Forecast",
        )
    )

    # Confidence Interval
    fig.add_trace(
        go.Scatter(
            x=future_forecast["ds"],
            y=future_forecast["yhat_upper"],
            mode="lines",
            line=dict(width=0),
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=future_forecast["ds"],
            y=future_forecast["yhat_lower"],
            mode="lines",
            fill="tonexty",
            fillcolor="rgba(0,100,80,0.2)",
            line=dict(width=0),
            name="Confidence Interval",
        )
    )

    fig.update_layout(
        title="Sales Forecast (Next 12 Months)",
        xaxis_title="Month",
        yaxis_title="Sales",
        template="plotly_white",
        hovermode="x unified",
    )

    return fig

def forecast_insights(forecast_df, forecast):
    """
    Generate business insights from the forecast.
    """

    last_date = forecast_df["ds"].max()

    future = forecast[forecast["ds"] > last_date]

    highest = future.loc[future["yhat"].idxmax()]
    lowest = future.loc[future["yhat"].idxmin()]

    first = future.iloc[0]["yhat"]
    last = future.iloc[-1]["yhat"]

    growth = ((last - first) / first) * 100

    return {
        "growth": growth,
        "highest_month": highest["ds"],
        "highest_sales": highest["yhat"],
        "lowest_month": lowest["ds"],
        "lowest_sales": lowest["yhat"],
    }

from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


def evaluate_model(test_df, forecast):
    """
    Evaluate the model on unseen test data.
    """

    predictions = forecast.tail(len(test_df))

    mae = mean_absolute_error(
        test_df["y"],
        predictions["yhat"]
    )

    rmse = np.sqrt(
        mean_squared_error(
            test_df["y"],
            predictions["yhat"]
        )
    )

    return mae, rmse