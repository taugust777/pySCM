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
  


   
