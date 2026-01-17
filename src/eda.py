import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    # Top 10 countries by revenue
    country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

    plt.figure()
    country_sales.plot(kind='bar')
    plt.title("Top 10 Countries by Revenue")
    plt.xlabel("Country")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

    # Distribution of order values
    plt.figure()
    sns.histplot(df['TotalPrice'], bins=50)
    plt.title("Distribution of Order Values")
    plt.show()