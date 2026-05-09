import pandas as pd

# Load Google Ads data
google_ads = pd.read_csv('../data/google_ads_campaigns.csv')

# Display first few rows
print("Google Ads Data:")
print(google_ads.head())

# Check for missing values
print("\nMissing Values:")
print(google_ads.isnull().sum())

# Remove duplicates
google_ads = google_ads.drop_duplicates()

# Standardize column names
google_ads.columns = google_ads.columns.str.lower()

# Save cleaned data
google_ads.to_csv('../data/google_ads_campaigns_cleaned.csv', index=False)

print("\nData cleaning completed successfully.")
