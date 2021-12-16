from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')


if __name__=='__main__':
    app.run(debug=True, port=8000,host ='127.0.0.1')

