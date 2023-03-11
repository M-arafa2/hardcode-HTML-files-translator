# Site Translator
this script is for translating the language of any site source code
it has auto detect source language
you need to specify the target language on the translator page
the variable "lang"
and install the requirements

its splitted in two files
## navigator.py
it will locate all html files in root directory the script is placed into
and sub directories from that root directort
then it will list them and pass it to the translator function

## translator.py
i used the deep_translator package and googletranslate api
this script finds all text in the html without changing any html, css or javascript
pass it to googletranslate api , get translation and replace the text in html file

the final result is hardcoded translated files