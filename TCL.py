import os
import sys
import time                                         #Time is used to delay execution of code for a specified amount of seconds
from selenium import webdriver                                                                        #Importing the WebDriver
from selenium.webdriver.common.keys import Keys                            #Keys lets me use Keyboard keys like Enter,Alt,Ctrl
from selenium.webdriver.common.by import By                          #By Locates Tags and Elements within documents (Webpages)
from selenium.webdriver.support import expected_conditions as EC                            #Used to wait for elements to load
from selenium.webdriver.support.ui import WebDriverWait                                     #Used to wait for elements to load


sys.stderr = open('NUL', 'w')                                                                  #Suppressing Errors and Verbose
browser_options = webdriver.ChromeOptions()
#browser_options.add_argument("--headless")                                                           #Run Browser in Background
#browser_options.add_argument("--disable-gpu")                                                         #Disable GPU Acceleration
browser_options.add_argument("--disable-logging")                                                  #Disable Verbose and logging
browser_options.add_argument("--log-level=3")                                                             #Disable console logs
Navigator = webdriver.Chrome(options=browser_options)            #Start a Chrome instance , Firefox and Edge are also available
Wait = WebDriverWait(Navigator, 10)
os.system("cls")
def Menu(Navigator,Wait):
    X = int(input("Tunisian Car Lookup"+'\n'+"Menu :" + '\n' + "1) Car Plates" + '\n' + "2) Plates Lookup"+ '\n'))
    if X==1 :
        Plates(Navigator,Wait)
    elif X==2 :
        Lookup(Navigator,Wait)
    else :
        print('Invalid Input')
    os.system("cls")
    
def Plates(Navigator,Wait):
    os.system("cls")
    Navigator.get("http://bit.ly/Car-Plates-TN") #Get Method will navigate to the URL given
    # --> https://www.automobile.tn/fr/guide/dernieres-immatriculations.html Replace with this URL if shortened EXPIRED
    Matricules = Wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))  #Get all text in <Span> tags
    Mat=((Matricules.text).replace('\n',' '))
    Mat1=(Mat[0:13])
    reverse = lambda Mat: Mat[0:4]+(Mat[4:8])[::-1]+Mat[8::]
    correct= lambda Mat,x : Mat[x::] + (Mat[:x])[::-1]
    Mat2=(Mat[31:41])
    Mat3=(Mat[59:69])
    Mat4=(Mat[86:97])
    Mat5=(Mat[114:126])
    Mat6=(Mat[143:151])
    Mat7=(Mat[169:179])
    Mat8=(Mat[196:206])
    print("Latest Car Plates in the Tunisian Streets"+'\n'+reverse(Mat1)+'\n'+correct(Mat2,4)+'\n'+correct(Mat3,4)+'\n'+correct(Mat4,4)+'\n'+correct(Mat5,5)+'\n'+correct(Mat6,4)+'\n'+correct(Mat7,4)+'\n'+correct(Mat8,4))
    Navigator.quit()
    
def Lookup(Navigator,Wait):
    Navigator.get("https://vidange.tn/") #Get Method will navigate to the URL given
    os.system("cls")
    Plate=input("Type Plate Number : ")
    if 'TUN' in Plate:
        Serial=Plate[:Plate.find('TUN')]
        Num=Plate[Plate.find('TUN')+3:]
        SerialInput=Navigator.find_element(By.ID,'numSerie')
        SerialInput.send_keys(Serial)
        NumInput=Navigator.find_element(By.ID,'numCar')
        NumInput.send_keys(Num)
        Navigator.find_element(By.NAME, "btn-search-mat").click()
        TITLES = Wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "title")))
        VALUES = Wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "value"))) 
        for title, value in zip(TITLES, VALUES):
            print(title.text)
            print(value.text)
        time.sleep(30)
    elif 'RS' in Plate:
        SerialNum=Plate[2:]
        Navigator.find_element(By.ID, "RSi").click()
        time.sleep(2)
        SerialNumInput=Navigator.find_element(By.ID , 'numRS')
        SerialNumInput.send_keys(SerialNum)
        Navigator.find_element(By.NAME, "btn-search-mat").click()
        TITLES = Wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "title")))
        VALUES = Wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "value"))) 
        for title, value in zip(TITLES, VALUES):
            print(title.text)
            print(value.text)
        time.sleep(30)
    else :
        print('Invalid Plate')
        time.sleep(30)
    Navigator.quit()
    

Menu(Navigator,Wait)