# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
BASKETBALLv2_BASKETBALL_EXPERIENCE_SF = dataiku.Dataset("BASKETBALLv2_BASKETBALL_EXPERIENCE_SF")
BASKETBALLv2_BASKETBALL_EXPERIENCE_SF_df = BASKETBALLv2_BASKETBALL_EXPERIENCE_SF.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Test_Python_output_df = BASKETBALLv2_BASKETBALL_EXPERIENCE_SF_df # For this sample code, simply copy input to output


# Write recipe outputs
Test_Python_output = dataiku.Dataset("Test_Python_output")
Test_Python_output.write_with_schema(Test_Python_output_df)
