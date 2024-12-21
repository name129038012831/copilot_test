import fitz  # PyMuPDF

def extract_economic_events(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")
        
        # Process the text to extract economic event data
        lines = text.split('\n')
        for line in lines:
            # Assuming the data is structured in a specific format
            # Adjust the parsing logic based on the actual PDF content
            if "Event Name" in line:
                continue  # Skip header line
            parts = line.split()
            if len(parts) >= 6:
                date = parts[0]
                time = parts[1]
                event_name = " ".join(parts[2:-3])
                actual = parts[-3]
                forecast = parts[-2]
                previous = parts[-1]
                print(f"Date: {date}, Time: {time}, Event: {event_name}, Actual: {actual}, Forecast: {forecast}, Previous: {previous}")

# Example usage
pdf_path = '2.pdf'
extract_economic_events(pdf_path)