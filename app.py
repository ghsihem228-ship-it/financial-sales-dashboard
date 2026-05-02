import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Financial Sales Dashboard", layout="wide")

st.title("💰 Financial Sales Dashboard")
st.write("Interactive dashboard for analyzing sales, profit, products, and regions.")

df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.sidebar.header("Filters")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

product_filter = st.sidebar.multiselect(
    "Select Product",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Product"].isin(product_filter))
]

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
profit_margin = (total_profit / total_sales) * 100

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Profit Margin", f"{profit_margin:.2f}%")

st.subheader("Dataset Preview")
st.dataframe(filtered_df)

st.subheader("Sales by Region")
sales_region = filtered_df.groupby("Region")["Sales"].sum()

fig1, ax1 = plt.subplots()
sales_region.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Sales")
st.pyplot(fig1)

st.subheader("Profit by Product")
profit_product = filtered_df.groupby("Product")["Profit"].sum()

fig2, ax2 = plt.subplots()
profit_product.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Profit")
st.pyplot(fig2)

st.subheader("Sales Trend Over Time")
sales_time = filtered_df.groupby("Date")["Sales"].sum()

fig3, ax3 = plt.subplots()
sales_time.plot(ax=ax3)
ax3.set_ylabel("Sales")
st.pyplot(fig3)

st.success("Dashboard loaded successfully.")
