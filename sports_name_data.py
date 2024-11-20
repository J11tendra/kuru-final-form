import uuid
import random, string

sports_name_data = {
    "Athletics": {
        "Athletics 100M [Male]": {
            "gender": "male",
            "price": 212,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "16 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Athletics 100M [Female]": {
            "gender": "female",
            "price": 212,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "16 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Athletics 200M [Male]": {
            "gender": "male",
            "price": 212,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "16 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Athletics 200M [Female]": {
            "gender": "female",
            "price": 212,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "16 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Athletics 400M [Male]": {
            "gender": "male",
            "price": 212,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "16 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Athletics 400M [Female]": {
            "gender": "female",
            "price": 212,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "16 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Athletics 4 x 100M [Male]": {
            "gender": "male",
            "price": 590,
            "event_type": "team",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "16 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Athletics 4 x 100M [Female]": {
            "gender": "female",
            "price": 590,
            "event_type": "team",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "16 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Athletics 4 x 100M [Mixed]": {
            "gender": "open",
            "price": 590,
            "event_type": "team",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "16 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Swimming": {
        "Swimming 50M Freestyle [Male]": {
            "gender": "male",
            "price": 250,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 50M Freestyle [Female]": {
            "gender": "female",
            "price": 250,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 50M Breaststroke [Male]": {
            "gender": "male",
            "price": 250,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 50M Breaststroke [Female]": {
            "gender": "female",
            "price": 250,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 50M Backstroke [Male]": {
            "gender": "male",
            "price": 250,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 50M Backstroke [Female]": {
            "gender": "female",
            "price": 250,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 50M Butterfly [Male]": {
            "gender": "male",
            "price": 250,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 50M Butterfly [Female]": {
            "gender": "female",
            "price": 250,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 4 x 50M Freestyle Relay [Male]": {
            "gender": "male",
            "price": 700,
            "event_type": "single",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 4 x 50M Freestyle Relay [Female]": {
            "gender": "female",
            "price": 700,
            "event_type": "single",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 4 x 50M Medley Relay [Male]": {
            "gender": "male",
            "price": 700,
            "event_type": "single",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 4 x 50M Medley Relay [Female]": {
            "gender": "female",
            "price": 700,
            "event_type": "single",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 4 x 50M Freestyle Relay [Mixed]": {
            "gender": "open",
            "price": 700,
            "event_type": "single",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Swimming 4 x 50M Medley Relay [Mixed]": {
            "gender": "open",
            "price": 700,
            "event_type": "single",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Mr and Ms Kurukshetra": {
        "Mr and Ms Kurukshetra [Male]": {
            "gender": "male",
            "price": 750,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "23/01/2025 to 24/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Mr and Ms Kurukshetra [Female]": {
            "gender": "female",
            "price": 740,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "23/01/2025 to 24/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Cricket ": {
        "Cricket [Male]": {
            "gender": "Male",
            "price": 25_000,
            "event_type": "team",
            "min_participants": 13,
            "max_participants": 16,
            "min_managers": 1,
            "max_managers": 2,
            "date_of_event": "3/01/2025 to 26/01/2025",
            "age_category": "16 to 30",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Frisbee": {
        "Frisbee [Mixed]": {
            "gender": "open",
            "price": 5310,
            "event_type": "team",
            "min_participants": 7,
            "max_participants": 16,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "3/01/2025 to 26/01/2025",
            "age_category": "16 to 30",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Snooker": {
        "Snooker Solos[Mixed]": {
            "gender": "open",
            "price": 354,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "16 to 30",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Football": {
        "Football [Male]": {
            "gender": "male",
            "price": 9_440,
            "event_type": "team",
            "min_participants": 11,
            "max_participants": 18,
            "min_managers": 1,
            "max_managers": 2,
            "date_of_event": "15/01/2025 to 24/01/2025",
            "age_category": "15 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Football [Female]": {
            "gender": "female",
            "price": 4_130,
            "event_type": "team",
            "min_participants": 11,
            "max_participants": 18,
            "min_managers": 1,
            "max_managers": 2,
            "date_of_event": "15/01/2025 to 24/01/2025",
            "age_category": "15 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Chess": {
        "Chess Team Tournament [Mixed]": {
            "gender": "open",
            "price": 1_500,
            "event_type": "team",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "26/1/2025",
            "age_category": "18 to 30",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Esports": {
        "Esports FIFA / EA FC [Mixed]": {
            "gender": "open",
            "price": 300,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "20/01/2025 to 22/01/2025",
            "age_category": "18 to 30",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Esports BGMI [Mixed]": {
            "gender": "open",
            "price": 800,
            "event_type": "team",
            "min_participants": 4,
            "max_participants": 5,
            "min_managers": 0,
            "max_managers": 1,
            "date_of_event": "23/01/2025 to 24/01/2025",
            "age_category": "18 to 30",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Volleyball": {
        "Volleyball [Male]": {
            "gender": "male",
            "price": 2_400,
            "event_type": "team",
            "min_participants": 6,
            "max_participants": 12,
            "min_managers": 1,
            "max_managers": 3,
            "date_of_event": "23/01/2025 to 24/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Volleyball [Female]": {
            "gender": "female",
            "price": 1_600,
            "event_type": "team",
            "min_participants": 6,
            "max_participants": 12,
            "min_managers": 1,
            "max_managers": 3,
            "date_of_event": "23/01/2025 to 24/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Table Tennis": {
        "Table Tennis Team [Male]": {
            "gender": "male",
            "price": 1_180,
            "event_type": "team",
            "min_participants": 2,
            "max_participants": 2,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Table Tennis Team [Female]": {
            "gender": "open",
            "price": 1000,
            "event_type": "team",
            "min_participants": 2,
            "max_participants": 2,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Table Tennis Doubles [Male]": {
            "gender": "open",
            "price": 400,
            "event_type": "team",
            "min_participants": 2,
            "max_participants": 2,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": 0,
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Table Tennis Mixed Doubles [Mixed]": {
            "gender": "open",
            "price": 400,
            "event_type": "team",
            "min_participants": 2,
            "max_participants": 2,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "5k Hill Run": {
        "5k Hill Run [Mixed]": {
            "gender": "open",
            "price": 501,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Basketball": {
        "3v3 Basketball [Male]": {
            "gender": "male",
            "price": 2_124,
            "event_type": "team",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 1,
            "max_managers": 2,
            "date_of_event": "20/01/2025 to 21/01/2025",
            "age_category": "18 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "3v3 Basketball [Female]": {
            "gender": "female",
            "price": 1_770,
            "event_type": "team",
            "min_participants": 4,
            "max_participants": 4,
            "min_managers": 1,
            "max_managers": 2,
            "date_of_event": "20/01/2025 to 21/01/2025",
            "age_category": "18 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "5v5 Basketball [Male]": {
            "gender": "Male",
            "price": 4_720,
            "event_type": "team",
            "min_participants": 5,
            "max_participants": 12,
            "min_managers": 0,
            "max_managers": 2,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "18 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "5v5 Basketball [Female]": {
            "gender": "female",
            "price": 3_540,
            "event_type": "team",
            "min_participants": 5,
            "max_participants": 12,
            "min_managers": 1,
            "max_managers": 2,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "18 to 25",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Handball": {
        "Handball [Male]": {
            "gender": "male",
            "price": 1_180,
            "event_type": "team",
            "min_participants": 7,
            "max_participants": 14,
            "min_managers": 1,
            "max_managers": 2,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "18 to 30",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Handball [Female]": {
            "gender": "female",
            "price": 1_180,
            "event_type": "team",
            "min_participants": 7,
            "max_participants": 14,
            "min_managers": 1,
            "max_managers": 2,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "18 to 30",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Squash": {
        "Squash Solos [Male]": {
            "gender": "male",
            "price": 450,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 1,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Squash Solos [Female]": {
            "gender": "female",
            "price": 450,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 1,
            "date_of_event": "22/01/2025 to 26/01/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Martial Arts": {
        "Musical Martial Arts [Mixed]": {
            "gender": "open",
            "price": 472,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 26/01/2025 ",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Badminton": {
        "Badminton Men's Singles [Male]": {
            "gender": "male",
            "price": 500,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "23/01/2025 to  26/01/2025 ",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Badminton Women's Singles [Female]": {
            "gender": "female",
            "price": 500,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "23/01/2025 to  26/01/2025 ",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Badminton Men's doubles [Male]": {
            "gender": "male",
            "price": 850,
            "event_type": "team",
            "min_participants": 2,
            "max_participants": 2,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "23/01/2025 to  26/01/2025 ",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Badminton Women's doubles [Female]": {
            "gender": "female",
            "price": 850,
            "event_type": "team",
            "min_participants": 2,
            "max_participants": 2,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "23/01/2025 to  26/01/2025 ",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Badminton Mixed doubles [Mixed]": {
            "gender": "open",
            "price": 850,
            "event_type": "team",
            "min_participants": 2,
            "max_participants": 2,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "23/01/2025 to  26/01/2025 ",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Tennis": {
        "Tennis Men's Singles [Male]": {
            "gender": "male",
            "price": 500,
            "event_type": "single",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 24/01/2025 ",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Tennis Men's Doubles [Male]": {
            "gender": "male",
            "price": 1000,
            "event_type": "team",
            "min_participants": 2,
            "max_participants": 2,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 24/01/2025 ",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
        "Tennis Mixed Doubles [Mixed]": {
            "gender": "open",
            "price": 1000,
            "event_type": "team",
            "min_participants": 1,
            "max_participants": 1,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "22/01/2025 to 24/01/2025 ",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
    "Yoga": {
        "Yoga Competetion [Open]": {
            "gender": "open",
            "price": 251,
            "event_type": "team",
            "min_participants": 1,
            "max_participants": 5,
            "min_managers": 0,
            "max_managers": 0,
            "date_of_event": "25/10/2025",
            "age_category": "17 to 27",
            "docs_required": "ID Proof",
            "unique_id": ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        },
    },
}
