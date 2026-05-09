import pandas as pd

# Load email campaign data
df = pd.read_csv('../data/mailchimp_email_campaigns.csv')

# Calculate totals
total_sent = len(df)
opens = (df['opened'] == 'Yes').sum()
clicks = (df['clicked'] == 'Yes').sum()
conversions = (df['converted'] == 'Yes').sum()
unsubscribes = (df['unsubscribed'] == 'Yes').sum()

# Calculate rates
open_rate = (opens / total_sent) * 100
click_rate = (clicks / total_sent) * 100
conversion_rate = (conversions / total_sent) * 100
unsubscribe_rate = (unsubscribes / total_sent) * 100

print("Email Campaign Performance:")
print(f"Total Sent: {total_sent}")
print(f"Open Rate: {open_rate:.2f}%")
print(f"Click Rate: {click_rate:.2f}%")
print(f"Conversion Rate: {conversion_rate:.2f}%")
print(f"Unsubscribe Rate: {unsubscribe_rate:.2f}%")

# Save summary
summary = pd.DataFrame({
    'metric': ['total_sent', 'open_rate', 'click_rate', 'conversion_rate', 'unsubscribe_rate'],
    'value': [total_sent, open_rate, click_rate, conversion_rate, unsubscribe_rate]
})

summary.to_csv('../data/email_performance_summary.csv', index=False)

print("\nEmail performance analysis completed successfully.")
