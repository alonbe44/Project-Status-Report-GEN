import os
from datetime import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from multiprocessing import context
from unittest.mock import MagicMock

from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt, RGBColor, Inches
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from docx import Document
from selenium.webdriver.edge.options import Options

# Global variables
size = 33
GREEN = "\033[32m"
RESET = "\033[0m"
RED = "\033[31m"
PASS = 0
FAIL = 0
username = "Abdelrahman.Rasem"
password = "20111940@A"
os.environ['PATH'] += r"C:\Users\Abdelrahman.Rasem\Downloads\edgedriver_win64 (1)\msedgedriver.exe"


def send_email(fn):
    """
    Sends an email with an attachment.

    Args:
        fn (str): The filename of the attachment to be sent.

    """
    try:
        # Create a message object
        msg = MIMEMultipart()

        # Get the current week of the year
        weekemail = str(datetime.now().isocalendar()[1])

        # Set email details (sender, recipient, subject)
        msg['From'] = 'globtesting0@gmail.com'
        #msg['To'] = 'Mohammad.Farah@globitel.com'
        msg['To'] = 'Abdelrahman.Rasem@globitel.com'
        # Add CC recipients
        #msg['CC'] = 'Abdelrahman.Rasem@globitel.com'

        # Set the subject of the email
        msg['Subject'] = 'Project Status ' + weekemail + ' 2023'


        # Attach the file to the email
        filename2email = fn
        attachment = open(filename2email, 'rb')


        # Create a MIMEBase object to represent the attachment
        part = MIMEBase('application', 'octet-stream')

        # Read the attachment file and encode it using base64
        part.set_payload(attachment.read())
        encoders.encode_base64(part)

        # Set the header for the attachment
        part.add_header('Content-Disposition', f'attachment; filename="{filename2email}"')

        # Attach the attachment to the email message
        msg.attach(part)

        # Connect to the email server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # Start a secure TLS connection
        server.starttls()

        # Login to the email account
        server.login('globtesting0@gmail.com', 'vfqmlzzwiubkyxlg')

        # Send the email
        server.send_message(msg)

        # Quit the email server connection
        server.quit()
        return msg

    except Exception as error:
        #print("An error occurred:", error)
        print(type(error).__name__)
        # Additional code to handle or raise the exception as needed
        raise error
        #print("Error message:", str(error))

# Objective: The Gen_Document function aims to generate a Word document containing a table with project status
# information. The function takes a hash map as input, which contains project details such as project name,
# engineer name, related information, status, and comments. The function highlights the rows of the table based on
# the status value and saves the document with a filename that includes the current week number.
#
# Inputs: - mp: a hash map containing project details such as project name, engineer name, related information,
# status, and comments.
#
# Flow:
# 1. Create a new Word document.
# 2. Add a header to the document with the title "Globitel Project Status Report" and the current date.
# 3. Create a table with headers for project name, engineer name, related information, status, and comments.
# 4. Iterate over the hash map and add data to the table.
# 5. Highlight rows based on the status value.
# 6. Save the document with a filename that includes the current week number.
# 7. Modify the page size for landscape orientation.
# 8. Adjust the width of the last column in the table.
# 9. Save the modified document.
#
# Outputs:
# - A Word document containing a table with project status information.
# - The document is saved with a filename that includes the current week number.
#
# Additional aspects:
# - The function uses the docx library to create and modify Word documents.
# - The function uses RGBColor to set the font color of the status cell based on the status value.
# - The function assumes that the table is the first and only table in the document.
# - The function adjusts the width of the last column in the table to 4 inches.


