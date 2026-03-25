def calculate_risk(findings):
    score = 0

    for item in findings:
        if item["risk"] == "low":
            score += 1
        elif item["risk"] == "high":
            score += 3
        elif item["risk"] == "critical":
            score += 5

    if score >= 10:
        level = "high"
    elif score >= 5:
        level = "medium"
    else:
        level = "low"

    return score, level