from flask import Flask,render_template
import gspread
import pandas
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('hassan.json', scope)

#gc = gspread.authorize(credentials)

#wks = gc.open("Where is the money Lebowski?").sheet1



app = Flask(__name__)
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'cargo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

"""Changes that i have made to enable me use gspread to display my data"""
####################################################################
## i)pip install gspread oauth2client(installed gspread )                                                              
##                                                              
####################################################################

conn = mysql.connect()

cursor =conn.cursor()

sql = "SELECT * FROM lori"

cursor.execute(sql)

results = cursor.fetchall()

# Say, you need A2
#val = worksheet.cell(2, 1).value

# And then update
#worksheet.update_cell(2, 1, '42') 

@app.route("/db")
def connection():
	

	#cursor = db.cursor()
	sql = "SELECT * FROM lori" 
	"""
	if mysql.connect():
		return "hey connected"
	else:
		return "not connected"
		"""
	cursor.execute(sql)
	results = cursor.fetchall()

	return render_template('index.html',results=results)







@app.route("/yes")
def connect():
	gc = gspread.authorize(credentials)
	if gspread.authorize(credentials):
		spreadsheet = gc.open("Hassan")
		worksheet = spreadsheet.add_worksheet(title="serials", rows="100", cols="3")
		#worksheet = spreadsheet.worksheet("cargo")
		#row = ["Serial","Commodity","Amount"]
		#index = 1
		#worksheet.insert_row(row,index)
		for record in results:
			"""serial = record[0]
			commodity = record[1]
			amount = record[2]"""
			col = record
			row = record
			worksheet.update_cell(row, col, record)











if __name__ == '__main__':
	app.run(debug=True)
