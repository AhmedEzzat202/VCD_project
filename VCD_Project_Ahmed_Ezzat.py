import datetime
import random
import time
import math
import matplotlib.pyplot as plt

speed=int(input("please write the speed in km/h= ")) * 0.277778 #multiplied by0.277778 to convert speed to m/s
s_nod= 0 #Assume intial distance is Zero
road_Type= input("write type of the road if it is concrete/ice/water/gravel/sand= ")
road_condition= input("write condition of the road if it is dry/wet/aquaplanning= ")
u_static= 0
u_dynamic= 0

#s_distance= s_nod+(speed*t)+(0.5*a*(t^2)) #this is the main equation as we can get the value of time and accelration
if road_Type == "concrete" and road_condition =="dry" :
    u_static = 0.6
    u_dynamic= 0.5
elif road_Type == "concrete" and road_condition =="wet" :
    u_static = 0.4
    u_dynamic = 0.35
elif road_Type == "ice" and road_condition == "dry":
    u_static = 0.2
    u_dynamic =0.15
elif road_Type == "ice" and road_condition == "wet":
    u_static = 0.1
    u_dynamic = 0.08
elif road_Type == "water" and road_condition == "aquaplaning":
    u_static = 0.1
    u_dynamic = 0.05
elif road_Type == "gravel" and road_condition == "dry":
    u_static = 0
    u_dynamic = 0.35
elif road_Type == "sand" and road_condition == "dry":
    u_static = 0
    u_dynamic = 0.3
else: print("wrong type road & conditions")

a=-1*9.8*u_dynamic #decelration
sample_time=0.1
times = [0.0]
positions=[0.0]
velocities=[speed]

while velocities [-1] >0.0:
    times.append(times[-1]+sample_time)
    speed= (sample_time*a)+ velocities[-1]
    velocities.append(speed)
    s_distance= positions[-1]+(speed*sample_time)+(0.5*a*sample_time**2)
    positions.append(s_distance)
    if len(positions) > 1000:
        break

print('Breaking distance = ',s_distance)
print('accelration = ',a)

plt.plot(times,positions)
plt.xlabel('Time (sec)')
plt.ylabel('Breaking Distance (meters)')
plt.title('Breaking Distance vs. time')
plt.show()

plt.plot(times,velocities)
plt.xlabel('Time (sec)')
plt.ylabel('velocities (meters)')
plt.title('velocities vs. time')
plt.show()
