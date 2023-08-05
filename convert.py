import re
import PyPDF2
import datetime
from tkinter import filedialog
import tkinter as tk

def extract_text_from_pdf(input_file_path):
    with open(input_file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def find_bill_number(text):
    pattern = r'Bill NO\s*([A-Za-z0-9]+)'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None

def find_bill_date(text):
    pattern = r'Statement Date:\s*(\d{1,2}[-/ ]\w{3,9}[-/ ]\d{2,4})'
    match = re.search(pattern, text)
    if match:
        date_str = match.group(1).replace('-', ' ').replace('/', ' ')
        return datetime.datetime.strptime(date_str, "%d %b %Y").strftime("%d %B %Y")
    return None

def find_bill_period(text):
    pattern = r'Statement Period:\s*([\d -A-Za-z]+)\s*-\s*([\d -A-Za-z]+)'
    match = re.search(pattern, text)
    if match:
        return f"{match.group(1)} - {match.group(2)}"
    return None

def find_total_amount(text):
    pattern = r'Total Amount\s*` ([\d.]+)'
    match = re.search(pattern, text)
    if match:
        return float(match.group(1))
    return None

def find_gst_registration_number(text):
    pattern = r'GST registration no\.\s*:\s*([A-Z0-9]+)'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None

def find_taxes_amount(text):
    pattern = r'Taxes \(GST\).*?` ([\d.]+)'
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        return float(match.group(1))
    return None

def process_pdf_file(file_path):
    pdf_text = extract_text_from_pdf(file_path)
    if pdf_text:
        bill_number = find_bill_number(pdf_text)
        bill_date = find_bill_date(pdf_text)
        bill_period = find_bill_period(pdf_text)
        total_amount = find_total_amount(pdf_text)
        gst_registration_number = find_gst_registration_number(pdf_text)
        taxes_amount = find_taxes_amount(pdf_text)
        taxes_half = taxes_amount / 2

        print(f"File: {file_path}")
        print(f"Bill NO: {bill_number}")
        print(f"Bill Date: {bill_date}")
        print(f"Bill Period: {bill_period}")
        print(f"Total Amount: {total_amount}")
        print(f"GST Registration Number: {gst_registration_number}")
        print(f"Taxes Half Amount (CGST/SGST): {taxes_half}")
        print()
    else:
        print(f"Extraction from PDF failed for {file_path}.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if file_paths:
        for file_path in file_paths:
            process_pdf_file(file_path)
    else:
        print("No files selected.")


# pip3 install PyPDF2
# pip3 install tkinter
