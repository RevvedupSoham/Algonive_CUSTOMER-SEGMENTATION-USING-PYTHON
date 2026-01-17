import pandas as pd

def generate_segment_insights(df):
    # Map cluster numbers to segment names
    segment_map = {
        0: "Active Customers",
        1: "Low-Value Customers",
        2: "Occasional Customers",
        3: "High-Value but Inactive"
    }

    df["Segment"] = df["Cluster"].map(segment_map)

    summary = (
        df.groupby("Segment")
        .agg({
            "Recency": "mean",
            "Frequency": "mean",
            "Monetary": "mean",
            "CustomerID": "count"
        })
        .rename(columns={"CustomerID": "CustomerCount"})
        .round(2)
        .reset_index()
    )

    recommendations = {
        "Active Customers": "Offer loyalty rewards and upselling opportunities",
        "Low-Value Customers": "Run discount campaigns to increase engagement",
        "Occasional Customers": "Send personalized reminders and product suggestions",
        "High-Value but Inactive": "Launch win-back offers with exclusive incentives"
    }

    summary["Recommended Action"] = summary["Segment"].map(recommendations)

    return summary


if __name__ == "__main__":
    df = pd.read_csv("outputs/clustered_customers.csv")
    insights = generate_segment_insights(df)
    insights.to_csv("outputs/segment_insights.csv", index=False)
    print(insights)