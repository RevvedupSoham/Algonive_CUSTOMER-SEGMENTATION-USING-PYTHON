import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(rfm):
    plt.figure()
    sns.scatterplot(
        data=rfm,
        x='Recency',
        y='Monetary',
        hue='Cluster',
        palette='Set2'
    )
    plt.title("Customer Segments based on RFM")
    plt.show()