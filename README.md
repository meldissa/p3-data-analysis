# Economics Data Analysis Tool

[View published application on Heroku](https://p3-data-analysis.herokuapp.com/).

[View Google Sheets Data used for the project](https://docs.google.com/spreadsheets/d/1q9xDlLLc2jBNZncPqXOUpQ4JlAWxshT-2HE1O2b6yNc/edit?usp=sharing).

![](docs/images/responsive-img.png)

Image from [Am I Responsive](http://ami.responsivedesign.is/).

## Project Overview

The Economics Data Analysis Tool is a terminal based application that allows for data calculation and plotting using Google Sheets. This has been created as part of my Project 3 for Code Institute.

## Table of Contents

1. [User Experience (UX)](#ux)
    * [Strategy](#strategy)
        * [Project Goals](#project-goals)
        * [User Stories](#user-stories)
    * [Scope](#scope)
    * [Design](#design)
    * [Skeleton](#skeleton)
        * [Flowchart](#flowchart)
2. [Features](#features)
    * [Current Features](#current-features)
    * [Future Features](#future-features)
3. [Technologies Used](#tech-used)
4. [Testing](#testing)
    * [User Stories Testing](#user-testing)
    * [Validation Testing](#validation-testing)
    * [Known Issues and Resolutions](#issues)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

## User Experience (UX) <a name="ux"></a>

## Strategy <a name="strategy"></a>

### Project Goals <a name="project-goals"></a>

The main goal for the Economics Data Analysis Tool is to provide a terminal based application which allows the user to import data from Google Sheets, and complete various calculations with the scope for plotting the data as the end result.

The main target audience for this application is a fictional economist who is interested in analysis various economic data for the UK over the past 10 years. The application would allow for such analysis by completing various calculations and exporting this data back to Google Sheets, as well as allowing the economist to plot data based on their selection. 

### User Stories <a name="user-stories"></a>

* __Site User Goals:__

    * I want to import data from Google Sheets.
    * I want to calculate the total sum for each column of data and update the worksheet.
    * I want to calculate the average for each column of data and update the worksheet.
    * I want to calculate the estimate for each column of data for the next year and update the worksheet.
    * I want to plot the data across all available 'Years' for the selected column inclusive of the estimate data and choose the plot type.
    * I want to view the underlying data for the plotted output.

* __Site Owner Goals:__

    * I want to provide an application which allows user to import data from Google Sheets.
    * I want to provide an application which allows for data calculation for imported data (sum, average, estimate).
    * I want to provide an application which allows user to plot data based on their selection.
    * I want to provide an application which allows user to view the data selected for the plotting.


## Scope <a name="scope"></a>

To achieve the strategy goals, I want to implement the following features:

* A function which will import the data from Google Sheets.
* A function which will calculate the total sum and update the worksheet.
* A function which will calculate the average and update the worksheet.
* A function which will calculate the estimate for next year and update the worksheet.
* A function which will allow the user to select column to plot data for y-axis.
* A function which will allow user to select the plot type from the listed options.
* A function which will plot data based on the selection and confirm to the user that this has been plotted, in addition displaying the data selected for the plot on the terminal.

## Design <a name="design"></a>

As this is terminal based application, the design is kept as the basic terminal colours and fonts as per the template used for the deployed project.

## Skeleton <a name="skeleton"></a>

### Flowchart <a name="flowchart"></a>

Due to the project being a terminal based application, no wireframes were created for this. Instead a flowchart has been created to display the application process.

Flowchart was created using [diagrams.net](https://www.diagrams.net/).

![](docs/images/flowchart.png)

## Features <a name="features"></a>

### Current Features <a name="current-features"></a>


### Future Features <a name="future-features"></a>


## Technologies Used <a name="tech-used"></a>

For this project the main language used is __Python__.

I have also utilised the following frameworks, libraries, and tools:

* [Pandas](https://pandas.pydata.org/): 
    * Pandas Library has been used to allow for the creation of DataFrames and for plotting data.
* [Plotext](https://pypi.org/project/plotext/):
    * Plotext has been used to for plotting data in the terminal.
* [GitPod](https://www.gitpod.io/): 
    * I used GitPod as the IDE for this project and Git has been used for Version Control.
* [GitHub](https://www.github.com/): 
    * GitHub has been used to create a repository for the project and receive updated commits from GitPod.
* [Heroku](https://www.heroku.com/): 
    * Heroku has been used to create a repository to host the project and receive updated commits from GitPod.
* [gspread](https://pypi.org/project/gspread/): 
    * gspread has been used to access, update and manipulate data from Google Sheets.
* [Google Cloud Platform](https://cloud.google.com/): 
    * Google Cloud Platform has been used for APIs and credentials to be able to access Google Sheets with the relevant data.
* [World Bank Data](https://data.worldbank.org/): 
    * World Bank was used as a source of the data for the economic indicators used in this project.
* [PEP8 Online Validation Service](http://pep8online.com/): 
    * The PEP8 Online Validation Service was used to validate the Python document for this project and to identify any issues with the code.
* [StackOverflow](https://stackoverflow.com/): 
    * StackOverflow was used to assist with any troubleshooting issues during the course of the project.
* [diagrams.net](https://www.diagrams.net/):
    * diagrams.net was used to create the flowchart for this project.
* [Am I Responsive](http://ami.responsivedesign.is/):
    * Am I Responsive was used to create the header image for the README file.

## Testing <a name="testing"></a>

### User Stories Testing <a name="user-testing"></a>


### Validation Testing <a name="validation-testing"></a>

To test the Python code, I used the __PEP8 Online Validation Service__:

![](docs/images/python-testing.png)

No issues were detected with the code.

This website was tested on the following browsers:

* Google Chrome
* Safari
* Mozilla Firefox

Although this is a web application, it is visible on mobile and tablets, even though it is not responsive. This web application was also tested on the following devices:

* iPhone 11 Pro
* iPad Pro
* MacBook Air

### Known Issues and Resolutions <a name="issues"></a>


## Deployment <a name="deployment"></a>

The project was developed using GitPod and was deployed via the GitHub repository to Heroku.

The following steps were followed to deploy this project:

1. From the Heroku dashboard, select 'New' in the top right hand corner.
2. Click 'Create new app'.
3. Enter the app name and choose region as Europe. 
4. Click 'Create app'.
5. Select the 'Settings' tab, and scroll down to 'Buildpacks'. 
6. Add 'Python' and save changes, then add 'Node.js' and save the changes again.
7. Scroll down to 'Config Vars' section, and add the 'KEY' and 'PORT' for the credentials and additional 8000 port for running the app.
8. At the top of the page, click on the 'Deploy' section.
9. Select Github as deployment method.
10. Select 'Connect to Github', and locate the repository name and click on 'Connect' to link my Heroku app to my Github repository code.
11. Scroll further down, select 'Enable Automatic Deploys' and then select 'Deploy Branch' to deploy project.
12. After it has successfully deployed a 'view' button appears on screen and when clicked opens the deployed application.

## Credits <a name="credits"></a>

### Content

The economic data used for the project was obtained from the [World Bank Data](https://data.worldbank.org/) for the following parameters:

* Unemployment, total (% of total labor force) (modeled ILO estimate)
* Exports of goods and services (% of GDP)
* GDP growth (annual %)
* GDP per capita growth (annual %)
* General government final consumption expenditure (% of GDP)
* Imports of goods and services (% of GDP)

The data covered was for UK over 10 years from 2010 to 2020.

### Code

* The Code Institute Love Sandwiches tutorial for Python was used to assist with creating this project. Certain code was borrowed and used for the run.py file, in addition to some of the borrowed code being customised specifically for the project and new code added by me.

## Acknowledgements <a name="acknowledgements"></a>

* I would like to thank my family and friends for their support throughout this project.
* My mentor, Guido Cecilio, for being of great support and providing valuable guidance and feedback throughout this process.
