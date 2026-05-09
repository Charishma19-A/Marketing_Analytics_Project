-- CRM Lifecycle Analysis
-- Tracks lead stages and lead status from Salesforce CRM data

SELECT
    lifecycle_stage,
    lead_status,
    COUNT(*) AS total_leads
FROM salesforce_crm_leads
GROUP BY lifecycle_stage, lead_status
ORDER BY total_leads DESC;
