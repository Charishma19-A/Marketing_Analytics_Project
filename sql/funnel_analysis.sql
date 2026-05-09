-- Customer Funnel Analysis
-- Tracks customer movement through website funnel stages

SELECT
    event_name,
    COUNT(*) AS total_events
FROM ga4_website_events
GROUP BY event_name
ORDER BY total_events DESC;
