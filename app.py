from flask import Flask, render_template, abort
from flask_frozen import Freezer
import random

app = Flask(__name__)
freezer = Freezer(app)

# --- DATA: NMW VIDEOS (Shuffled) ---
nmw_videos = [
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_1_Dizzy.mp4", "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_1_Dizzy.jpg" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_2_Blood.mp4", "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_2_Blood.jpg" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_3_BadRomance.mp4", "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_3_BadRomance.jpg" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_4_TwelfthHour.mp4", "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_4_TwelfthHour.jpg" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_5_Viceversa.mp4", "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_5_Viceversa.jpg" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_6_WannaGoOutside.mp4", "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_6_WannaGoOutside.jpg" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_7_Daydreams.mp4", "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_7_Daydreams.jpg" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_8_RealHigh.mp4", "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_8_RealHigh.jpg" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_9_5IVEQUID.mp4", "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_9_5IVEQUID.jpg" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_10_FLESH.mp4", "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_10_FLESH.jpg" }
]
random.shuffle(nmw_videos)

# --- DATA: MAIN PORTFOLIO SECTIONS ---
portfolio = [
    {
        "id": "content",
        "title": "CONTENT",
        # Uses the first Event Recap video as the banner background
        "banner_video": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Event%20Recaps/PERREOTON%20V2.mp4",
        "sub_sections": [
            {
                "title": "New Music Wednesdays",
                "videos": nmw_videos
            },
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
            }
        ]
    },
    {
        "id": "narrative",
        "title": "NARRATIVE",
        "banner_video": "", # Add URL for Narrative Background Loop
        "sub_sections": [] # Add videos here later
    },
    {
        "id": "documentary",
        "title": "DOCUMENTARY",
        "banner_video": "", # Add URL for Doc Background Loop
        "sub_sections": [] 
    },
    {
        "id": "hijos",
        "title": "HIJOS DE LA DIÁSPORA",
        "banner_video": "", # Add URL for Hijos Background Loop
        "sub_sections": [
            {
                "title": "Feature Documentary",
                "videos": [
                    # Add Hijos video/trailer link here
                ]
            }
        ] 
    },
    {
        "id": "always-lunes",
        "title": "ALWAYS LUNES",
        "banner_video": "", # Add URL for Always Lunes Background Loop
        "sub_sections": [] 
    }
]

@app.route('/')
def intro(): return render_template('intro.html')

# This is the NEW main page
@app.route('/work/')
def work(): 
    # Reshuffle NMW on refresh
    random.shuffle(nmw_videos)
    # Update reference inside portfolio
    portfolio[0]['sub_sections'][0]['videos'] = nmw_videos
    return render_template('work.html', sections=portfolio)

@app.route('/about/')
def about(): return render_template('about.html')

# Deprecated but kept for safety/reference if needed
@app.route('/archive/') 
def archive(): return "Old Work Page Archive" 

if __name__ == '__main__':
    freezer.freeze()
