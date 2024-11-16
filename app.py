from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
from bson import Binary

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['MONGO_URI'] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

# Access collections
db = mongo.db
users_collection = db['Users']
managers_collection = db['Managers']
participants_collection = db['Participants']

costs = {
    "badminton-men-single": 472,
    "badminton-men-double": 826,
    "badminton-mixed-double": 826,
    "basketball-women": 5074,
    "basketball-men": 5074,
    "frisbee-open": 5310,
    "handball-women": 1180,
    "handball-male": 1180,
    "sqaush-women-single": 413,
    "swimming-4x50-relay-freestyle-men": 708,
    "swimming-4x50-relay-freestyle-women": 708,
    "swimming-50m-freestyle-men": 295,
    "swimming-50m-backstroke-men": 295,
    "swimming-50m-breaststroke-men": 295,
    "swimming-50m-butterfly-men": 295,
    "swimming-50m-freestyle-women": 295,
    "swimming-50m-backstroke-women": 295,
    "swimming-50m-breaststroke-women": 295,
    "swimming-50m-butterfly-women": 295,
    "table-tennis-mens-team": 1180,
    "table-tennis-womens-team": 1003,
    "table-tennis-mens-doubles": 295,
    "table-tennis-mixed-doubles": 295,
    "tennis-mens-singles": 472,
    "tennis-mens-doubles": 826,
    "tennis-mixed-doubles": 826,
    "sprints-100m-male": 212,
    "volleyball-male": 2596,
    "volleyball-women": 1534,
    "chess-open": 319,
    "snooker-open": 354,
    "rhythm-solo-dance": 295,
    "step-off-group-dance": 1180,
    "group-dance-classical": 1180,
    "music-solo": 295,
    "art": 59,
    "photography": 59,
    "marcurious": 590,
    "digi-quest": 590,
    "bull-bear-brawl": 590,
    "mystery-maze": 826
}

single_or_team = {
    "badminton-men-single": "single",
    "badminton-men-double": "team",
    "badminton-mixed-double": "team",
    "basketball-women": "team",
    "basketball-men": "team",
    "frisbee-open": "team",
    "handball-women": "team",
    "handball-male": "team",
    "sqaush-women-single": "single",
    "swimming-4x50-relay-freestyle-men": "team",
    "swimming-4x50-relay-freestyle-women": "team",
    "swimming-50m-freestyle-men": "single",
    "swimming-50m-backstroke-men": "single",
    "swimming-50m-breaststroke-men": "single",
    "swimming-50m-butterfly-men": "single",
    "swimming-50m-freestyle-women": "single",
    "swimming-50m-backstroke-women": "single",
    "swimming-50m-breaststroke-women": "single",
    "swimming-50m-butterfly-women": "single",
    "table-tennis-mens-team": "team",
    "table-tennis-womens-team": "team",
    "table-tennis-mens-doubles": "team",
    "table-tennis-mixed-doubles": "team",
    "tennis-mens-singles": "single",
    "tennis-mens-doubles": "team",
    "tennis-mixed-doubles": "team",
    "sprints-100m-male": "single",
    "volleyball-male": "team",
    "volleyball-women": "team",
    "chess-open": "single",
    "snooker-open": "single",
    "rhythm-solo-dance": "single",
    "step-off-group-dance": "team",
    "group-dance-classical": "team",
    "music-solo": "single",
    "art": "single",
    "photography": "single",
    "marcurious": "team",
    "digi-quest": "team",
    "bull-bear-brawl": "team",
    "mystery-maze": "team"
}


