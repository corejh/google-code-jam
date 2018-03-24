#!/usr/bin/python3
#Google Jam Qualification Round 2008
#Problem B

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def choo_choo_trains():
    turn_around = int(input()) #turn around time
    trip_data = input().split()
    num_trips_a, num_trips_b = int(trip_data[0]), int(trip_data[1])
    trips = [] #stores trains scheduled to leave
    trains = ([],[]) #stores ready trains with time arrived
    num_trains = [0, 0] #tally and final output
    
    for j in range(num_trips_a):
        a = input().split()
        trips.append((get_minutes(a[0]),get_minutes(a[1]),0))
    for k in range(num_trips_b):
        b = input().split()
        trips.append((get_minutes(b[0]),get_minutes(b[1]),1))
    
    trips = sorted(trips, key=lambda x: (x[0], x[1])) #sort by departure time, then arrival
    #print(len(trips))
    for trip in trips:
        station = trip[2]
        if (trains[station]) and (trains[station][0] <= trip[0]): #if a train is ready
            #print("station: " + str(station) + "pop",trains[station][0],trip[0])
            trains[station].pop(0)
        else:
            num_trains[station] += 1
            #print("station " + str(station) + " count: " + str(num_trains[station]))
            
        trains[1-station].append(trip[1] + turn_around)
        trains[1-station].sort()
    
    return str(num_trains[0]) + " " + str(num_trains[1])
    
def get_minutes(time_str):
    h, m = time_str.split(':')
    return int(h) * 60 + int(m)

for i in range(int(input())):
    print("Case #{}: {}".format(i+1, choo_choo_trains()))
     
    