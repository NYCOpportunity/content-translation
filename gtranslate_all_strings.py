from google_trans_new import google_translator
import os
import sys
import pandas as pd

# #####
# Creates or updates a PO file with new/modified strings for WP Menus
# Note: Google updates their translator often, so this script may need to be updated if there are errors
# #####

if len(sys.argv) == 1:
  print('No post type specified... Exiting.')
  sys.exit()

file = sys.argv[1]
sheet = sys.argv[2]

df = pd.read_excel(file+".xlsx", sheet_name=sheet)

# The first 2 columns are in English
for r in range(df.shape[0]):
  for c in range(df.shape[1]):
    translator = google_translator()
    if df.columns[c] != "String" and df.columns[c] != 'en':
      if pd.isna(df[df.columns[c]][r]):
        print('Translating ' + str(df['String'][r]) + ' for ' + df.columns[c])
        lang = df.columns[c]

        if df.columns[c] == 'zh-hant':
          lang = "zh-TW"

        df[df.columns[c]][r] = translator.translate(str(df['String'][r]), lang_tgt=lang)

df.to_excel(file+".xlsx", sheet_name='master', index=False)
