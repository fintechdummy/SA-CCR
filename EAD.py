from PFE import *
from RC import *

# alpha value provided by regulatory board cfr. https://www.bis.org/publ/bcbs279.pdf (pag. 1)
alpha = 1.4

# calculate the exposure at default (EAD) including all parameters
EAD = alpha*(RC+PFE)

print(EAD)