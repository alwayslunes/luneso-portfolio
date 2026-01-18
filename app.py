from flask import Flask, render_template, abort
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# YOUR UPDATED PROJECT DATA
projects = [
    {
        "id": 1,
        "title": "Always Lunes",
        "category": "Brand Development & Design",
        "image": "alwayslunes.jpg", 
        "description": "Established the complete visual identity for Miami's leading underground culture platform. Executed weekly motion graphics and static social assets, driving audience growth to 15k+ followers. Awarded <a href='https://www.miaminewtimes.com/best-of-miami/2023/arts-and-entertainment/best-instagram-17198798/' target='_blank' style='color:#d4af37;text-decoration:underline;'>'Best Instagram' of 2023 by Miami New Times</a>."
    },
    {
        "id": 2,
        "title": "Hijos de la Diaspora",
        "category": "Feature Documentary",
        "image": "hijos.jpg",
        "description": "Solely executed the entire visual pipeline (directed, shot, edited, and color graded) for my debut 60-minute feature documentary and delivered the final master for theatrical exhibition and digital distribution."
    },
    {
        "id": 3,
        "title": "Event Coverage",
        "category": "Videography & Editing",
        "image": "events.jpg",
        "description": "High-energy recap edits for live music and art events. Specialized in capturing the atmosphere and delivering polished 9:16 social cuts within 24 hours to maximize post-event engagement."
    },
    {
        "id": 4,
        "title": "Print & Digital Design",
        "category": "Graphic Design & Layout",
        "image": "design.jpg",
        "description": "Creation of high-volume marketing collateral including event flyers, poster signage, and digital banners. Expert proficiency in Photoshop and Illustrator with a focus on typography and print-ready file preparation."
    }
]

# Helper function to find a project by ID
def get_project(project_id):
    for project in projects:
        if project['id'] == project_id:
            return project
    return None

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>/')
def project_detail(project_id):
    project = get_project(project_id)
    if project is None:
        abort(404)
    return render_template('project.html', project=project)

# This tells Freezer how to generate the subpages
@freezer.register_generator
def project_detail():
    for project in projects:
        yield {'project_id': project['id']}

if __name__ == '__main__':
    freezer.freeze()
