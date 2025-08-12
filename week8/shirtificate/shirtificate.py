from fpdf import FPDF
from fpdf.enums import Align
# Specifications
# Shirt image centered horizontally
# User's name should be on top of the shirt, in white text

class PDF(FPDF):
    def header(self):
        # Setting font
        self.set_font('Courier', style='B', size=36)
        # Printing title
        title_w = self.get_string_width("CS50 Shirtificate")
        self.set_xy((210 - title_w) / 2, 20)
        self.cell(title_w, 10, "CS50 Shirtificate", align='C')
        # linebreak for the header
        self.ln(30)

# Prompt the user for thier name
name = input("Name: ").title().strip()

text = f"{name} took CS50"

# make a PDF and imbed the png image inside it
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False)

pdf.add_page()
pdf.image("shirtificate.png", x=0, y=60, w=210)

# Font size and color
pdf.set_font('Courier', style='B', size=20)
pdf.set_text_color(255, 255, 255)

# Print text on the shirt
text_w = pdf.get_string_width(text)
pdf.set_xy((210 - text_w) / 2, 140)
pdf.cell(text_w, 10, text, align="C")

pdf.output("shirtificate.pdf")



