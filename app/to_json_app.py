#!/usr/bin/python

import os
import pandas as pd
import json

# VARIABLES
INPUT_PATH="sample_data"
OUTPUT_PATH="output"
INPUT_DATA="wine-ratings-small"
OUTPUT_DATA="filtered_ratings"
INPUT_EXTENSION="csv"
OUTPUT_EXTENSION="json"
INPUT_FILE=f"{INPUT_DATA}.{INPUT_EXTENSION}"
OUTPUT_FILE=f"{OUTPUT_DATA}.{OUTPUT_EXTENSION}"
INPUT_ABS_APTH=os.path.abspath(os.path.join(INPUT_PATH, INPUT_FILE))
OUTPUT_ABS_APTH=os.path.abspath(os.path.join(OUTPUT_PATH, OUTPUT_FILE))

# READ COLUMN NAMES
cols = list(pd.read_csv(INPUT_ABS_APTH, nrows =1))
print(cols, "\n")

# LOAD CSV
df = pd.read_csv(INPUT_ABS_APTH, usecols =[i for i in cols if i != "Unnamed: 0"])
print(df.head(), "\n")

#GET CSV INFO
print(df.info(), "\n")

# GET WHITE WINE SCORED BETWEEN 90 AND 92 POINTS FROM FRANCE
df_filtered = df[
    (df["variety"] == "White Wine")\
    & (df["rating"].between(90, 92))\
    & (df["region"].str.contains("France"))
    ].to_json(indent=2, orient="table")

# PARSE JSON
json_parsed = json.loads(df_filtered)

# DUMPS TO JSON
with open(OUTPUT_ABS_APTH, 'w', encoding='utf-8') as f:
    f.write(json.dumps(json_parsed, ensure_ascii=True, indent=2))
