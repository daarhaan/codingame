import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
reapers = {}
epaves = {}

# game loop
while True:
    reapers.clear()
    epaves.clear()
    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())
    for i in range(unit_count):
        unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2 = input().split()
        unit_id = int(unit_id)
        unit_type = int(unit_type)
        player = int(player)
        mass = float(mass)
        radius = int(radius)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        extra = int(extra)
        extra_2 = int(extra_2)
        if player >= 0:
            reapers[unit_id]=(x,y)
        else :
            if extra > 0:
                epaves[unit_id]=(x,y,extra)

    print("Debug messages..." + str(reapers), file=sys.stderr)
    print("Debug messages..." + str(epaves), file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    def decide_action():
        my_reaper = reapers[0]
        print("Debug messages...my_reaper " + str(my_reaper), file=sys.stderr)
        d_min = 6000
        id_min = 0
        for id_e, ep in epaves.items():
            d = math.sqrt(math.pow(my_reaper[0]-ep[0],2) + math.pow(my_reaper[1]-ep[1],2))
            if d < d_min:
                d_min = d
                id_min = id_e
        print("Debug messages...closest epave at  " + str(d_min), file=sys.stderr)
        print("Debug messages...closest epave id  " + str(id_min), file=sys.stderr)

        if id_min == 0:
            return "WAIT"
        else:
            return str(epaves[id_min][0])+" "+str(epaves[id_min][1])+" 250"


    action = decide_action()
    print("Debug messages...action :  " + action , file=sys.stderr)

    print(action)
    print("WAIT")
    print("WAIT")