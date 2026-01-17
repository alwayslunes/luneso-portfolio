from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# CONFIGURATION
# ---------------------------------------------------------
# UPDATE YOUR PROJECT DATA HERE
projects = [
    {
        "id": 1,
        "title": "Always Lunes",
        "category": "Brand Identity",
        "image": "https://via.placeholder.com/600x338/1a1a1a/555555?text=Brand+Identity", 
        "link": "#",
        "description": "Designed total visual identity and executed daily social assets, growing audience to 10k+."
    },
    {
        "id": 2,
        "title": "Hijos de la Diaspora",
        "category": "Documentary",
        "image": "https://via.placeholder.com/600x338/1a1a1a/555555?text=Documentary",
        "link": "https://youtube.com",
        "description": "Full-cycle post-production: Editing, Color Grading, and Sound Design for 60-min feature."
    },
    {
        "id": 3,
        "title": "Event Visuals",
        "category": "Graphic Design",
        "image": "https://via.placeholder.com/600x338/1a1a1a/555555?text=Event+Flyers",
        "link": "#",
        "description": "High-volume print and digital asset creation for weekly live events."
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    freezer.freeze()  # Freezes to /build folder when run