def Gen_Document(mp):
    # Create a new Word document
    doc = Document()

    # Add a header to the document
    header = doc.sections[0].header
    header_paragraph = header.paragraphs[0]
    header_paragraph.text = "Globitel Project Status Report"
    header_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    header_paragraph.style = doc.styles["Heading 1"]

    # Add the current date on the left side of the header
    date_paragraph = header.add_paragraph()
    date_paragraph.text = datetime.now().strftime("%B %d, %Y")
    date_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

    # Create a table with headers
    table = doc.add_table(rows=1, cols=5)
    table.style = 'Table Grid'
    header_cells = table.rows[0].cells
    header_cells[0].text = 'project name'
    header_cells[1].text = 'Engineer name'
    header_cells[2].text = 'Related To'
    header_cells[3].text = 'status'
    header_cells[4].text = 'Comments'

    # Set the header cells' formatting
    for cell in header_cells:
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(12)

    status_cell = table.cell(0, 4)
    status_cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    status_cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    status_cell.paragraphs[0].runs[0].bold = True
    status_cell.paragraphs[0].runs[0].font.size = Pt(12)
    status_cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 0, 0)  # Red color

    # Iterate over the hash map and add data to the table
    for number in range(1, size):
        row_cells = table.add_row().cells
        row_cells[0].text = mp['project name'].get(number,
                                                   '')  # Get project name, defaulting to empty string if not found
        row_cells[1].text = mp['Engineer name'].get(number,
                                                    '')  # Get engineer name, defaulting to empty string if not found
        row_cells[2].text = mp['Related To'].get(number,
                                                 '')  # Get engineer name, defaulting to empty string if not found
        row_cells[3].text = mp['status'].get(number, '')  # Get status, defaulting to empty string if not found
        row_cells[4].text = mp['Details'].get(number, '')

    # Highlight rows based on the status value
    for row in table.rows:
        status_cell = row.cells[3]
        status = status_cell.text.strip().lower()

        # Define the highlighting color based on the status value
        if status == 'in progress':
            highlight_color = RGBColor(0, 0, 255)  # Blue
        elif status == 'completed':
            highlight_color = RGBColor(0, 255, 0)  # Green
        elif status == 'on hold':
            highlight_color = RGBColor(255, 0, 0)  # Red
        elif status == 'Initiated':
            highlight_color = RGBColor(64, 64, 64)  # Gray
        else:
            highlight_color = RGBColor(64, 64, 64)  # Gray

        if highlight_color:
            status_cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            status_cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            status_cell.paragraphs[0].runs[0].bold = True
            status_cell.paragraphs[0].runs[0].font.size = Pt(12)
            status_cell.paragraphs[0].runs[0].font.color.rgb = highlight_color

    current_week = str(datetime.now().isocalendar()[1])
    filename = 'Project Status Week ' + current_week + ' 2023.docx'
    doc.save(filename)

    # Open the Word document
    doc = Document(filename)

    # Get the first section of the document
    section = doc.sections[0]

    # Modify the page size for landscape orientation
    section.page_width = Pt(792)  # Set the width to 11 inches (792 points)
    section.page_height = Pt(612)  # Set the height to 8.5 inches (612 points)

    # Assuming the table is the first and only table in the document
    table = doc.tables[0]

    # Get the last column index
    last_column_index = len(table.columns) - 1

    # Iterate over the cells in the last column and adjust the width
    for row in table.rows:
        cell = row.cells[last_column_index]
        cell.width = Inches(4)  # Adjust the width as needed

    # Save the modified document
    doc.save(filename)

