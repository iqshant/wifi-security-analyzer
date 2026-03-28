from scanner import scan_networks
from analyzer import analyze_security

networks = scan_networks()

for net in networks:
    security = analyze_security(net)

    print("SSID:", net['ssid'])
    print("Signal:", net['signal'])
    print("Security:", security)
    print("-" * 40)