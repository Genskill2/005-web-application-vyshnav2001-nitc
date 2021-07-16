import json
import math

def load_journal(fname) :
    f = open(fname,"r")                 # opens file in write mode
    data = json.loads(f.read())         # loads json file and returns dictonary of values
    f.close()
    return data
    
def compute_phi(fname,event) :
    ldic = load_journal(fname)
    n11 , n00 , n10 , n01 , n1plus , n0plus , nplus1 , nplus0 = 0,0,0,0,0,0,0,0
    
    for i in ldic :
        if event in i['events'] and i['squirrel'] == True :
            n11 += 1
            nplus1 += 1
            n1plus += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        elif event not in i['events'] and i['squirrel'] == True :
            n01 += 1
            nplus1 += 1
            n0plus += 1
        elif event in i['events'] and i['squirrel'] == False :
            n10 += 1
            n1plus += 1 
            nplus0 += 1
        else :
            n00 += 1
            n0plus += 1
            nplus0 += 1
    return ((n11*n00)-(n01*n10))/((n1plus*nplus1*n0plus*nplus0)**0.5)
    
def compute_correlations(fname) :
    data = load_journal(fname)
    eventPhi = {}
    vis = []
    for i in data :
        for j in i['events'] :
            if j not in vis :
                eventPhi[j] = compute_phi(file_name,j)
                vis.append(j)
    return eventPhi
    
def diagnose(fname) :
    eventPhi = compute_correlations(fname)
    maxval , minval = -100 , 100
    for i in eventPhi :
        if( eventPhi[i] > maxval ) :
            maxval = phidict[i]
            maxeve = i
        if( eventPhi[i] < minval ) :
            minval = eventPhi[i]
            mineve = i
    return maxeve , mineve
