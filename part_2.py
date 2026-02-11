rover_status = {
    "Battery": 100,
    "Heater": "Off"}
print("Battery charge:", rover_status["Battery"])
rover_status["Heater"] = "On"
rover_status["Battery"] = 85
rover_status["Speed"] = 5
print(rover_status)

