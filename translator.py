from bs4 import BeautifulSoup, Tag,NavigableString
from deep_translator import GoogleTranslator
import logging
logger =logging.getLogger()

def translate(t, tag, lang):
  for i in range(0, len(t)):
    if type(t[i])== NavigableString:
      #print("t[i] " + t[i])
      translation = GoogleTranslator(source='auto', target=str(lang)).translate(t[i])
      #translation = GoogleTranslator(source='auto', target=str(lang)).translate(tag.get_text())    
      #print(translation)
      new_text = tag.find(text=str(t[i])).replace_with(translation)
    else:
      translate(t[i].contents,tag, lang)
      
  
def translate_file(file):
  lang = "hi"
  html_file = open(file,encoding="utf8").read()
  soup = BeautifulSoup(html_file,"lxml")
  tags = soup.find_all(["p", "a", "h1", "h2", "h3", "h4", "h5", "h6", "td", "strong", "span", "title", "em"])
  
  for tag in tags:
    try:
      translate(tag.contents, tag, lang)
    except AttributeError as a:
      pass
    except Exception as e :
      logger.exception("Exception Occured while code Execution: "+ str(e))
 


      
    
  with open(file, "wb") as final_output:
    final_output.write(soup.prettify("utf-8"))


  


      
    
    
