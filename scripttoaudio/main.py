from gtts import gTTS
from pydub import AudioSegment
from pydub.generators import Sine
import os

# Your narration script
script = """
A failed rebellion… the death of a friend… and a secret betrayal.
Picking up in the aftermath of Season 2’s bloody cliffhanger, the third and final season of Netflix’s most popular series finds Gi-hun — a.k.a. Player 456 — at his lowest point yet.

But the Squid Game stops for no one.
Gi-hun must make critical choices in the face of overwhelming despair, as he and the remaining players are thrust into even deadlier games that test their resolve like never before.

With each round, the consequences grow more severe.
Meanwhile, In-ho resumes his chilling role as the Front Man to welcome the mysterious VIPs.
His brother Jun-ho continues his search for the elusive island — unaware that a traitor walks among them.

Will Gi-hun make the right decisions?
Or will the Front Man finally shatter his spirit?

Director Hwang Dong-hyuk — the visionary who made history at the 74th Primetime Emmys, becoming the first Asian to win Outstanding Directing for a Drama Series — returns once again as director, writer, and producer.

Season 3 stars:
Lee Jung-jae, Lee Byung-hun, Yim Si-wan, Kang Ha-neul, Wi Ha-jun, Park Gyu-young, Park Sung-hoon, Yang Dong-geun, Kang Ae-sim, Jo Yu-ri, Chae Kuk-hee, Lee David, Roh Jae-won, and Jun Suk-ho — with a special appearance by Park Hee-soon.

The game continues. But the stakes?
They've never been higher.
"""

# Step 1: Generate the voice audio
tts = gTTS(text=script, lang='en')
tts.save("voice.mp3")

# Step 2: Load the voice
voice = AudioSegment.from_mp3("voice.mp3")

# Step 3: Generate or load background music
# Example: generate a soft ambient tone (optional, you can replace with a real track)
background = Sine(440).to_audio_segment(duration=len(voice)) - 30  # softer volume

# OR use real music (comment above and use below if you have a file)
# background = AudioSegment.from_file("background_music.mp3").set_duration(len(voice)) - 20

# Step 4: Mix both audios
final = background.overlay(voice)

# Step 5: Export final audio
final.export("final_squid_game_audio.mp3", format="mp3")

print("✅ Final audio saved as final_squid_game_audio.mp3")
