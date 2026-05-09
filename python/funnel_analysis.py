import pandas as pd

# Load website event data
df = pd.read_csv('../data/ga4_website_events.csv')

# Count each funnel stage
funnel = df['event_name'].value_counts()

print("Website Funnel Analysis:")
print(funnel)

# Save results
funnel.to_csv('../data/funnel_stage_counts.csv')

print("\nFunnel analysis completed successfully.")
