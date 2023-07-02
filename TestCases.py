import smtplib
# Author: Abedalrahman Rasem

import unittest
from datetime import datetime

from main import send_email

"""
Code Analysis

Objective:
The objective of the 'send_email' function is to send an email with an attachment. The function takes the filename of the attachment as input and sends an email to the specified recipient with the attachment.

Inputs:
The 'send_email' function takes a single input, which is the filename of the attachment to be sent.

Flow:
The 'send_email' function first creates a message object and sets the email details such as sender, recipient, and subject. It then attaches the specified file to the email and connects to the email server. The function starts a secure TLS connection, logs in to the email account, sends the email, and quits the email server connection.

Outputs:
The main output of the 'send_email' function is an email sent to the specified recipient with the specified attachment.

Additional aspects:
- The function checks if the specified attachment file exists before attaching it to the email.
- The function raises a 'FileNotFoundError' exception if the specified attachment file is not found.
- The function handles any other exceptions that may occur during the email sending process and raises them with additional information.
"""
class TestSendEmail(unittest.TestCase):
    #  Tests that an email is sent successfully
    def test_successful_email(self):
        try:
            send_email('test.txt')
        except:
            self.fail('An exception was raised')
        self.assertTrue(True)

    #  Tests that an error is raised when attachment file is not found
    def test_attachment_not_found(self):
        with self.assertRaises(FileNotFoundError):
            send_email('nonexistent_file.txt')

    #  Tests that an error is raised when there is an SMTP login error
    def test_smtp_login_error(self):
        with self.assertRaises(smtplib.SMTPAuthenticationError):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('globtesting0@gmail.com', 'wrong_password')
            send_email('test_attachment.txt')
            server.quit()

    #  Tests that email details (sender, recipient, subject) are set correctly
    def test_email_details(self):
        msg=send_email('test.txt')
        self.assertEqual(msg['From'], 'globtesting0@gmail.com')
        self.assertEqual(msg['To'], 'Abdelrahman.Rasem@globitel.com')
        self.assertEqual(msg['Subject'], 'Project Status ' + str(datetime.now().isocalendar()[1]) + ' 2023')




    def test_successful_email(self, mocker):
        mocker.patch('smtplib.SMTP')
        mocker.patch('smtplib.SMTP.starttls')
        mocker.patch('smtplib.SMTP.login')
        mocker.patch('smtplib.SMTP.send_message')
        mocker.patch('smtplib.SMTP.quit')
        send_email('test.txt')
        smtplib.SMTP.assert_called_once_with('smtp.gmail.com', 587)
        smtplib.SMTP.starttls.assert_called_once()
        smtplib.SMTP.login.assert_called_once_with('globtesting0@gmail.com', 'vfqmlzzwiubkyxlg')
        smtplib.SMTP.send_message.assert_called_once()
        smtplib.SMTP.quit.assert_called_once()