# Objective: The objective of the function is to collect data from a web page, create a Word document, and highlight
# rows in the table based on the status value. The function also prints the number of passed and failed projects and
# sends an email if all projects have passed.
#
# Inputs:
# - None
#
# Flow:
# 1. Create an EdgeOptions object and a new instance of the Edge driver.
# 2. Navigate to the login page and enter the username and password.
# 3. Open a new tab and navigate to a new page.
# 4. Find the project details and add them to a hash map.
# 5. Highlight rows based on the status value.
# 6. Generate a Word document with the project details and save it.
# 7. Modify the page size for landscape orientation.
# 8. Close the browser window.
#
# Outputs:
# - A Word document with the project details.
# - The number of passed and failed projects.
# - An email sent if all projects have passed.
#
# Additional aspects:
# - The function uses the Selenium and docx libraries.
# - The function uses global variables for the username, password, PASS, FAIL, GREEN, RED, RESET, and size.
# - The function uses a try-except block to handle exceptions when finding project details.
# - The function uses a delay of 3 seconds between finding project details.
# - The function uses the send_email() function to send an email.
def Collect_Data():
    global PASS, FAIL, username, password, GREEN, RED, RESET, size
    # Create EdgeOptions object
    options = Options()

    # Add headless argument
    # options.add_argument('--headless')

    # Set the path to the Microsoft Edge WebDriver
    # Replace "path/to/edge/driver" with the actual path on your system

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
        "https://supportcrm.globitel.com/index.php?module=Project&parent=&page=&view=List&viewname=297&orderby"
        "=&sortorder"
        "=&app=MARKETING&tag_params=%5B%5D&nolistcache=0&list_headers=&tag=")
    # Open a new tab and navigate to a new page
    browser.execute_script(
        "window.open('https://supportcrm.globitel.com/index.php?module=Project&parent=&page=&view=List&viewname=297"
        "&orderby=&sortorder=&app=MARKETING&tag_params=%5B%5D&nolistcache=0&list_headers=&tag=',"
        "'_blank')")

    actions = ActionChains(browser)
    actions.send_keys(Keys.END).perform()

    # listopen=browser.find_element(By.CLASS_NAME, "app-icon fa fa-bars")

    # Find all buttons on the page by their tag name
    secound_tab = browser.window_handles[1]

    browser.switch_to.window(first_tab_handle)
    browser.close()
    browser.switch_to.window(secound_tab)

    print("---------------------------------- target elem --------------------------------")

    mp = {'project name': {}, 'Engineer name': {}, 'Related To': {}, 'status': {}, 'Details': {}}

    i = 9
    size = int(
        browser.find_element(By.XPATH, '//*[@id="listview-actions"]/div/div[3]/div/span/span[1]').text.split(' to ')[
            1]) + 1
    print("Starting Test on Total project size = ", size)

    for number in range(1, size):
        time.sleep(3)  # Add a delay of 3 seconds
        mp['project name'][number] = browser.find_element(By.XPATH,
                                                          '//*[@id="Project_listView_row_' + str(
                                                              number) + '"]/td[2]').text
        try:
            mp['Engineer name'][number] = browser.find_element(By.XPATH,
                                                               '//*[@id="Project_listView_row_' + str(
                                                                   number) + '"]/td[4]').text
            if mp['Engineer name'][number] == "":
                print("Engineer name is empty")

            mp['Related To'][number] = browser.find_element(By.XPATH,
                                                            '//*[@id="Project_listView_row_' + str(
                                                                number) + '"]/td[8]').text
            if mp['Related To'][number] == "":
                print("Related To is empty")

            mp['status'][number] = browser.find_element(By.XPATH,
                                                        '//*[@id="Project_listView_row_' + str(
                                                            number) + '"]/td[6]').text

            if mp['status'][number] == "":
                print("status is empty")

            browser.find_element(By.XPATH, '//*[@id="Project_listView_row_' + str(
                number) + '"]/td[1]/div/span[2]/a').click()

        except:
            print("project : ", mp['project name'][number], RED + "FAIL" + RESET)
            FAIL = FAIL + 1
            continue

        time.sleep(3)  # Add a delay of 3 seconds
        try:
            mp['Details'][number] = browser.find_element(By.XPATH,
                                                         '//*[@id="detailView"]/div/div/div/div[2]/div/div['
                                                         '3]/div/div[1]').text
            if mp['Details'][number] == "":
                print("Details is empty")

            browser.find_element(By.XPATH,
                                 '//*[@id="mCSB_' + str(i) + '_container"]/div[1]/div[2]/button').click()
        except:
            print("project : ", mp['project name'][number], RED + "FAIL" + RESET)
            FAIL = FAIL + 1
            continue

        i = i + 1
        print("project : ", mp['project name'][number], GREEN + "PASS" + RESET)
        PASS = PASS + 1

        if number > 3:
            browser.execute_script("arguments[0].scrollIntoView(true);",
                                   browser.find_element(By.XPATH, '//*['
                                                                  '@id="Project_listView_row_' + str(
                                       number - 3) + '"]/td[1]'))

    print(GREEN + "PASS: " + RESET, PASS, "/", size - 1)
    print(RED + "FAIL: " + RESET, FAIL, "/", size - 1)

    Gen_Document(mp)
    if PASS == size - 1:
        print("Sending Email....")
        # uncomment the next line to send email
        # send_email(filename)
    # #Schedule the email to be sent every day at 9:00 AM
    # schedule.every().week.monday.at('01:00').do(lambda: send_email("Project Status Week 24 2023.docx"))
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

    # Close the browser window
    browser.quit()


Collect_Data()
