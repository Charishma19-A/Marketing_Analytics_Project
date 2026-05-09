import pandas as pd

# Load cleaned Google Ads data
df = pd.read_csv('../data/google_ads_campaigns_cleaned.csv')

# Calculate KPIs
df['CTR (%)'] = (df['clicks'] / df['impressions']) * 100
df['CPC'] = df['spend'] / df['clicks']
df['CPA'] = df['spend'] / df['conversions']
df['ROAS'] = df['revenue'] / df['spend']

# Display results
print("Campaign KPI Analysis:")
print(df[['campaign_name', 'CTR (%)', 'CPC', 'CPA', 'ROAS']])

# Save output
df.to_csv('../data/google_ads_campaigns_kpi.csv', index=False)

print("\nKPI analysis completed successfully.")
