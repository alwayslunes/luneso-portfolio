from flask import Flask, render_template, abort
from flask_frozen import Freezer
import random

app = Flask(__name__)
freezer = Freezer(app)

# Define NMW videos separately so we can shuffle them
nmw_videos = [
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMWDizzy.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_1_Dizzy.jpg" 
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMWBlood.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_2_Blood.jpg" 
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMWBadRomance.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_3_BadRomance.jpg" 
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMWTwelfthHour.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_4_TwelfthHour.jpg" 
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMWViceversa.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_5_Viceversa.jpg" 
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMWWannaGoOutside.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_6_WannaGoOutside.jpg" 
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMWDaydreams.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_7_Daydreams.jpg" 
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMWRealHigh.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_8_RealHigh.jpg" 
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW5IVEQUID.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_9_5IVEQUID.jpg" 
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMWFLESH.mp4",
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_10_FLESH.jpg"
    }
]

# Randomize order
random.shuffle(nmw_videos)

projects = [
    {
        "id": 1,
        "slug": "video",
        "title": "Video",
        "category": "Commercial, Narrative & Social",
        "video_loop": "post_loop.mp4",
        "image": "editing.jpg",
        "reel_sections": [
            {
                "title": "Event Recaps",
                "videos": [
                    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Event%20Recaps/PERREOTON%20V2.mp4" },
                    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Event%20Recaps/CTA%20v7.mp4" },
                    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Event%20Recaps/CTA%20DEC%20RECAP_6.mp4" }
                ]
            },
            {
                "title": "Beyond the Club",
                "videos": [
                    { "url": "https://lunes-bucket.nyc3.cdn.digitaloceanspaces.com/btc_1.mp4" },
                    { "url": "https://lunes-bucket.nyc3.cdn.digitaloceanspaces.com/btc_2.mp4" },
                    { "url": "https://lunes-bucket.nyc3.cdn.digitaloceanspaces.com/btc_3.mp4" }
                ]
            },
            {
                "title": "New Music Wednesdays",
                "videos": nmw_videos
            }
        ]
    },
    { "id": 2, "slug": "design", "title": "Design", "category": "Print, Digital & Web", "video_loop": "design_loop.mp4", "image": "design.jpg" },
    { "id": 3, "slug": "always-lunes", "title": "Always Lunes", "category": "Creative Direction", "video_loop": "lunes_loop.mp4", "image": "lunes.jpg" },
    { "id": 4, "slug": "hijos-de-la-diaspora", "title": "Hijos de la Diáspora", "category": "Feature Documentary", "video_loop": "hijos_loop.mp4", "image": "hijos.jpg" }
]

def get_project(slug):
    # Re-shuffle if it's the video page so refreshes feel dynamic (optional)
    if slug == "video":
        random.shuffle(nmw_videos)
        # Update the project object reference
        projects[0]['reel_sections'][2]['videos'] = nmw_videos
        
    for project in projects:
        if project['slug'] == slug:
            return project
    return None

@app.route('/')
def intro(): return render_template('intro.html')

@app.route('/work/')
def work(): return render_template('work.html', projects=projects)

@app.route('/about/')
def about(): return render_template('about.html')

@app.route('/<slug>/')
def project_detail(slug):
    project = get_project(slug)
    if project is None: abort(404)
    return render_template('project.html', project=project)

@freezer.register_generator
def project_detail():
    for project in projects: yield {'slug': project['slug']}

if __name__ == '__main__':
    freezer.freeze()
