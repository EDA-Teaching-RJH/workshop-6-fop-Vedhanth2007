new_findings = []
c = 0
while c < 3:
    rock = input("Enter rock name: ").strip().title()
    new_findings.append(rock)
    c = c + 1

for i in range(len(new_findings)):
    print(new_findings[i])

