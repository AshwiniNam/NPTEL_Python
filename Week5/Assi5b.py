import math
position=[0,0]
n=int(input())
for i in range(n):
    s=input()
    movement=s.split(" ")
    direction=movement[0]
    steps=int(movement[1])
    if direction=="UP":
        position[0]+=steps
    elif direction=="DOWN":
        position[0]-=steps
    elif direction=="LEFT":
        position[1]-=steps
    elif direction=="RIGHT":
        position[1]+=steps
    else:
        pass
print(int(round(math.sqrt(position[0]**2+position[1]**2))))
