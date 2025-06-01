
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('credit_card_segmentation_data.csv')

# Feature engineering for behavior analysis
df['PurchaseAmount'] = df['Monthly_Spend']
df['NumberofPurchases'] = df['Transactions_Last_6M']
df['EngagementScore'] = (df['Transactions_Last_6M'] + df['Response_to_Offers'] * 20) / 2
df['Days Since Last Purchase'] = 400 - (df['Tenure_Years'] * 20 + df['Transactions_Last_6M'])

# Select features for clustering
features = ['PurchaseAmount', 'NumberofPurchases', 'EngagementScore', 'Days Since Last Purchase']
X = df[features]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Save output
df.to_csv('credit_card_segmented_data.csv', index=False)

# Save segment summary
summary = df.groupby('Cluster')[features].mean().round(2)
summary.to_csv('credit_card_segment_summary.csv')

# Visualizations
sns.set(style='whitegrid')
# Pairplot
pair = sns.pairplot(df[features + ['Cluster']].astype({ 'Cluster': str }), hue='Cluster', palette='Set2', diag_kind='hist')
pair.fig.suptitle('📊 Customer Clusters Based on Key Behavioral Metrics', y=1.02)
pair.savefig('cc_tarun_style_pairplot_updated_colors.png')
plt.close()

# Income vs Spend
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Annual_Income', y='Monthly_Spend', hue='Cluster', palette='Set2')
plt.title('Customer Segments by Income vs Monthly Spend')
plt.tight_layout()
plt.savefig('cc_income_spend_clusters.png')
plt.close()
