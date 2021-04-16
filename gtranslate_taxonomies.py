# from googletrans import Translator
from google_trans_new import google_translator
import pandas as pd
import os
import sys

# #####
# Google Translate Taxonomy Groups
# python taxonomies.py brain-building-tip-categories
# Requires filename
# #####

# check for arguments
if len(sys.argv) == 1:
  print('No post type specified... Exiting.')
  sys.exit()

# Begin the translator and translate!
translator = google_translator()
taxonomy_group = sys.argv[1]
file = os.path.join(os.getcwd(), taxonomy_group+'.csv')

taxes = pd.read_csv(file)

tax_df = pd.DataFrame()
tax_df['en'] = taxes['en']
print(tax_df)

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

for i in range(len(language_codes)):
  tax_df = pd.DataFrame()
  tax_df['en'] = taxes['en']
  tax_df['slug_en'] = taxes['slug_en']
  tax_df['id_en'] = taxes['id_en']
  tax_df['desc_en'] = taxes['desc_en']

  for j in range(len(tax_df)):

    if language_codes[i] == 'zh-TW':
      tax_df.at[j, 'name'] = translator.translate(
          str(tax_df['en'][j]), lang_tgt=language_codes[i])
      tax_df.at[j, 'slug'] = tax_df.at[j, 'slug_en'] + '-zh-hant'
      tax_df.at[j, 'desc'] = translator.translate(str(tax_df['desc_en'][j]), lang_tgt=language_codes[i])
    else:
      tax_df.at[j, 'name'] = translator.translate(
          str(tax_df['en'][j]), lang_tgt=language_codes[i])
      tax_df.at[j, 'slug'] = tax_df.at[j, 'slug_en'] + '-'+language_codes[i]
      tax_df.at[j, 'desc'] = translator.translate(str(tax_df['desc_en'][j]), lang_tgt=language_codes[i])

  # exports a single csv for current language
  tax_df.to_csv(taxonomy_group+'-' +
                language_codes[i]+'.csv', index=False, encoding='utf-8-sig')
