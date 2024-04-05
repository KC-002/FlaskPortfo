from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("./index.html")


# @app.route("/works.html")
# def works():
#     return render_template("./works.html")



# @app.route("/work.html")
# def work():
#     return render_template("./work.html")

# @app.route("/about.html")
# def about():
#     return render_template("./about.html")


# @app.route("/contact.html")
# def contact():
#     return render_template("./contact.html")


# @app.route("/components.html")
# def components():
#     return render_template("./components.html")

@app.route("/<string:page_name>")
def html_pages(page_name):
        return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv',mode='a', newline='') as database1:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit():
   
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
             return 'Something went wrong'
    else:
         return 'Something went wrong. Try again!'