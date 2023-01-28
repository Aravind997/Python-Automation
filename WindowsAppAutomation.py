
import pyautogui
from win32api import GetSystemMetrics
import os
print("SalesMate + Backup Menu Test")

print("Create a Database Backup directory called SMP")

path="E:/SMP"
if not os.path.exists(path):
    os.makedirs(path)
    
    #get the width and height of the monitor
    width=GetSystemMetrics(1)
    height=GetSystemMetrics(1)
    
    #click on the bottom left to lauch the start menu
    print("click on the bottom left to lauch the start menu")
    pyautogui.leftClick(1,height)
    print("Select the Salesmate + Application")
    pyautogui.typewrite("Salesmate +")
    print("Press Enter Key to Launch Salesmate + Application and wait for 8 sec")
    pyautogui.press("enter",1,8)
    print("Press the to close the tip of the Day instruction")
    pyautogui.press("enter")
    print("shortcut to invoke file menu")
    pyautogui.press(['alt','f'])
    print("Press b to invoke the backup folder Dialog")
    pyautogui.press("b")
    print("Go to E drive")
    pyautogui.press("down",8,1)
    print("Press Right arraow Key to Expand Options")
    pyautogui.press("right")
    print("Go to SMP Folder")
    pyautogui.typewrite("SMP")
    print("Press Enter Key to Backup Data")
    pyautogui.press("enter",1,2)
    print("Press Enter Again to Close the OK Button")
    pyautogui.press("enter")
    
    #Adding customer details
    print("Adding new customer details")
    pyautogui.press(['alt','c'])
    pyautogui.press("enter")
    print("Fill customer details")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.typewrite("Amazon")
    pyautogui.press("enter")
    pyautogui.typewrite("Google")
    pyautogui.press("enter")
    pyautogui.typewrite("Mr")
    pyautogui.press("enter")
    pyautogui.typewrite("Silicon Valley America")
    pyautogui.press("enter")
    pyautogui.typewrite("9748273647")
    pyautogui.press("enter")
    pyautogui.typewrite("amazon@gmail.com")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    
    #Saving Customer Details
    print("Save the Customer Details")
    pyautogui.typewrite("s")
    pyautogui.press("enter")
    pyautogui.press("esc")
    
    
    
    
    
    
    
    
    
    
    
    

    
     
    
    
   
    
