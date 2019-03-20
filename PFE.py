from RC import *
import numpy as np
from addon import *

# the floor to the multiplier  is set by Basel Committee to 5% cfr. https://www.bis.org/publ/bcbs279.pdf (pag.8)
floor = 0.05

# calculate potential future exposure
def potential_future_exposure(RC, addon):
    if RC < 0:
        multiplier = min(1, floor + (1-floor) * np.exp(V_C/(2*(1-floor)*addon)))
    else:
        multiplier = 1
    return multiplier * addon

# globalising the function and assigning it to a to a temporary variable
tempfunc2 = potential_future_exposure(RC, addon)

PFE = tempfunc2

PFE
