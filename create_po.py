import os
import sys
import pandas as pd

# #####
# Creates or updates a PO file with new/modified strings for WP Menus
# #####

if len(sys.argv) == 1:
  print('No post type specified... Exiting.')
  sys.exit()

file = sys.argv[1]
file_prefix = file.replace("_template", "")

df = pd.read_excel(file+".xlsx", None)
sheets = df.keys()

# loop through the sheets to create a po file
for sheet in sheets:
  print(sheet)
  new_df = pd.read_excel(file+".xlsx", sheet_name=sheet)

  filename = file_prefix + "-" + sheet + ".po"

  if not os.path.exists(filename):
    new_file = open(filename, 'a+')
  else:
    new_file = open(filename, 'w+')
 
  for p in range(new_df.shape[0]):
    new_file.write(new_df['location'][p])
    new_file.write("\n")
    new_file.write("msgid \"" + str(new_df['source'][p]) + "\"")
    new_file.write("\n")
    new_file.write("msgstr \"" + str(new_df['target'][p]) + "\"")
    new_file.write('\n\n')
  
  new_file.close()
