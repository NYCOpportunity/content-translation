import pandas as pd
import sys
import glob
import os

# #####
# Opens Excel workbooks and compile a csv for each language
# Requires folder name that contains all the files to be converted
# #####

# check for arguments
if len(sys.argv) == 1:
  print('No post type specified... Exiting.')
  sys.exit()

posttype = sys.argv[1]

if '/' in posttype:
  posttype = posttype.replace('/', '_')

os.chdir(sys.argv[1])

languages = [
    'English',
    'Arabic',
    'Bengali',
    'Traditional Chinese',
    'French',
    'Haitian Creole',
    'Korean',
    'Polish',
    'Russian',
    'Urdu',
    'Spanish'
]

# loop through each language
for i in range(len(languages)):
  print('#####')
  print(languages[i])
  new_df = pd.DataFrame()

  for file in glob.glob("*.xlsx"):
    print(file)

    df = pd.read_excel(file, None)
    sheets = df.keys()
    print(sheets)

    # loop through the sheets
    for sheet in sheets:
      temp_df = pd.read_excel(file, sheet_name=sheet)
      new_df = new_df.append(temp_df.loc[[i]])

  # export as CSV
  new_df.to_csv(posttype+"-"+languages[i]+".csv", index=False, encoding='utf-8-sig')
