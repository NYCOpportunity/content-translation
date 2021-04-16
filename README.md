# Content Translation

This repository contains scripts to manage content translations. For a number of NYCO products, the WordPress plugins, [WPML](https://wpml.org/) and [WP All Import](https://www.wpallimport.com/), is used to help manage translations as well as bulk imports.

**Features**:
* Translate rows and columns in a spreadsheet using the Google Translate API via Python package
* Take a human translated CSV and create appropriate language spreadsheets to import into WordPress
* Create PO files of strings to import into WordPress

## Getting Started
**Requirements**
* [Python](https://www.python.org/downloads/)
* [virtualenv](https://docs.python.org/3/tutorial/venv.html)

**What do you want to do?**
* <a href="#Auto-translations">Auto-translations</a>
    * <a href="#Google-Translate-Strings">Google Translate Strings</a>
    * <a href="#Google-Translate-Content-in-CSV">Google Translate Content in CSV</a>
    * <a href="#Google-Translate-Taxonomies">Google Translate Taxonomies</a>
* <a href="#Generate-template-to-send-to-translators">Generate template to send to translators</a>
* <a href="#Creating-PO-files-from-spreadsheet">Creating PO Files from speadsheet</a>
* <a href="#Export-sheets-in-spreadsheet-as-individual-CSV">Export sheets in spreadsheet as individual CSV</a>
* <a href="#Combine-spreadsheets-in-directory-Export-for-each-language">Combine spreadsheets in directory; Export for each language</a>

## Auto-translations
There are times when you need translations for some content immediately. This section will focus on how to leverage the Google Translate API for temporary translations. It is recommended to only use this on small tasks and rely more heavily on human translations.

### Google Translate Strings
Strings are global snippets of text that can appear at multiple locations on an application. For example, "Learn more" is a string as it could be used on links or buttons throughout a website.

`gtranslate_all_strings.py` takes 2 arguments:
1. Name of the spreadsheet containing the strings you want to translate
2. The name of the sheet that contains the strings to be translated, with headers matching the language code approved by Google's translate API

```
python gtranslate_all_strings.py demos/gtranslate_all_strings/sample-translate-all-strings master
```
The script will open the `demos/gtranslate_all_strings/sample-translate-all-strings.xlsx` and loop thru all the rows to check to see if there's a translation for the English text. If not, that English text will be sent to the Google Translate API along with the language code for the desired translation and the cell will be populated. The script will save in the same file.

In the demo, the translations for "Hello" are currently empty for all languages that are not English. When you run the script, the translations for "Hello" will be populated.

### Google Translate Content in CSV
There are times when you need translations for some content immediately. This section will focus on how to generate a translation for a single post in all the langues, either in a single file or as a separate file.

`gtranslate_post.py` takes 2 arguments:
1. Name of the CSV with content that you want translated
2. True or False - True if you would like to create a separate file for each language; False if you want all the translations in one CSV.

**Example**: Compile translations in single file
```
python gtranslate_post.py demos/gtranslate_post_types/sample-gtranslate_post_types
```
The script will open `demos/gtranslate_post_types/sample-gtranslate_post_types.csv` and loop thru the first row, sending each cell of English text to Google Translate API to generate a translation. The translations will be exported into a single CSV:
* `demos/gtranslate_post_types/sample-gtranslate_post_types-all.csv`

**Example**: Compile translations into a separate file for each language
```
python gtranslate_post.py demos/gtranslate_post_types/sample-gtranslate_post_types True
```
The script with the **True** argument will open `demos/gtranslate_post_types/sample-gtranslate_post_types.csv` and loop thru the first row, sending each cell of English text to Google Translate API to generate a translation for a language that will be exported as a CSV:
* `demos/gtranslate_post_types/sample-gtranslate_post_types-ar.csv`
* `demos/gtranslate_post_types/sample-gtranslate_post_types-bn.csv`
* `demos/gtranslate_post_types/sample-gtranslate_post_types-fr.csv`
* ...

## Google Translate Taxonomies
There are times when you want to quickly translate strings associated with taxonomies. This section highlights how to create a separate CSV of translated taxonomies.

`gtranslate_taxonomies.py` takes 1 argument:
* The name of the CSV that contains the taxonomies that need translating

```
python gtranslate_taxonomies.py demos/gtranslate_taxonomies/sample-gtranslate_taxonomies
```
The script will loop thru the taxonomies in `demos/gtranslate_taxonomies/sample-gtranslate_taxonomies.csv` and sends each English string to Google Translate API and store it in a new CSV for a single language:
* `demos/gtranslate_taxonomies/sample-gtranslate_taxonomies-ar.csv`
* `demos/gtranslate_taxonomies/sample-gtranslate_taxonomies-bn.csv`
* `demos/gtranslate_taxonomies/sample-gtranslate_taxonomies-es.csv`
* ...

## Generate template to send to translators
The following commands allow you to create a xlsx template that translators will open to enter translations.

`generate_template.py` accepts 2 arguments:
* Name of the Spreadsheet to convert to a template
* Name of the first sheet in the Spreadsheet

**Example**:
```
python generate_template.py demos/generate_template/sample-initial-content-export "Sheet1"
```
The script will open the `demos/generate_template/sample-initial-content-export.xlsx`, iterate over the rows and columns in "Sheet1" and export a template file `demos/generate_template/sample-initial-content-export-template.xlsx`


## Creating PO files from spreadsheet
PO files are portable object files that contain translations. If you are using WPML and WPML String translation in your application, you may need to generate PO files to bulk upload/update translations of strings. Strings are snippets of text that can be accessed anywhere on an application, whether it be a header or a menu link.

`create_po.py` takes 1 argument:
* The name of the spreadsheet that contains a sheet for each of the 11 languages.
    * **NOTE**: The value under location should make the wpml-name for the field in WordPress otherwise WP will not register the string.

**Example**:
```
python create_po.py demos/create_po/sample-create-po
```
The script will open the `demos/create_po/sample-create-po.xlsx` and create a PO file for each sheet, with the output being:
* `demos/create_po/sample-create-po-ar.po`
* `demos/create_po/sample-create-po-bn.po`
* `demos/create_po/sample-create-po-es.po`
* `demos/create_po/sample-create-po-fr.po`
* ...

These files can be imports into WPML > String Translation.

## Export sheets in spreadsheet as individual CSV
There might be times when you want a CSV based on every single sheet in a spreadsheet.

`export_sheets.py` takes 1 argument:
* The name of the spreadsheet where each sheet is a different post

**Example**:

```
 python export_sheets.py demos/export_sheets/sample-export_sheets
```
The script will loop through all the sheets in `demos/export_sheets/sample-export_sheets` and create a individual CSV from it:
* `demos/export_sheets/sample-export_sheets-ar.csv`
* `demos/export_sheets/sample-export_sheets-bn.csv`
* `demos/export_sheets/sample-export_sheets-es.csv`
* `demos/export_sheets/sample-export_sheets-fr.csv`
* ...

## Combine spreadsheets in directory; Export for each language
In order to bulk import content in WordPress with the WP All Import plugin, you need to have a CSV that contains all the post content for a single language.

`generate_bulk_csv.py` takes 1 argument:
* The name of the directory that has all the spreadsheets you want to combine for each language

**Example**:

```
python generate_bulk_csv.py demos/generate_bulk_csv
```
The script will loop through every xlsx file in the `programs` directory and create a CSV for each language ("English", "Arabic", "Bengali", "Traditional Chinese", "French", "Haitian Creole", "Korean", "Polish", "Russian", "Urdu"):

* `demos_generate_bulk_csv-Arabic.csv`
* `demos_generate_bulk_csv-Bengali.csv`
* `demos_generate_bulk_csv-English.csv`
* ...