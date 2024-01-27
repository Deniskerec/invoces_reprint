import psycopg2

def fetch_invoice_data(ticket_id, document_id, financial_id):
    # Database connection details
    db_host = "10.229.236.158"
    db_name = "Reporting_database"
    db_user = "invoice_user"
    db_password = "invoice_password"

    conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cur = conn.cursor()
    query = """
    SELECT * FROM public.tickets_sold_manual_update_denis 
    WHERE ticket_id = %s OR document_id = %s OR financial_id = %s
    """
    cur.execute(query, (ticket_id, document_id, financial_id))
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data
