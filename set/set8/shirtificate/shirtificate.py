from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(
    w=None,
    h=10,
    text='CS50 Shirtificate',
    align="C",
    center=True,)


img_w = 180
x_center = (pdf.w - img_w) / 2
pdf.image("shirtificate.png", x=x_center, y=60, w=img_w)

pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 120)
pdf.cell(0, 10, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")

