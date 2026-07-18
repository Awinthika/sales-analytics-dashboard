import streamlit as st


from data_loader import load_data
from preprocessing import clean_data, feature_engineering
from analytics import calculate_kpis
from visualizations import (
    monthly_sales_chart,
    monthly_profit_chart,
    sales_by_category_chart,
    profit_by_category_chart,
    top_products_chart,
    sales_by_region_chart,
    top_customers_chart,
    sales_by_state_chart,
    discount_profit_chart,
)
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Analytics Dashboard")

st.caption(
    "Analyze sales performance, profitability, customers, products, and regional trends using interactive visualizations."
)

df = load_data()
df = clean_data(df)
df = feature_engineering(df)

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.header("🔍 Filters")
years = sorted(df["Order Year"].unique())

selected_year = st.sidebar.selectbox(
    "Select Year",
    options=["All"] + list(years)
)
regions = sorted(df["Region"].unique())

selected_region = st.sidebar.selectbox(
    "Select Region",
    options=["All"] + regions
)
categories = sorted(df["Category"].unique())

selected_category = st.sidebar.selectbox(
    "Select Category",
    options=["All"] + categories
)
segments = sorted(df["Segment"].unique())

selected_segment = st.sidebar.selectbox(
    "Select Segment",
    options=["All"] + segments
)
filtered_df = df.copy()
if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["Order Year"] == selected_year
    ]
if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]
if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]
if selected_segment != "All":
    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_segment
    ]



kpis = calculate_kpis(filtered_df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Sales",
        f"${kpis['Total Sales']:,.2f}"
    )

with col2:
    st.metric(
        "📈 Total Profit",
        f"${kpis['Total Profit']:,.2f}"
    )

with col3:
    st.metric(
        "📦 Orders",
        f"{kpis['Total Orders']:,}"
    )

with col4:
    st.metric(
        "👥 Customers",
        f"{kpis['Total Customers']:,}"
    )

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Monthly Sales Trend")
    sales_fig = monthly_sales_chart(filtered_df)
    st.plotly_chart(sales_fig, use_container_width=True)

with col2:
    st.subheader("📈 Monthly Profit Trend")
    profit_fig = monthly_profit_chart(filtered_df)
    st.plotly_chart(profit_fig, use_container_width=True)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Sales by Category")
    sales_category_fig = sales_by_category_chart(filtered_df)
    st.plotly_chart(sales_category_fig, use_container_width=True)

with col2:
    st.subheader("💰 Profit by Category")
    profit_category_fig = profit_by_category_chart(filtered_df)
    st.plotly_chart(profit_category_fig, use_container_width=True)
st.divider()

st.subheader("🌍 Sales by Region")

region_fig = sales_by_region_chart(filtered_df)

st.plotly_chart(region_fig, use_container_width=True)

st.divider()

st.subheader("🏆 Top 10 Products by Sales")

product_fig = top_products_chart(filtered_df)

st.plotly_chart(product_fig, use_container_width=True)

st.divider()

st.subheader("👥 Top 10 Customers by Sales")

customer_fig = top_customers_chart(filtered_df)

st.plotly_chart(customer_fig, use_container_width=True)

st.divider()

st.subheader("🗺️ Sales by State")

state_fig = sales_by_state_chart(filtered_df)

st.plotly_chart(state_fig, use_container_width=True)

st.divider()

st.subheader("📉 Discount vs Profit")

discount_fig = discount_profit_chart(filtered_df)

st.plotly_chart(discount_fig, use_container_width=True)

csv = filtered_df.to_csv(index=False)

st.sidebar.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv",
)