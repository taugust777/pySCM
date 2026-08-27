# pySCM

## Overview

This repository utilizes the pySCM (Python Simple Climate Model). The documentation for the model is listed below, as well as the GitHub repository for the model:

Documentation: https://pyscm.readthedocs.io/en/latest/code.html

GitHub Repository: https://github.com/bodekerscientific/pyscm

This repository makes use of pySCM and contains files for model output. Simple Python scripts to compute GHG emissions have also been created and are stored in this repository as well.

## Contents and Model Information

For full information on pySCM, see the documentation listed above. The model requires two input files (these are listed in the repository):

1. SimpleClimateModelParameterFile.txt
   - This file contains parameters needed to run the model itself, including start year, end year, years to evaluate the response              function, and ocean mixed layer depth in meters.
   - This file also contains information about the output scripts.
   - An example of this file can be seen listed under the file named "SimpleClimateModelParameterFile.txt".
   
2. EmissionsForSCM.txt
   - This file contains the concentrations of the following greenhouse gases: CO2, CH4, N2O, and SOx for the chosen number of years            specified in the "SimpleClimateModelParameterFile.txt" file.
   - An example of this file can be seen listed under the file named "EmissionsForSCM.txt".
  
The model returns the following 5 output files:

1. temp_output.txt
2. slr_output.txt
3. co2_output.txt
4. ch4_output.txt
5. n20_output.txt

Each file contains the raw results from the model run.

## Repository Scripts

This repository contains the following two scripts that have been created to run different experiments with pySCM:

1. GHG.py
   - IMPORTANT NOTE: This file operates under the assumption that the pySCM code has been modified to update the greenhouse gas                base values. In pySCM, the greenhouse gas base values are set to the pre-industrial level. This script assumes the user has changed       the greenhouse gas base values in the model code itself to modern-day (2025) values.
   - This script allows the user to pick an annual growth rate for each GHG, which then compounds from the base for the given number of        years.
   - The script also writes the resulting concentrations directly to the "EmissionsForSCM.txt" file.

2. pySCM_demo.py
   - 
   
