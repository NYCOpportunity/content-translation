import os
import sys
import pandas as pd
import re
import xlsxwriter

# #####
# Creates a sheet in a workbook for each program with rows for translations
# #####

if len(sys.argv) == 1:
  print('No post type specified... Exiting.')
  sys.exit()

file = sys.argv[1]
sheet = sys.argv[2]

df = pd.read_excel(file+".xlsx", sheet_name=sheet)

columns = df.columns

language_codes = [
  'English',
  'Arabic',
  'Bangla',
  'French',
  'Haitian Creole',
  'Korean',
  'Polish',
  'Russian',
  'Spanish',
  'Traditional Chinese',
  'Urdu',
]

# create or open spreadsheet
file_name = file+"-template.xlsx"
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

if os.path.exists(file_name):
  book = xlsxwriter.Workbook(file_name)
  writer.book = book

# create a sheet for each row
for r in range(df.shape[0]):
  new_df = pd.DataFrame(columns=columns)
  
  # append program and reset the index
  new_df = new_df.append(df.iloc[r])
  new_df = new_df.reset_index(drop=True)

  name = re.sub('[^A-Za-z0-9]+', '', new_df['title'].values[0])
  name = name[0:10] + '-' + str(r)

  # creates empty language column
  new_df['language'] = ''

  # adds language code to row
  for l in range(len(language_codes)):
    new_df.loc[l, 'language'] = language_codes[l]

  # write to sheet
  col = new_df.pop("language")
  new_df.insert(0, col.name, col)
  print(new_df)
  new_df.to_excel(writer, sheet_name=name, engine='xlsxwriter')

# save workbook
writer.save()
writer.close()

