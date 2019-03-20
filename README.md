# SA-CCR
This repository contains an exploratory implementation of the Basel III Standardized Approach for Counterparty Credit Risk Management. (the complete regulation can be referenced here: http://www.bis.org/publ/bcbs279.htm)

The repository is divided in nine files, six scripts for the actual calculations, two for sample testing and a data example file. The correct order to perform calculations is the following:

1) read_raw_data.py
2) clean_data.py
3) RC_py
4) addon.py
5) PFE.py
6) EAD.py

The code structure is based on functional programming and I chose to utilize pandas dataframes in certain instances. The code is commented thoroughly for clarity, including references to the piece of legislation where required.

Many assumptions where made throughout the calculations, such as:

- I worked under the assumptions to only have interest rate derivatives trades at hand
- No optionality in the financial instruments
- No forward start for calculation purposes
- No margins or collateral
- All the securities have the same maturity buckets and always > 1yr, hence no cross-correlations among hedge sets
- Maturity factors = 1

Thanks everyone supporting the project and enjoy the read.
