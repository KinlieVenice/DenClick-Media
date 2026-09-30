# DenClick — “A returning patient”

**Final duration: exactly 60.00 seconds.** Master: 1920×1080, 25 fps, 1,500 frames. All timeline times below are decimal seconds, on 25 fps frame boundaries. Out points are exclusive.

This is an editing plan, not a newly rendered video. Required pickup shots are explicitly identified below. Voiceover windows are recording targets; the revised voice has not yet been recorded or timed.

The story follows **one fictional returning patient, Paolo Cruz**. The front desk searches for his paper record, finds him in DenClick, reviews his history, checks a tooth and appointment, then records a payment. The wider clinic appears only after that patient’s journey makes sense.

The visual payoff is the change from searching through folders to finding the right information. The commercial payoff is a one-time payment option with no required monthly subscription. Use that offer exactly as supplied by the owner; do not expand it into “free forever,” “lifetime everything,” or a price promise.

## 1. Asset review and source selection

I catalogued the available recordings, graphics and audio; read the tutorial action script and caption timing; and visually inspected the candidate search, patient, chart, payment, appointment and dashboard material, including the first promo.

| Asset | Finding | Decision |
|---|---|---|
| `client/tutorial-output/DenClick-Tutorial.webm` | 1280×720, 25 fps, 09:48.80. Original recording made with accelerated tutorial waits. Captions, amber cursor and highlights are baked in. | Best existing picture source; use before the re-encoded MP4 when salvaging shots. |
| `client/tutorial-output/raw/denclick-tutorial-DenClick-tutorial-Tagalog-/video.webm` | Same size and SHA-256 as the WebM above. | Duplicate, not another take. |
| `client/tutorial-output/DenClick-Tutorial.mp4` | 1280×720, 25 fps, 39:15.20. Four-times-longer viewing version. | Source time reference for this plan. Its timestamps are easier to review. |
| `DenClick-Tutorial-Voiced.mp4` | Same tutorial picture, with Tagalog narration and music. | No picture advantage. Do not bring its audio into this edit. |
| `client/promo-output/DenClick-60s-Demo.mp4` and `scene-*.mp4` | Reframed derivatives of the same take; oversized branding and long sentences make them feel like slides. | Do not use as the picture source. |
| `client/public/logo.png` / `logo-mark.png` | Actual DenClick identity, with transparency. | Use the real logo at the ending. The app’s own logo can appear naturally after the reveal. |
| `tutorial-output/audio/DenClick-background-original.wav` | Original synthesized instrumental from the earlier tutorial. | Available fallback only. The story needs a more restrained arrangement than the first promo. |
| Prior English `voice-*.mp3` | Feature-led wording with some accelerated delivery. | Replace with the shorter story narration below. |
| PDFs, exported patient ZIP and screenshots | Demo support material, not physical clinic footage. The attachment labelled “Panoramic X-ray” is a sample PDF, not an actual radiograph. | Do not open it and imply it is a diagnostic X-ray. Use an attachment tile or a clearly labelled sample consent file. |
| Physical clinic footage / recorded Foley | None found in the available assets. | Short opening recreation and subtle paper sounds required. |

There are **no independent alternate takes** of the same workflow to choose between. There is also no fully clean, caption-free recording of the complete patient journey.

**Existing-shot locator.** These are reviewed candidate ranges, not claims that every frame in each range is ready to use. “M” means the long MP4. For original WebM seeking, divide M seconds by four. Retiming the raw take to 25% reproduces M timing; a 2× edit of M equals 50% raw playback. Do not mistake accelerated recording speed for real app performance.

