#!/usr/bin/env python3

import pandas as pd

from constants.schemas import FEC_DATA_SCHEMA

df = pd.read_csv('data/kamala/schedule_a-2019-01-29T21_37_01.csv', dtype=FEC_DATA_SCHEMA)

df_groupedby = df.groupby('contributor_name')['contribution_receipt_amount'].sum()
