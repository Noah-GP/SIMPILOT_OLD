from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
db = SQLAlchemy(app)

# Define ForumPost model
class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Ensure database tables are created before the first request
@app.before_first_request
def create_tables():
    db.create_all()

checklists = {
    'Boeing 737': ['Pre-flight', 'Takeoff', 'Cruise', 'Landing'],
    'Airbus A320': ['Pre-flight', 'Takeoff', 'Cruise', 'Landing']
}

aircraft_profiles = {
    'Boeing 737': 'Detailed information about Boeing 737.',
    'Airbus A320': 'Detailed information about Airbus A320.'
}

multiplayer_sessions = [
    {'id': 1, 'name': 'Session 1', 'users': ['User1', 'User2']},
    {'id': 2, 'name': 'Session 2', 'users': ['User3', 'User4']}
]

training_resources = [
    {'title': 'Tutorial 1', 'description': 'Description of tutorial 1', 'link': 'http://tutorial1.com'},
    {'title': 'Tutorial 2', 'description': 'Description of tutorial 2', 'link': 'http://tutorial2.com'}
]

addons = [
    {'name': 'Addon 1', 'description': 'Description of addon 1', 'price': '$10', 'link': 'http://addon1.com'},
    {'name': 'Addon 2', 'description': 'Description of addon 2', 'price': '$15', 'link': 'http://addon2.com'}
]

events = [
    {'title': 'Event 1', 'date': '2024-05-10', 'description': 'Description of event 1'},
    {'title': 'Event 2', 'date': '2024-05-15', 'description': 'Description of event 2'}
]

user_content = [
    {'username': 'User1', 'content': 'This is the first user-generated content.'},
    {'username': 'User2', 'content': 'This is the second user-generated content.'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checklists/<aircraft>')
def show_checklist(aircraft):
    if aircraft in checklists:
        return render_template('checklist.html', aircraft=aircraft, items=checklists[aircraft])
    else:
        return 'Checklist not found'

@app.route('/forum', methods=['GET', 'POST'])
def forum():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = ForumPost(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return 'Post created successfully'
    else:
        posts = ForumPost.query.all()
        return render_template('forum.html', posts=posts)

@app.route('/aircraft/<aircraft>')
def show_aircraft_profile(aircraft):
    if aircraft in aircraft_profiles:
        return aircraft_profiles[aircraft]
    else:
        return 'Aircraft profile not found'

@app.route('/flight-tracking/<flight_number>')
def track_flight(flight_number):
    # Integrate with flight tracking service here
    return f'Tracking flight {flight_number}'

@app.route('/multiplayer')
def multiplayer():
    return render_template('multiplayer.html', sessions=multiplayer_sessions)

@app.route('/training-resources')
def show_training_resources():
    return render_template('training_resources.html', resources=training_resources)

@app.route('/addons')
def browse_addons():
    return render_template('addons.html', addons=addons)

@app.route('/events')
def events_calendar():
    return render_template('events.html', events=events)

@app.route('/flight-analysis')
def flight_analysis():
    # Add code to provide flight analysis tools
    return 'Flight analysis tools will be available here'

@app.route('/user-content')
def showcase_user_content():
    return render_template('user_content.html', user_content=user_content)

@app.route('/messages')
def messages():
    # Add code for secure messaging system
    return 'Direct secure messaging system will be available here'

if __name__ == '__main__':
    app.run(debug=True)
