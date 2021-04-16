import pandas as pd
import sys

# #####
# Export sheets in a workbook as single CSVs
# #####

# check for arguments
if len(sys.argv) == 1:
  print('No post type specified... Exiting.')
  sys.exit()

file = sys.argv[1]

df = pd.read_excel(file+".xlsx", None)
sheets = df.keys()
for sheet in sheets:
  print(sheet)
  new_df = pd.read_excel(file+".xlsx", sheet_name=sheet)
  new_df.to_csv(file+"-"+sheet+".csv", index=False, encoding='utf-8-sig')