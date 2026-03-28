import pywifi
import time

def scan_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(3)

    results = iface.scan_results()

    networks = []

    for net in results:
        network_info = {
            "ssid": net.ssid,
            "signal": net.signal,
            "bssid": net.bssid,
            "akm": net.akm
        }
        networks.append(network_info)

    return networks