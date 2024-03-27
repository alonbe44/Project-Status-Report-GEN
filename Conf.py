#  Copyright (c) 2024. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
# Global variables
size = 33
GREEN = "\033[32m"
RESET = "\033[0m"
RED = "\033[31m"
PASS = 0
FAIL = 0
username = "Abdelrahman.Rasem"
password = "20111940@A"
startDate = {}
actend = {}
end = {}
preduction_period = {}

def init():
    mp = {'project name': {1: 'Accudial call accounting - extension lic...', 2: 'SpeechLog Al Rajhi Bank',
                           3: 'Display line status /E911', 4: 'E911 (Caller Barring Status)',
                           5: 'E911 integration with XLM', 6: 'Maintenance Visit', 7: 'Orange – PPMD CR',
                           8: 'Speech Log expansion', 9: 'Provisioning Mediator (PM)', 10: 'IVR professional recording',
                           11: 'SpeechLog', 12: 'Speech log Recording', 13: 'Speech Log expansion- Soltek',
                           14: 'Speech Log Recorder (HA)', 15: 'Speech Log Expansion', 16: 'SpeechLog (34 IP)',
                           17: 'SpeechLog', 18: 'Social Security Investment Fund – Speech...', 19: 'Host Monitor',
                           20: 'Speech Log expansion Arab Bank', 21: 'Archiving Module including the decryptio...',
                           22: 'Speech Log Voice Recorder RHC', 23: 'SpeechLog (Expansion 4 Analog)',
                           24: 'SpeechLog (Expansion 8 IPs)'},
          'Engineer name': {1: 'Bilal Al-Noori', 2: 'Abdulrahman Hasan', 3: 'Hamzeh Shwemeh', 4: 'Hamzeh Shwemeh',
                            5: 'Hamzeh Shwemeh', 6: 'Bilal Al-Noori', 7: 'Yousif Rayyan', 8: 'Osama Gharbieh',
                            9: 'aladdin Shishani', 10: 'Osama Gharbieh', 11: 'CCE', 12: 'Abdulrahman Hasan',
                            13: 'Osama Gharbieh', 14: 'Bilal Al-Noori', 15: 'Bilal Al-Noori', 16: 'Abdulrahman Hasan',
                            17: 'Abdulrahman Hasan', 18: 'Abdulrahman Hasan', 19: 'Ahmad AlHasan', 20: 'Osama Gharbieh',
                            21: 'Abdellateef Ibrahim', 22: 'Abdulrahman Hasan', 23: 'CCE', 24: 'Abdulrahman Hasan'},
          'Related To': {1: 'Ministry of Tourism and Antiquities', 2: 'Al Rajhi Bank', 3: 'PSD', 4: 'Orange', 5: 'PSD',
                         6: 'Nabulsi - Burger Makers', 7: 'Orange Jo', 8: 'Housing Bank', 9: 'Orange Jo', 10: 'ISTD',
                         11: 'Unitel (Palace of Justice)', 12: 'Arab Bank', 13: 'Safwa Bank', 14: 'Housing Bank',
                         15: 'Housing Bank', 16: 'ABC BANK BH', 17: 'Al Rajhi Bank', 18: 'Social Security',
                         19: 'Extensya-SL', 20: 'Arab Bank', 21: 'Extensya-SL', 22: 'The Royal Hashemite Court (RHC)',
                         23: 'Global Telecommunication Technology (Alm...', 24: 'VTEL'},
          'status': {1: 'Completed', 2: 'In Progress', 3: 'Completed', 4: 'In Progress', 5: 'In Progress',
                     6: 'Completed', 7: 'Completed', 8: 'Completed', 9: 'Completed', 10: 'Completed', 11: 'On Hold',
                     12: 'Completed', 13: 'Completed', 14: 'Completed', 15: 'Completed', 16: 'Completed',
                     17: 'Archived', 18: 'Completed', 19: 'Completed', 20: 'Completed', 21: 'Completed',
                     22: 'Completed', 23: 'Completed', 24: 'Completed'},
          'Details': {1: 'Ab\nAbdelrahman Rasem\n2023-12-05 06:29 AM (12 days ago)',
                      2: 'Ab\nAbdelrahman Rasem\n2023-12-05 06:22 AM (12 days ago)',
                      3: 'Ab\nAbdelrahman Rasem\n2023-12-04 12:07 PM (12 days ago)',
                      4: 'Ab\nAbdelrahman Rasem\n2023-12-04 09:15 AM (13 days ago)',
                      5: 'Ab\nAbdelrahman Rasem\n2023-11-27 09:37 AM (20 days ago)',
                      6: 'Ab\nAbdelrahman Rasem\n2023-11-21 06:07 AM (26 days ago)',
                      7: 'Mo\nMohammad Farah\n2023-11-06 09:10 AM (1 month ago)',
                      8: 'Abdelrahman Rasem\n2023-11-01 12:08 PM (1 month ago)',
                      9: 'Mo\nMohammad Farah\n2023-10-22 06:32 AM (1 month ago)',
                      10: 'Abdelrahman Rasem\n2023-10-23 08:10 AM (1 month ago)',
                      11: 'Ab\nAbdelrahman Rasem\n2023-10-10 06:19 AM (2 months ago)',
                      12: 'Ab\nAbdelrahman Rasem\n2023-10-03 10:57 AM (2 months ago)',
                      13: 'Mohammad Farah\n2023-09-12 05:57 AM (3 months ago)',
                      14: 'Abdelrahman Rasem\n2023-08-29 06:16 AM (3 months ago)',
                      15: 'Abdelrahman Rasem\n2023-08-29 06:15 AM (3 months ago)',
                      16: 'Mo\nMohammad Farah\n2023-08-17 11:34 AM (4 months ago)',
                      17: 'Mo\nMohammad Farah\n2023-08-15 06:34 AM (4 months ago)',
                      18: 'Abdelrahman Rasem\n2023-06-26 11:20 AM (5 months ago)',
                      19: 'Ab\nAbdelrahman Rasem\n2023-06-22 09:47 AM (5 months ago)',
                      20: 'Abdelrahman Rasem\n2023-06-06 07:09 AM (6 months ago)',
                      21: 'Abdelrahman Rasem\n2023-06-11 08:36 AM (6 months ago)',
                      22: 'Ab\nAbdelrahman Rasem\n2023-04-10 10:22 AM (8 months ago)',
                      23: 'Mo\nMohammad Farah\n2023-02-22 08:52 AM (9 months ago)',
                      24: 'Mo\nMohammad Farah\n2023-01-23 3:20 PM (10 months ago)'},
          'Duration': {1: 49, 2: 84, 3: 81, 4: 59, 5: 101, 6: 21, 7: 55, 8: 42, 9: 49, 10: 35, 11: 59, 12: 56, 13: 54,
                       14: 42, 15: 42, 16: 40, 17: 395, 18: 56, 19: 56, 20: 35, 21: 26, 22: 56, 23: 58, 24: 31}}
    return mp