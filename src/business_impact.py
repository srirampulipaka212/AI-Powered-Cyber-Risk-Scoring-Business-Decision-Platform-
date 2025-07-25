import pandas as pd

df = pd.read_csv('processed/scored_data.csv')
# Example: map anomalies to business processes and simulate impact
df['downtime_cost'] = df['anomaly_score'].apply(lambda x: x * 10000)  # Mock business logic
df['reputation_risk'] = df['risk_score'].apply(lambda x: x * 5)       # Scale as needed
df.to_csv('processed/final_data.csv', index=False)