| ID | M source location | What it actually shows | Use / limitation |
|---|---|---|---|
| E1 | 10:41.40–10:45.00 | “Paolo Cruz” typed into Patients search; result clicked. | Strongest existing reveal. No tutorial caption across the key search area. Trim the incoming wandering cursor. Cut before the chapter card. |
| E2 | Freeze at 10:49.52 | Paolo’s profile, before the long caption resumes. | Useful clean profile hold. Does not prove prior visit history by itself. |
| E3 | 14:16.00–14:18.80 | Populated Treatments tab. | Existing treatment list, but before the later price correction. Do not match its ₱900 balance to the later ₱700 payment example without showing a price change. Replace for continuity. |
| E4 | 19:39.80–19:44.80 | Attachment tile. | Usable as a file-list insert; do not open the sample PDF as if it were a radiograph. |
| E5 | 19:51.20–19:57.20 | Chart and tooth #16 selection. | Selection is usable if tightly trimmed. |
| E6 | 20:08–20:33 | Tooth condition selection, notes and history. | Reject for the final clinical-detail shot: the saved status is “Incipient Caries” while the note says the tooth was filled. Do not digitally relabel it. |
| E7 | 11:04–11:25; 05:11–05:38 | Paolo’s empty appointments tab; a later calendar detail for Liza. | Reject as Paolo’s upcoming appointment. Needs a same-patient pickup. |
| E8 | 15:03; 15:09–15:28; 15:38.48 | ₱700 balance; ₱200 payment flow; ₱500 remaining balance. | Correct arithmetic. Actual new method is **GCash**, despite the tutorial script intending Cash. Older history includes a pending HMO claim and the earlier price correction. Useful reference, but a clean pickup tells the story better. |
| E9 | 01:22–01:27; 02:32–02:39 | Dashboard money cards; Revenue Trend. | Supporting fallback, with tutorial overlays/cursor to remove through framing. Prefer a clean final clinic overview from the same demo session. |

Contact sheets in this folder: `search-history.jpg`, `payment-chart.jpg`, `continuity-check.jpg`. They document the continuity issues above.

## 2. Required pickups and preparation

**B1 — physical clinic opening, three shots.** Film a small, believable reception desk with warm daylight, neutral folders and paper patient cards. Use hands/shoulder framing; no acting to camera, exaggerated frustration, visible real records or identifiable patient faces. A returning patient approaches the counter, the receptionist checks several folders, then finds a card labelled **PAOLO CRUZ**. The name must be sharp and composed to match the digital result. About 20–30 seconds of raw footage is enough for seven seconds on screen. Record a separate 10-second paper shuffle and folder-set-down sound. If filming is unavailable, use a tasteful tabletop recreation of this exact action; a generated still can establish the desk but cannot convincingly replace the hand/searching action by itself.

**P1 — one clean demo capture session.** Record at least 2560×1440/25 fps with readable browser scaling, no tutorial banners and a normal pointer. Use only a local/demo dataset. Prepare Paolo with a genuinely populated past treatment, a consistent tooth record, an upcoming appointment and a simple installment balance. Capture each action with two seconds of clean handles before and after it. This is a few short takes in one session, not another full tutorial.

- P1a: search Paolo → result → profile, with realistic system response time.
- P1b: profile → populated Treatments tab → attachment list. Prior visits must predate the current visit.
- P1c: tooth #16 → an existing completed filling and its dated history. If a tooth needing attention is also visible, show it in the chart without opening a second modal. Do not call a caries status a completed treatment.
- P1d: Paolo’s upcoming appointment from his profile → the matching calendar entry. Name, date and dentist must agree.
- P1e: treatment total ₱1,000; already paid ₱300 cash; balance ₱700. Enter ₱200 GCash, save, confirm, then show paid ₱500 / remaining ₱500. This is a recommended **new demo setup**, not a description of the old footage’s HMO history.
- P1f: dashboard from the same session, with readable Revenue, Expenses and Receivables cards. Capture a stable end-state. No need to stage unrelated inventory or expense transactions.

**Graphics:** real logo; one simple 20–24 px outline lock at 1080p; one restrained click ring; two pricing text states and a CTA. No new illustration package, security animation sequence or decorative feature cards required.

