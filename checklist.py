from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import time
from encrypt import decode
from dotenv import load_dotenv

def checklist(username, crypt_password, course_id=18):
    # Opens Selenium Chrome Webdriver:
    try:
        browser = webdriver.Chrome()
    except:
        raise ValueError("Cannot open Selenium Chrome Web Driver :c")
    
    # Try to go to course url:
    try:
        course_url = "https://moodle.ccbas.uaa.mx/course/view.php?id="+str(course_id)
        browser.get(course_url)
    except:
        raise ValueError(f"URL {course_url} does not works :c")
    
    # Login process:
    try:
        # Gets the bars and buttons on login:
        username_bar = browser.find_element(By.ID, "username")
        password_bar = browser.find_element(By.ID, "password")
        login_button = browser.find_element(By.ID, "loginbtn")

        # Decodes the password:
        load_dotenv()
        KEY = os.getenv("KEY")
        password = decode(crypt_password, KEY)

        # Send the data to login:
        username_bar.send_keys(username)
        password_bar.send_keys(password)
        login_button.click()
    except:
        raise ValueError("Maybe text bars or buttons change id ;:T")

    # Click on submit checklist link:
    try:
        # Find the <a> element with a <span> containing text starting with "Pase":
        time.sleep(6)
        link_elements = browser.find_elements(By.XPATH, '//div[@class="media-body align-self-center"]//a[.//span[starts-with(text(), "Pase")]]')

        if link_elements:
            link_elements[0].click()
        else:
            print("No matching elements found for \"Pase de lista\";:T")
    except:
        raise ValueError(f"Incorrect Password for \"{username}\" ;:T")
    
    # Click on return submit checklist button:
    try:
        check_button = browser.find_element(By.NAME, "submit")
        check_button.click()
    except:
        raise ValueError(f"Maybe wrong page, not checklist ;:T")

    # Close the browser:
    browser.quit()
    return True

checklist("al243681", "+\u0007\u0005\u0012*\u001a\u001a\u000b\fYG")