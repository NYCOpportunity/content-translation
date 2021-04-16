from google_trans_new import google_translator
import pandas as pd
import os
import sys

# #####
# Google Translate Post
# python posttypes.py brain-building
# Requires filename
# Optional: True/False to create a single file of all posts or a single CSV for each language
# #####

# check for arguments
if len(sys.argv) == 1:
  print('No post type specified... Exiting.')
  sys.exit()

if len(sys.argv) > 2:
  separate = True
else:
  separate = False
post_type = sys.argv[1]

file = os.path.join(os.getcwd(), post_type+'.csv')
posts = pd.read_csv(file)
posts = posts.dropna(how='all', axis='columns')

language_codes = [
    'es',
    'ht',
    'fr',
    'ko',
    'pl',
    'ru',
    'bn',
    'ar',
    'ur',
    'zh-TW'
]

new_df = pd.DataFrame(columns = posts.columns)
for i in range(len(language_codes)):
  print(language_codes[i])
  for p in range(posts.shape[0]):
    for c in range(len(posts.columns)):
      translator = google_translator()
      if (c > 1):
        new_df.loc[i, posts.columns[c]] = translator.translate(str(posts[posts.columns[c]][p]), lang_tgt=language_codes[i])
        # print(new_df.loc[i, posts.columns[c]])
      else:
        if posts.columns[c] == 'id':
          new_df.loc[i, posts.columns[c]] = int(posts[posts.columns[c]][p])
        else:
          new_df.loc[i, posts.columns[c]] = posts[posts.columns[c]][p]

  if separate == True:
    s_row_df = new_df.iloc[[-1]]
    s_row_df.to_csv(
        post_type+'-' + language_codes[i]+'.csv', index=False, encoding='utf-8-sig')

if separate == False:
  new_df.to_csv(post_type+'-all.csv', index=False, encoding='utf-8-sig')
