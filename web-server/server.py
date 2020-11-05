from flask import Flask,render_template,request
import csv

app = Flask(__name__)

# Main Route
@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def my_about(page_name):
    return render_template(f'./{page_name}.html')

def write_to_file(data):
    with open('./database.txt','a') as database:
        email= data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('./database.csv','a',newline='') as database2:
        email= data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('./thankyou.html')
        except:
            return 'Something went wrong with database'
    else:
        return 'Something went wrong'
        