import random

valasztasok = ['Kő', 'Papír', 'Olló']
robot_pont = 0
jatekos_pont = 0

for i in range(3):

    jatekos = input("Valasztasod:")

    robot = random.choice(valasztasok)
    while not jatekos in valasztasok:
        jatekos = input("Ujra:")
        break

    if jatekos == robot:
        print("Draw")
        print(robot, jatekos)
    elif jatekos == 'Kő' and robot == 'olló' or jatekos == 'Papír' and robot == 'Kő' or jatekos == 'Olló' and robot == 'Papír':
        print("You win")
        print(robot, jatekos)
        jatekos_pont += 1
    elif jatekos == 'Kő' and robot == 'Papír' or jatekos == 'Papír' and robot == 'Olló' or jatekos == 'Olló' and robot == "Kő":
        print("Robot win")
        print(robot, jatekos)
        robot_pont += 1
    else:
        pass

if robot_pont > jatekos_pont:
    print("Robot win")
elif jatekos_pont > robot_pont:
    print("You Win")
else:
    print("Draw")
