import PyPDF2

# Open the PDF file in read-binary mode
with open('engg_cutoff_gen.pdf', 'rb') as f:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(f)
    
    # Get the number of pages in the PDF document
    num_pages = pdf_reader.getNumPages()

    # Loop through each page in the PDF document
    for page_num in range(num_pages):
        # Get the page object for the current page
        page = pdf_reader.getPage(page_num)
        
        # Extract the text from the page
        text = page.extractText()
        
        # Split the text into a list of lines
        lines = text.splitlines()
        
        # Loop through each line in the list of lines
        for line in lines:
            # Do something with the line (e.g., print it to the console)
            print(line)
            print('\n')
