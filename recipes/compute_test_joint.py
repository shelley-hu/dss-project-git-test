# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
BASKETBALLv2_BASKETBALL_EXPERIENCE_SF = dataiku.Dataset("BASKETBALLv2_BASKETBALL_EXPERIENCE_SF")
BASKETBALLv2_BASKETBALL_EXPERIENCE_SF_df = BASKETBALLv2_BASKETBALL_EXPERIENCE_SF.get_dataframe()
BASKETBALL_SF_SQL = dataiku.Dataset("BASKETBALL_SF_SQL")
BASKETBALL_SF_SQL_df = BASKETBALL_SF_SQL.get_dataframe()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

test_joint_df = ... # Compute a Pandas dataframe to write into test_joint


# Write recipe outputs
test_joint = dataiku.Dataset("test_joint")
test_joint.write_with_schema(test_joint_df)
