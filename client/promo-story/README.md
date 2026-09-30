# DenClick — A Few Clicks Away

Final: `DenClick-Story-60s.mp4`. 60.00 seconds, 1920×1080, 25 fps, H.264 video, 48 kHz AAC stereo. Open `index.html` for playback. Separate SRT and WebVTT captions included.

## What is real and what is generated

- UI: newly recorded actual DenClick application using the isolated `dental_clinic_e2e` database. All patient records are fictional. Paolo Cruz stays consistent across profile, treatment, tooth #16, appointment and payment.
- Payment: real UI entry of ₱200 through GCash changes the demo treatment balance from ₱700 to ₱500. Total cost is ₱1,000, with an earlier ₱300 cash installment.
- Opening: two images generated using the built-in image-generation tool, edited with subtle camera movement. These are a cinematic recreation, not filmed clinic B-roll or generated full-motion video. Assets are saved in `assets/`.
- Logo: actual `client/public/logo.png`.
- Voice: synthesized English narration, en-PH-RosaNeural. Two lines shortened to fit; every final voice clip remains at 1.0× speed. See `audio-check.json` and `final-script.md`.
- Score and Foley: original synthesized bright 104 BPM major-key instrumental with light plucks, bass and soft percussion, light paper/keyboard/click sounds, and a soft payment tone. No third-party sampled music. Music ducks under narration.
- Offer: one-time payment option / no required monthly subscription, supplied by the product owner.
- Security: precise patient-details-and-files encryption wording; no certification or absolute-security claims.

## Verification

The isolated capture completed successfully, including the ₱500 remaining-balance assertion. The final MP4 decodes without errors and measures exactly 60 seconds. All voice clips fit their scene windows without tempo changes. Representative frames were checked across opening, search, profile, chart, appointment, payment, dashboard, offer and CTA. `review.jpg` contains the contact sheet.

## Editable sources

`render.py`: picture edit, text graphics, music, Foley and final audio mix. `edit-timeline.json`: exact shot choices and crops. `narrate.py`: speech generation. `../story-capture/story.spec.js`: repeatable app capture. `capture-markers.json`: raw video time references. `../playwright.story.config.js` and `../vite.story.config.js`: isolated capture configuration with development reloads disabled. `assets/prompts.md`: image generation prompts.

Render dependencies: Pillow, NumPy, imageio-ffmpeg. Speech generation additionally uses edge-tts and network access. Temporary packages were installed under `/tmp/denclick-video-tools`; restore them if that directory is cleared.

No production app behavior or upload limits were changed.

Audio revision: replaced the sparse 82 BPM score with a brighter 104 BPM arrangement. Existing narration and picture are preserved; the encoded video stream matches the previous version exactly. Prior mix retained in `DenClick-Story-60s-previous-audio.mp4`.

Caption revision: feature labels now use larger dark teal text at the upper center, without a caption background. Labeled scenes reserve a top margin so captions do not cover patient details or controls. Existing upbeat audio is copied without re-encoding.
