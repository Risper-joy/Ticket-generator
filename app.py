from flask import Flask, render_template, request

app = Flask(__name__)

# Data storage (optional, similar to Colab example)
ticket_count = 0
office_codes = {"Identity Cards": "ID", "Passport Office": "PO", "Imigration" : "IO"}

def generate_ticket(office):
    global ticket_count
    ticket_count += 1
    code = office_codes[office]
    ticket_number = f"{code}{ticket_count:03d}"
    return ticket_number

@app.route("/")
def home():
    return render_template("ticketUI.html", office_codes=office_codes)

@app.route("/generate", methods=["POST"])
def generate():
    office = request.form["office"]
    ticket_number = generate_ticket(office)
    return render_template("ticket.html", ticket_number=ticket_number)

if __name__ == "__main__":
    app.run(debug=True)