from flask import Flask, render_template
from flask_frozen import Freezer
import random

app = Flask(__name__)
freezer = Freezer(app)

# --- 1. NEW MUSIC WEDNESDAYS (Shuffled) ---
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

# --- 3. SOCIAL CONTENT ---
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
    "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Underground.mp4"
]

cat_recaps = []
cat_underground_interviews = []
cat_venues = []

for url in raw_content_urls:
    filename = url.split('/')[-1]
    
    # "Shot On" Logic
    label = ""
    if filename.startswith("Cam_"):
        label = "Shot on Blackmagic PCC 6K G2"
    elif filename.startswith("Phone_"):
        label = "Shot on iPhone"
    
    video_obj = { "url": url, "shot_on": label }

    # Categorization Logic
    if "Interview" in filename or "Underground" in filename:
        cat_underground_interviews.append(video_obj)
    elif "Venue" in filename:
        cat_venues.append(video_obj)
    else:
        cat_recaps.append(video_obj)

random.shuffle(cat_recaps)
random.shuffle(cat_underground_interviews)
random.shuffle(cat_venues)

# --- PORTFOLIO STRUCTURE ---
portfolio = [
    {
        "id": "content",
        "title": "CONTENT",
        # Default banner: First video of "Social Content"
        "banner_video": cat_recaps[0]['url'] if cat_recaps else "",
        "sub_sections": [
            {
                "title": "Social Content",
                "videos": cat_recaps
            },
            {
                "title": "Beyond the Club",
                "videos": btc_videos
            },
            {
                "title": "Underground & Interviews",
                "videos": cat_underground_interviews
            },
            {
                "title": "Venues",
                "videos": cat_venues
            },
            {
                "title": "New Music Wednesdays",
                "videos": nmw_videos
            }
        ]
    },
    {
        "id": "narrative",
        "title": "NARRATIVE",
        "banner_video": "",
        "sub_sections": [] 
    },
    {
        "id": "documentary",
        "title": "DOCUMENTARY",
        "banner_video": "",
        "sub_sections": [] 
    },
    {
        "id": "hijos",
        "title": "HIJOS DE LA DIÁSPORA",
        "banner_video": "",
        "sub_sections": [] 
    },
    {
        "id": "always-lunes",
        "title": "ALWAYS LUNES",
        "banner_video": "",
        "sub_sections": [] 
    }
]

@app.route('/')
def intro(): return render_template('intro.html')

@app.route('/work/')
def work(): 
    # Reshuffle on refresh
    random.shuffle(nmw_videos)
    random.shuffle(cat_recaps)
    random.shuffle(cat_underground_interviews)
    random.shuffle(cat_venues)
    
    # Update portfolio references
    content_subs = portfolio[0]['sub_sections']
    content_subs[0]['videos'] = cat_recaps
    content_subs[2]['videos'] = cat_underground_interviews
    content_subs[3]['videos'] = cat_venues
    content_subs[4]['videos'] = nmw_videos
    
    # Ensure banner is valid
    if cat_recaps:
        portfolio[0]['banner_video'] = cat_recaps[0]['url']
    
    return render_template('work.html', sections=portfolio)

@app.route('/about/')
def about(): return render_template('about.html')

if __name__ == '__main__':
    freezer.freeze()
