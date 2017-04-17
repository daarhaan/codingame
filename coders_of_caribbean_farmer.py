import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop


while True:
    my_ship_count = int(input())  # the number of remaining ships
    entity_count = int(input())  # the number of entities (e.g. ships, mines or cannonballs)
    targets = []
    d_min=32
    x_ship=0
    y_ship=0
    z_ship=0
    s_ship=0
    stock_ship=0
    x_ship_en=0
    y_ship_en=0
    s_ship_en=0
    z_ship_en=0
    x_target=0
    y_target=0
    z_target=0
    z=0
    nb_barrels=0
    
    action=""

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
        z=-x-y
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        print(str(entity_id) +" "+ str(entity_type)+" "+str(x)+" "+str(y)+" "+str(arg_1)+" "+str(arg_2)+" "+str(arg_3)+" "+str(arg_4),file=sys.stderr)
        #targets.append([entity_id,entity_type,x,y,arg_1,arg_2,arg_3,arg_4])
        if entity_type =="SHIP":
            if arg_4==1:
                x_ship=x
                y_ship=y
                z_ship=z
                s_ship=arg_2
                stock_ship=arg_3
            else:
                x_ship_en=x
                y_ship_en=y
                z_ship_en=z
                s_ship_en=arg_2
        if entity_type == "BARREL":
            #d = math.pow(x-x_ship,2) + math.pow(y-y_ship,2)
            d = max(abs(x-x_ship),abs(y-y_ship),abs(z-z_ship))
            nb_barrels=nb_barrels+1
            print( "d is :" + str(d),file=sys.stderr)
            if d<d_min:
                d_min=d
                x_target=x
                y_target=y
                z_target=z
            
    print(targets,file=sys.stderr)
    for i in range(my_ship_count):
        #"print("WAIT")

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # Any valid action, such as "WAIT" or "MOVE x y"
        d_en=(abs(x_ship_en-x_ship)+abs(y_ship_en-y_ship)+abs(z_ship_en-z_ship))/3
        action="MOVE " + str(x_target) +" "+str(y_target)
        print("my stock is : " + str(stock_ship),file=sys.stderr)
        print("d_en is : " + str(d_en),file=sys.stderr)
        print("my ship : " + str(x_ship) +" " +str(y_ship) +" "+str(z_ship),file=sys.stderr)
        print("enemi ship : " + str(x_ship_en) +" " +str(y_ship_en) +" "+str(z_ship_en),file=sys.stderr)
        if stock_ship > 70:
            if d_en <= 10:
                action = "FIRE " + str(x_ship_en+random.randint(-1,1)) +" "+str(y_ship_en+random.randint(-1,1))
            else:
                action = "MOVE " + str(x_ship_en) +" "+str(y_ship_en)
        else:
            action="MOVE " + str(x_target) +" "+str(y_target)
            
        if nb_barrels == 0:
            if d_en <= 10:
                action = "FIRE " + str(x_ship_en+random.randint(-1,1)) +" "+str(y_ship_en+random.randint(-1,1))
            else:
                action = "MOVE " + str(x_ship_en) +" "+str(y_ship_en)
        
        print(action)
        #print("MOVE " + str(x_target) +" "+str(y_target))
