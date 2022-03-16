# Power-automate
UPCEA 2022 Poster Presentation - Boosting your online administration efficiency by automating complex course operations for a large online program

This would be additional information on how to automate data reports for assignment extension.


1. Reference the date sheet
All the assignment extension records are stored on the internal Google sheet, and we can't share some of the information with the Public. 

      a. We created a new Google sheet and reference to the extension record sheet and filter out all the sensitive information, and only keep course ID, Stats and Submission time. 

       =IMPORTRANGE("your sheet url","Sheet1!A:H")

      b. Then we public the Google sheet so everyone can download as csv file from the sheet url,so the data will be accessible for our Python Script. 
  
  
  
 2. Develop the Python script to pull the data from the Google sheet URL every week - please see the extension.py
 
        a. We use Slack to publish the chart every Monday with team members, so you will need to set up your Slack API Token.
        b. The script is hosted at the internal Linux server


 3. Set up the auto run by using Crontab - https://crontab.guru/#0_6_*_*_1