def check_if_user_exists():
    if 'user' not in session.keys():
        return redirect(url_for('main'))

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/submit_user_information', methods=["GET", "POST"])
def submit_user_information():
    check_if_user_exists()
    if request.method == "POST":
        # Capture form fields
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        registration_type = request.form.get("registration_type")
        institute_name = request.form.get("institute_name")
        person_incharge_phone = request.form.get("person_incharge_phone")
        shuttle_interest = request.form.get("shuttle_interest")
        user_info = {
            "first_name": first_name,
            "last_name": last_name,
            "registration_type": registration_type,
            "institute_name": institute_name,
            "person_incharge_phone": person_incharge_phone,
            "shuttle_interest": shuttle_interest,
            "categories": []  # Initialize an empty list for events
        }
        session['user'] = user_info

    return redirect(url_for('choose_areas'))

@app.route('/choose_areas')
def choose_areas():
    return check_if_user_exists() or render_template('choose_area.html')

@app.route('/area_submit', methods=["GET", "POST"])
def area_choice():
    if request.method == "POST":
        chosen_areas = request.form.getlist('areas')
        user_info = session['user']
        user_info['categories'] = chosen_areas
        session['user'] = user_info
        return redirect(url_for('choose_events'))
    return "No areas selected"

@app.route('/choose_events', methods=["GET", "POST"])
def choose_events():
    chosen_areas = session['user']['categories']
    return render_template('choose_culs_sports_etc.html', chosen_categories=chosen_areas)

@app.route('/submit', methods=["GET", "POST"])
def submit():
    user_cost = 0
    chosen_sports = []
    chosen_culturals = []
    chosen_management = []

    if request.method == "POST":
        chosen_sports = request.form.getlist('sports')
        chosen_culturals = request.form.getlist('culturals')
        chosen_management = request.form.getlist('management')

        cultural_cost = 0
        sports_cost = 0
        management_cost = 0
        for i in chosen_culturals:
            cultural_cost += costs[i]
            user_cost += costs[i]
        
        for i in chosen_sports:
            sports_cost += costs[i]
            user_cost += costs[i]
        
        for i in chosen_management:
            management_cost += costs[i]
            user_cost += costs[i]
        
        user = session['user']
        if "chosen_sports" in session["user"]: del user["chosen_sports"]
        if "chosen_culturals" in session["user"]:del user["chosen_culturals"]
        if "chosen_managment" in session["user"]:del user["chosen_management"]

        if "sports" in user["categories"]:
            user["chosen_sports"] = chosen_sports
            user["sports_cost"] = sports_cost

        if "management" in user["categories"]:
            user["chosen_management"] = chosen_management
            user["management_cost"] = management_cost
        
        if "culturals" in user["categories"]:
            user["chosen_culturals"] = chosen_culturals
            user["cultural_cost"] = cultural_cost
        
        user["total_cost"] = user_cost
        session["user"] = user

    sport_names = {
        "badminton-men-single": "Men's Singles (Badminton)",
        "badminton-men-double": "Men's Doubles (Badminton)",
        "badminton-mixed-double": "Mixed Doubles (Badminton)",
        "basketball-women": "Women (Basketball)",
        "basketball-men": "Men (Basketball)",
        "frisbee-open": "Open (Frisbee)",
        "handball-women": "Women (Handball)",
        "handball-male": "Men (Handball)",
        "sqaush-women-single": "Women's Singles (Squash)",
        "swimming-4x50-relay-freestyle-men": "4x50m Relay Freestyle Men (Swimming)",
        "swimming-4x50-relay-freestyle-women": "4x50m Relay Freestyle Women (Swimming)",
        "swimming-50m-freestyle-men": "50m Freestyle Men (Swimming)",
        "swimming-50m-backstroke-men": "50m Backstroke Men (Swimming)",
        "swimming-50m-breaststroke-men": "50m Breaststroke Men (Swimming)",
        "swimming-50m-butterfly-men": "50m Butterfly Men (Swimming)",
        "swimming-50m-freestyle-women": "50m Freestyle Women (Swimming)",
        "swimming-50m-backstroke-women": "50m Backstroke Women (Swimming)",
        "swimming-50m-breaststroke-women": "50m Breaststroke Women (Swimming)",
        "swimming-50m-butterfly-women": "50m Butterfly Women (Swimming)",
        "table-tennis-mens-team": "Men's Team (Table Tennis)",
        "table-tennis-womens-team": "Women's Team (Table Tennis)",
        "table-tennis-mens-doubles": "Men's Doubles (Table Tennis)",
        "table-tennis-mixed-doubles": "Mixed Doubles (Table Tennis)",
        "tennis-mens-singles": "Men's Singles (Tennis)",
        "tennis-mens-doubles": "Men's Doubles (Tennis)",
        "tennis-mixed-doubles": "Mixed Doubles (Tennis)",
        "sprints-100m-male": "Sprints - 100m Male (Athletics)",
        "volleyball-male": "Men (Volleyball)",
        "volleyball-women": "Women (Volleyball)",
        "chess-open": "Open (Chess)",
        "snooker-open": "Open (Snooker)"
    }

    cultural_names = {
        "rhythm-solo-dance": "Rhythm - Solo Dance",
        "step-off-group-dance": "Step Off - Group Dance",
        "group-dance-classical": "Natyanjali - Group Dance Classical",
        "music-solo": "Spotlight - Music Solo",
        "art": "Pixelate - Art",
        "photography": "Kahaani - Photography"
    }

    management_names = {
        "marcurious": "Marcurious",
        "digi-quest": "Digi Quest",
        "bull-bear-brawl": "Bull & Bear Brawl",
        "mystery-maze": "Mystery Maze"
    }


    return render_template('summary.html', 
                           chosen_sports=chosen_sports, 
                           chosen_culturals=chosen_culturals,
                           chosen_management=chosen_management,
                           total_cost=user_cost,
                           costs=costs,
                           sport_names=sport_names,
                           cultural_names=cultural_names,
                           management_names=management_names)

