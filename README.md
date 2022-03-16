# Power-automate
UPCEA 2022 Poster Presentation - Boosting your online administration efficiency by automating complex course operations for a large online program

This would be addtional inforamtion how to autoamte data reports for assignment extension.


1. Reference the date sheet
All the assignment extension reocrds are stored on the internal Google sheet, and we can't share some of information on the Public. 

  a. We created a new Google sheet and reference to the extension record sheet and filter out all the senstive informaiton. 
  
   =IMPORTRANGE("your sheet url","Sheet1!A:H")

  b. Then we public the Google sheet so everyone can download as csv file from the sheet url
  
  
  
 2. Develop the Python script to pull the data from the Google sheet URL every week - please see the extension.py


 3. Set up the auto run by using Crontab - https://crontab.guru/#0_6_*_*_1
