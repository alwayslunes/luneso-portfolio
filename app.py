from flask import Flask, render_template
from flask_frozen import Freezer
import random

app = Flask(__name__)
freezer = Freezer(app)

# --- 1. NEW MUSIC WEDNESDAYS ---
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

# --- 2. BEYOND THE CLUB ---
btc_urls = [
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_Brocklee.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_EliasRischmawi.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_JupiterVelvet.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_MikahAmani.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_OpalAmRah.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_Sayje.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_Ultrathem.mp4"
]
btc_videos = [{"url": url} for url in btc_urls]

# --- 3. SOCIAL CONTENT (Updated with New Venue Videos) ---
raw_content_urls = [
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Cam_Arlo_Masisi-CTA-Soiree.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Cam_CTA_DearEleanor.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Cam_MicDrop_AlwaysLunes.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_CaribbeanCunt_Willys.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_GrampsClosing.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_HobNobHomies_Unseen.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_HowBazar.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_IIIPoints2025.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Interview_TrustNobody.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_MMW.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_MiamiZineFair.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_OtraNoche.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_PAMM_THFF.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_PerreoDelPasado_THFF.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Rumbass_TheCorner.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_SonidoErotik_Willys.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Underground.mp4",
    # NEW VIDEOS ADDED BELOW
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Venue_DaleZine.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Venue_Gramps.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Venue_TerrestrialFunk.mp4",
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_WillysClosingNight.mp4"
]

social_videos = []
for url in raw_content_urls:
    filename = url.split('/')[-1]
    
    label = ""
    if filename.startswith("Cam_"):
        label = "Shot on Blackmagic PCC 6K G2"
    elif filename.startswith("Phone_"):
        label = "Shot on iPhone"
    
    social_videos.append({
        "url": url,
        "shot_on": label
    })

# --- PORTFOLIO STRUCTURE ---
portfolio = [
    {
        "id": "content",
        "title": "CONTENT",
        "banner_video": "", 
        "sub_sections": [
            {
                "title": "Social Content",
                "videos": social_videos
            },
            {
                "title": "Beyond the Club",
                "videos": btc_videos
            },
            {
                "title": "New Music Wednesdays",
                "videos": nmw_videos
            }
        ]
    },
    { "id": "narrative", "title": "NARRATIVE", "banner_video": "", "sub_sections": [] },
    { "id": "documentary", "title": "DOCUMENTARY", "banner_video": "", "sub_sections": [] },
    { "id": "hijos", "title": "HIJOS DE LA DIÁSPORA", "banner_video": "", "sub_sections": [] },
    { "id": "always-lunes", "title": "ALWAYS LUNES", "banner_video": "", "sub_sections": [] }
]

@app.route('/')
def intro(): return render_template('intro.html')

@app.route('/work/')
def work(): 
    random.shuffle(nmw_videos)
    random.shuffle(btc_videos)
    random.shuffle(social_videos)
    
    subs = portfolio[0]['sub_sections']
    subs[0]['videos'] = social_videos
    subs[1]['videos'] = btc_videos
    subs[2]['videos'] = nmw_videos
    
    if social_videos:
        portfolio[0]['banner_video'] = social_videos[0]['url']
    
    return render_template('work.html', sections=portfolio)

@app.route('/about/')
def about(): return render_template('about.html')

if __name__ == '__main__':
    freezer.freeze()
