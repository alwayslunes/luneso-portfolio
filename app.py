from flask import Flask, render_template, abort
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

projects = [
    {
        "id": 1,
        "slug": "video",
        "title": "Video",
        "category": "Commercial, Narrative & Social",
        "video_loop": "post_loop.mp4",
        "image": "editing.jpg",
        "description": "A comprehensive showcase of editorial work ranging from fast-paced social recaps to multi-camera narrative thesis projects. Features proficiency in offline/online workflows, DIT data management, and color grading.",
        
        "reel_sections": [
            {
                "title": "Event Recaps",
                "videos": [
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Event%20Recaps/PERREOTON%20V2.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Event%20Recaps/CTA%20v7.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Event%20Recaps/CTA%20DEC%20RECAP_6.mp4"
                ]
            },
            {
                "title": "Beyond the Club",
                "videos": [
                    "https://lunes-bucket.nyc3.cdn.digitaloceanspaces.com/btc_1.mp4",
                    "https://lunes-bucket.nyc3.cdn.digitaloceanspaces.com/btc_2.mp4",
                    "https://lunes-bucket.nyc3.cdn.digitaloceanspaces.com/btc_3.mp4"
                ]
            },
            {
                "title": "New Music Wednesdays",
                "videos": [
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_1_Dizzy.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_2_Blood.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_3_BadRomance.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_4_TwelfthHour.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_5_Viceversa.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_6_WannaGoOutside.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_7_Daydreams.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_8_RealHigh.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_9_5IVEQUID.mp4",
                    "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_10_FLESH.mp4"
                ]
            }
        ]
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
        "description": "Established the complete visual identity for Miami's leading underground culture platform. Awarded <a href='https://www.miaminewtimes.com/best-of-miami/2023/arts-and-entertainment/best-instagram-17198798/' target='_blank' style='color:#d4af37;'>'Best Instagram' of 2023</a>. This page showcases the brand strategy, event photography, and community impact."
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
