import os
import re
import pandas as pd
from PyPDF2 import PdfReader

def extract_economic_data(pdf_file):
    # Initialize empty lists to store extracted data
    times = []
    events = []
    actuals = []
    forecasts = []
    previous_values = []

    # Open the PDF file and read its contents
    with open(pdf_file, 'rb') as f:
        pdf_reader = PdfReader(f)
        num_pages = len(pdf_reader.pages)

        for page in range(num_pages):
            # Get the text from the current page
            page_text = pdf_reader.pages[page].extract_text()

            # Use regular expressions to match desired data format
            pattern = r"(\d{1,2}:\d{2})\s+([A-Z]+)\s+(\w+)\s*\((?P<actual>-?\d+\.\d*[M%])\)\s*(?P<forecast>\S+)\s*\((?P<previous>-?\d+\.\d*[M%])\)"
            matches = re.findall(pattern, page_text)

            # Extract data from the matched patterns
            for match in matches:
                times.append(match[0])
                events.append(match[1])
                actuals.append(match['actual'])
                forecasts.append(match['forecast'])
                previous_values.append(match['previous'])

    return {
        'Time': times,
        'Event Name': events,
        'Actual': actuals,
        'Forecast': forecasts,
        'Previous': previous_values
    }

# Example usage:
pdf_file = '2.pdf'
data = extract_economic_data(pdf_file)
df = pd.DataFrame(data)

print(df)