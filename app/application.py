from flask import Flask, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# from flask_cors import CORS
#AWS API
headers = {
        "Content-Type": "application/json" 
}

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.config['SECRET_KEY'] = 'WordToTheWise'


# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

@application.route('/tweet/<text>', methods=['GET'])
def detemineValidity(text):
    loaded_model = None
    with open('basic_classifier.pkl','rb') as fid:
        loaded_model = pickle.load(fid)
    vectorier = None
    with open('count_vectorizer.pkl','rb') as vd:
        vectorier = pickle.load(vd)
    prediction = loaded_model.predict(vectorier.transform([text]))[0]
    response = jsonify(prediction)
    return response

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