## 3. Locked picture edit — 60.00 seconds

“P1” rows are pickup requirements, not footage already on disk. Use E1/E2 as the existing-footage fallback for the reveal; their motion is the reference for the new capture. Do not splice a different patient into any of these rows.

| Output in–out | Exact picture order / action | Source | Exact editorial text | Edit, emphasis and hold |
|---|---|---|---|---|
| 00.00–02.80 | Returning patient at reception; desk and paper cards in foreground. | B1 wide/detail | **Still searching through patient cards?** | Start in the real clinic. Static or very slight camera drift. No logo or UI. |
| 02.80–05.40 | Receptionist checks two or three folders. | B1 hands close-up | Continue the same text. | Straight cut. Let the physical searching take time. |
| 05.40–07.00 | Patient name on paper card: PAOLO CRUZ. | B1 card detail | Fade the hook off by 06.00; card name is the focus. | Hold the name steady. Frame it at the same position/scale as the upcoming digital name. |
| 07.00–08.80 | Type Paolo into patient search; name resolves. | P1a; fallback E1 typing | **A few clicks away.** | Match cut on the name. Keyboard sound bridges the cut. No logo sting. |
| 08.80–10.20 | One search result: Paolo Cruz. Click it once. | P1a; fallback E1 result | Continue. | 1-second readable result, then one small click ring. Remove cursor travel. |
| 10.20–12.00 | Paolo’s profile appears. | P1a; fallback E2 hold | Continue, then fade by 11.80. | Hard cut only if required to remove the tutorial chapter card. Do not fake zero loading time with a stopwatch or speed claim. |
| 12.00–14.40 | Profile identity and medical summary. | P1b | None. | Same framing as previous shot; let the name anchor the story. |
| 14.40–18.00 | Treatments tab opens with a dated previous treatment. | P1b | **Patient history** | Click tab, then leave the list still for at least 2 seconds. |
| 18.00–21.00 | Relevant attachment tile / consent record. | P1b; E4 fallback | None. | One cut or tab click, no PDF viewer detour. |
| 21.00–25.00 | Return to the same patient profile; restrained lock beside the header. | P1b clean hold | **Protected with encryption** | Freeze the settled profile if needed. Lock/text fade in over 0.24 sec, out over 0.24 sec. Keep UI visible. |
| 25.00–27.00 | Open Odontogram. | P1c; E5 selection fallback | **Digital dental chart** | Stay inside Paolo’s record. No transition to an unrelated full-screen title. |
| 27.00–29.00 | Click tooth #16; its details open. | P1c | Continue label. | Single click ring, no bouncing tooth or pulsing loop. |
| 29.00–32.00 | Show consistent condition and dated treatment/history. | P1c | None. | Static close framing. The viewer reads one clear clinical example. |
| 32.00–34.00 | Hold that result, then close the modal if it helps the next cut. | P1c | None. | Freeze 1.5–2 seconds if live motion is distracting. Never freeze mid-click. |
| 34.00–36.00 | Paolo’s upcoming appointment in his record. | P1d | **Next appointment** | Name remains visible. One click on the scheduled visit. |
| 36.00–40.00 | Matching calendar entry/detail, same patient and date. | P1d | None. | 2-second readable hold on the appointment. No dragging/rescheduling demo. |
| 40.00–42.00 | Treatment detail: balance ₱700, total ₱1,000. | P1e | **Payments & installments** | Crop to treatment name and totals. Brief outline on the real balance field. |
| 42.00–44.00 | Enter ₱200; GCash selected. | P1e | None. | Amount and method both visible. No tour of every payment option. |
| 44.00–45.20 | Save Billing → confirm. | P1e | None. | Trim pauses, preserve actual order. Show confirmation click; cut success-modal dwell. |
| 45.20–48.00 | Updated remaining balance: ₱500; new payment visible. | P1e | None. | At least 2 seconds on the true updated state. One soft confirmation tone. No synthetic counting animation over an unchanged UI. |
| 48.00–52.00 | Pull back to clinic dashboard: Revenue, Expenses, Receivables. | P1f | **Your clinic. Organized.** | One calm cut. Hold overview for 4 seconds; no rapid module montage. |
| 52.00–55.00 | Continue dashboard; gently give it more breathing room. | P1f | **Built for small dental clinics** | Begin closing voice here so pricing is not rushed into five seconds. A single 100%→97% easing move is sufficient. |
| 55.00–58.00 | Actual logo over a softly subdued dashboard. | Logo + P1f clean still | **One-time payment option** / **No required monthly subscription** | Both pricing lines visible together for 3 seconds. Use a small logo, generous space; no extra slogan or CTA yet. |
| 58.00–60.00 | Same end composition; pricing fades out, invitation replaces it. | Logo + P1f clean still | **Message us for a free demo.** | Hold logo + one invitation for 2 seconds. End on this frame, not on black. |

