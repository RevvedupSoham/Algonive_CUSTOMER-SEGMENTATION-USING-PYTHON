import pandas as pd

def load_and_clean_data(path):
    # Load dataset
    df = pd.read_excel(path)

    # Drop rows with missing CustomerID
    df = df.dropna(subset=['CustomerID'])

    # Remove cancelled orders (InvoiceNo starts with 'C')
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

    # Remove negative or zero values
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Create TotalPrice column
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    return df

if __name__ == "__main__":
    data = load_and_clean_data("data/Online Retail.xlsx")
    print(data.head())