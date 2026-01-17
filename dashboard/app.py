import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    layout="wide"
)

# Load data
df = pd.read_csv("../outputs/clustered_customers.csv")

cluster_names = {
    0: "Active Customers",
    1: "Low-Value Customers",
    2: "Occasional Customers",
    3: "High-Value but Inactive"
}

# Add cluster name column
df["Segment"] = df["Cluster"].map(cluster_names)

st.sidebar.title("Controls")
selected_segments = st.sidebar.multiselect(
    "Select Customer Segment(s)",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

filtered_df = df[df["Segment"].isin(selected_segments)]

st.title("Customer Segmentation Dashboard")
st.markdown("RFM-based customer segmentation using KMeans clustering")

st.divider()

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", df.shape[0])
col2.metric("Customer Segments", df["Segment"].nunique())
col3.metric("Avg Frequency", round(df["Frequency"].mean(), 2))
col4.metric("Avg Monetary Value", round(df["Monetary"].mean(), 2))

st.divider()

# Segment Distribution
st.subheader("Customer Segment Distribution")
segment_counts = df["Segment"].value_counts()
st.bar_chart(segment_counts)

st.divider()

# Customer Table
st.subheader("Customer Details")
st.dataframe(
    filtered_df[["CustomerID", "Recency", "Frequency", "Monetary", "Segment"]],
    use_container_width=True
)

# Download button
st.download_button(
    label="Download Segmented Customer Data (CSV)",
    data=filtered_df.to_csv(index=False),
    file_name="segmented_customers.csv",
    mime="text/csv"
)

st.divider()

# Segment Summary
st.subheader("Segment Summary Statistics")
summary = (
    df.groupby("Segment")
    .agg({
        "Recency": "mean",
        "Frequency": "mean",
        "Monetary": "mean"
    })
    .round(2)
)

st.dataframe(summary, use_container_width=True)

st.divider()
st.subheader("Segment Insights & Recommendations")

insights = pd.read_csv("../outputs/segment_insights.csv")
st.dataframe(insights, use_container_width=True)
st.download_button(
    label="Download Segment Insights (CSV)",
    data=insights.to_csv(index=False),
    file_name="segment_insights.csv",
    mime="text/csv"
)