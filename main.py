# ==============================================
# ====== Welcome to Python PDF Generator =======
# ==============================================
# = You can generate random PDF files. This is =
# ======== good for Scribd downloads. ==========
# ==============================================
# = Made by by Masterbros Developers, Barnabás =
# ==============================================
# ==============================================
# ===============     v1.3     =================
# ==============================================

# Import modules
# The following modules are needed for the PDF generation
from reportlab.lib.pagesizes import A4 # Used for defining the PDF page size
from reportlab.pdfgen import canvas # Used for generating the PDF file
from random import choice # Used for generating random strings
from string import ascii_letters, digits # Used for generating random strings
import random # Used for generating random numbers
import os # Used for clearing the console


def clear():
    # Clear the console
    # This function is used for clearing the console before displaying the banner
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def banner():
    # Display the banner
    # This function is used for displaying the banner
    clear()
    print("""
 _____  _____  ______        _ _    _ _   _ _  __
|  __ \|  __ \|  ____|      | | |  | | \ | | |/ /
| |__) | |  | | |__         | | |  | |  \| | ' / 
|  ___/| |  | |  __|    _   | | |  | | . ` |  <  
| |    | |__| | |      | |__| | |__| | |\  | . \ 
|_|    |_____/|_|       \____/ \____/|_| \_|_|\_\ """)

    print(" by Masterbros Developers, Barnabás")
    print()
    print()

# Functions
def random_string(length):
    # Generate a random string
    # This function is used for generating a random string
    return ''.join(random.choice(ascii_letters + digits) for _ in range(length))

def create_junk_pdf(file_name, content="This is a really important PDF file."):
    # Create a junk PDF file
    # This function is used for creating a junk PDF file
    # Set up PDF document
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # Add some junk content
    for y in range(100, int(height), 10):
        c.drawString(100, y, content + random_string(25))

    # Save the PDF
    c.showPage()
    c.save()


def generatepdf(n):
    # Generate the specified number of junk PDF files
    try:
        # Loop through the specified number of times
        for i in range(1, (int(n)+1)):
            file_name = f"book_{i}.pdf"
            # Generate a random content string
            content = f"This is book number {i}. "
            # Create the PDF file
            create_junk_pdf(file_name, content)
        # Display the banner
        banner()
        # Print a success message
        print(f"{n} junk PDF files created successfully.")
    except Exception as e:
        # Print an error message if an error occurs
        print(f"An error occurred: {e}")

def main():
    # Display the banner
    banner()
    # Get the number of PDF files to generate
    generatepdf(input("How many PDF files do you want to generate? "))

#Main
main()