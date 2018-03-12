#!/usr/bin/python
#Google Jam Qualification Round 2008
#Problem A

from collections import Counter

def switch_engines():
    switches = 0
    num_eng = input()
    engines = [raw_input() for j in range(num_eng)]
    num_quer = input()
    queries = [raw_input() for j in range(num_quer)]
    current_engine = ""
    current_engine_index = 0;
        
    for engine in engines:
        if engine in queries:
            #Use the engine that takes you the furthest
            if queries.index(engine) >= current_engine_index:
                current_engine = engine
                current_engine_index = queries.index(engine)
        #There is an engine that isn't in the queries list
        #Use that, 0 switches
        else:
            return 0
    
    #Start index is last query, 0 switches
    if current_engine_index + 1 == len(queries):
        return 0
            
    for query in queries[current_engine_index:]:
        if query == current_engine:
            switches += 1
            new_engine_list = [x for x in engines if x != current_engine]
            next_engine = pick_next_engine(queries[current_engine_index + 1:], new_engine_list, current_engine)
            current_engine = next_engine[0]
            current_engine_index += next_engine[1]
    
    return switches
    
def pick_next_engine(queries, engines, current_engine):
    next_engine = ""
    current_engine_index = 0
    for engine in engines:
        if engine in queries:
            #Use the engine that takes you the furthest
            if queries.index(engine) >= current_engine_index:
                next_engine = engine
                current_engine_index = queries.index(engine)
        #There is an engine that isn't in the remaining queries list
        #Use that engine
        else:
            return (engine,len(queries))
    
    return (next_engine,current_engine_index);
    
for i in range(input()):
    print "Case #%d: %d" % (i+1, switch_engines()) 
    