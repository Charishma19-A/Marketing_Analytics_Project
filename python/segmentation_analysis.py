import pandas as pd

# Load HubSpot segmentation data
df = pd.read_csv('../data/hubspot_segments.csv')

# Analyze average engagement by segment
segment_summary = df.groupby('segment_name').agg(
    total_customers=('user_id', 'count'),
    avg_engagement_score=('engagement_score', 'mean')
).reset_index()

# Sort by engagement score
segment_summary = segment_summary.sort_values(by='avg_engagement_score', ascending=False)

print("Customer Segmentation Analysis:")
print(segment_summary)

# Save summary
segment_summary.to_csv('../data/segmentation_summary.csv', index=False)

print("\nSegmentation analysis completed successfully.")
