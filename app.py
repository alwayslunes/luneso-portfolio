from flask import Flask, render_template, abort
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

projects = [
    {
        "id": 1,
        "slug": "video",  # UPDATED LINK
        "title": "Video", # UPDATED TITLE
        "category": "Commercial, Narrative & Social",
        "video_loop": "post_loop.mp4", # Keeping same file name to avoid errors
        "image": "editing.jpg", 
        "description": "A comprehensive showcase of editorial work ranging from fast-paced social recaps to multi-camera narrative thesis projects. Features proficiency in offline/online workflows, DIT data management, and color grading."
    },
    {
        "id": 2,
        "slug": "design",
        "title": "Design",
        "category": "Print, Digital & Web",
        "video_loop": "design_loop.mp4",
        "image": "design.jpg",
        "description": "High-volume creation of marketing collateral including event flyers, poster signage, and responsive website layouts. Demonstrates expert proficiency in Photoshop, Illustrator, and web design principles."
    },
    {
        "id": 3,
        "slug": "always-lunes",
        "title": "Always Lunes",
        "category": "Creative Direction",
        "video_loop": "lunes_loop.mp4",
        "image": "lunes.jpg", 
        "description": "Established the complete visual identity for Miami's leading underground culture platform. Executed weekly motion graphics and static social assets. Awarded <a href='https://www.miaminewtimes.com/best-of-miami/2023/arts-and-entertainment/best-instagram-17198798/' target='_blank' style='color:#d4af37;'>'Best Instagram' of 2023</a>."
    },
    {
        "id": 4,
        "slug": "hijos-de-la-diaspora",
        "title": "Hijos de la Diáspora",
        "category": "Feature Documentary",
        "video_loop": "hijos_loop.mp4",
        "image": "hijos.jpg",
        "description": "Solely executed the entire visual pipeline (directed, shot, edited, and color graded) for my debut 60-minute feature documentary. Managed 4TB+ of 4K footage and delivered the final master for theatrical exhibition."
    }
]

def get_project(slug):
    for project in projects:
        if project['slug'] == slug:
            return project
    return None

@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/work/')
def work():
    return render_template('work.html', projects=projects)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/<slug>/')
def project_detail(slug):
    project = get_project(slug)
    if project is None:
        abort(404)
    return render_template('project.html', project=project)

@freezer.register_generator
def project_detail():
    for project in projects:
        yield {'slug': project['slug']}

if __name__ == '__main__':
    freezer.freeze()
