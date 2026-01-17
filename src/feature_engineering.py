import pandas as pd

def create_rfm(df):
    snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    })

    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    return rfm


if __name__ == "__main__":
    from data_preprocessing import load_and_clean_data
    data = load_and_clean_data("data/Online Retail.xlsx")
    rfm = create_rfm(data)
    print(rfm.head())