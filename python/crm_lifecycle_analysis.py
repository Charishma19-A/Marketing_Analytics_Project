import pandas as pd

# Load Salesforce CRM data
df = pd.read_csv('../data/salesforce_crm_leads.csv')

# Count leads by lifecycle stage
stage_summary = df.groupby('lifecycle_stage').agg(
    total_leads=('lead_id', 'count')
).reset_index()

# Count leads by status
status_summary = df.groupby('lead_status').agg(
    total_leads=('lead_id', 'count')
).reset_index()

print("CRM Lifecycle Stage Summary:")
print(stage_summary)

print("\nCRM Lead Status Summary:")
print(status_summary)

# Save outputs
stage_summary.to_csv('../data/crm_stage_summary.csv', index=False)
status_summary.to_csv('../data/crm_status_summary.csv', index=False)

print("\nCRM lifecycle analysis completed successfully.")
