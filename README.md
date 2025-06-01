# Credit-Card-Customer-Segmentation-Strategy
This project segments credit card users into behavioral clusters to inform personalization strategies, boost retention, and tailor digital product experiences. Inspired by real-world credit analytics, it blends data science and business strategy to derive insight-rich customer personas.
This project segments credit card users into behavioral clusters to inform personalization strategies, boost retention, and tailor digital product experiences. Inspired by real-world credit analytics, it blends data science and business strategy to derive insight-rich customer personas.

📊 Dataset Overview
Simulated data for 1,000 customers:

Age, Annual Income, Monthly Spend
Credit Utilization
Transactions (last 6M), Payment Delays
Cash Advance Amount
Tenure (Years), Offer Response
🔍 Features Engineered
To reflect engagement and behavior:

PurchaseAmount
NumberofPurchases
EngagementScore
Days Since Last Purchase
🧪 Clustering Methodology
Standardized core behavioral features
K-Means (k=3) applied after elbow method
Pairplot visualized segment patterns
Summary stats extracted for each cluster
🧠 Segment Personas
Cluster	Profile Name	Key Traits
0	Engaged Transactors	High spend, frequent use, low delay
1	Casual Users	Mid-spend, moderate activity
2	At-Risk Drifters	Low spend, low frequency, delayed payments
📸 Visual Highlights
cc_pairplot_updated_colors.png: Cluster pairplot
cc_income_spend_clusters.png: Income vs Spend scatterplot
📈 Strategic Recommendations
Cluster 0 – Engaged Transactors
Personalized offers and loyalty upgrades
Early access to premium products
Referral reward programs
Cluster 1 – Casual Users
Upsell with bundle offers and milestone campaigns
Monthly activity nudges
App engagement incentives
Cluster 2 – At-Risk Drifters
Win-back emails with discount triggers
Retargeting through product education
Behavior-based reactivation journeys
📁 Files Included
credit_card_segmentation_data.csv – Raw dataset
credit_card_segmented_data.csv – Clustered users
credit_card_segment_summary.csv – Segment stats
cc_pairplot.png – Pairplot
cc_income_spend_clusters.png – Spend vs Income clusters
credit_card_segmentation.py – Full Python workflow
