# DenClick — Less searching. More caring.

`DenClick-Energetic-107s-v2.mp4` is the extended energetic 107-second ad. The previous 60- and 95-second MP4s are retained. The earlier promo remains in `../promo-story/`.

- 0–21.5s: returning-patient problem, DenClick reveal, search and populated Medical Info.
- 21.5–33.5s: open Paolo’s braces treatment; read four dated visits, adjustment notes and linked appointments.
- 33.5–49s: treatment list, three attachment thumbnails, dental chart and appointments.
- 49–59s: record a ₱1,500 braces installment; remaining balance changes from ₱25,500 to ₱24,000.
- 59–62s: encrypted sensitive details and files.
- 62–70s: all-time receivables.
- 70–78s: three pending/submitted HMO claims totaling ₱8,000.
- 78–82s: expenses; 82–86s: inventory.
- 86–97s: activity log showing who viewed, created and edited records.
- 97–107s: one-time payment option, no required monthly subscription, free-demo invitation.

## Picture and sound

The UI was recorded again in the isolated test environment. All patient information is fictional. Paolo now has 10 treatment cases across multiple visits: nine paid cases and the active braces treatment. Three actual uploaded image attachments display working thumbnails: an X-ray, an original fictional referral form, and a treatment-reference model. Asset provenance is in `assets/SOURCES.md`. A visible arrow follows actual browser mouse movements. Click rings are recorded into the UI; click and typing sounds use captured event timestamps mapped through the edit. Camera moves focus on search, tooth details, payment typing, save, and the remaining balance.

The opening uses the previously generated clinic photographs with camera movement; it is not filmed live-action footage. The notebook is a fictional motion graphic. The original DenClick logo is used. The closing uses a consistent logo frame with animated text. Captions have no solid text boxes.

Narration is synthesized English (en-US-AvaMultilingualNeural) at natural pitch and synthesis rate, with no playback speed-up. Fourteen connected passages replace the previous 15 short fragments. See `final-script.md`. Music is an original synthesized 120 BPM arrangement with bass, chord stabs, plucks and percussion, gaining layers at the reveal and closing. Music ducks beneath speech.

Security wording is limited to encrypted sensitive patient details and files. The subscription/payment positioning was supplied by the product owner. No certification or absolute security guarantees are claimed.

## Sources

- `render.py`: camera paths, graphics, edit, synchronized sound effects, music, audio mixing, and export.
- `narrate.py`: voice script and speech generation.
- `edit-timeline.json`: shot list, source times and camera coordinates.
- `braces-capture/pointer-events.json` and `sound-events.json`: actual browser input events and edited sound timing.
- `audio-check.json`: narration placement and measured durations.
- `DenClick-Energetic-107s.srt` / `.vtt`: optional full narration captions.
- `../story-capture/story.spec.js`: repeatable real-application capture; set `STORY_OUTPUT=promo-energy/braces-capture`.

Export: 1920×1080, 30 fps, H.264 CRF 17, AAC stereo 48 kHz 256 kbps, fast-start MP4. All narration fits its scene windows. The capture test verifies six appointments, 10 treatment links, three successfully loaded image thumbnails, three unpaid HMO claims, and the ₱24,000 balance after payment. Full-file decoding and final audio measurements are recorded in `verification.txt`.

Synchronization revision: cuts are driven by measured word timestamps, including X-rays, save, remaining balance, profile, and the closing CTA. Captions also use word timestamps. See `sync-timing.json` and `sync-review.jpg`. The mouth photograph is no longer shown.

Medical Info shows Penicillin and Latex allergies and two fictional medical-history notes. All current UI footage comes from `braces-capture/`. The braces case is ₱45,000: ₱15,000 down payment plus three ₱1,500 payments before the new installment. Every historical payment includes a visit note and appointment link.

Treatment edit revision: 21.5–39s uses consecutive source footage and a consistent crop, with no replayed history or repeated zooms. One stationary label covers the treatment sequence, then changes for attachments. Click sounds are remapped to the revised timing. The earlier 107-second export remains available.
