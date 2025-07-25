import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv('processed/merged_data.csv')
# Example features: event_count, threat_score, is_after_hours
X = df[['event_count', 'threat_score', 'is_after_hours']]
y = df['is_incident']  # If labeled data exists

# Anomaly detection
clf = IsolationForest(contamination=0.01)
clf.fit(X)
df['anomaly_score'] = clf.decision_function(X)

# Supervised risk scoring (if y exists)
if 'is_incident' in df.columns:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    df['risk_score'] = model.predict_proba(X)[:, 1]
    joblib.dump(model, 'models/risk_scorer.pkl')

df.to_csv('processed/scored_data.csv', index=False)
