# DenClick 60-second promo

Deliverable: `DenClick-60s-Demo.mp4` — exactly 60 seconds, 1920×1080, 25 fps, H.264 video and AAC stereo audio. Open `index.html` to play locally.

- Actual logo: `client/public/logo.png`, used in the introduction and ending.
- Footage: existing DenClick tutorial; fictional sample records. No new recording.
- Narration: synthesized English voice, en-PH-RosaNeural, generated with edge-tts. See `DenClick-60s-script.md`.
- Music: original synthesized major-key instrumental from the tutorial, made slightly more upbeat and lowered beneath narration. No third-party music samples.
- Encryption wording describes sensitive patient details and uploaded files, rather than claiming every database field is encrypted.
- Verified: full video decodes successfully; voice clips fit their scenes; audio mix has no clipped samples. Rendered frames reviewed for logo, captions, chart, calendar, payments, finance, inventory, security and CTA.

Build sources: `build-promo.py` generates narration; `render-promo.py` assembles footage, graphics and audio. They use Pillow, NumPy, imageio-ffmpeg and edge-tts. The music source is in `client/tutorial-output/audio`.
