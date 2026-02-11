rover_state = {
    "x": 0,
    "y": 0,
    "samples": 0
}
cmd = input("Is there more in the command batch: ").strip().title()
if cmd == "Yes":
    while True:
        part0 = input("What is the command: ").strip().title()
        part1 = input("How much space to move")
        if part0 == "Move":
            try:
                space = int(part1)
            except ValueError:
                print("bad distance")
            else:
                rover_state["y"] = space
        elif part0 =="Dig":
            rover_state["samples"] = 1
        else:
            print("Unknown command")
else:
    print(rover_state)
