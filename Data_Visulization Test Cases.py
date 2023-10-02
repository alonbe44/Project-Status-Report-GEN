import os
# Generated by CodiumAI

import unittest

import pandas as pd

from data import Data_Visualization


class TestDataVisualization(unittest.TestCase):

    #  Generates all visualizations for valid input data.
    def test_generates_all_visualizations_for_valid_input_data(self):
        map_data =pd.DataFrame( {'project name': {1: 'Speech Log expansion', 2: 'PMP (Expansion Telesales)',
                       3: 'SpeechLog (Screen Capture, 27 Licenses)', 4: 'SpeechLog', 5: 'SpeechLog (30 IP)',
                       6: 'RQMS on SAS', 7: 'SpeechLog Retail Zain KW (POC)', 8: 'Speech Log Recorder House Bank',
                       9: 'SpeechLog Voice Recording (IP) Kalaam', 10: 'Move 4 licenses to new server',
                       11: 'SpeechLog (Backup Recorder)', 12: 'SpeechLog (20 IP)', 13: 'Accudial (Upgrade)',
                       14: 'SpeechLog Al Rajhi Bank', 15: 'E911 integration with XLM',
                       16: 'E911 (Caller Barring Status)', 17: 'LTE, ITS & RS Upgrade',
                       18: 'Data Rating and Charging (Redundancy)', 19: 'Customer Order (Phase II)',
                       20: 'VAS Sub-charging CR', 21: 'MLC Upgrade', 22: 'Enabling-4G', 23: 'USSD GW Upgrade & CR',
                       24: 'SpeechLog (34 IP)', 25: 'JRM – E1 Recorder', 26: 'SpeechLog',
                       27: 'Roaming (Links Migration to HSL)', 28: 'Speech Analytics (POC)'},
      'Engineer name': {1: 'Nabeel Nusair', 2: 'Abdellateef Ibrahim', 3: 'Ahmad AlHasan', 4: 'Ahmad AlHasan',
                        5: 'Ahmad AlHasan', 6: 'Mohammad Alalami', 7: 'Tamer Wathaifi', 8: 'Bilal Al-Noori',
                        9: 'Hamzeh Shwemeh', 10: 'Bilal Al-Noori', 11: 'Abdulrahman Hasan', 12: 'Abdulrahman Hasan',
                        13: 'Abdulrahman Hasan', 14: 'Abdulrahman Hasan', 15: 'Hamzeh Shwemeh', 16: 'Hamzeh Shwemeh',
                        17: 'Yousef Mishael', 18: 'aladdin Shishani', 19: 'Khairy Khdeir', 20: 'Laith Al-Janaideh',
                        21: 'Zaid Hina', 22: 'Khairy Khdeir', 23: 'Zaid Hina', 24: 'Abdulrahman Hasan',
                        25: 'Abdulrahman Hasan', 26: 'Abdulrahman Hasan', 27: 'Yousef Mishael', 28: 'Nabeel Nusair',
                        },
      'Related To': {1: 'Earth Link', 2: 'Zain Jordan', 3: 'Zain Jordan', 4: 'Takamol (Switch IRAQ)',
                     5: 'Takamol (ALghanim)', 6: 'Etisalat UAE', 7: 'Zain KW', 8: 'Housing Bank', 9: 'Kalaam',
                     10: 'Metropolitan (Cinnamon Lakeside Colombo)', 11: 'Arab Bank',
                     12: 'Jordan Commercial Bank (JCB)', 13: 'Housing Bank', 14: 'Al Rajhi Bank', 15: 'PSD',
                     16: 'Orange', 17: 'Ufone', 18: 'TeleCel', 19: 'Asiacell', 20: 'Golis Somalia', 21: 'Zain Jordan',
                     22: 'Asiacell', 23: 'Zain Jordan', 24: 'ABC BANK BH', 25: 'JRM', 26: 'Al Rajhi Bank', 27: 'Ufone',
                     28: 'Zain Iraq'},
      'status': {1: 'Initiated', 2: 'Waiting for Feedback', 3: 'In Progress', 4: 'In Progress', 5: 'In Progress',
                 6: 'In Progress', 7: 'In Progress', 8: 'Initiated', 9: 'In Progress', 10: 'On Hold', 11: 'On Hold',
                 12: 'In Progress', 13: 'In Progress', 14: 'In Progress', 15: 'On Hold', 16: 'On Hold',
                 17: 'In Progress', 18: 'In Progress', 19: 'In Progress', 20: 'In Progress', 21: 'In Progress',
                 22: 'In Progress', 23: 'In Progress', 24: 'In Progress', 25: 'In Progress', 26: 'In Progress',
                 27: 'On Hold', 28: 'On Hold'},
      'Details': {1: 'No comments',
                  2: 'Ab\nAbdelrahman Rasem\n2023-07-03 12:08 PM (17 hours ago)\nwaiting from commercial .\n ',
                  3: 'Ab\nAbdelrahman Rasem\n2023-07-03 12:07 PM (17 hours ago)\n\nwe took new package from dev and'
                     'we are still testing with development.\n ',
                  4: 'Ab\nAbdelrahman Rasem\n2023-07-03 12:06 PM (17 hours ago)\nwe had sent reminder waiting for '
                     'client.\n ',
                  5: 'Ab\nAbdelrahman Rasem\n2023-07-03 12:05 PM (17 hours ago)\n\n ',
                  6: 'Ab\nAbdelrahman Rasem\n2023-07-03 11:37 AM (18 hours ago)\n\nwe are waiting onside '
                     'implementation to be ready,\n ',
                  7: 'Ab\nAbdelrahman Rasem\n2023-07-03 11:36 AM (18 hours ago)\nthe client had sent feedback on '
                     'reports we will replay ASAP.\n ',
                  8: 'Ab\nAbdelrahman Rasem\n2023-07-03 11:33 AM (18 hours ago)\nwe are preparing the SRD.\n ',
                  9: 'Ha\nHamzeh Shwemeh\n2023-07-03 11:34 AM (18 hours ago)\nWe have completed the installation '
                     'based on the agreement to support CSTAIII-SPAN\n ',
                  10: 'Ab\nAbdelrahman Rasem\n2023-07-03 11:29 AM (18 hours ago)\n\ncontact with Sales .@Osama '
                      'Hammouh \n ',
                  11: 'Ab\nAbdelrahman Rasem\n2023-07-03 11:23 AM (18 hours ago)\n\nwe will contact the client,\n ',
                  12: 'Ab\nAbdelrahman Rasem\n2023-07-03 11:17 AM (18 hours ago)\n\n ',
                  13: 'Ab\nAbdelrahman Rasem\n2023-07-03 11:09 AM (18 hours ago)\nWe did recover the DB, still we '
                      'need to check with Development (Migration script for notification ). \n ',
                  14: 'Ab\nAbdelrahman Rasem\n2023-07-03 11:05 AM (18 hours ago)\nwe need to install 2 recorder in '
                      'the test tomorrow.\n ',
                  15: 'Ab\nAbdelrahman Rasem\n2023-07-03 09:41 AM (20 hours ago)\nwaiting for Orange to provide us '
                      'with XLM ,\n ',
                  16: 'Ab\nAbdelrahman Rasem\n2023-07-03 09:38 AM (20 hours ago)\nWaiting for PSD  PO.\n ',
                  17: 'Ab\nAbdelrahman Rasem\n2023-07-03 09:35 AM (20 hours ago)\nRS internal testing completed , '
                      'The updated UI added , Operation will be arranged .\n ',
                  18: 'Ab\nAbdelrahman Rasem\n2023-07-03 09:28 AM (20 hours ago)\nwe had activated the OS, '
                      'DB licenses our team will arrange with the client to sync DB.\n ',
                  19: 'Ab\nAbdelrahman Rasem\n2023-07-03 09:26 AM (20 hours ago)\nwe are having a meeting today with '
                      'Thaer also will send a status update.\n ',
                  20: 'Ab\nAbdelrahman Rasem\n2023-07-03 09:25 AM (20 hours ago)\nwe are supposed to send a reminder '
                      'today. \n ',
                  21: 'Ab\nAbdelrahman Rasem\n2023-07-03 09:24 AM (20 hours ago)\nwaiting for development , '
                      'also to check with commercial. \n ',
                  22: 'Ab\nAbdelrahman Rasem\n2023-07-03 09:11 AM (20 hours ago)\n\n \n \n ',
                  23: 'Mo\nMohammad Farah\n2023-07-03 07:52 AM (21 hours ago)\nUAT will start today.\n ',
                  24: 'Ab\nAbdelrahman Rasem\n2023-07-02 06:40 AM (1 day ago)\nthe client is asking for a handover '
                      'documentation, but we are pushing to get the PAC first so we are waiting for client '
                      'feedback.\n ',
                  25: 'Ab\nAbdelrahman Rasem\n2023-07-02 06:31 AM (1 day ago)\nwe had sent the PAC for the client '
                      'Before EID at 25/6/2023 still waiting for Feedback.\n ',
                  26: 'Mo\nMohammad Farah\n2023-05-22 09:02 AM (1 month ago)\n\nTesting in Main site will begin '
                      'tomorrow.\n\nIn regard to HA and DR, we are waiting for Rajhi Bank to provide the needed '
                      'requirements (site is not ready).\n ',
                  27: 'Mo\nMohammad Farah\n2023-02-21 07:47 AM (4 months ago)\nA plan was submitted to Ufone on '
                      'transferring the server in ISB to KHI, also the commercial team shall submit their offerings\n ',
                  28: 'Mo\nMohammad Farah\n2022-12-12 11:57 AM (6 months ago)\nOn hold, till we finalize RQM POC.\n ',
                  },
      'Duration': {1: 42, 2: 79, 3: 107,
                   4: 59, 5: 19, 6: 46,
                   7: 56, 8: 42, 9: 21,
                   10: 29, 11: 87, 12: 76,
                   13: 61, 14: 84, 15: 101,
                   16: 59, 17: 72, 18: 306,
                   19: 382, 20: 22, 21: 92,
                   22: 84, 23: 61, 24: 40,
                   25: 56, 26: 153, 27: 81,
                   28: 118},
      'DEP': {1: 'CCS',
              2: 'CCS',
              3: 'CCS',
              4: 'CCS',
              5: 'CCE',
              6: 'CCE',
              7: 'CCE',
              8: 'CCE',
              9: 'CCE',
              10: 'CCE',
              11: 'CCS',
              12: 'OS',
              13: 'OS',
              14: 'OS',
              15: 'OS',
              16: 'OS',
              17: 'OS',
              18: 'OS',
              19: 'OS',
              20: 'CCS',
              21: 'CCE',
              22: 'CCE',
              23: 'OS',
              24: 'CCE',
              25: 'OS',
              26: 'CCE',
              27: 'CCS',
              28: 'OS'}
      })
    
        result = Data_Visualization(map_data)
    
        self.assertEqual(result, "Data visualization completed successfully")

    #  Saves all generated plots successfully.
    def test_saves_all_generated_plots_successfully(self):
        map_data = [
            {'status': 'Completed', 'Related To': 'A', 'Duration': 10, 'Engineer name': 'John', 'DEP': 'Sales'},
            {'status': 'In Progress', 'Related To': 'B', 'Duration': 15, 'Engineer name': 'Jane', 'DEP': 'Marketing'},
            {'status': 'Completed', 'Related To': 'C', 'Duration': 20, 'Engineer name': 'John', 'DEP': 'Sales'},
            {'status': 'In Progress', 'Related To': 'D', 'Duration': 25, 'Engineer name': 'Jane', 'DEP': 'Marketing'}
        ]
    
        result = Data_Visualization(map_data)
    
        self.assertEqual(result, "Data visualization completed successfully")
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'Diagrams', 'project_status_bar_chart.png')))
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'Diagrams', 'related_to_pie_chart.png')))
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'Diagrams', 'project_duration_histogram.png')))
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'Diagrams', 'project_duration_box_plot.png')))
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'Diagrams', 'count_of_projects_by_engineer.png')))
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'Diagrams', 'project_duration_over_time_line_chart.png')))
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'Diagrams', 'pair_plot.png')))
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'Diagrams', 'project_duration_by_department_violin_plot.png')))
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'Diagrams', 'project_status_by_engineer_stacked_bar_chart.png')))

    #  Returns a success message for valid input data.
    def test_returns_success_message_for_valid_input_data(self):
        map_data = [
            {'status': 'Completed', 'Related To': 'A', 'Duration': 10, 'Engineer name': 'John', 'DEP': 'Sales'},
            {'status': 'In Progress', 'Related To': 'B', 'Duration': 15, 'Engineer name': 'Jane', 'DEP': 'Marketing'},
            {'status': 'Completed', 'Related To': 'C', 'Duration': 20, 'Engineer name': 'John', 'DEP': 'Sales'},
            {'status': 'In Progress', 'Related To': 'D', 'Duration': 25, 'Engineer name': 'Jane', 'DEP': 'Marketing'}
        ]
    
        result = Data_Visualization(map_data)
    
        self.assertEqual(result, "Data visualization completed successfully")

    #  Returns a success message for empty input data.
    def test_returns_success_message_for_empty_input_data(self):
        map_data = []
    
        result = Data_Visualization(map_data)
    
        self.assertEqual(result, "Data visualization completed successfully")

    #  Returns an error message for invalid input data.
    def test_returns_error_message_for_invalid_input_data(self):
        map_data = [
            {'status': 'Completed', 'Related To': 'A', 'Duration': 10, 'Engineer name': 'John'},
            {'status': 'In Progress', 'Related To': 'B', 'Duration': 15, 'Engineer name': 'Jane'},
            {'status': 'Completed', 'Related To': 'C', 'Duration': 20, 'Engineer name': 'John'},
            {'status': 'In Progress', 'Related To': 'D', 'Duration': 25, 'Engineer name': 'Jane'}
        ]
    
        result = Data_Visualization(map_data)
    
        self.assertEqual(result, "Data visualization failed")

    #  Handles exceptions while generating visualizations.
    def test_handles_exceptions_while_generating_visualizations(self):
        map_data = [
            {'status': 'Completed', 'Related To': 'A', 'Duration': 10, 'Engineer name': 'John', 'DEP': 'Sales'},
            {'status': 'In Progress', 'Related To': 'B', 'Duration': 15, 'Engineer name': 'Jane', 'DEP': 'Marketing'},
            {'status': 'Completed', 'Related To': 'C', 'Duration': 20, 'Engineer name': 'John', 'DEP': 'Sales'},
            {'status': 'In Progress', 'Related To': 'D', 'Duration': 25, 'Engineer name': 'Jane', 'DEP': 'Marketing'}
        ]
    
        result = Data_Visualization(map_data)
    
        self.assertEqual(result, "Data visualization failed")
