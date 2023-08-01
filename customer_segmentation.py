import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def customer_segmentation():
    # Load and preprocess customer data (using dummy data for demonstration)
    customer_data = pd.DataFrame({
        'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        'Age': [32, 45, 27, 58, 39, 21, 48, 36, 55, 29],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'State': ['Vienna', 'Styria', 'Upper Austria', 'Tyrol', 'Carinthia', 'Salzburg', 'Lower Austria', 'Vorarlberg', 'Burgenland', 'Tyrol'],
        'Total_Purchases': [15, 28, 6, 50, 24, 3, 35, 19, 40, 8]
    })

    # Prepare features for segmentation and lifetime value analysis
    X = customer_data[['Age', 'Total_Purchases']]

    # Perform customer segmentation using K-means
    kmeans = KMeans(n_clusters=3, random_state=42)
    customer_data['Cluster'] = kmeans.fit_predict(X)

    # Calculate customer lifetime value (using dummy data for demonstration)
    customer_data['Lifetime_Value'] = customer_data['Total_Purchases'] * 500

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    for cluster in sorted(customer_data['Cluster'].unique()):
        ax.scatter(customer_data.loc[customer_data['Cluster'] == cluster, 'Age'], 
                    customer_data.loc[customer_data['Cluster'] == cluster, 'Total_Purchases'], 
                    label=f'Cluster {cluster+1}')
    ax.set_title('Customer Segmentation')
    ax.set_xlabel('Age')
    ax.set_ylabel('Total Purchases')
    ax.legend()
    ax.grid(True)

    # Analyze customer segments and make business recommendations (using dummy insights for demonstration)
    recommendations = []
    for cluster in sorted(customer_data['Cluster'].unique()):
        segment_data = customer_data[customer_data['Cluster'] == cluster]
        avg_age = segment_data['Age'].mean()
        avg_purchases = segment_data['Total_Purchases'].mean()
        avg_lifetime_value = segment_data['Lifetime_Value'].mean()

        recommendations.append({
            'segment': cluster + 1,
            'average_age': avg_age,
            'average_total_purchases': avg_purchases,
            'average_lifetime_value': avg_lifetime_value
        })

    return {'segmentation_results': customer_data, 'segmentation_plot': fig, 'recommendations': recommendations}
