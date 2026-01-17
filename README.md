# Algonive_CUSTOMER-SEGMENTATION-USING-PYTHON
This project implements a customer segmentation solution using transactional retail data. Customers are grouped based on purchasing behavior to support business use cases. The project was developed during an internship as part of hands-on learning in data analytics and machine learning.

## Approach
The solution follows a modular analytics pipeline:
- Data cleaning and preprocessing of raw transactions
- Feature engineering using RFM (Recency, Frequency, Monetary) analysis
- Customer segmentation using K-Means clustering
- Visualization through an interactive dashboard
Each stage is implemented as a reusable and independent module.

## Dataset
- Online Retail Dataset  
- Transaction-level e-commerce data aggregated to customer-level features

## Output
The final output is a customer-level dataset containing:
- RFM features
- Assigned customer segments
- Business-friendly segment labels
This dataset is directly used by the dashboard for analysis and export.

## Dashboard
A Streamlit-based dashboard provides:
- Customer segment distribution
- Segment-wise behavior analysis
- Interactive filtering
- CSV download of segmented customer data

## Technologies
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit

## Key Learnings
- Handling real-world transactional data
- Applying unsupervised learning to business problems
- Translating analysis into actionable insights
- Building dashboards for non-technical stakeholders
