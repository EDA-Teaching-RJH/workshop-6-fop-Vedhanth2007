inp = input("Enter speed here: ")
try: 
    speed = int(inp)
    print("speed is set to", speed)
except ValueError:
    print("Error: Corrupted signal")

