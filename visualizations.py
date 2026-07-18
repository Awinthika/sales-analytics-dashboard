import pandas as pd
import plotly.express as px


def monthly_sales_chart(df):
    """
    Creates an interactive monthly sales trend chart.
    """

    # Step 1: Group sales by month
    monthly_sales = (
        df.groupby("Order Month")["Sales"]
        .sum()
        .reset_index()
    )

    # Step 2: Correct month order
    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    monthly_sales["Order Month"] = pd.Categorical(
        monthly_sales["Order Month"],
        categories=month_order,
        ordered=True,
    )

    monthly_sales = monthly_sales.sort_values("Order Month")

    # Step 3: Create chart
    fig = px.line(
        monthly_sales,
        x="Order Month",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend",
    )

    return fig

def monthly_profit_chart(df):
    """
    Creates an interactive monthly profit trend chart.
    """

    monthly_profit = (
        df.groupby("Order Month")["Profit"]
        .sum()
        .reset_index()
    )

    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    monthly_profit["Order Month"] = pd.Categorical(
        monthly_profit["Order Month"],
        categories=month_order,
        ordered=True,
    )

    monthly_profit = monthly_profit.sort_values("Order Month")

    fig = px.line(
        monthly_profit,
        x="Order Month",
        y="Profit",
        markers=True,
        title="Monthly Profit Trend",
    )

    return fig
def sales_by_category_chart(df):
    """
    Creates an interactive bar chart showing sales by category.
    """

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        color="Category",
        title="Sales by Category",
        text_auto=".2s",
    )

    fig.update_layout(
        showlegend=False,
        xaxis_title="Category",
        yaxis_title="Sales ($)",
    )

    return fig

def profit_by_category_chart(df):
    """
    Creates an interactive bar chart showing profit by category.
    """

    category_profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
        .sort_values("Profit", ascending=False)
    )

    fig = px.bar(
        category_profit,
        x="Category",
        y="Profit",
        color="Category",
        title="Profit by Category",
        text_auto=".2s",
    )

    fig.update_layout(
        showlegend=False,
        xaxis_title="Category",
        yaxis_title="Profit ($)",
    )

    return fig

def sales_by_region_chart(df):
    """
    Creates an interactive bar chart showing sales by region.
    """

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        color="Region",
        title="Sales by Region",
        text_auto=".2s",
    )

    fig.update_layout(
        showlegend=False,
        xaxis_title="Region",
        yaxis_title="Sales ($)",
    )

    return fig

def top_products_chart(df):
    """
    Creates an interactive bar chart showing the top 10 products by sales.
    """

    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products by Sales",
        text_auto=".2s",
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        xaxis_title="Sales ($)",
        yaxis_title="Product",
    )

    return fig

def top_customers_chart(df):
    """
    Creates an interactive bar chart showing the top 10 customers by sales.
    """

    top_customers = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top_customers,
        x="Sales",
        y="Customer Name",
        orientation="h",
        title="Top 10 Customers by Sales",
        text_auto=".2s",
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        xaxis_title="Sales ($)",
        yaxis_title="Customer",
    )

    return fig

def sales_by_state_chart(df):

    state_sales = (
        df.groupby("State")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        state_sales,
        x="State",
        y="Sales",
        title="Sales by State",
        text_auto=".2s",
    )

    fig.update_layout(
        xaxis_tickangle=-45
    )

    return fig

def discount_profit_chart(df):

    fig = px.scatter(
        df,
        x="Discount",
        y="Profit",
        color="Category",
        size="Sales",
        hover_name="Product Name",
        title="Discount vs Profit",
    )

    return fig