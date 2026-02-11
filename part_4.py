travel_log = []


while True:
    try:
        #num = int(sens)
        sens = int(input("Enter sensor value: "))
        if sens < 45: 
            print(sens)
            print("path stable")
            travel_log.append(sens)
            print(travel_log)

        else:
            print("CRTICAL TILT HALTING")
            break
    except ValueError:
        print("Sensor glitch")
print("Mission terminated")