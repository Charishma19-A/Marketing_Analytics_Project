-- Customer Segmentation Analysis
-- Analyzes customer groups by engagement and campaign response

SELECT
    segment_name,
    lifecycle_group,
    campaign_response,
    COUNT(*) AS total_customers,
    ROUND(AVG(engagement_score), 2) AS avg_engagement_score
FROM hubspot_segments
GROUP BY segment_name, lifecycle_group, campaign_response
ORDER BY avg_engagement_score DESC;
