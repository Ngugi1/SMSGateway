"""
Queue SMS Dispatcher

"""

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
import nexmo
import africastalking


from .util import env_var, extract_error

# Enviromental loader
load_dotenv('.env')

# Enviroment settings nexmo
NEXMO_API_KEY = env_var('NEXMO_API_KEY')
NEXMO_API_SECRET = env_var('NEXMO_API_SECRET')
NEXMO_NUMBER = env_var('NEXMO_NUMBER')

# Initialize nexmo
nexmo_client = nexmo.Client(
    api_key=NEXMO_API_KEY, api_secret=NEXMO_API_SECRET
)

# Enviroment settings africastalking
ASTALKING_USERNAME = env_var('ASTALKING_USERNAME')
ASTALKING_API_KEY = env_var('ASTALKING_API_KEY')


# Initialize africastalking
africastalking.initialize(ASTALKING_USERNAME, ASTALKING_API_KEY) 

# Setup flask
app = Flask(__name__)
app.config['SECRET_KEY'] = env_var('FLASK_SECRET_KEY')


@app.route('/')
def index():
    """ A view that renders the Send SMS form. """
    return render_template('queue_sms.html')


@app.route('/dispatch_sms', methods=['POST'])
def dispatch_sms():
    """ A POST endpoint that sends an SMS. """

    # form data
    provider_direct = request.form['provider_direct']
    destination_number = request.form['destination_number']
    content = request.form['content']
    
    if provider_direct == 'nexmo':
        # Send the SMS message nexmo
        result = nexmo_client.send_message({
            'from': NEXMO_NUMBER,
            'to': destination_number,
            'text': content,
        })
    else:
        # Send the SMS message Africa Stalking
        sms = africastalking.SMS
        result = sms.send(content, ["+" + destination_number])

    err = extract_error(result)
    if err is not None:
        flash("Error occurred sending message " + err, 'error')
    else:
        flash("Message Successfully sent to " + destination_number)

    
    return redirect(url_for('index'))

@app.route('/dispatch_queue', methods=['POST'])
def dispatch_queue():
    """ A POST endpoint that sends an SMS. """

    # form data
    provider_queue = request.form['provider_queue']
    destination_numbers = request.form['destination_numbers'].split(",")
    content = request.form['content']
    
    
    # Send the SMS message:
    for destination_number in destination_numbers:
        if provider_queue == 'nexmo':
            result = nexmo_client.send_message({
                'from': NEXMO_NUMBER,
                'to': destination_number,
                'text': content,
            })
        else:
            sms = africastalking.SMS
            result = sms.send(content, ["+" + destination_number])


    err = extract_error(result)
    if err is not None:
        flash("Error occurred sending message " + err, 'error')
    else:
        flash("Message Successfully sent to " + destination_number)

    
    return redirect(url_for('index'))
