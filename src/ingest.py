import pandas as pd
import os

def ingest_logs(log_dir):
    logs = []
    for f in os.listdir(log_dir):
        if f.endswith('.csv'):
            logs.append(pd.read_csv(os.path.join(log_dir, f)))
        elif f.endswith('.json'):
            logs.append(pd.read_json(os.path.join(log_dir, f)))
    return pd.concat(logs, ignore_index=True) if logs else pd.DataFrame()

# Simulate for threat feeds and business events
def ingest_feeds(feed_dir):
    pass

def ingest_business(biz_dir):
    pass

if __name__ == "__main__":
    logs = ingest_logs('data/security_logs')
    threats = ingest_feeds('data/threat_feeds')
    biz = ingest_business('data/business_events')
    pd.concat([logs, threats, biz], axis=0).to_csv('processed/merged_data.csv', index=False)