from flask import jsonify, request, session
from bson.objectid import ObjectId
from bson import Binary

# Utility function to convert ObjectIds to strings
def convert_objectid_to_str(obj):
    if isinstance(obj, dict):
        return {k: convert_objectid_to_str(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_objectid_to_str(i) for i in obj]
    elif isinstance(obj, ObjectId):
        return str(obj)
    else:
        return obj

# Endpoint for handling event submission
@app.route('/management_particpant_submit', methods=["POST"])
def management_particpant_submit():
    user = session['user']
    events = user.get('chosen_sports', []) + user.get('chosen_culturals', []) + user.get('chosen_management', [])
    user['event_details'] = {}

    for event in events:
        managers = []
        participants = []

        # Collect managers for this event
        manager_names = request.form.getlist(f'managerName{event}[]')
        manager_phones = request.form.getlist(f'managerPhone{event}[]')
        manager_images = request.files.getlist(f'managerImage{event}[]')

        for name, phone, image in zip(manager_names, manager_phones, manager_images):
            if name and phone:
                manager = {
                    'name': name,
                    'phone': phone,
                    'event': event,
                    'role': 'manager',
                    'status': "Outside Campus",
                    'image_data': Binary(image.read()) if image else None
                }
                managers_collection.insert_one(manager)
                managers.append(manager)

        # Collect participants for this event
        participant_names = request.form.getlist(f'participantName{event}[]')
        participant_phones = request.form.getlist(f'participantPhone{event}[]')
        participant_images = request.files.getlist(f'participantImage{event}[]')

        for name, phone, image in zip(participant_names, participant_phones, participant_images):
            if name and phone:
                participant = {
                    'name': name,
                    'phone': phone,
                    'event': event,
                    'role': 'participant',
                    'status': "Outside Campus",
                    'image_data': Binary(image.read()) if image else None
                }
                participants_collection.insert_one(participant)
                participants.append(participant)

        # Save event details for user
        user['event_details'][event] = {
            'managers': managers,
            'participants': participants
        }

    users_collection.insert_one(user).inserted_id
    session['user'] = user
    return session['user']






if __name__ == '__main__':
    app.run(debug=True)