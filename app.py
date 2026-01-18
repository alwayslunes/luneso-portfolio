from flask import Flask, render_template, abort
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# YOUR PROJECT DATA
projects = [
    {
        "id": 1,
        "title": "Always Lunes",
        "category": "Brand Development & Design",
        "image": "lunes.jpg", 
        "description": "Established the complete visual identity for Miami's leading underground culture platform. Executed weekly motion graphics and static social assets. Awarded <a href='https://www.miaminewtimes.com/best-of-miami/2023/arts-and-entertainment/best-instagram-17198798/' target='_blank' style='color:#d4af37;'>'Best Instagram' of 2023</a>."
    },
    {
        "id": 2,
        "title": "Hijos de la Diaspora",
        "category": "Feature Documentary",
        "image": "hijos.jpg",
        "description": "Solely executed the entire visual pipeline (directed, shot, edited, and color graded) for my debut 60-minute feature documentary. Managed 4TB+ of 4K footage and delivered the final master for theatrical exhibition."
    },
    {
        "id": 3,
        "title": "Post Production",
        "category": "Commercial, Narrative & Social",
        "image": "editing.jpg", 
        "description": "A comprehensive showcase of editorial work ranging from fast-paced social recaps to multi-camera narrative thesis projects. Features proficiency in offline/online workflows, DIT data management, and color grading."
    },
    {
        "id": 4,
        "title": "Design",
        "category": "Print, Digital & UI Layout",
        "image": "design.jpg",
        "description": "Creation of marketing collateral including event flyers, poster signage, and responsive website layouts. Demonstrates expert proficiency in Photoshop and Illustrator."
    }
]

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

@freezer.register_generator
def project_detail():
    for project in projects:
        yield {'project_id': project['id']}

if __name__ == '__main__':
    freezer.freeze()
