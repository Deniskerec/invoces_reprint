from flask import Flask, request, send_file, render_template
from db_utils import fetch_invoice_data
from pdf_utils import create_pdf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticket_id = request.form.get('ticket_id')
        document_id = request.form.get('document_id')
        financial_id = request.form.get('financial_id')
        data = fetch_invoice_data(ticket_id, document_id, financial_id)
        if data:
            pdf_filename = create_pdf(data)
            return send_file(pdf_filename, as_attachment=True)
        else:
            return "No matching record found."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
