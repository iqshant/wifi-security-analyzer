def analyze_security(network):
    akm = network["akm"]

    if not akm:
        return "Open Network (No Security)"

    if 1 in akm:
        return "WEP (Insecure)"

    if 2 in akm:
        return "WPA"

    if 4 in akm:
        return "WPA2"

    return "Unknown"