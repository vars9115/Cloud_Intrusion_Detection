def detect_intrusion(data):
    packet_count = int(data.get("packet_count", 0))
    failed_logins = int(data.get("failed_logins", 0))
    port = int(data.get("port", 0))

    reasons = []

    if packet_count > 1000:
        reasons.append("High network traffic")

    if failed_logins > 5:
        reasons.append("Multiple failed login attempts")

    if port in [21, 23, 445, 3389]:
        reasons.append("Suspicious port detected")

    if reasons:
        return {
            "status": "INTRUSION DETECTED",
            "message": ", ".join(reasons)
        }

    return {
        "status": "NORMAL",
        "message": "No suspicious activity detected"
    }