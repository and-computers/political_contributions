#!/usr/bin/env python3

import pandas as pd

from constants.schemas import FEC_DATA_SCHEMA

df_kamala = pd.read_csv('data/kamala/schedule_a-2019-01-29T21_37_01.csv', dtype=FEC_DATA_SCHEMA)

df_groupedby = df_kamala.groupby('contributor_name')['contribution_receipt_amount'].sum()


df_warren = pd.read_csv('data/elizabeth_warren/schedule_a-2019-01-30T21_21_49.csv', dtype=FEC_DATA_SCHEMA)
df_warren_groupedby = df_warren.groupby('contributor_name')['contribution_receipt_amount'].sum()


import pdb
pdb.set_trace()


def sum_group_contributions(input_df):
    """pass in a dataframe and group it to a new series that is sorted in the order of contibutors to the campaign.

    [description]

    Arguments:
            input_df {[pandas DataFrame]} -- raw dataframe directly from the FEC site.

    Returns:

    """
    return input_df.groupby('contributor_name')['contribution_receipt_amount']