The clinic overview deliberately uses the dashboard’s expense and receivable cards. Inventory and separate Finance/Expenses pages are omitted from this cut: they are not needed to understand this patient’s story. No claims of live dashboard changes tied to Paolo’s payment unless that state is actually captured.

## 4. Exact voiceover placement

Warm, conversational English, with natural pauses. The revised script is 115 words. Aim for roughly 125–145 spoken words per minute, allowing visual silence between thoughts. Record to these windows; shorten a line if needed rather than applying unnatural time compression. The final closing line starts over the dashboard at 52 seconds, three seconds before the logo.

| Target voice window | Exact spoken words | Picture under it |
|---|---|---|
| 00.40–06.60 | “When a patient returns, their history shouldn’t be buried in a stack of folders.” | Reception, searching, paper name. |
| 07.20–11.60 | “With DenClick, find their record in just a few clicks.” | Search, result, profile opens. |
| 12.20–20.20 | “Open their profile. Previous treatments, medical details, and important files—all together, ready for the next visit.” | Profile, history, attachments. |
| 21.20–24.60 | “Sensitive patient details and files are encrypted.” | Same profile, small lock. |
| 25.20–32.60 | “Check the dental chart, review previous work, and see what needs attention before treatment begins.” | Chart, tooth, history; final result breathes until 34.00. |
| 34.20–38.80 | “Then check their appointment and keep the next visit organized.” | Paolo’s upcoming visit. |
| 40.20–47.40 | “Record today’s payment. See what’s paid, and what’s left—even when the patient pays in installments.” | ₱700 → ₱200 GCash entry → ₱500. |
| 48.20–51.60 | “The rest of your clinic stays organized, too.” | Dashboard. |
| 52.00–59.60 | “Built for small clinics. One-time payment available, with no required monthly subscription. Message us for a free demo.” | Dashboard → pricing → CTA. |

Pronounce DenClick naturally as “Den Click.” No theatrical sales inflection. Deliver “a few clicks” as relief, not excitement. No artificial acceleration of the final offer.

**Security accuracy:** the reviewed implementation encrypts patient identity/medical fields, supported sensitive text and uploaded file bytes. It does not justify a blanket claim that every clinic/database record is encrypted. That is why the final line specifies “patient details and files.” No certification, compliance or absolute-safety claims appear.

## 5. Cropping, camera movement, cursor and transitions

**Default:** use actual UI as the frame, rather than a tiny browser floating inside a branded slide. Keep the patient name, active tab and result visible whenever the crop permits. Maintain consistent text size across cuts. Prefer clean high-resolution pickups over magnifying the old 720p source.

