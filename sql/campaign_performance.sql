-- Campaign Performance Analysis
-- This query calculates key Google Ads marketing KPIs

SELECT
    campaign_id,
    campaign_name,
    date,
    audience,
    impressions,
    clicks,
    spend,
    conversions,
    revenue,

    ROUND((clicks * 100.0) / impressions, 2) AS ctr_percentage,
    ROUND(spend / clicks, 2) AS cpc,
    ROUND(spend / conversions, 2) AS cpa,
    ROUND(revenue / spend, 2) AS roas

FROM google_ads_campaigns;
