import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop

while True:
    my_ship_count = int(input())  # the number of remaining ships
    entity_count = int(input())  # the number of entities (e.g. ships, mines or cannonballs)
    targets = []
    print(targets, file=sys.stderr)
    for i in range(entity_count):
        entity_id, entity_type, x, y, arg_1, arg_2, arg_3, arg_4 = input().split()
        entity_id = int(entity_id)
        if(entity_type == "SHIP"):
            entity_type_id = 0
        else:
            entity_type_id = 1
        x = int(x)
        y = int(y)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        print(str(entity_id) +" "+ str(entity_type)+" "+str(x)+" "+str(y)+" "+str(arg_1)+" "+str(arg_2)+" "+str(arg_3)+" "+str(arg_4),file=sys.stderr)
        targets.append([entity_id,entity_type,x,y,arg_1,arg_2,arg_3,arg_4])
    print(targets,file=sys.stderr)
    for i in range(my_ship_count):
        #"print("WAIT")

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # Any valid action, such as "WAIT" or "MOVE x y"
        print("MOVE 11 10")
