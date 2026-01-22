from flask import Flask, render_template
from flask_frozen import Freezer
import random

app = Flask(__name__)
freezer = Freezer(app)

# --- HELPER: DETECT CAMERA ---
def get_shot_on_label(url):
    filename = url.split('/')[-1]
    if filename.startswith("Cam_"):
        return "SHOT ON BLACKMAGIC 6K G2"
    elif filename.startswith("Phone_"):
        return "SHOT ON IPHONE"
    return ""

# --- 1. NEW MUSIC WEDNESDAYS ---
nmw_data = [
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_1_Dizzy.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_1_Dizzy.jpg",
        "title": "Dizzy by MajorNine ft. Phoenix James"
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_2_Blood.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_2_Blood.jpg",
        "title": "Blood by RealLiveAnimals"
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_3_BadRomance.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_3_BadRomance.jpg",
        "title": "Bad Romance by raygunscottie"
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_4_TwelfthHour.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_4_TwelfthHour.jpg",
        "title": "Twelfth Hour by Project Rukus."
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_5_Viceversa.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_5_Viceversa.jpg",
        "title": "Viceversa by Chigusa"
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_6_WannaGoOutside.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_6_WannaGoOutside.jpg",
        "title": "Wanna Go Outside by ilikebloo"
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_7_Daydreams.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_7_Daydreams.jpg",
        "title": "Daydreams by MMW ft. ilikebloo"
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_8_RealHigh.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_8_RealHigh.jpg",
        "title": "Real High by Rayan"
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_9_5IVEQUID.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_9_5IVEQUID.jpg",
        "title": "5IVEQUID by nezerat"
    },
    { 
        "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/NMW_10_FLESH.mp4", 
        "thumbnail": "https://lunes.nyc3.cdn.digitaloceanspaces.com/NMW/Thumbnails/NMW_10_FLESH.jpg",
        "title": "FLESH by Hayelo & Ezra Made It"
    }
]

# --- 2. BEYOND THE CLUB ---
btc_data = [
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_Teaser.mp4", "title": "Announcement" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_Brocklee.mp4", "title": "Brocklee" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_EliasRischmawi.mp4", "title": "Elias Rischmawi" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_JupiterVelvet.mp4", "title": "Jupiter Velvet" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_MikahAmani.mp4", "title": "Mikah Amani" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_OpalAmRah.mp4", "title": "Opal Am Rah" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_Sayje.mp4", "title": "Sayje" },
    { "url": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Beyond%20the%20Club/BTC_Ultrathem.mp4", "title": "ULTRATHEM" }
]

# --- 3. SOCIAL CONTENT ---
social_mapping = [
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Cam_Arlo_Masisi-CTA-Soiree.mp4", "Arlo Masisi-CTA-Soiree"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Cam_CTA_DearEleanor.mp4", "CTA DearEleanor"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_CTA_DearEleanor.mp4", "CTA DearEleanor"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Cam_MicDrop_AlwaysLunes.mp4", "M!C DROP by Always Lunes"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_CaribbeanCunt_Willys.mp4", "Caribbean Cunt at Willy's"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_GrampsClosing.mp4", "Closing Night at Gramps"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_HobNobHomies_Unseen.mp4", "Hob Nob Homies at Unseen Creatures"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_HowBazar.mp4", "How Bazar Miami Market"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_IIIPoints2025.mp4", "III Points 2025"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Interview_TrustNobody.mp4", "Trust Nobody at Big"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_MMW.mp4", "Miami Music Week"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_MiamiZineFair.mp4", "Miami Zine Fair"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_OtraNoche.mp4", "Otra noche en Miami"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_PAMM_THFF.mp4", "THFF Opening at PAMM"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_PerreoDelPasado_THFF.mp4", "THFF x Perreo del Pasado at The Corner"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Rumbass_TheCorner.mp4", "Rumbass at The Corner"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_SonidoErotik_Willys.mp4", "Serpent's Ball at Willy's"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Underground.mp4", "Welcome to the Underground"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Venue_DaleZine.mp4", "Venue: DaleZine"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Venue_Gramps.mp4", "Venue: Gramps"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_Venue_TerrestrialFunk.mp4", "Venue: TerrestrialFunk"),
    ("https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_WillysClosingNight.mp4", "Closing Night at Willy's")
]

social_videos = []
for url, title in social_mapping:
    social_videos.append({
        "url": url,
        "title": title,
        "shot_on": get_shot_on_label(url)
    })

# --- PORTFOLIO STRUCTURE ---
portfolio = [
    {
        "id": "content",
        "title": "CONTENT",
        # HARDCODED BANNER VIDEO: Closing Night at Willys
        "banner_video": "https://lunes.nyc3.cdn.digitaloceanspaces.com/Content/Phone_WillysClosingNight.mp4",
        "sub_sections": [
            { "title": "Social Content", "videos": social_videos },
            { "title": "Beyond the Club", "videos": btc_data },
            { "title": "New Music Wednesdays", "videos": nmw_data }
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
    # Clone and shuffle lists
    shuffled_nmw = nmw_data.copy()
    shuffled_btc = btc_data.copy()
    shuffled_social = social_videos.copy()

    random.shuffle(shuffled_nmw)
    random.shuffle(shuffled_btc)
    random.shuffle(shuffled_social)
    
    subs = portfolio[0]['sub_sections']
    subs[0]['videos'] = shuffled_social
    subs[1]['videos'] = shuffled_btc
    subs[2]['videos'] = shuffled_nmw
    
    # Banner is now fixed in the portfolio structure, so we don't overwrite it here
    
    return render_template('work.html', sections=portfolio)

@app.route('/about/')
def about(): return render_template('about.html')

if __name__ == '__main__':
    freezer.freeze()
