from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as db:
		email=data['email']
		subject = data['subject']
		message = data['message']

		csv_writer = csv.writer(db,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form',methods = ['POST','GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'Didn\'t save to database' 
	else:
		return "Oops! try again"

@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)
