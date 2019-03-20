import pandas as pd
from read_raw_data import *

# transform the list into a pandas dataframe for easier manipulation
netting_set = pd.DataFrame(netting_set)

# cleaning the dataframe to calculate Si and Ei
def changedate(netting_set):
    netting_set.loc[:, ['date','trade_date','value_date','start_date','end_date']] = \
        netting_set.loc[:, ['date','trade_date','value_date','start_date','end_date']].apply(pd.to_datetime, errors='coerce')
    pass

changedate(netting_set)
