# TeleCom-Data-Analysis
This is a 10Academy's Week 1 Batch 6 challenge and this repository analyzes a telecommunication dataset that contains useful information about the customers &amp; their activities on the network.

## Use Case
You are working for a wealthy investor that specializes in purchasing assets that are undervalued. The investor is interested in purchasing TellCo, an existing mobile service provider in the Republic of Pefkakia. You will analyze a telecommunication dataset that contains useful information about the customers & their activities on the network.
### Getting Started
This repository aims to address the following points:
* User Overview analysis
  * Data Exploration
  * Data Cleaning/Manipulation
  * Uni-Variate and Multivariate Analysis
  * Outlier Treatment
  * Correlation Analysis
  * Feature Engineering
* User Engagement analysis
  * computer engagement score
  * 
  * 
* User Experience analysis
  * compute experience score
  * 
  * 
* User Satisfaction analysis
  * compute satisfaction score
  * 
  * 

## Project Structure
The repository has a number of files including python scripts, jupyter notebooks, pdfs and text files. Here is their structure with a brief explanation.

### data:
- the folder where the dataset csv files are stored

### models:
- the folder where trained ML model files are stored

### tests:
- the folder where tests for the python scripts are written

### notebooks:
- `Task-0-Data_Exploration _and_Analysis.ipynb`: a jupyter notebook that explore, prepare and perform a general data analysis
- `Task-1-User_Overview_Analysis.ipynb`: a jupyter notebook that analyzes telecom users' behaviour
- `Task-2-User_Engagement_Analysis.ipynb`: a jupyter notebook that analyzes the engagement of users
- `Task-3-User_Experience_Analysis.ipynb`: a jupyter notebook that analyzes telecom users' experience
- `Task-4-User_Satisfaction_Analysis.ipynb`: a jupyter notebook that analyzes the satisfaction of users

### scripts
- `data_cleaning.py`: a python script for cleaning pandas dataframes
- `data_description.py`: a python script for providing information abouthe the pandas dataframe
- `data_loading.py`: a python script for loading csv and excel files to a dataframe
- `data_plots.py`: a python script(utility functions) for plotting dataframes
- `user_overview.py`: a python script that helps `Task-1-User_Overview_Analysis.ipynb`:

### root folder
- `app.py`: entry point for the streamlit application
- `Dockerfile`: a configuration file for Docker
- `requirements.txt`: a text file lsiting the projet's dependancies
- `Procfile`: a configuration file for the application deployment
- `.gitignore`: a text file listing files and folders to be ignored
- `setup.py`: a configuration file for installing the scripts as a package
- `README.md`: Markdown text with a brief explanation of the challenge project and the repository structure.

## Installation guide
```
git clone https://github.com/YohansSamuel/TeleCom-Data-Analysis.git
cd TeleCom-Data-Analysis
pip install -r requirements.txt
```



