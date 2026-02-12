rover_state = {
    "x": 0,
    "y": 0,
    "samples": 0
}
cmd = input("Is there more in the command batch: ").strip().title()
if cmd == "Yes":
    for i in range(10):
        part = input("What is the command and space: ").split()
        if part[0] == "move":
            try:
                space = int(part[1])
            except ValueError:
                print("bad distance")
            else:
                rover_state["y"] = rover_state["y"] + space
        elif part[0] =="dig":
            rover_state["samples"] = rover_state["samples"] + 1
        else:
            print("Unknown command")
    print(rover_state)
elif cmd == "No":
    print(rover_state)
else: 
    print("Unknown command")
