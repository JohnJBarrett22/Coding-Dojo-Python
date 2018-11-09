from flask import Flask, render_template
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('lead_gen_business')
    print("All clients...", mysql.query_db("SELECT clients.first_name AS clients, COUNT(leads.leads_id) AS leads FROM clients JOIN sites ON clients.client_id = sites.client_id JOIN leads ON sites.site_id = leads.site_id GROUP BY clients.first_name;"))
    mysql = connectToMySQL('lead_gen_business')
    bizdata = mysql.query_db("SELECT clients.first_name AS clients, COUNT(leads.leads_id) AS leads FROM clients JOIN sites ON clients.client_id = sites.client_id JOIN leads ON sites.site_id = leads.site_id GROUP BY clients.first_name;")
    return render_template('index.html', bizdata = bizdata)
    
if __name__=="__main__":
    app.run(debug=True)