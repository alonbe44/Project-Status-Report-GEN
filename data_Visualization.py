import logging
from datetime import datetime, timedelta


#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Example Data usage


# mp = {
#     2019: {'project name':
#     {1: 'PMP', 2: 'Raoming upgrade', 3: 'LBS (Enhancement CR)', 4: 'SpeechLog (Expansion)', 5: 'SpeechLog (Expansion)', 6: 'SpeechLog', 7: 'USSD GW CR (CGI and IMEI injection)'}, 'Engineer name': {1: 'Abdallah Halaweh', 2: 'Abdallah Halaweh', 3: 'Mohammad Farah', 4: 'CCE', 5: 'CCE', 6: 'CCE', 7: 'Mohammad Farah'}, 'Related To': {1: 'Raya', 2: 'Asiacell', 3: 'Lebara KSA', 4: 'MenaITech', 5: 'Tawasol (Voitech Solutions)', 6: 'Tawasol (FAMA)', 7: 'Asiacell'}, 'status': {1: 'Completed', 2: 'Completed', 3: 'Completed', 4: 'Archived', 5: 'Archived', 6: 'Archived', 7: 'Completed'}, 'Details': {1: 'Ab\nAbdallah Halaweh\n2021-11-23 2:43 PM (2 years ago)', 2: 'Wi\nWisam Ammori\n2021-07-29 12:13 PM (2 years ago)', 3: 'Mo\nMohammad Farah\n2020-09-24 10:38 AM (3 years ago)', 4: 'Mo\nMohammad Farah\n2021-07-05 11:06 AM (2 years ago)', 5: 'Mo\nMohammad Farah\n2021-07-05 11:05 AM (2 years ago)', 6: 'Mo\nMohammad Farah\n2021-07-05 11:04 AM (2 years ago)', 7: 'Mo\nMohammad Farah\n2020-10-19 11:46 AM (3 years ago)'}, 'Duration': {1: datetime.timedelta(days=968), 2: datetime.timedelta(days=460), 3: datetime.timedelta(days=462), 4: datetime.timedelta(days=1629), 5: datetime.timedelta(days=1595), 6: datetime.timedelta(days=1734), 7: datetime.timedelta(days=425)}, 'DEP': {1: 'CCS', 2: 'OS', 3: 'OS', 4: 'CCE', 5: 'CCE', 6: 'CCE', 7: 'OS'}},
#     2020:{'project name': {1: 'Video call', 2: 'SpeechLog (Upgrade to V7.x)', 3: 'SpeechLog Retail (RQM)', 4: 'RBT (Expansion & CRs)', 5: 'USSD Virtualization & ATI GW', 6: 'RQM (CRs)', 7: 'SpeechLog (Upgrade to 7.x)', 8: 'Collect Call (CAP4)', 9: 'USSD (Upgrade V3.7)', 10: 'SpeechLog (Upgrade to 7.x and DR site)', 11: 'SpeechLog', 12: 'SpeechLog', 13: 'SpeechLog (Upgrade to 7.x)', 14: 'SpeechLog (Expansion "16 Ports")', 15: 'SpeechLog (Expansion)', 16: 'E911 & SpeechLog Upgrade', 17: 'Concurrent Recording (POC)', 18: 'SpeechLog (Upgrade to 7.x)', 19: 'SpeechLog (Upgrade V7.x)', 20: 'SpeechLog (Maintenance Visit)', 21: 'Roaming & VAS (Upgrade & Migration)', 22: 'SpeechLog (Upgrade to 7.x)', 23: 'RQM (POC)', 24: 'E911 (Expansion and HW modernization)', 25: 'Virtual Shop (POC)', 26: 'Virtual Shop (POC)', 27: 'SpeechLog (Expansion 40 Ports)', 28: 'RQM (Expansion 90 Licenses)', 29: 'SpeechLog (Public)', 30: 'Speech Analytics (POC)', 31: 'Accudial (Upgrade)', 32: 'SpeechLog (Digital 8 Ports)', 33: 'SpeechLog (Expansion)', 34: 'SpeechLog (Upgrade to 7.x)', 35: 'SpeechLog (Temp. License "WFH Agents)', 36: 'SpeechLog (Expansion 6 IPs)', 37: 'SpeechLog (Expansion 43 Ports)', 38: 'RQM (POC)', 39: 'SpeechLog (Expansion 30 IPs)', 40: 'SpeechLog (Expansion "2 Ports")'}, 'Engineer name': {1: 'Hamzeh Shwemeh', 2: 'Nabeel Nusair', 3: 'Abdallah Halaweh', 4: 'Mohammad Farah', 5: 'Laith Al-Janaideh', 6: 'Mohammad Al-Mahrok', 7: 'Tamer Wathaifi', 8: 'Mohammad Khalil', 9: 'Laith Al-Janaideh', 10: 'Ahmad AlHasan', 11: 'Mohammad Farah', 12: 'CCE', 13: 'CCE', 14: 'Mohammad Farah', 15: 'CCE', 16: 'Mohammad Farah', 17: 'Mohammad Farah', 18: 'Abdulrahman Hasan', 19: 'Mohammad Farah', 20: 'Abdulrahman Hasan', 21: 'Mohammad Farah', 22: 'Mohammad Hamaideh', 23: 'Mohammad Hamaideh', 24: 'Mohammad Khalil', 25: 'CCE', 26: 'CCE', 27: 'Mohammad Farah', 28: 'Mohammad Alalami', 29: 'Mohammad Farah', 30: 'Mohammad Farah', 31: 'Tamer Wathaifi', 32: 'CCE', 33: 'Mohammad Farah', 34: 'Abdulrahman Hasan', 35: 'CCE', 36: 'Tamer Wathaifi', 37: 'CCE', 38: 'Mohammad Farah', 39: 'Mohammad Farah', 40: 'Mohammad Farah'}, 'Related To': {1: 'PSD', 2: 'QualityNet', 3: 'Mobily KSA', 4: 'Sabafon', 5: 'Asiacell', 6: 'Etisalat UAE', 7: 'Bank of Jordan', 8: 'Sabafon', 9: 'MTN_Yemen', 10: 'Infoline (Bank Muscat)', 11: 'Qaizer Colombo Wala -DWP', 12: 'JRM (MOI)', 13: 'Bank Audi', 14: 'Umniah', 15: 'KHCC-JBS', 16: 'PSD', 17: 'Reach', 18: 'JEPCO', 19: 'Intelcom (RCAR)', 20: 'Tamweelcom', 21: 'MTN_Sudan', 22: 'GIH', 23: 'Orange Jo', 24: 'Orange Jo', 25: 'Batelco', 26: 'Invest Bank', 27: 'Zain Jordan', 28: 'Etisalat UAE', 29: 'Reach', 30: 'Reach', 31: 'Artelco (JWICO)', 32: 'ATCOM', 33: 'STC', 34: 'JKB', 35: 'JEPCO', 36: 'Unitel (Ajyad)', 37: 'JEFB', 38: 'STC', 39: 'Extensya-SL', 40: 'Umniah'}, 'status': {1: 'On Hold', 2: 'Archived', 3: 'Archived', 4: 'Archived', 5: 'Completed', 6: 'Completed', 7: 'Archived', 8: 'Completed', 9: 'Completed', 10: 'Completed', 11: 'Completed', 12: 'Completed', 13: 'Completed', 14: 'Completed', 15: 'Completed', 16: 'Completed', 17: 'Completed', 18: 'Completed', 19: 'Completed', 20: 'Completed', 21: 'Completed', 22: 'Completed', 23: 'Completed', 24: 'Completed', 25: 'Completed', 26: 'Completed', 27: 'Completed', 28: 'Completed', 29: 'Completed', 30: 'Completed', 31: 'Completed', 32: 'Completed', 33: 'Completed', 34: 'Completed', 35: 'Completed', 36: 'Completed', 37: 'Completed', 38: 'Completed', 39: 'Completed', 40: 'Completed'}, 'Details': {1: 'Abdelrahman Rasem\n2023-08-21 12:14 PM (4 months ago)', 2: 'Mo\nMohammad Farah\n2023-03-06 1:40 PM (10 months ago)', 3: 'Mo\nMohammad Farah\n2023-01-03 06:22 AM (1 year ago)', 4: 'Mo\nMohammad Farah\n2022-11-30 08:04 AM (1 year ago)', 5: 'Mo\nMohammad Farah\n2022-08-01 08:37 AM (1 year ago)', 6: 'Mo\nMohammad Farah\n2022-07-26 07:52 AM (1 year ago)', 7: 'Mo\nMohammad Farah\n2022-06-01 10:10 AM (1 year ago)', 8: 'Mo\nMohammad Farah\n2022-02-28 09:11 AM (1 year ago)', 9: 'Mo\nMohammad Farah\n2022-02-01 10:40 AM (1 year ago)', 10: 'Mo\nMohammad Farah\n2021-12-27 11:08 AM (2 years ago)', 11: 'Mo\nMohammad Farah\n2021-09-28 09:58 AM (2 years ago)', 12: 'Mo\nMohammad Farah\n2020-11-01 1:55 PM (3 years ago)', 13: 'Mo\nMohammad Farah\n2020-10-13 09:22 AM (3 years ago)', 14: 'Mo\nMohammad Farah\n2020-10-08 09:25 AM (3 years ago)', 15: 'Mo\nMohammad Farah\n2020-12-29 07:20 AM (3 years ago)', 16: 'Mo\nMohammad Farah\n2021-03-30 12:20 PM (2 years ago)', 17: 'Mo\nMohammad Farah\n2021-07-07 11:00 AM (2 years ago)', 18: 'Wi\nWisam Ammori\n2021-06-30 11:16 AM (2 years ago)', 19: 'Mo\nMohammad Farah\n2021-01-27 12:29 PM (2 years ago)', 20: 'No comments', 21: 'Mo\nMohammad Farah\n2021-03-07 08:15 AM (2 years ago)', 22: 'Mo\nMohammad Farah\n2021-07-07 11:40 AM (2 years ago)', 23: 'Mo\nMohammad Farah\n2021-03-10 12:56 PM (2 years ago)', 24: 'Mo\nMohammad Farah\n2021-03-03 12:40 PM (2 years ago)', 25: 'Mo\nMohammad Farah\n2021-05-30 10:24 AM (2 years ago)', 26: 'Mo\nMohammad Farah\n2021-05-30 10:25 AM (2 years ago)', 27: 'Mo\nMohammad Farah\n2021-07-07 11:06 AM (2 years ago)', 28: 'Mo\nMohammad Farah\n2021-06-15 12:18 PM (2 years ago)', 29: 'Mo\nMohammad Farah\n2021-05-31 10:53 AM (2 years ago)', 30: 'Mo\nMohammad Farah\n2021-05-31 10:51 AM (2 years ago)', 31: 'Mo\nMohammad Farah\n2020-09-27 12:24 PM (3 years ago)', 32: 'Mo\nMohammad Farah\n2020-12-29 07:55 AM (3 years ago)', 33: 'Mo\nMohammad Farah\n2021-01-27 12:26 PM (2 years ago)', 34: 'Mo\nMohammad Farah\n2020-10-05 11:07 AM (3 years ago)', 35: 'Mo\nMohammad Farah\n2020-12-24 8:19 PM (3 years ago)', 36: 'No comments', 37: 'Mo\nMohammad Farah\n2020-12-14 08:47 AM (3 years ago)', 38: 'Mo\nMohammad Farah\n2020-12-14 08:28 AM (3 years ago)', 39: 'No comments', 40: 'Mo\nMohammad Farah\n2020-10-19 11:59 AM (3 years ago)'}, 'Duration': {1: datetime.timedelta(days=1335), 2: datetime.timedelta(days=180), 3: datetime.timedelta(days=1308), 4: datetime.timedelta(days=180), 5: datetime.timedelta(days=341), 6: datetime.timedelta(days=646), 7: datetime.timedelta(days=1270), 8: datetime.timedelta(days=472), 9: datetime.timedelta(days=643), 10: datetime.timedelta(days=-686), 11: datetime.timedelta(days=590), 12: datetime.timedelta(days=199), 13: datetime.timedelta(days=2), 14: datetime.timedelta(days=8), 15: datetime.timedelta(days=4), 16: datetime.timedelta(days=100), 17: datetime.timedelta(days=304), 18: datetime.timedelta(days=287), 19: datetime.timedelta(days=23), 20: datetime.timedelta(days=41), 21: datetime.timedelta(days=305), 22: datetime.timedelta(days=77), 23: datetime.timedelta(days=104), 24: datetime.timedelta(days=181), 25: datetime.timedelta(days=336), 26: datetime.timedelta(days=318), 27: datetime.timedelta(days=3), 28: datetime.timedelta(days=188), 29: datetime.timedelta(days=155), 30: datetime.timedelta(days=174), 31: datetime.timedelta(days=250), 32: datetime.timedelta(days=33), 33: datetime.timedelta(days=1299), 34: datetime.timedelta(days=95), 35: datetime.timedelta(days=2), 36: datetime.timedelta(days=3), 37: datetime.timedelta(days=2), 38: datetime.timedelta(days=35), 39: datetime.timedelta(days=11), 40: datetime.timedelta(days=50)}, 'DEP': {1: 'CCS', 2: 'CCS', 3: 'KSA', 4: 'OS', 5: 'OS', 6: 'CCE', 7: 'CCE', 8: 'OS', 9: 'OS', 10: 'CCS', 11: 'CCS', 12: 'CCE', 13: 'CCE', 14: 'CCS', 15: 'CCE', 16: 'CCS', 17: 'CCS', 18: 'CCE', 19: 'CCS', 20: 'CCE', 21: 'OS', 22: 'CCE', 23: 'CCE', 24: 'OS', 25: 'CCE', 26: 'CCE', 27: 'CCS', 28: 'CCE', 29: 'CCS', 30: 'CCS', 31: 'CCE', 32: 'CCE', 33: 'CCS', 34: 'CCE', 35: 'CCE', 36: 'CCE', 37: 'CCE', 38: 'CCE', 39: 'CCS', 40: 'CCS'}},
#     2021: {'project name': {1: 'SpeechLog (Backup Recorder)', 2: 'Customer Order (Phase II)', 3: 'Roaming (Links Migration to HSL)', 4: 'SpeechLog Retail (RQM)', 5: 'USSD', 6: 'E-FAX Migration', 7: 'SpeechLog (CRs)', 8: 'Consolidated Roaming Solutions', 9: 'SpeechLog 8.0 (POC)', 10: 'Raya CC - PMP Temp License', 11: 'RBT (CRs)', 12: 'SpeechLog 8.0', 13: 'SpeechLog (Upgrade to 8.x)', 14: 'National Roaming', 15: 'RQM POC JAZZ', 16: 'SpeechLog (Expansion)', 17: 'RQM -Orange', 18: 'SpeechLog (POC)', 19: 'Speech Analytics', 20: 'RQM (POC)', 21: 'SpeechLog (License 4 IPs)', 22: 'SpeechLog (16 ports licenses and voice c...', 23: 'AutoDialer (Upgrade & Migration)', 24: 'RQM', 25: 'WFO (SL, PMP, WFM)', 26: 'WFO (250 Agents)', 27: 'SMS Dispatcher', 28: 'Speech Analytics', 29: 'SpeechLog (E1)', 30: 'SpeechLog (Upgrade 7.6)', 31: 'Roam Salute (Migration to VMs)', 32: 'GDRC (Redundancy)', 33: 'SpeechLog (Expansion 15 IPs)', 34: 'SpeechLog (Expansion)', 35: 'SpeechLog (8 Analog ports)', 36: 'SpeechLog (Expansion 33 IP ports)', 37: 'SpeechLog (Expansion 75 Licenses)', 38: 'SpeechLog (Encryption)', 39: 'SpeechLog (Expansion)', 40: 'SpeechLog (CRs)'}, 'Engineer name': {1: 'Abdulrahman Hasan', 2: 'Khairy Khdeir', 3: 'Yousef Mishael', 4: 'Tamer Wathaifi', 5: 'Mariam Al-Issa', 6: 'Yousef Mishael', 7: 'Ahmad AlHasan', 8: 'Mohammad Farah', 9: 'Mutaz Althaher', 10: 'Abdallah Halaweh', 11: 'Laith Al-Janaideh', 12: 'Mutaz Althaher', 13: 'Ahmad AlHasan', 14: 'Mohammad Farah', 15: 'Tamer Wathaifi', 16: 'Abdulrahman Hasan', 17: 'Abdulrahman Hasan', 18: 'Ahmad AlHasan', 19: 'Mohammad Farah', 20: 'Mohammad Al-Mahrok', 21: 'CCE', 22: 'CCE', 23: 'Yousif Rayyan', 24: 'Abdallah Halaweh', 25: 'Tamer Moalla', 26: 'Tamer Moalla', 27: 'Abdallah Halaweh', 28: 'Abdallah Halaweh', 29: 'CCE', 30: 'CCE', 31: 'Khairy Khdeir', 32: 'Mohammad Farah', 33: 'Mohammad Farah', 34: 'Mutaz Althaher', 35: 'CCE', 36: 'CCE', 37: 'Abdellateef Ibrahim', 38: 'Mohammad Farah', 39: 'Abdellateef Ibrahim', 40: 'Mutaz Althaher'}, 'Related To': {1: 'Arab Bank', 2: 'Asiacell', 3: 'Ufone', 4: 'STC KW', 5: 'KocharTech (Telesur)', 6: 'STC BH', 7: 'VIVA STC - KW', 8: 'Jawwal', 9: 'Earth Link', 10: 'Raya', 11: 'Golis Somalia', 12: 'Earth Link', 13: 'Zain Jordan', 14: 'Telenity (Mobily)', 15: 'Jazz', 16: 'Unitel (Ajyad)', 17: 'Orange Jo', 18: 'ooredoo Kuwait', 19: 'ADTC', 20: 'ALHAFIDH Group', 21: 'KHCC-JBS', 22: 'JRM (MOI)', 23: 'Orange Jo', 24: 'AlRajhi Bank KSA', 25: 'tawuniya', 26: 'Majorel Citizen', 27: 'Orange Jo', 28: 'Bank AlBilad', 29: 'JRM (Water Authority)', 30: 'BTC (Intercontinental Hotel)', 31: 'AlbTelecom', 32: 'TeleCel', 33: 'Umniah', 34: 'NCR (Ajman Bank)', 35: 'Jordan Commercial Bank (JCB)', 36: 'Egyptian Arab Land Bank-JBS', 37: 'ADTC', 38: 'The Royal Hashemite Court (RHC)', 39: 'KDCC (IICO)', 40: 'MTN Afghanistan'}, 'status': {1: 'On Hold', 2: 'In Progress', 3: 'Completed', 4: 'Completed', 5: 'Completed', 6: 'Completed', 7: 'Archived', 8: 'Completed', 9: 'Completed', 10: 'Completed', 11: 'Completed', 12: 'Completed', 13: 'Completed', 14: 'Completed', 15: 'Completed', 16: 'Completed', 17: 'Completed', 18: 'Completed', 19: 'Archived', 20: 'Archived', 21: 'Completed', 22: 'Completed', 23: 'Completed', 24: 'Completed', 25: 'Archived', 26: 'Archived', 27: 'Completed', 28: 'Completed', 29: 'Completed', 30: 'Completed', 31: 'Completed', 32: 'Archived', 33: 'Completed', 34: 'Completed', 35: 'Completed', 36: 'Completed', 37: 'Completed', 38: 'Completed', 39: 'Completed', 40: 'Completed'}, 'Details': {1: 'Ab\nAbdelrahman Rasem\n2024-01-07 12:08 PM (8 days ago)', 2: 'Mo\nMohammad Farah\n2023-12-18 07:21 AM (28 days ago)', 3: 'Ab\nAbdelrahman Rasem\n2023-10-30 05:49 AM (2 months ago)', 4: 'Mo\nMohammad Farah\n2023-06-11 10:35 AM (7 months ago)', 5: 'Mo\nMohammad Farah\n2023-06-12 11:40 AM (7 months ago)', 6: 'Mo\nMohammad Farah\n2022-02-28 11:55 AM (1 year ago)', 7: 'Mo\nMohammad Farah\n2023-03-06 1:40 PM (10 months ago)', 8: 'Mo\nMohammad Farah\n2023-01-31 11:23 AM (11 months ago)', 9: 'Mo\nMohammad Farah\n2021-11-10 07:43 AM (2 years ago)', 10: 'Ab\nAbdallah Halaweh\n2021-10-26 07:36 AM (2 years ago)', 11: 'Mo\nMohammad Farah\n2022-11-03 09:40 AM (1 year ago)', 12: 'Mo\nMohammad Farah\n2022-12-27 1:24 PM (1 year ago)', 13: 'Mo\nMohammad Farah\n2022-12-14 09:22 AM (1 year ago)', 14: 'Mo\nMohammad Farah\n2022-07-04 06:36 AM (1 year ago)', 15: 'Mo\nMohammad Farah\n2022-06-01 10:23 AM (1 year ago)', 16: 'No comments', 17: 'Mo\nMohammad Farah\n2022-06-02 07:15 AM (1 year ago)', 18: 'Mo\nMohammad Farah\n2022-04-17 12:08 PM (1 year ago)', 19: 'Mo\nMohammad Farah\n2022-05-10 2:14 PM (1 year ago)', 20: 'Mo\nMohammad Farah\n2022-05-10 1:13 PM (1 year ago)', 21: 'Mo\nMohammad Farah\n2021-12-05 12:00 PM (2 years ago)', 22: 'Mo\nMohammad Farah\n2021-12-14 12:41 PM (2 years ago)', 23: 'Mo\nMohammad Farah\n2022-03-09 11:49 AM (1 year ago)', 24: 'Ab\nAbdallah Halaweh\n2022-02-15 10:58 AM (1 year ago)', 25: 'Mo\nMohammad Farah\n2022-02-28 12:49 PM (1 year ago)', 26: 'Mo\nMohammad Farah\n2022-02-28 12:47 PM (1 year ago)', 27: 'Ab\nAbdallah Halaweh\n2022-02-15 12:16 PM (1 year ago)', 28: 'Ab\nAbdallah Halaweh\n2022-01-04 07:30 AM (2 years ago)', 29: 'Mo\nMohammad Farah\n2022-01-30 3:31 PM (1 year ago)', 30: 'Mo\nMohammad Farah\n2021-12-27 09:26 AM (2 years ago)', 31: 'Mo\nMohammad Farah\n2021-12-23 1:06 PM (2 years ago)', 32: 'Mo\nMohammad Farah\n2021-12-13 10:42 AM (2 years ago)', 33: 'Mo\nMohammad Farah\n2021-12-12 1:29 PM (2 years ago)', 34: 'Mo\nMohammad Farah\n2021-06-17 07:12 AM (2 years ago)', 35: 'Mo\nMohammad Farah\n2021-10-31 06:33 AM (2 years ago)', 36: 'Mo\nMohammad Farah\n2021-10-24 2:29 PM (2 years ago)', 37: 'Mo\nMohammad Farah\n2021-10-20 06:30 AM (2 years ago)', 38: 'Mo\nMohammad Farah\n2021-09-30 11:16 AM (2 years ago)', 39: 'Mo\nMohammad Farah\n2021-09-28 12:08 PM (2 years ago)', 40: 'Mo\nMohammad Farah\n2021-09-27 12:06 PM (2 years ago)'}, 'Duration': {1: datetime.timedelta(days=892), 2: datetime.timedelta(days=831), 3: datetime.timedelta(days=692), 4: datetime.timedelta(days=355), 5: datetime.timedelta(days=652), 6: datetime.timedelta(days=381), 7: datetime.timedelta(days=1049), 8: datetime.timedelta(days=278), 9: datetime.timedelta(days=105), 10: datetime.timedelta(days=26), 11: datetime.timedelta(days=431), 12: datetime.timedelta(days=400), 13: datetime.timedelta(days=150), 14: datetime.timedelta(days=296), 15: datetime.timedelta(days=233), 16: datetime.timedelta(days=4), 17: datetime.timedelta(days=-502), 18: datetime.timedelta(days=254), 19: datetime.timedelta(days=1097), 20: datetime.timedelta(days=1015), 21: datetime.timedelta(days=1), 22: datetime.timedelta(days=106), 23: datetime.timedelta(days=262), 24: datetime.timedelta(days=179), 25: datetime.timedelta(days=1064), 26: datetime.timedelta(days=1103), 27: datetime.timedelta(days=188), 28: datetime.timedelta(days=1116), 29: datetime.timedelta(days=94), 30: datetime.timedelta(days=28), 31: datetime.timedelta(days=81), 32: datetime.timedelta(days=878), 33: datetime.timedelta(days=5), 34: datetime.timedelta(days=106), 35: datetime.timedelta(days=22), 36: datetime.timedelta(days=21), 37: datetime.timedelta(days=28), 38: datetime.timedelta(days=11), 39: datetime.timedelta(days=90), 40: datetime.timedelta(days=86)}, 'DEP': {1: 'CCE', 2: 'OS', 3: 'OS', 4: 'CCE', 5: 'OS', 6: 'OS', 7: 'CCS', 8: 'OS', 9: 'CCS', 10: 'CCS', 11: 'OS', 12: 'CCS', 13: 'CCS', 14: 'KSA', 15: 'CCE', 16: 'CCE', 17: 'CCE', 18: 'CCS', 19: 'CCS', 20: 'CCE', 21: 'CCE', 22: 'CCE', 23: 'OS', 24: 'KSA', 25: 'KSA', 26: 'KSA', 27: 'OS', 28: 'KSA', 29: 'CCE', 30: 'CCE', 31: 'OS', 32: 'OS', 33: 'CCS', 34: 'CCS', 35: 'CCE', 36: 'CCE', 37: 'CCS', 38: 'CCS', 39: 'CCS', 40: 'CCS'}},
#     2022: {'project name': {1: 'SpeechLog (30 IP)', 2: 'LTE, ITS & RS Upgrade', 3: 'Data Rating and Charging (Redundancy)', 4: 'Accudial (Upgrade)', 5: 'RQMS on SAS', 6: 'USSD GW Upgrade & CR', 7: 'SpeechLog (20 IP)', 8: 'Roaming Bundle (Reinstallation)', 9: 'MLC Upgrade', 10: 'Speech Analytics (POC)', 11: 'SpeechLog (Screen Capture, 27 Licenses)', 12: 'VAS Sub-charging CR', 13: 'PMP (Expansion Telesales)', 14: 'Move 4 licenses to new server', 15: 'SpeechLog migration to VM', 16: 'RQM (POC)', 17: 'RQM (POC)', 18: 'eWRMS Expansion & Campaign Manager', 19: 'Speech Analytics (POC)', 20: 'SpeechLog (Testing with Alcatel)', 21: 'SpeechLog (3 IP)', 22: 'BTS (LTE)', 23: 'SpeechLog (Quality Management Licenses2)', 24: 'WFO', 25: 'RQM (25 Seats)', 26: 'SpeechLog (Digital Recorder)', 27: 'New BV API', 28: 'SpeechLog (60 IP)', 29: 'SpeechLog ( Expansion 26 IPs)', 30: 'SpeechLog (Expansion 20 IP)', 31: 'RQM (Expansion 300 Seats)', 32: 'SpeechLog (Reinstallation)', 33: 'SpeechLog (Expansion 250 IP)', 34: 'SpeechLog (10 IP)', 35: 'RQM', 36: 'RQM (Expansion 50 Seats)', 37: 'Migration of SpeechLog license from anal...', 38: 'SpeechLog (Mitel POC)', 39: 'RQM (POC)', 40: 'SpeechLog (10 SIP on Mitel)'}, 'Engineer name': {1: 'Ahmad AlHasan', 2: 'Yousef Mishael', 3: 'Yousef Mishael', 4: 'Abdulrahman Hasan', 5: 'Mohammad Alalami', 6: 'Zaid Hina', 7: 'Abdulrahman Hasan', 8: 'aladdin Shishani', 9: 'Zaid Hina', 10: 'Nabeel Nusair', 11: 'Ahmad AlHasan', 12: 'Laith Al-Janaideh', 13: 'Abdellateef Ibrahim', 14: 'Bilal Al-Noori', 15: 'Adel Bataineh', 16: 'Mohammad Alalami', 17: 'Tamer Wathaifi', 18: 'Yousef Mishael', 19: 'Mutaz Althaher', 20: 'Hamzeh Shwemeh', 21: 'Abdulrahman Hasan', 22: 'Mohammad Farah', 23: 'Mohammad Farah', 24: 'Mohammad alamm', 25: 'Tamer Wathaifi', 26: 'Bilal Al-Noori', 27: 'Yousif Rayyan', 28: 'Mutaz Althaher', 29: 'Ahmad AlHasan', 30: 'Bilal Al-Noori', 31: 'Tamer Wathaifi', 32: 'Abdulrahman Hasan', 33: 'Hamzeh Shwemeh', 34: 'Abdulrahman Hasan', 35: 'Mohammad Alalami', 36: 'CCE', 37: 'Abdulrahman Hasan', 38: 'CCE', 39: 'Tamer Wathaifi', 40: 'Tamer Wathaifi'}, 'Related To': {1: 'Takamol (ALghanim)', 2: 'Ufone', 3: 'TeleCel', 4: 'Housing Bank', 5: 'Etisalat UAE', 6: 'Zain Jordan', 7: 'Jordan Commercial Bank (JCB)', 8: 'Sudatel', 9: 'Zain Jordan', 10: 'Zain Iraq', 11: 'Zain Jordan', 12: 'Golis Somalia', 13: 'Zain Jordan', 14: 'Metropolitan (Cinnamon Lakeside Colombo)', 15: 'DAMAC', 16: 'Zain Iraq', 17: 'Earth Link', 18: 'Telenity (Mobily)', 19: 'Bank Muscat', 20: 'PSD', 21: 'ALTABADUL', 22: 'Jawwal', 23: 'Zain Jordan', 24: 'Majorel (NWC)', 25: 'International Development Bank', 26: 'Al Kattan & Co', 27: 'Ooredoo Oman', 28: 'NABS (Abu Dhabi Ports)', 29: 'Zain Jordan', 30: 'Housing Bank', 31: 'Etisalat Misr', 32: 'Unitel (IDECO)', 33: 'ooredoo Qatar', 34: 'Jordan Central Bank (unitel)', 35: 'Ooredoo (Kuwait) -RQM', 36: 'Zain Jordan', 37: 'Jordan Kuwait Bank', 38: 'SPEC (ENR)', 39: 'International Development Bank', 40: 'Metropolitan (Cinnamon Lakeside Colombo)'}, 'status': {1: 'In Progress', 2: 'In Progress', 3: 'In Progress', 4: 'Completed', 5: 'Completed', 6: 'Completed', 7: 'Completed', 8: 'On Hold', 9: 'Completed', 10: 'Archived', 11: 'Completed', 12: 'Completed', 13: 'Completed', 14: 'On Hold', 15: 'Completed', 16: 'Completed', 17: 'Completed', 18: 'Archived', 19: 'Completed', 20: 'Archived', 21: 'Completed', 22: 'Completed', 23: 'Completed', 24: 'Archived', 25: 'Completed', 26: 'Completed', 27: 'Completed', 28: 'Completed', 29: 'Completed', 30: 'Completed', 31: 'Completed', 32: 'Completed', 33: 'Completed', 34: 'Archived', 35: 'Completed', 36: 'Completed', 37: 'Completed', 38: 'Completed', 39: 'Completed', 40: 'Completed'}, 'Details': {1: 'Abdelrahman Rasem\n2024-01-08 12:15 PM (7 days ago)', 2: 'Ab\nAbdelrahman Rasem\n2024-01-08 09:41 AM (7 days ago)', 3: 'Ab\nAbdelrahman Rasem\n2024-01-08 09:38 AM (7 days ago)', 4: 'Abdelrahman Rasem\n2023-12-27 6:11 PM (18 days ago)', 5: 'Mo\nMohammad Farah\n2023-12-03 08:16 AM (1 month ago)', 6: 'Ab\nAbdelrahman Rasem\n2023-11-20 09:11 AM (1 month ago)', 7: 'Ab\nAbdelrahman Rasem\n2023-11-14 05:58 AM (2 months ago)', 9: 'Mo\nMohammad Farah\n2023-09-17 10:13 AM (4 months ago)', 10: 'Mo\nMohammad Farah\n2023-08-28 12:28 PM (4 months ago)', 11: 'Mo\nMohammad Farah\n2023-08-27 12:16 PM (4 months ago)', 12: 'Mo\nMohammad Farah\n2023-07-20 09:55 AM (5 months ago)', 13: 'Mo\nMohammad Farah\n2023-07-18 10:53 AM (6 months ago)', 14: 'Ab\nAbdelrahman Rasem\n2023-07-17 08:23 AM (6 months ago)', 15: 'Mo\nMohammad Farah\n2023-06-12 12:25 PM (7 months ago)', 16: 'Mo\nMohammad Farah\n2023-06-05 12:35 PM (7 months ago)', 17: 'Mo\nMohammad Farah\n2023-06-05 12:34 PM (7 months ago)', 18: 'Mo\nMohammad Farah\n2023-01-03 06:19 AM (1 year ago)', 19: 'Mo\nMohammad Farah\n2023-05-08 12:28 PM (8 months ago)', 20: 'Mo\nMohammad Farah\n2023-03-06 1:39 PM (10 months ago)', 21: 'Mo\nMohammad Farah\n2023-02-22 08:59 AM (10 months ago)', 22: 'Mo\nMohammad Farah\n2023-01-31 11:19 AM (11 months ago)', 23: 'No comments', 24: 'Mo\nMohammad Farah\n2023-01-03 06:20 AM (1 year ago)', 25: 'Mo\nMohammad Farah\n2022-12-27 08:10 AM (1 year ago)', 26: 'Mo\nMohammad Farah\n2022-12-26 2:09 PM (1 year ago)', 27: 'Mo\nMohammad Farah\n2022-12-18 10:49 AM (1 year ago)', 28: 'Mo\nMohammad Farah\n2022-12-13 08:19 AM (1 year ago)', 29: 'Mo\nMohammad Farah\n2022-12-05 3:17 PM (1 year ago)', 30: 'Mo\nMohammad Farah\n2022-11-16 08:00 AM (1 year ago)', 31: 'Mo\nMohammad Farah\n2022-11-13 08:16 AM (1 year ago)', 32: 'Mo\nMohammad Farah\n2022-11-07 2:26 PM (1 year ago)', 33: 'Mo\nMohammad Farah\n2022-11-06 5:10 PM (1 year ago)', 34: 'Mo\nMohammad Farah\n2022-10-18 09:51 AM (1 year ago)', 35: 'Mo\nMohammad Farah\n2022-10-25 12:45 PM (1 year ago)', 36: 'Mo\nMohammad Farah\n2022-10-25 09:28 AM (1 year ago)', 37: 'Mo\nMohammad Farah\n2022-08-30 08:47 AM (1 year ago)', 38: 'Mo\nMohammad Farah\n2022-09-19 08:59 AM (1 year ago)', 39: 'Mo\nMohammad Farah\n2022-09-19 09:12 AM (1 year ago)', 40: 'Mo\nMohammad Farah\n2022-09-06 10:25 AM (1 year ago)'}, 'Duration': {1: datetime.timedelta(days=627), 2: datetime.timedelta(days=696), 3: datetime.timedelta(days=755), 4: datetime.timedelta(days=469), 5: datetime.timedelta(days=287), 6: datetime.timedelta(days=313), 7: datetime.timedelta(days=477), 8: datetime.timedelta(days=600), 9: datetime.timedelta(days=316), 10: datetime.timedelta(days=529), 11: datetime.timedelta(days=216), 12: datetime.timedelta(days=293), 13: datetime.timedelta(days=215), 14: datetime.timedelta(days=500), 15: datetime.timedelta(days=23), 16: datetime.timedelta(days=232), 17: datetime.timedelta(days=359), 18: datetime.timedelta(days=549), 19: datetime.timedelta(days=158), 20: datetime.timedelta(days=635), 21: datetime.timedelta(days=351), 22: datetime.timedelta(days=78), 23: datetime.timedelta(days=7), 24: datetime.timedelta(days=774), 25: datetime.timedelta(days=89), 26: datetime.timedelta(days=92), 27: datetime.timedelta(days=77), 28: datetime.timedelta(days=141), 29: datetime.timedelta(days=7), 30: datetime.timedelta(days=9), 31: datetime.timedelta(days=3), 32: datetime.timedelta(days=16), 33: datetime.timedelta(days=6), 34: datetime.timedelta(days=213), 35: datetime.timedelta(days=114), 36: datetime.timedelta(days=7), 37: datetime.timedelta(days=37), 38: datetime.timedelta(days=11), 39: datetime.timedelta(days=78), 40: datetime.timedelta(days=178)}, 'DEP': {1: 'CCS', 2: 'OS', 3: 'OS', 4: 'CCE', 5: 'CCE', 6: 'OS', 7: 'CCE', 8: 'OS', 9: 'OS', 10: 'CCS', 11: 'CCS', 12: 'OS', 13: 'CCS', 14: 'CCE', 15: 'CCS', 16: 'CCE', 17: 'CCE', 18: 'KSA', 19: 'CCS', 20: 'CCS', 21: 'CCE', 22: 'OS', 23: 'CCS', 24: 'KSA', 25: 'CCE', 26: 'CCE', 27: 'OS', 28: 'CCS', 29: 'CCS', 30: 'CCE', 31: 'CCE', 32: 'CCE', 33: 'CCS', 34: 'CCE', 35: 'CCE', 36: 'CCE', 37: 'CCE', 38: 'CCE', 39: 'CCE', 40: 'CCE'}},
#     2023: {'project name': {1: 'MoDEE – CBS', 2: 'ITS POC', 3: 'E911 integration with XLM', 4: 'Roaming Bundle License Expansion', 5: 'WFM, PMP, and SpeechLog Voice Recording ...', 6: 'SpeechLog IP Recorder License & HA & DR', 7: 'E911 (Caller Barring Status)', 8: 'SpeechLog Retail POC', 9: 'Umniah - NPS CR', 10: 'Accudial call accounting - extension lic...', 11: 'Expand SpeechLog Recording', 12: 'SpeechLog Al Rajhi Bank', 13: 'Display line status /E911', 14: 'Maintenance Visit', 15: 'CLI Screening', 16: 'SpeechLog', 17: 'SpeechLog Quality Management system', 18: 'Orange – PPMD CR', 19: 'Speech Log Retail Demo system', 20: 'Speech Log expansion', 21: 'Provisioning Mediator (PM)', 22: 'Speech Log reinstallation', 23: 'OmanTel Speech Log Retail POC', 24: 'IVR professional recording', 25: 'Collect Call & Caller ID', 26: 'SpeechLog', 27: 'Speech log Recording', 28: 'SpeechLog expansion', 29: 'Speech Log expansion- Soltek', 30: 'Speech Log Recorder (HA)', 31: 'Speech Log Expansion', 32: 'Enabling-4G', 33: 'Speech Log Expansion', 34: 'SpeechLog (34 IP)', 35: 'SpeechLog', 36: 'RQM (Expansion 25 Seats)', 37: 'Collect Call expansion Licenses', 38: 'SpeechLog Voice Recording (IP) Kalaam', 39: 'SpeechLog Retail Zain KW (POC)', 40: 'JRM – E1 Recorder'}, 'Engineer name': {1: 'aladdin Shishani', 2: 'Yousif Rayyan', 3: 'Hamzeh Shwemeh', 4: 'aladdin Shishani', 5: 'Abdellateef Ibrahim', 6: 'Adel Bataineh', 7: 'Hamzeh Shwemeh', 8: 'Osama Gharbieh', 9: 'Mohammad Al-Mahrok', 10: 'Bilal Al-Noori', 11: 'Nabeel Nusair', 12: 'Abdulrahman Hasan', 13: 'Hamzeh Shwemeh', 14: 'Bilal Al-Noori', 15: 'Khairy Khdeir', 16: 'Ahmad AlHasan', 17: 'Mutaz Althaher', 18: 'Yousif Rayyan', 19: 'Qusai Abdel-Razaq', 20: 'Osama Gharbieh', 21: 'aladdin Shishani', 22: 'Bilal Al-Noori', 23: 'Osama Gharbieh', 24: 'Osama Gharbieh', 25: 'aladdin Shishani', 26: 'CCE', 27: 'Abdulrahman Hasan', 28: 'Mutaz Althaher', 29: 'Osama Gharbieh', 30: 'Bilal Al-Noori', 31: 'Bilal Al-Noori', 32: 'Khairy Khdeir', 33: 'Osama Gharbieh', 34: 'Abdulrahman Hasan', 35: 'Abdulrahman Hasan', 36: 'Mohammad Alalami', 37: 'aladdin Shishani', 38: 'Hamzeh Shwemeh', 39: 'Tamer Wathaifi', 40: 'Abdulrahman Hasan'}, 'Related To': {1: 'MODEE', 2: 'Ooredoo Oman', 3: 'PSD', 4: 'Asiacell', 5: 'Jawwal', 6: 'Ajman Bank', 7: 'Orange', 8: 'Etisalat UAE', 9: 'Umniah', 10: 'Ministry of Tourism and Antiquities', 11: 'Zain Jordan', 12: 'Al Rajhi Bank', 13: 'PSD', 14: 'Nabulsi - Burger Makers', 15: 'Zain JO', 16: 'Takamol (Switch IRAQ)', 17: 'Space Town', 18: 'Orange Jo', 19: 'Flex Technology', 20: 'Housing Bank', 21: 'Orange Jo', 22: 'Farouq Medical City', 23: 'Oman Tel', 24: 'ISTD', 25: 'Ethio Telecom', 26: 'Unitel (Palace of Justice)', 27: 'Arab Bank', 28: 'Earth Link', 29: 'Safwa Bank', 30: 'Housing Bank', 31: 'Housing Bank', 32: 'Asiacell', 33: 'ZAK', 34: 'ABC BANK BH', 35: 'Al Rajhi Bank', 36: 'ooredoo Kuwait', 37: 'Sabafon', 38: 'Kalaam', 39: 'Zain KW', 40: 'JRM'}, 'status': {1: 'Initiated', 2: 'In Progress', 3: 'In Progress', 4: 'In Progress', 5: 'Initiated', 6: 'Completed', 7: 'Completed', 8: 'Initiated', 9: 'Completed', 10: 'Completed', 11: 'Completed', 12: 'In Progress', 13: 'Completed', 14: 'Completed', 15: 'Completed', 16: 'Completed', 17: 'On Hold', 18: 'Completed', 19: 'Completed', 20: 'Completed', 21: 'Completed', 22: 'Completed', 23: 'Completed', 24: 'Completed', 25: 'On Hold', 26: 'On Hold', 27: 'Completed', 28: 'Completed', 29: 'Completed', 30: 'Completed', 31: 'Completed', 32: 'Completed', 33: 'Completed', 34: 'Completed', 35: 'Archived', 36: 'Completed', 37: 'Completed', 38: 'Completed', 39: 'Completed', 40: 'Completed'}, 'Details': {1: 'Ab\nAbdelrahman Rasem\n2024-01-15 09:41 AM (2 hours ago)', 2: 'Abdelrahman Rasem\n2024-01-15 09:38 AM (2 hours ago)', 3: 'Ab\nAbdelrahman Rasem\n2024-01-15 09:34 AM (3 hours ago)', 4: 'Ab\nAbdelrahman Rasem\n2024-01-08 09:36 AM (7 days ago)', 5: 'Abdelrahman Rasem\n2024-01-07 12:14 PM (8 days ago)', 6: 'Abdelrahman Rasem\n2023-12-20 2:34 PM (25 days ago)', 7: 'Ab\nAbdelrahman Rasem\n2023-12-04 09:15 AM (1 month ago)', 8: 'No comments', 9: 'Ab\nAbdelrahman Rasem\n2023-12-05 06:28 AM (1 month ago)', 10: 'Ab\nAbdelrahman Rasem\n2023-12-05 06:29 AM (1 month ago)', 11: 'Abdelrahman Rasem\n2023-12-04 12:03 PM (1 month ago)', 12: 'Ab\nAbdelrahman Rasem\n2023-12-05 06:22 AM (1 month ago)', 13: 'Ab\nAbdelrahman Rasem\n2023-12-04 12:07 PM (1 month ago)', 14: 'Ab\nAbdelrahman Rasem\n2023-11-21 06:07 AM (1 month ago)', 15: 'Ab\nAbdelrahman Rasem\n2023-11-22 3:04 PM (1 month ago)', 16: 'Ab\nAbdelrahman Rasem\n2023-11-20 12:10 PM (1 month ago)', 17: 'Ab\nAbdelrahman Rasem\n2023-11-20 12:01 PM (1 month ago)', 18: 'Mo\nMohammad Farah\n2023-11-06 09:10 AM (2 months ago)', 19: 'Ab\nAbdelrahman Rasem\n2023-11-07 06:31 AM (2 months ago)', 20: 'Abdelrahman Rasem\n2023-11-01 12:08 PM (2 months ago)', 21: 'Mo\nMohammad Farah\n2023-10-22 06:32 AM (2 months ago)', 22: 'Mo\nMohammad Farah\n2023-10-22 07:28 AM (2 months ago)', 23: 'Abdelrahman Rasem\n2023-10-25 06:28 AM (2 months ago)', 24: 'Abdelrahman Rasem\n2023-10-23 08:10 AM (2 months ago)', 25: 'Mo\nMohammad Farah\n2023-09-11 09:25 AM (4 months ago)', 26: 'Ab\nAbdelrahman Rasem\n2023-10-10 06:19 AM (3 months ago)', 27: 'Ab\nAbdelrahman Rasem\n2023-10-03 10:57 AM (3 months ago)', 28: 'No comments', 29: 'Mohammad Farah\n2023-09-12 05:57 AM (4 months ago)', 30: 'Abdelrahman Rasem\n2023-08-29 06:16 AM (4 months ago)', 31: 'Abdelrahman Rasem\n2023-08-29 06:15 AM (4 months ago)', 32: 'Abdelrahman Rasem\n2023-08-29 07:14 AM (4 months ago)', 33: 'Mo\nMohammad Farah\n2023-08-15 06:59 AM (5 months ago)', 34: 'Mo\nMohammad Farah\n2023-08-17 11:34 AM (5 months ago)', 35: 'Mo\nMohammad Farah\n2023-08-15 06:34 AM (5 months ago)', 36: 'Mo\nMohammad Farah\n2023-04-27 08:43 AM (8 months ago)', 37: 'Mo\nMohammad Farah\n2023-07-26 12:02 PM (5 months ago)', 38: 'Ab\nAbdelrahman Rasem\n2023-07-24 3:09 PM (5 months ago)', 39: 'Abdelrahman Rasem\n2023-07-17 08:00 AM (6 months ago)', 40: 'Ab\nAbdelrahman Rasem\n2023-07-11 12:03 PM (6 months ago)'}, 'Duration': {1: datetime.timedelta(days=161), 2: datetime.timedelta(days=192), 3: datetime.timedelta(days=451), 4: datetime.timedelta(days=109), 5: datetime.timedelta(days=123), 6: datetime.timedelta(days=17), 7: datetime.timedelta(days=310), 8: datetime.timedelta(days=116), 9: datetime.timedelta(days=109), 10: datetime.timedelta(days=57), 11: datetime.timedelta(days=2), 12: datetime.timedelta(days=182), 13: datetime.timedelta(days=86), 14: datetime.timedelta(days=7), 15: datetime.timedelta(days=77), 16: datetime.timedelta(days=301), 17: datetime.timedelta(days=271), 18: datetime.timedelta(days=43), 19: datetime.timedelta(days=30), 20: datetime.timedelta(days=8), 21: datetime.timedelta(days=66), 22: datetime.timedelta(days=19), 23: datetime.timedelta(days=104), 24: datetime.timedelta(days=12), 25: datetime.timedelta(days=251), 26: datetime.timedelta(days=453), 27: datetime.timedelta(days=9), 28: datetime.timedelta(days=5), 29: datetime.timedelta(days=22), 30: datetime.timedelta(days=83), 31: datetime.timedelta(days=22), 32: datetime.timedelta(days=181), 33: datetime.timedelta(days=263), 34: datetime.timedelta(days=143), 35: datetime.timedelta(days=424), 36: datetime.timedelta(days=10), 37: datetime.timedelta(days=16), 38: datetime.timedelta(days=123), 39: datetime.timedelta(days=85), 40: datetime.timedelta(days=49)}, 'DEP': {1: 'OS', 2: 'OS', 3: 'OS', 4: 'OS', 5: 'CCS', 6: 'CCS', 7: 'OS', 8: 'CCE', 9: 'CCE', 10: 'CCE', 11: 'CCS', 12: 'CCE', 13: 'CCS', 14: 'CCE', 15: 'OS', 16: 'CCS', 17: 'CCS', 18: 'OS', 19: 'CCE', 20: 'CCE', 21: 'OS', 22: 'CCE', 23: 'CCE', 24: 'CCE', 25: 'OS', 26: 'CCE', 27: 'CCE', 28: 'CCS', 29: 'CCE', 30: 'CCE', 31: 'CCE', 32: 'OS', 33: 'CCE', 34: 'CCE', 35: 'CCE', 36: 'CCE', 37: 'OS', 38: 'CCS', 39: 'CCE', 40: 'CCE'}}}