| Scene | Crop instruction | Movement |
|---|---|---|
| Paper/search | Card name and digital name centered near 42% frame width / 40% height. Match letter height within 10%. | Locked card detail into a direct match cut. No flying folder animation. |
| Search result | Frame search field plus the single result row; remove sidebar and unused bottom space. | Fixed crop while typing and clicking. Widen only after profile opens. |
| Profile/history | Main content panel: retain Paolo’s header, tab row and relevant history rows. Exclude sidebar and empty bottom space. | One gentle 100%→104% move across the first profile hold, then stop. No zoom for each tab. |
| Encryption | Same profile crop as before, with lock/text outside clinical fields. | No new zoom. A settled freeze is acceptable. |
| Dental chart | First retain chart context and patient name; then cut to modal containing tooth number, condition and history. | Prefer a cut in framing to a long animated zoom. Hold selected state. |
| Appointment | First retain patient header and appointment; then frame the relevant calendar day and selected event. | Fixed while date/name is read. Do not show the entire month reduced to tiny text. |
| Payment | Crop first to total/balance; next to amount, method and save; finally to updated balance plus the new payment row. | Match the before/after balance at the same screen position. Avoid pan-and-zoom while numbers change. |
| Dashboard | Main money/receivables area plus enough heading to establish a clinic overview. | Single mild pullback at 52–55 seconds. |
| Ending | Freeze dashboard, mild blur and a translucent warm-white layer so logo/offer remain clear. | Background motion stops; text changes by opacity only. |

**Fallback crop coordinates on the existing 1280×720 source:** E1 search: x=275, y=50, w=980, h=330; E2 profile: x=260, y=30, w=1000, h=540; E4 attachment list: x=270, y=80, w=980, h=500; E5 chart selection: x=275, y=160, w=980, h=430. Fit these crops proportionally in the output; never stretch them to 16:9. These are starting crops for the inspected shots, not a universal crop for the whole tutorial. For new pickups, use the element-based framing above and set final pixel coordinates after capture.

**Cursor:** normal pointer, no constant glow. At important clicks only: a 28–36 px teal ring at 1080p, 25% opacity, 0.24-second fade. Max one ring per click. Important clicks: patient result, tooth #16, appointment, Save Billing. The old large amber dot cannot be cleanly “turned off”; use a pickup when it obstructs text, rather than stacking a second pointer on it.

**Transitions:** direct cuts within the patient journey; the name match cut at 07.00 is the only featured transition. Use a 0.24-second dissolve into the closing subdued dashboard. No white flashes between every section, slide wipes, logo stings or whooshes on ordinary tab changes.

## 6. Sound, music and timing cleanup

| Output time | Sound placement |
|---|---|
| 00.00–00.80 | Quiet clinic room tone. No dramatic problem cue. |
| 02.80 and 04.40 | Two restrained folder/card shuffles, synced to hands. |
| 06.76–08.80 | Soft typing begins just before the digital cut; stop when typing stops. |
| 09.76 | Small mouse click on the patient result. Adjust within that shot to the final visual click frame. |
| 27.40 | Tooth-selection click. |
| 35.20 | Appointment-selection click. |
| 42.20–43.00 | Brief typing for the amount. No repeated keyboard loop. |
| 44.20 and 44.80 | Low-level Save and confirmation clicks. |
| 45.40 | One short, warm two-note confirmation, synced to the actual updated state. |
| 58.00–60.00 | Music gently resolves under the invitation; no sales sting. |

Sound times within action shots are intended sync targets; conform them to the selected take’s actual click frame. Do not play confirmation before the app confirms success.

**Music:** original composition or a track licensed for commercial promotion. Approximately 78–88 BPM, soft felt piano, muted plucked notes, warm sustained backing and almost no percussion. Keep the opening sparse; introduce one warmer layer at the digital reveal. No acoustic corporate strumming, claps, bouncy bells, aggressive synth bass or emotional crescendo. The earlier music may be stripped back and slowed, but should not be reused at its prior upbeat arrangement unchanged.

**Mix:** voice clearly foregrounded; music roughly 18–24 dB below voice while speaking, rising only slightly in pauses. Foley should be felt rather than announced. Suggested final master: around −16 LUFS integrated, true peak at or below −1 dBTP, checked on a phone speaker and headphones. These are mix targets, not measured results for this unmade edit.

