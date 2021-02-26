from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from io import BytesIO
import os
import time
cwd = os.getcwd()


def takess():
        return driver.find_element_by_id('problem_statement').screenshot_as_png
        

PATH = '../'


if(len(sys.argv)==1):
    val = input("Please Enter Contest Number (btw you had to pass it as an argument): ")
else:
    val = sys.argv[1]
print('please wait while we open Firefox...')
print('Fact: Firefox may take upto 30 seconds when started using selenium')
driver = webdriver.Firefox(executable_path='..\geckodriver.exe')

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#driver.fullscreen_window()
os.mkdir('./'+val)

for letter in letters:
    #path = cwd+'\\'+val+'\\'+letter+'\\problem.png'

    driver.get("https://codeforces.com/problemset/problem/"+val+'/'+letter)
#     print(driver.current_url)
    if(driver.current_url != ("https://codeforces.com/problemset/problem/"+val+'/'+letter)):
        break
    os.mkdir('./'+val+'/'+letter)
    path = './'+val+'/'+letter+'/problem.png'
#     print(path)
    #driver.fullscreen_window()
    driver.find_element_by_class_name('problem-statement').screenshot(path)
    element = driver.find_element_by_class_name('sample-test')
    text = element.get_attribute('innerText')
    inin=0
    opin=0
#     print(text)
    for texts in text.split("output\nCopy\n"):
        if(opin!=0):
            #print('ye outut no.')
            #print(opin)
            #print(texts.split('\n')[0])
            file = open('./'+val+'/'+letter+'/output'+str(opin)+'.txt', 'w')
            file.write(texts.split('input')[0])
            file.close()
        opin=opin+1
    for texts in text.split("input\nCopy\n"):
        if(inin!=0):
            file = open('./'+val+'/'+letter+'/input'+str(inin)+'.txt', 'w')
            file.write(texts.split('output')[0])
            file.close()
        inin=inin+1
print('Task Complete')
driver.quit()