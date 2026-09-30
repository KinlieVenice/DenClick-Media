from pathlib import Path
import asyncio,json
import edge_tts
R=Path(__file__).resolve().parent
lines=[(.4,6.6,'When a patient returns, their history should not be buried in a stack of folders.'),(7.2,11.6,'With Den Click, find their record in just a few clicks.'),(12.2,20.2,'Open their profile. Previous treatments, medical details, and important files, together in one place.'),(21.2,24.6,'Sensitive patient details and files are encrypted.'),(25.2,32.6,'Check the dental chart, review previous work, and see what needs attention before treatment begins.'),(34.2,38.8,'Then check their appointment and keep the next visit organized.'),(40.2,47.4,'Record today’s payment. See what’s paid, and what’s left, even when the patient pays in installments.'),(48.2,51.6,'The rest of your clinic stays organized, too.'),(52,59.6,'One-time payment available, with no required monthly subscription. Message us for a free demo.')]
(R/'narration.json').write_text(json.dumps([dict(start=a,end=b,text=t) for a,b,t in lines],indent=2))
async def main():
 for i,(_,_,t) in enumerate(lines):
  p=R/f'voice-{i}.mp3'
  if not p.exists() or p.stat().st_size<1000:await edge_tts.Communicate(t,voice='en-PH-RosaNeural',rate='+0%',receive_timeout=30).save(str(p))
  print('Narration',i,flush=True)
asyncio.run(main())
