from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=10)
pdf.cell(100,100, txt= "Social Brothers Advice Report", ln=1, align = "C")
pdf.output("Advice.pdf")
