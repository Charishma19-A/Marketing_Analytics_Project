-- Email Campaign Performance Analysis
-- Tracks opens, clicks, conversions, unsubscribes

SELECT
    COUNT(*) AS total_emails_sent,
    SUM(CASE WHEN opened = 'Yes' THEN 1 ELSE 0 END) AS opens,
    SUM(CASE WHEN clicked = 'Yes' THEN 1 ELSE 0 END) AS clicks,
    SUM(CASE WHEN converted = 'Yes' THEN 1 ELSE 0 END) AS conversions,
    SUM(CASE WHEN unsubscribed = 'Yes' THEN 1 ELSE 0 END) AS unsubscribes
FROM mailchimp_email_campaigns;
