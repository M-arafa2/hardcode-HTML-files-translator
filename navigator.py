import os
import glob
from translator import translate_file
from multiprocessing import Pool

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)
dir_list=[]

for file in glob.iglob(ROOT_DIR+'/**/*.html',recursive=True):
    dir_list.append(file)

def partial(dir_list):
    Files_remaining = len(dir_list)
    print(str(len(dir_list))+" Files Detected")
    for file in dir_list:
        print(file+" translating....") 
        translate_file(file)
        print(file+" translated ")
        Files_remaining -=1
        if Files_remaining ==0:
            print("All Files Translated Successfully")
        else:
            print(str(Files_remaining )+ " Files Remaining")
        
        
partial(dir_list)
#if __name__ == '__main__':
    

    #print(str(len(dir_list)) + " HTML Files detected") 
    #with Pool(10) as p:
        #p.imap(translate_file, dir_list)
        #for file in p.imap_unordered(translate_file, dir_list):
            #print(str(len(dir_list)-1) +" Files Remaining")