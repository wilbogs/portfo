from flask import Flask, url_for, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])

#GET - send data using URL
#POST - 
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
		    data = request.form.to_dict()
		    write_to_csv(data)
		    return redirect('/thankyou.html')
		except:
		 	return'did not save to database'
	else:
		return 'something went wrong. try again.'

		
# @app.route('/works.html')
# def works_page():
#     return render_template('works.html') 

# @app.route('/work.html')
# def work_page():
#     return render_template('work.html')     

# @app.route('/about.html')
# def about_page():
#     return render_template('about.html')    

# @app.route('/contact.html')
# def contact_page():
#     return render_template('contact.html')   

# @app.route('/components.html')
# def components_page():
#     return render_template('components.html')    

       

