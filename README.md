# CSV-Analysis-Project-Using-Django-
Project Overview:

The project aims to provide a web application using Django for analyzing CSV files uploaded by users. 
It includes features for basic data analysis and visualization.

Key Features:

*File Upload:

    Users can upload CSV files via a web interface.
    The uploaded files are saved on the server for processing.
    
*Data Analysis:

     The application reads the uploaded CSV files and performs basic data analysis using pandas.
     
*Data Visualization:
      The application generates histograms for numeric columns in the CSV file using matplotlib and seaborn.
      The generated plots are saved as static images and displayed to the user.
      
*Result Presentation:
      The results of the data analysis and visualization are presented on a web page.
      Users can view the data summary, null value counts, and generated plots directly on the results page.
      
Technical Stack:

Django Framework: Provides the web application structure, handling URL routing, views, and templates.

Pandas: Used for data manipulation and analysis, particularly reading CSV files and performing basic statistics (head(), describe(), etc.).

Matplotlib and Seaborn: Used for generating histograms to visualize data distributions.

Workflow:

Upload Form: Users can upload CSV files using a web form (upload.html).

File Handling: Django views handle the uploaded file, save it to the server, and perform data analysis (handle_uploaded_file function).

Data Analysis: Pandas processes the CSV file to generate summary statistics (head(), describe(), null values count) and matplotlib/seaborn creates histograms.

Results Display: Results are displayed on a results page (results.html), showing tables (converted to HTML) and plots (linked as static files).

Error Handling:

Errors during file upload or data analysis are caught and displayed to the user (error_message variable in upload_file view).
Users are informed of issues such as file format errors, missing data, or internal server errors.

Project Setup Instructions:-
1.Project Initialization
Create Django Project:django-admin startproject csv_analysis_project

2.Navigate to Project Directory:
cd csv_analysis_project

3.Create a Django App:
python manage.py startapp data_analysis

4.Define Models and Forms:
 models (UploadedFile) and forms (UploadFileForm) in data_analysis/models.py and data_analysis/forms.py 
 
5.Configure Templates and Static Files:

6.Adjust settings.py

7.Migrate Database:
python manage.py makemigrations
python manage.py migrate

8.Update Views (data_analysis/views.py):

9.Handle File Upload Logic:
Use pandas for data analysis (handle_uploaded_file function) and matplotlib/seaborn for generating plot

10.Create Templates:
Create upload.html for file upload form.
Create results.html for displaying data analysis results including tables and plots.

11.Run Django Development Server:
python manage.py runserver
