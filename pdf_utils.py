from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont



def create_pdf(data):
    pdf_filename = f"invoice_{data[0]}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, height - 50, "SIMPLIFIED TAX INVOICE")
    c.setFont("Helvetica-Bold", 10)
    #c.drawString(200, height - 50, "فاتورة ضريبية المبسطة")
    

    c.line(30, height - 80, width - 50, height - 80)
    
    c.setFont("Helvetica-Bold", 12) 
    c.drawString(40, height - 100, f"Ticket: ")
    c.setFont("Helvetica-Bold", 10)  
    #c.drawString(200, height - 120, "تذكرة")
    
    
    # Invoide data 
    c.setFont("Helvetica", 8)
    c.drawString(40, height - 130, f"Invoice Number: ")
    c.drawString(200, height - 130, f"Invoice Number: ")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(500, height - 130, f"{data[0]}") 

    
    c.line(30, height - 140, width - 50, height - 140)
    # main details 
    #left
    c.setFont("Helvetica", 8)
    c.drawString(40, height - 160, f"Seller")
    c.drawString(40, height - 175, f"Date and Time:")
    c.drawString(150, height - 175, f"{data[1]}")
    c.drawString(40, height - 190, f"Terminal ID:")
    c.drawString(150, height - 190, f"{data[9]}")
    c.drawString(40, height - 205, f"Merchant Name:")
    c.drawString(150, height - 205, f" / ")
    # right 
    c.drawString(360, height - 160, f"VAT No:")
    c.drawString(360, height - 175, f"Location:")
    c.drawString(470, height - 175, f"{data[29]}")
    c.drawString(360, height - 190, f"Payment Type:")
    c.drawString(470, height - 190, f"{data[28]}")
    c.drawString(360, height - 205, f"Merchant Location:")
    c.drawString(470, height - 205, f" / ")
    # ... Add more invoice details ...

    # Add Table for Ticket Details

    c.line(30, height - 220, width - 50, height - 220)
    c.line(30, height - 230, width - 50, height - 230)
    c.line(30, height - 265, width - 50, height - 265)

    # Add ticket details
    c.drawString(40, height - 250, f"NO")
    c.drawString(40, height - 280, f"1")
    c.drawString(80, height - 250, f"TICKET NO")
    c.drawString(80, height - 280, f"{data[25]}")
    c.drawString(140, height - 250, f"PASSENGER NAME")
    c.drawString(140, height - 280, f"{data[24]}")
    c.drawString(260, height - 250, f"PASSENGER TYPE")
    c.drawString(260, height - 280, f"{data[7]}")
    c.drawString(360, height - 250, f"UNIT PRICE")
    c.drawString(360, height - 280, f"{data[2]}  SAR")
    c.drawString(420, height - 250, f"QTY")
    c.drawString(420, height - 280, f"1")
    c.drawString(470, height - 250, f"SUBTOTAL(INC. VAT)")
    c.drawString(470, height - 280, f"{data[2]}   SAR")
    
    # ... Add more ticket details ...
    
    c.line(30, height - 295, width - 50, height - 295)
    
    c.drawString(100, height - 310, f"TRIP NUMBER")
    c.drawString(100, height - 340, f"{data[10]}")
    c.drawString(200, height - 310, f"ROUTE DETAILS")
    c.drawString(200, height - 340, f"{data[12]} - {data[13]}  ")
    c.drawString(300, height - 310, f"DEPARTURE DATE")
    c.drawString(300, height - 340, f"{data[11]}")
    c.drawString(400, height - 310, f"BOARDING/ALIGHTING")
    c.drawString(400, height - 340, f"{data[14]} - {data[15]}  ")
    
    
    c.line(30, height - 355, width - 50, height - 355)
    c.line(30, height - 365, width - 50, height - 365)
    
    c.setFont("Helvetica-Bold", 11)
    #c.drawString(40, height - 380, f"TOTAL TAXABLE AMOUNT (EXCLUDING VAT)")
    c.drawString(40, height - 400, f"TOTAL VAT")
    c.drawString(40, height - 420, f"TOTAL AMOUNT DUE")
    #c.drawString(400, height - 380, f"{data[2-3]}")
    c.drawString(396, height - 400, f"{data[3]}   SAR")
    c.drawString(400, height - 420, f"{data[2]}   SAR")
    
    # Add Footer
    c.setFont("Helvetica", 9)
    c.drawString(40, height - 560, "Thank you for using our services")

    c.save()
    return pdf_filename
