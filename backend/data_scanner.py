import re

def scan_data(lines):
    findings = []

    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    password_pattern = r"password\s*=\s*\S+"
    api_key_pattern = r"sk-[a-zA-Z0-9]+"
    phone_pattern = r"\b\d{10}\b"
    token_pattern = r"token\s*=\s*\S+"
    stack_trace_pattern = r"(Exception|Error|Traceback)"
    failed_login_pattern = r"(failed login|invalid password)"

    failed_login_count = 0

    for i, line in enumerate(lines):
        line_lower = line.lower()

        if re.search(email_pattern, line):
            findings.append({
                "type": "email",
                "risk": "low",
                "line": i + 1,
                "content": line
            })

        if re.search(password_pattern, line):
            findings.append({
                "type": "password",
                "risk": "critical",
                "line": i + 1,
                "content": line
            })

        if re.search(api_key_pattern, line):
            findings.append({
                "type": "api_key",
                "risk": "high",
                "line": i + 1,
                "content": line
            })

        if re.search(phone_pattern, line):
            findings.append({
                "type": "phone",
                "risk": "low",
                "line": i + 1,
                "content": line
            })

        if re.search(token_pattern, line):
            findings.append({
                "type": "token",
                "risk": "high",
                "line": i + 1,
                "content": line
            })

        if re.search(stack_trace_pattern, line):
            findings.append({
                "type": "stack_trace",
                "risk": "medium",
                "line": i + 1,
                "content": line
            })

        if re.search(failed_login_pattern, line_lower):
            failed_login_count += 1

    # Brute-force detection logic
    if failed_login_count >= 3:
        findings.append({
            "type": "brute_force_attempt",
            "risk": "high",
            "line": "multiple",
            "content": f"{failed_login_count} failed login attempts detected"
        })

    return findings