mp={'project name': {1: 'Accudial call accounting - extension lic...', 2: 'SpeechLog Al Rajhi Bank', 3: 'Display line status /E911', 4: 'E911 (Caller Barring Status)', 5: 'E911 integration with XLM', 6: 'Maintenance Visit', 7: 'Orange – PPMD CR', 8: 'Speech Log expansion', 9: 'Provisioning Mediator (PM)', 10: 'IVR professional recording', 11: 'SpeechLog', 12: 'Speech log Recording', 13: 'Speech Log expansion- Soltek', 14: 'Speech Log Recorder (HA)', 15: 'Speech Log Expansion', 16: 'SpeechLog (34 IP)', 17: 'SpeechLog', 18: 'Social Security Investment Fund – Speech...', 19: 'Host Monitor', 20: 'Speech Log expansion Arab Bank', 21: 'Archiving Module including the decryptio...', 22: 'Speech Log Voice Recorder RHC', 23: 'SpeechLog (Expansion 4 Analog)', 24: 'SpeechLog (Expansion 8 IPs)'}, 'Engineer name': {1: 'Bilal Al-Noori', 2: 'Abdulrahman Hasan', 3: 'Hamzeh Shwemeh', 4: 'Hamzeh Shwemeh', 5: 'Hamzeh Shwemeh', 6: 'Bilal Al-Noori', 7: 'Yousif Rayyan', 8: 'Osama Gharbieh', 9: 'aladdin Shishani', 10: 'Osama Gharbieh', 11: 'CCE', 12: 'Abdulrahman Hasan', 13: 'Osama Gharbieh', 14: 'Bilal Al-Noori', 15: 'Bilal Al-Noori', 16: 'Abdulrahman Hasan', 17: 'Abdulrahman Hasan', 18: 'Abdulrahman Hasan', 19: 'Ahmad AlHasan', 20: 'Osama Gharbieh', 21: 'Abdellateef Ibrahim', 22: 'Abdulrahman Hasan', 23: 'CCE', 24: 'Abdulrahman Hasan'}, 'Related To': {1: 'Ministry of Tourism and Antiquities', 2: 'Al Rajhi Bank', 3: 'PSD', 4: 'Orange', 5: 'PSD', 6: 'Nabulsi - Burger Makers', 7: 'Orange Jo', 8: 'Housing Bank', 9: 'Orange Jo', 10: 'ISTD', 11: 'Unitel (Palace of Justice)', 12: 'Arab Bank', 13: 'Safwa Bank', 14: 'Housing Bank', 15: 'Housing Bank', 16: 'ABC BANK BH', 17: 'Al Rajhi Bank', 18: 'Social Security', 19: 'Extensya-SL', 20: 'Arab Bank', 21: 'Extensya-SL', 22: 'The Royal Hashemite Court (RHC)', 23: 'Global Telecommunication Technology (Alm...', 24: 'VTEL'}, 'status': {1: 'Completed', 2: 'In Progress', 3: 'Completed', 4: 'In Progress', 5: 'In Progress', 6: 'Completed', 7: 'Completed', 8: 'Completed', 9: 'Completed', 10: 'Completed', 11: 'On Hold', 12: 'Completed', 13: 'Completed', 14: 'Completed', 15: 'Completed', 16: 'Completed', 17: 'Archived', 18: 'Completed', 19: 'Completed', 20: 'Completed', 21: 'Completed', 22: 'Completed', 23: 'Completed', 24: 'Completed'}, 'Details': {1: 'Ab\nAbdelrahman Rasem\n2023-12-05 06:29 AM (12 days ago)', 2: 'Ab\nAbdelrahman Rasem\n2023-12-05 06:22 AM (12 days ago)', 3: 'Ab\nAbdelrahman Rasem\n2023-12-04 12:07 PM (12 days ago)', 4: 'Ab\nAbdelrahman Rasem\n2023-12-04 09:15 AM (13 days ago)', 5: 'Ab\nAbdelrahman Rasem\n2023-11-27 09:37 AM (20 days ago)', 6: 'Ab\nAbdelrahman Rasem\n2023-11-21 06:07 AM (26 days ago)', 7: 'Mo\nMohammad Farah\n2023-11-06 09:10 AM (1 month ago)', 8: 'Abdelrahman Rasem\n2023-11-01 12:08 PM (1 month ago)', 9: 'Mo\nMohammad Farah\n2023-10-22 06:32 AM (1 month ago)', 10: 'Abdelrahman Rasem\n2023-10-23 08:10 AM (1 month ago)', 11: 'Ab\nAbdelrahman Rasem\n2023-10-10 06:19 AM (2 months ago)', 12: 'Ab\nAbdelrahman Rasem\n2023-10-03 10:57 AM (2 months ago)', 13: 'Mohammad Farah\n2023-09-12 05:57 AM (3 months ago)', 14: 'Abdelrahman Rasem\n2023-08-29 06:16 AM (3 months ago)', 15: 'Abdelrahman Rasem\n2023-08-29 06:15 AM (3 months ago)', 16: 'Mo\nMohammad Farah\n2023-08-17 11:34 AM (4 months ago)', 17: 'Mo\nMohammad Farah\n2023-08-15 06:34 AM (4 months ago)', 18: 'Abdelrahman Rasem\n2023-06-26 11:20 AM (5 months ago)', 19: 'Ab\nAbdelrahman Rasem\n2023-06-22 09:47 AM (5 months ago)', 20: 'Abdelrahman Rasem\n2023-06-06 07:09 AM (6 months ago)', 21: 'Abdelrahman Rasem\n2023-06-11 08:36 AM (6 months ago)', 22: 'Ab\nAbdelrahman Rasem\n2023-04-10 10:22 AM (8 months ago)', 23: 'Mo\nMohammad Farah\n2023-02-22 08:52 AM (9 months ago)', 24: 'Mo\nMohammad Farah\n2023-01-23 3:20 PM (10 months ago)'}, 'Duration': {1: 49, 2: 84, 3: 81, 4: 59, 5: 101, 6: 21, 7: 55, 8: 42, 9: 49, 10: 35, 11: 59, 12: 56, 13: 54, 14: 42, 15: 42, 16: 40, 17: 395, 18: 56, 19: 56, 20: 35, 21: 26, 22: 56, 23: 58, 24: 31}}

