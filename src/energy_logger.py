import random
from datetime import datetime

# Monitored cities and their Swedish electricity zones
cities = [
    {"name": "Malmö", "zone": "SE4"},
    {"name": "Göteborg", "zone": "SE3"},
    {"name": "Stockholm", "zone": "SE3"},
    {"name": "Luleå", "zone": "SE1"},
]

print("Logging hourly electricity prices and usage...\n")

for city in cities:
    # Southern zones (SE3/SE4) typically have higher prices than the North (SE1)
    base_price = 45.0 if city["zone"] == "SE1" else 115.0
    price_ore = round(base_price + random.uniform(-15.0, 45.0), 2)
    usage_kwh = round(random.uniform(1.2, 5.8), 2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{timestamp}] {city['name']} ({city['zone']}): {price_ore} öre/kWh | Usage: {usage_kwh} kWh")
