from pathlib import Path
import asyncio, json, subprocess, wave, math, textwrap
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg, edge_tts
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'tutorial-output/DenClick-Tutorial.mp4'
FF=imageio_ffmpeg.get_ffmpeg_exe()
SCENES=[
(0,5,'Your clinic. Too many places?', 'Still juggling patient records, appointments, payments, and expenses in different places?',52),
(5,10,'Meet your more organized clinic.', 'Meet Den Click. Your dental clinic, organized in one simple system.',None),
(10,18,'Every patient, one complete picture.', 'Create patient profiles, and find treatment histories, medical records, and uploaded files in just a few clicks.',654),
(18,27,'See the details. Plan the next step.', 'Use the digital dental chart to record tooth conditions and treatments, and see what needs attention at every visit.',1190),
(27,34,'A clearer day starts here.', 'Keep upcoming appointments and patient schedules together in one easy-to-use calendar.',189),
(34,43,'Payments made easier to track.', 'Record treatments, payments, and installment balances, with cash, G Cash, bank transfer, card, or H M O.',784),
(43,50,'Know how your clinic is doing.', 'Track expenses, receivables, inventory, and financial performance, with everything connected.',1479),
(50,56,'Patient records, protected.', 'Sensitive patient details and uploaded files are encrypted to help keep records secure.',None),
(56,60,'See DenClick in action.', 'Message us for a free demo. Discover Den Click today!',None),
]
(ROOT/'script.json').write_text(json.dumps([dict(start=a,end=b,heading=h,narration=t,source=s) for a,b,h,t,s in SCENES],indent=2))
async def voices():
 for i,(_,_,_,text,_) in enumerate(SCENES):
  p=ROOT/f'voice-{i}.mp3'
  if not p.exists() or p.stat().st_size < 1000: await edge_tts.Communicate(text,voice='en-PH-RosaNeural',rate='+5%').save(str(p))
  print('Voice',i,flush=True)
asyncio.run(voices())