# Summary
#
# The save_plot function is used to save a matplotlib plot as an image file in a specified directory.
# Example Usage
# save_plot(plt, 'project_status_bar_chart.png')
# This code will save the plt plot as an image file named 'project_status_bar_chart.png' in the 'Diagrams' directory.
# Code Analysis
# Inputs
# plot (matplotlib plot): The plot that needs to be saved as an image file.
# file_name (string): The name of the image file.
#
# Flow
# Get the current working directory using os.getcwd().
# Create the output directory path by appending '\Diagrams' to the current working directory.
# Save the plot as an image file in the output directory using plot.savefig().
# Close the plot using plot.close().
#
# Outputs
# None. The function only saves the plot as an image file.

def save_plot(plot, file_name, dpi=400, format=None, bbox_inches=None):
    """
    Save the given plot to a file.

    Args:
        plot (matplotlib.pyplot): The plot to be saved.
        file_name (str): The name of the file to save the plot to.
        dpi (int, optional): The resolution of the saved plot. Defaults to 400.
        format (str, optional): The file format of the saved plot. Defaults to None.
        bbox_inches (str, optional): The portion of the plot to save. Defaults to None.

    Returns:
        str: A status indicating whether the plot was saved successfully or not.
    """
    output_directory = os.getcwd() + '\Diagrams'  # This gets the current working directory
    try:
        os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist
        plot.savefig(os.path.join(output_directory, file_name), dpi=dpi, format=format, bbox_inches=bbox_inches)
        plot.close()
        return "Plot saved successfully"
    except Exception as e:
        logging.error(f"An error occurred while saving the plot: {e}")
        return f"An error occurred while saving the plot: {e}"