**Trim/speed rules:** remove tutorial reading waits, modal dwell after success, cursor wandering, backtracking, duplicate entries, the price correction, void/refund flow and HMO-status explanation. Show at most one relevant payment method. On clean pickups use 100% speed for reading/results; up to 150% for nonessential pointer travel or short typing. If an interaction cannot fit clearly, cut the idle section rather than accelerate the whole workflow. Never accelerate the voice to compensate.

**Freeze frames:** permitted on E2’s clean profile fallback, encryption hold, settled tooth-history result, settled ₱500 balance, and final dashboard. Limit intermediate holds to about 1–2 seconds unless the section explicitly calls for longer. Do not freeze spinners, success-modal fades, moving cursors or a blank page.

## 7. Masks, privacy and text treatment

The tutorial action script explicitly creates fictional demo records, including Paolo. Retain his name as the story’s link. Before export, check every selected frame for real or unverified identifying information, notifications, passwords, reset tokens, email addresses and live browser tabs. Replace data at capture wherever possible. Crop or track-blur unverified phone numbers, addresses and member IDs; never blur Paolo’s fictional name needed for continuity.

Existing captions are burned into the footage and sometimes move from bottom to top. Crop only when the full action remains readable. Do not repeat the first promo’s universal middle-strip crop: it cuts modal headings and can leave caption shadows. Where a caption covers the patient name or payment total, use the clean pickup. Do not cover real values with invented UI graphics.

Use one font family (Lato or the app’s existing sans serif), semibold labels, dark navy and restrained DenClick teal. Keep editorial overlays to one short phrase. At 1080p, use approximately 44–52 px labels; place them consistently with at least 96 px horizontal and 72 px vertical margins. Small security icon and label should sit in clear margin space, not cover medical details. Avoid extra branding during the patient workflow.

Deliver a separate SRT for accessibility. Optional open captions should be short, synchronized phrases, not the full narration sentence permanently under every scene. If an open caption occupies the lower area, move or remove the redundant feature label; never shrink the UI to make room for both.

## 8. Opening, ending and social exports

**Recommended opening frame:** a close, warm reception view: a hand reaches toward worn but orderly folders; a returning patient is suggested at the edge of frame. Text: “Still searching through patient cards?” No computer interface and no DenClick logo.

**Recommended final frame:** actual DenClick logo, a softly subdued dashboard behind it, and “Message us for a free demo.” The offer was readable immediately before this frame. Do not stack slogan, offer, subscription line, CTA and a footer all at once.

**Exports:**

- Primary readable demo: 1920×1080, 16:9, exactly 60.00 seconds, 25 fps, H.264 High, VBR approximately 10–16 Mbps, AAC stereo 48 kHz / 192–256 kbps, Rec.709 SDR, fast-start MP4.
- Social portrait version: 1080×1920, 9:16, same 60-second edit and voice. Reframe each shot individually. Use tight result/modal crops; do not center-crop the landscape film or shrink an entire desktop interface into portrait. Keep important text/actions roughly inside x=90–930, y=240–1500 and check the actual publishing preview for controls/caption overlap. This is a conservative working area, not a guarantee about every platform’s overlay placement.
- Optional feed version: 1080×1350, 4:5, separately reframed if that placement is needed.
- Package: clean master, optional captioned social export, SRT, poster frame and the final script. Do not interpolate to 60 fps or claim that upscaled 720p source is native 4K.

**Acceptance check:** patient name remains Paolo throughout; chart and notes agree; appointment belongs to him; ₱700 minus ₱200 becomes ₱500; UI stays readable on a phone; paper/search transition is clear without sound; pricing text is visible for three seconds; CTA holds for two; duration is 1,500 frames. If these fail, simplify or replace the affected shot instead of adding more motion graphics.
