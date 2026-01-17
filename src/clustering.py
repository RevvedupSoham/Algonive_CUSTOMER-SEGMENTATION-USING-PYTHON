import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def perform_clustering(rfm, k=4):
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm)

    kmeans = KMeans(n_clusters=k, random_state=42)
    rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

    return rfm


if __name__ == "__main__":
    from data_preprocessing import load_and_clean_data
    from feature_engineering import create_rfm

    data = load_and_clean_data("data/Online Retail.xlsx")
    rfm = create_rfm(data)
    clustered_rfm = perform_clustering(rfm)

    clustered_rfm.to_csv("outputs/clustered_customers.csv")
    print(clustered_rfm.head())