# Summary
# This code defines a function called Data_Visualization that generates various data visualizations using the
# pandas, matplotlib, and seaborn libraries. The function takes in a map_data parameter, which is expected to be a
# list of dictionaries representing project data. The function creates a directory for saving the generated diagrams
# if it doesn't already exist. It then converts the map_data into a pandas DataFrame and performs error handling in
# case of any exceptions. The function then proceeds to generate multiple visualizations, such as bar charts,
# pie charts, histograms, box plots, line charts, violin plots, and stacked bar charts, based on different aspects of
# the project data.
#
# Example Usage map_data = [ {'status': 'Completed', 'Related To': 'Marketing', 'Duration': 30,
# 'Engineer name': 'John', 'DEP': 'Sales'}, {'status': 'In Progress', 'Related To': 'Sales', 'Duration': 45,
# 'Engineer name': 'Jane', 'DEP': 'Sales'}, {'status': 'Completed', 'Related To': 'Finance', 'Duration': 60,
# 'Engineer name': 'John', 'DEP': 'Finance'}, ... ]
#
# Data_Visualization(map_data) Code Analysis Inputs map_data (list
# of dictionaries):
# A list of dictionaries representing project data. Each dictionary should contain keys such as
# 'status', 'Related To', 'Duration', 'Engineer name', and 'DEP'.
#
# Flow
# Create a directory named "Diagrams" if it doesn't already exist.
# Convert the map_data into a pandas DataFrame.
# Generate a bar chart showing the distribution of project statuses.
# Generate a pie chart showing the distribution of projects by their "Related To" category.
# Generate a histogram showing the distribution of project durations.
# Generate a box plot showing the project durations grouped by project status.
# Generate a count plot showing the count of projects for each engineer.
# Generate a line chart showing the project durations over time.
# Generate a pair plot showing pairwise relationships between numerical features.
# Generate a violin plot showing the project durations grouped by department.
# Generate a stacked bar chart showing the project statuses for each engineer.
#
# Outputs Diagrams: Various diagrams saved in the "Diagrams" directory, including bar charts, pie charts, histograms,
# box plots, line charts, violin plots, and stacked bar charts.
def Data_VisualizationDiagrams(map_data):
    """
    Generate various data visualizations based on the given map_data.

    Args:
        map_data (list): List of data for visualization.

    Returns:
        str: A message indicating the completion status of the data visualization.
    """
    # Create a directory for saving the diagrams if it doesn't exist
    output_directory = os.path.join(os.getcwd(), 'Diagrams')
    os.makedirs(output_directory, exist_ok=True)
    logging.debug('Start Creating Diagrams')
    if len(map_data) == 0:
        return "Data visualization completed successfully"

    try:
        data = pd.DataFrame(map_data)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        # Handle the exception or take appropriate action
        return "Data visualization failed"

    try:
        # Visualization 1: Bar Chart for Project Status
        plt.figure(figsize=(24, 12))
        sns.countplot(x='status', data=data, order=data['status'].value_counts().index)
        plt.xticks(rotation=45)
        plt.xlabel('Project Status')
        plt.ylabel('Count')
        plt.title('Distribution of Project Status')
        save_plot(plt, os.path.join(output_directory, 'project_status_bar_chart.png'))  # Save the chart
        logging.debug("project_status_bar_chart Finished ")

        # Visualization 2: Pie Chart for Related To
        plt.figure(figsize=(16, 16))
        data['Related To'].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title('Distribution of Projects by Related To')
        plt.ylabel('')
        save_plot(plt, os.path.join(output_directory, 'related_to_pie_chart.png'))  # Save the chart
        logging.debug("related_to_pie_chart Finished")

        # Visualization 3: Histogram for Project Duration
        plt.figure(figsize=(20, 12))
        sns.histplot(data['Duration'], bins=20, kde=True)
        plt.xlabel('Project Duration (Days)')
        plt.ylabel('Count')
        plt.title('Distribution of Project Durations')
        save_plot(plt, os.path.join(output_directory, 'project_duration_histogram.png'))  # Save the chart
        logging.debug("project_duration_histogram Finished")

        # Visualization 4: Box Plot for Project Duration by Status
        plt.figure(figsize=(24, 12))
        sns.boxplot(x='status', y='Duration', data=data, order=data['status'].value_counts().index)
        plt.xticks(rotation=45)
        plt.xlabel('Project Status')
        plt.ylabel('Project Duration (Days)')
        plt.title('Project Duration by Status')
        save_plot(plt, os.path.join(output_directory, 'project_duration_box_plot.png'))  # Save the chart
        logging.debug("project_duration_box_plot Finished")

        # Visualization 5: Count of Projects by Engineer
        plt.figure(figsize=(24, 12))
        sns.countplot(x='Engineer name', data=data, order=data['Engineer name'].value_counts().index)
        plt.xticks(rotation=45)
        plt.xlabel('Engineer Name')
        plt.ylabel('Count')
        plt.title('Count of Projects by Engineer')
        save_plot(plt, os.path.join(output_directory, 'count_of_projects_by_engineer.png'))  # Save the chart
        logging.debug("count_of_projects_by_engineer Finished")

        # Visualization 6: Line Chart for Project Duration Over Time
        plt.figure(figsize=(24, 12))
        sns.lineplot(x=data.index, y='Duration', data=data)
        plt.xlabel('Project Order')
        plt.ylabel('Project Duration (Days)')
        plt.title('Project Duration Over Time')
        plt.xticks(rotation=45)
        save_plot(plt, os.path.join(output_directory, 'project_duration_over_time_line_chart.png'))  # Save the chart
        logging.debug("project_duration_over_time_line_chart Finished")

        # # Visualization 7: Heatmap for Correlation Matrix
        # plt.figure(figsize=(10, 6))
        # correlation_matrix = data.corr()  # Assuming you have numerical columns
        # sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        # plt.title('Correlation Heatmap')
        # save_plot(plt, os.path.join(output_directory, 'correlation_heatmap.png'))  # Save the chart

        # Visualization 8: Pair Plot for Pairwise Relationships
        plt.figure(figsize=(120, 240))  # Increase the figure size for a bigger image
        sns.pairplot(data, hue='status', diag_kind='kde', height=4)  # Adjust height for clearer plots
        plt.title('Pair Plot of Numerical Features')
        save_plot(plt, os.path.join(output_directory, 'pair_plot.png'))  # Increase dpi for a clearer image
        logging.debug("pair_plot Finished")

        # Visualization 9: Violin Plot for Project Duration by Department (DEP)
        plt.figure(figsize=(48, 24))
        sns.violinplot(x='DEP', y='Duration', data=data)
        plt.xlabel('Department')
        plt.ylabel('Project Duration (Days)')
        plt.title('Project Duration by Department')
        plt.xticks(rotation=45)
        save_plot(plt,
                  os.path.join(output_directory, 'project_duration_by_department_violin_plot.png'))  # Save the chart
        logging.debug("project_duration_by_department_violin_plot Finished")

        # Visualization 10: Stacked Bar Chart for Project Status by Engineer
        plt.figure(figsize=(60, 30))
        status_by_engineer = data.groupby(['Engineer name', 'status']).size().unstack(fill_value=0)
        status_by_engineer.plot(kind='bar', stacked=True)
        plt.xlabel('Engineer Name')
        plt.ylabel('Count')
        plt.title('Project Status by Engineer')
        plt.xticks(rotation=45)
        plt.legend(title='Project Status', loc='upper right')
        save_plot(plt,
                  os.path.join(output_directory, 'project_status_by_engineer_stacked_bar_chart.png'))  # Save the chart
        logging.debug('project_status_by_engineer_stacked_bar_chart Finished')





        return "Data visualization completed successfully"
    except:
        return "Data visualization failed"


Data_VisualizationDiagrams(mp)
