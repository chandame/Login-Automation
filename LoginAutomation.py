import selenium
import time
from selenium import webdriver
import csv
from csv import reader
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def Connecting_To_Browser(id_str, pass_str,data):
    if id_str != "" and pass_str != "":
        
        options = webdriver.ChromeOptions()

        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome("chromedriver.exe",options=options)
        
        browser.get('https://accounts.google.com/o/oauth2/v2/auth/identifier?client_id=945920829530-vjjff7q3fkugsk4rc44nr678mdvgip96.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fauth.booyah.live%2Foauth%2Flogin%2Fgoogle&response_type=code&scope=profile%20email%20openid&state=%2526client_id%253D10058%2526redirect_uri%253Dhttps%25253A%25252F%25252Fbooyah.live%25252Flogin%2526response_type%253Dtoken%2526platform%253D8%2526locale%253Den-GB%2526state%253D&flowName=GeneralOAuthFlow')
        time.sleep(1)
        email_field = browser.find_element_by_id("identifierId")
        email_field.clear()
        browser.maximize_window()

        email_field.send_keys(id_str)
        
        email_next_button = browser.find_element_by_id("identifierNext")
        email_next_button.click()

        time.sleep(2)

        password_field = browser.find_element_by_name("password")
        password_field.clear()

        password_field.send_keys(pass_str)

        password_next_button = browser.find_element_by_id("passwordNext")
        password_next_button.click()
        time.sleep(4)

        #password_next_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/nav/ul/li[4]/a")
        #state = password_next_button.click()
        #print(state)
        browser.get(data)
        
    return 0

text_file = open("data.txt", "r")
data = text_file.read()
text_file.close()
 
print(data)
with open('id_pass.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

print("Total Ids and Passwords: ", len(list_of_rows))
total_Len = len(list_of_rows)

ids_pass_list = list_of_rows


count =1
for i in range(len(ids_pass_list)):
    id_str = ids_pass_list[i][0]
    id_pass = ids_pass_list[i][1]
    print("Record-",count)
    print("Login Id: ", id_str)
    print("Login Password: ", id_pass)
    #c = 'tab'+str(count)
    Connecting_To_Browser(id_str, id_pass,data)
    print("Login successful!")
    print("number of active chrome agent ",count)
    count=count+1
