import pandas as pd
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile
import matplotlib.pyplot as plt
import seaborn as sns
import os

def test_view(request):
    return render(request, 'data_analysis/upload.html')

def handle_uploaded_file(file):
    try:
        df = pd.read_csv(file)

        # Perform basic data analysis
        head = df.head()
        describe = df.describe()
        null_values = df.isnull().sum()

        # Convert Series to DataFrame if necessary
        if isinstance(head, pd.Series):
            head = head.to_frame().to_html()
        else:
            head = head.to_html()

        if isinstance(describe, pd.Series):
            describe = describe.to_frame().to_html()
        else:
            describe = describe.to_html()

        if isinstance(null_values, pd.Series):
            null_values = null_values.to_frame().to_html()
        else:
            null_values = null_values.to_html()

        # Generate plots
        plot_urls = []
        for column in df.select_dtypes(include=['float64', 'int64']).columns:
            plt.figure()
            sns.histplot(df[column].dropna(), kde=False)
            plot_path = f'static/plots/{column}.png'
            plt.savefig(plot_path)
            plot_urls.append(plot_path)

        return head, describe, null_values, plot_urls, None  # None as error_message

    except Exception as e:
        error_message = str(e)
        return None, None, None, [], error_message  # Return empty or None for other values and the error_message

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            head, describe, null_values, plot_urls, error_message = handle_uploaded_file(request.FILES['file'])
            if error_message:
                # Handle error message here, maybe redirect back to upload form with error message
                return render(request, 'data_analysis/upload.html', {'form': form, 'error_message': error_message})

            # Proceed with rendering results page
            return render(request, 'data_analysis/results.html', {
                'head': head,
                'describe': describe,
                'null_values': null_values,
                'plot_urls': plot_urls,
            })
    else:
        form = UploadFileForm()
    return render(request, 'data_analysis/upload.html', {'form': form})
