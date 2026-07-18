def calculate_basic_statistics(df):
    return {
        "total_orders": df["Order ID"].nunique(),
        "total_customers": df["Customer ID"].nunique(),
        "total_products": df["Product ID"].nunique(),
        "total_sales": df["Sales"].sum(),
        "total_profit": df["Profit"].sum(),
        "average_order_value": df["Sales"].sum() / df["Order ID"].nunique(),
        "average_discount": df["Discount"].mean(),
        "total_states": df["State"].nunique(),
        "total_cities": df["City"].nunique(),
    }

def calculate_kpis(df):
    return {
        "Total Sales": round(df["Sales"].sum(), 2),
        "Total Profit": round(df["Profit"].sum(), 2),
        "Total Orders": df["Order ID"].nunique(),
        "Total Customers": df["Customer ID"].nunique(),
        "Average Order Value": round(
            df["Sales"].sum() / df["Order ID"].nunique(), 2
        ),
        "Average Discount": round(df["Discount"].mean() * 100, 2),
        "Profit Margin": round(
            (df["Profit"].sum() / df["Sales"].sum()) * 100,
            2,
        ),
    }