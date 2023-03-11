from bs4 import BeautifulSoup,NavigableString
from deep_translator import GoogleTranslator
import logging
logger =logging.getLogger()

def translate(t, tag, lang):
  for i in range(0, len(t)):
    if type(t[i])== NavigableString:
      translation = GoogleTranslator(source='auto', target=str(lang)).translate(t[i])
      new_text = tag.find(text=str(t[i])).replace_with(translation)
    else:
      translate(t[i].contents,tag, lang)
      
  
def translate_file(file):
  # change this to any other language prefix for the
  #language you want to translate to
  #source language is auto detected
  lang = "hi"
  html_file = open(file,encoding="utf8").read()
  #used lxml parser because its faster
  soup = BeautifulSoup(html_file,"lxml")
  #those are all tags that contain text
  # i excluded "li" tag because it change the html attributes
  #which remove classes attributes etc
  tags = soup.find_all(["p", "a", "h1", "h2", "h3", "h4", "h5", "h6", "td", "strong", "span", "title", "em"])
  
  for tag in tags:
    try:
      translate(tag.contents, tag, lang)
    # attribute error happen when it pass empty text
    # it doesnt affect the process thatswhy i passed it
    except AttributeError as a:
      pass
    except Exception as e :
      logger.exception("Exception Occured while code Execution: "+ str(e))
 
  with open(file, "wb") as final_output:
    final_output.write(soup.prettify("utf-8"))


  


      
    
    
