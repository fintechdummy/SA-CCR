from clean_data import *
import numpy as np

# reference period for the interest rate trades, start is assumed to be as of today, no forward start
netting_set['si'] = 0
netting_set['ei'] = (netting_set['end_date'] - netting_set['value_date'])/np.timedelta64(1, 'Y')

# time buckets for the hedging sets
netting_set['time_bucket'] = (netting_set['ei']-netting_set['si']).map(lambda x: 1 if x < 1 else (2 if x < 5 else 3))

# supervisory duration
netting_set['s_duration'] = netting_set['ei'].map(lambda x: x**0.5 if x < 1 else (np.exp(-0.05*0)-np.exp(-0.05*x))/0.05)

#adjusted notional
# no cross-correlation among time buckets therefore equal to abs value
netting_set['adj_mtm_dirty'] = netting_set['mtm_dirty']*netting_set['s_duration']

# supervisory delta
# being long the floating rate equals delta = 1, short = -1, no other values as no options are present
netting_set['s_delta'] = netting_set['receive_type'].map(lambda x: 1 if x == 'floating' else -1)

# maturity factor = 1 as no margins and time buckets > 1
netting_set['MF'] = 1

# adjusted notional
netting_set['effective_mtm_dirty'] = abs((netting_set['adj_mtm_dirty']*netting_set['s_delta']*netting_set['MF']))

# supervisory factor given cfr. https://www.bis.org/publ/bcbs279.pdf (pag.24)
super_factor = 0.005

# addon calculation
addon = super_factor*netting_set['effective_mtm_dirty'][0] + super_factor*netting_set['effective_mtm_dirty'][1]

