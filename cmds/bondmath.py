# these functions were used in the 2024 final exam for FINM 37400

# the functions in treasury_cmds.py mostly presume dataframes with cashflow schedules

# these functions are more useful for clean, textbook-like problems


###########

import numpy as np



def bond_pricer_formula(ttm,ytm,cpn=None,freq=2,face=100):
    
    if cpn is None:
        cpn = ytm
    
    y = ytm/freq
    
    disc_factor = 1/((1+y)**(freq*ttm))

    cf_cpn = face * (cpn/freq)
    pv_cpns = cf_cpn * (1-disc_factor)/y

    pv_tv = face * disc_factor
    
    pv = pv_tv + pv_cpns
    
    return pv
    
    
    

def bond_pricer_dcf(ttm,ytm,cpn=None,freq=2,face=100):
    
    if cpn is None:
        cpn = ytm
        
    pv = 0
    
    c = (cpn/freq)*face
    disc = 1/(1+ytm/freq)
    
    for t in range(ttm*freq):
        pv += c * disc**(t+1)
    
    pv += face * disc**(ttm*freq)

    return pv
    
    
    

def duration_closed_formula(tau, ytm, cpnrate=None, freq=2):

    if cpnrate is None:
        cpnrate = ytm
        
    y = ytm/freq
    c = cpnrate/freq
    T = tau * freq
        
    if cpnrate==ytm:
        duration = (1+y)/y  * (1 - 1/(1+y)**T)
        
    else:
        duration = (1+y)/y - (1+y+T*(c-y)) / (c*((1+y)**T-1)+y)

    duration /= freq
    
    return duration
    