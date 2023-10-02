import logging
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


mp = {'project name': {1: 'Speech Log expansion', 2: 'PMP (Expansion Telesales)',
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
      }


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


def Data_Visualization(map_data):
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
        save_plot(plt, os.path.join(output_directory, 'project_duration_by_department_violin_plot.png'))  # Save the chart
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
        save_plot(plt, os.path.join(output_directory, 'project_status_by_engineer_stacked_bar_chart.png'))  # Save the chart
        logging.debug('project_status_by_engineer_stacked_bar_chart Finished')

        return "Data visualization completed successfully"
    except:
        return "Data visualization failed"


Data_Visualization(mp)
