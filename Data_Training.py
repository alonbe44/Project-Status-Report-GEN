#  Copyright (c) 2024. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from datetime import datetime, timedelta
from Conf import *


def data_train():
    global startDate, actend, end, preduction_period
    # Create EdgeOptions object
    options = Options()

    # Create a new instance of the Edge driver
    browser = webdriver.Edge(options=options)

    # Navigate to the login page
    browser.get("https://supportcrm.globitel.com/index.php")
    browser.maximize_window()

    # Find the username and password input fields and enter your credentials
    username_input = browser.find_element(By.ID, "username")
    username_input.send_keys(username)
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    # select first tab to close it.
    first_tab_handle = browser.window_handles[0]

    # waiting for page to load.
    browser.implicitly_wait(3)
    browser.get(
        "https://supportcrm.globitel.com//index.php?module=Project&view=List&viewname=213&app=MARKETING")
    # Open a new tab and navigate to a new page
    browser.execute_script(
        "window.open('https://supportcrm.globitel.com//index.php?module=Project&view=List&viewname=213&app=MARKETING')")

    actions = ActionChains(browser)
    actions.send_keys(Keys.END).perform()

    # listopen=browser.find_element(By.CLASS_NAME, "app-icon fa fa-bars")

    # Find all buttons on the page by their tag name
    secound_tab = browser.window_handles[1]

    browser.switch_to.window(first_tab_handle)
    browser.close()
    browser.switch_to.window(secound_tab)

    date_format = "%Y-%m-%d"
    # Get the current date

    # '//*[@id="Project_listView_row_1"]/td[5]/span[1]/span'
    for num in range(1, 11):
        startDate[num] = browser.find_element(By.XPATH, '//*[@id="Project_listView_row_' + str(
            num) + '"]/td[5]/span[1]/span').text
        actend[num] = browser.find_element(By.XPATH,
                                           '//*[@id="Project_listView_row_' + str(num) + '"]/td[6]/span[1]/span').text
        end[num] = browser.find_element(By.XPATH,
                                        '//*[@id="Project_listView_row_' + str(num) + '"]/td[7]/span[1]/span').text
        from_date = datetime.strptime(startDate[num], date_format)
        to_date = datetime.strptime(end[num], date_format)
        preduction_period[num] = to_date - from_date
        from_date = datetime.strptime(startDate[num], date_format)
        to_date = datetime.strptime(actend[num], date_format)
        actend[num] = to_date - from_date

    print("pass")
