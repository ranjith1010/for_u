import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# 1. Create charts using matplotlib
# Pie chart
labels = ['Product A', 'Product B', 'Product C']
sizes = [40, 35, 25]
plt.figure(figsize=(4, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Product Sales Share')
plt.savefig('pie_chart.png')
plt.close()

# Bar chart
categories = ['Q1', 'Q2', 'Q3', 'Q4']
values = [150, 200, 180, 220]
plt.figure(figsize=(5, 4))
plt.bar(categories, values)
plt.title('Quarterly Sales')
plt.xlabel('Quarter')
plt.ylabel('Revenue ($)')
plt.savefig('bar_chart.png')
plt.close()

# Line plot
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
profits = [20, 25, 22, 27, 30, 35]
plt.figure(figsize=(5, 4))
plt.plot(months, profits, marker='o')
plt.title('Profit Growth Over Months')
plt.xlabel('Month')
plt.ylabel('Profit ($k)')
plt.grid(True)
plt.savefig('line_plot.png')
plt.close()

# 2. Create a PDF and add content using reportlab
pdf_filename = "Business_Report.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=A4)

styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("<b>Business Performance Report</b>", styles['Title']))
story.append(Spacer(1, 0.2 * inch))

# Introduction text
intro_text = """
This report provides a visual summary of the business performance 
for the recent period. It includes data on product sales, 
quarterly revenue, and profit growth trends.
"""
story.append(Paragraph(intro_text, styles['Normal']))
story.append(Spacer(1, 0.3 * inch))

# Pie chart
story.append(Paragraph("<b>1. Product Sales Share</b>", styles['Heading2']))
story.append(Image('pie_chart.png', width=4*inch, height=4*inch))
story.append(Spacer(1, 0.3 * inch))

# Bar chart
story.append(Paragraph("<b>2. Quarterly Sales</b>", styles['Heading2']))
story.append(Image('bar_chart.png', width=5*inch, height=4*inch))
story.append(Spacer(1, 0.3 * inch))

# Line plot
story.append(Paragraph("<b>3. Profit Growth Over Time</b>", styles['Heading2']))
story.append(Image('line_plot.png', width=5*inch, height=4*inch))
story.append(Spacer(1, 0.3 * inch))

# Summary
summary_text = """
In summary, Product A continues to lead the market share, 
and profits have shown steady growth over the past six months.
"""
story.append(Paragraph(summary_text, styles['Normal']))

# Build the PDF
doc.build(story)
print(f"✅ PDF report generated successfully: {pdf_filename}")
