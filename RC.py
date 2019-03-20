from clean_data import *

# function to calculate the replacement cost as maximum between 0 and the sum of position market values
# the function assumes a lack of margin and collateral
def replacement_cost(netting_set):

    V_C = sum(netting_set['mtm_dirty'])

    RC = max(V_C, 0)

    return [V_C,RC]

# globalising the function and assigning it to a temporary variable
tempfunc = replacement_cost(netting_set)

# reassigning the value to RC and VC
RC = tempfunc[1]

V_C = tempfunc[0]

