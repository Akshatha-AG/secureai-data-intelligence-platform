def generate_insights(findings, risk_level):
    insights = []

    types_found = [item["type"] for item in findings]

    if "password" in types_found:
        insights.append("Sensitive passwords detected in logs")

    if "api_key" in types_found:
        insights.append("API keys exposed in logs")

    if "email" in types_found:
        insights.append("User email data found in logs")

    if risk_level == "high":
        insights.append("High risk detected. Immediate action required")

    if not insights:
        insights.append("No major security risks detected")

    return insights


def generate_summary(findings, risk_level):
    if not findings:
        return "No sensitive data found in logs"

    return f"Log contains {len(findings)} sensitive entries with {risk_level} risk level"