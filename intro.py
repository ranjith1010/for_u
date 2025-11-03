from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Frame, PageTemplate
from reportlab.pdfgen import canvas

# --- CONFIG ---
PAGE_WIDTH, PAGE_HEIGHT = A4
PDF_NAME = "Discrepancy_Report.pdf"
IMAGE_PATH = "mountain.jpg"  # <-- replace with your image path (or use the one you uploaded)

# --- HEADER AND FOOTER DRAWING FUNCTIONS ---
def draw_header_footer(canvas, doc):
    # Header text
    canvas.setFont("Helvetica", 10)
    canvas.setFillColor(colors.black)
    canvas.drawString(280, PAGE_HEIGHT - 40, "C1")

    # Header bar below "C1"
    canvas.setFillColor(colors.black)
    canvas.rect(298, PAGE_HEIGHT - 50, 1, 15, stroke=0, fill=1)

    # Footer image
    footer_img_width = 150
    footer_img_height = 90
    footer_img_x = (PAGE_WIDTH - footer_img_width) / 2
    footer_img_y = 40  # bottom margin

    try:
        canvas.drawImage(IMAGE_PATH, footer_img_x, footer_img_y, width=footer_img_width, height=footer_img_height)
    except:
        print("⚠️ Footer image not found at:", IMAGE_PATH)

# --- DOCUMENT SETUP ---
doc = SimpleDocTemplate(
    PDF_NAME,
    pagesize=A4,
    topMargin=1.5 * inch,
    bottomMargin=1.5 * inch
)

# --- CONTENT STYLES ---
title_style = ParagraphStyle(
    name="TitleStyle",
    fontName="Helvetica-Bold",
    fontSize=18,
    textColor=colors.HexColor("#A30000"),  # deep red
    alignment=1,  # center
    spaceAfter=6
)

subtitle_style = ParagraphStyle(
    name="SubtitleStyle",
    fontName="Helvetica",
    fontSize=12,
    textColor=colors.HexColor("#A30000"),
    alignment=1,  # center
    spaceAfter=20
)

# --- CONTENT ---
story = []
story.append(Spacer(1, 3 * inch))  # push content down
story.append(Paragraph("DISCREPANCY ANALYSIS", title_style))
story.append(Paragraph("Client Name", subtitle_style))
story.append(Spacer(1, 2 * inch))  # spacing before footer image

# --- APPLY HEADER/FOOTER TEMPLATE ---
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
template = PageTemplate(id='main', frames=frame, onPage=draw_header_footer)
doc.addPageTemplates([template])

# --- BUILD PDF ---
doc.build(story)
print(f"✅ PDF created successfully: {PDF_NAME}")
