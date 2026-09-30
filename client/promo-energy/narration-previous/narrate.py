from pathlib import Path
import asyncio,json
import edge_tts
R=Path(__file__).resolve().parent
lines=[(.25,3.5,'Patient records. Still on cards?'),(3.6,7.7,'Time wasted searching. And sometimes, records go missing.'),(7.9,11.9,'Installment balances? Another notebook to update.'),(12.1,14.5,'Meet Den Click.'),(14.7,21.7,'Search a name. Open their profile. Their history, right there.'),(22,26.7,'Previous treatments and important files, together in one place.'),(27,32.7,'Check the dental chart. See what’s been treated, and what needs attention.'),(33,36.7,'Next visit? It’s on the calendar.'),(37,39,'Track installments.'),(39,41.8,'Enter today’s payment.'),(42.1,43.2,'Save.'),(44,45.5,'The balance updates.'),(45.4,49.9,'Sensitive patient details and files are encrypted.'),(50,55,'One-time payment available. No required monthly subscription.'),(55,59.9,'Less searching. More caring. Message us for a free demo.')]
(R/'narration.json').write_text(json.dumps([dict(start=a,end=b,text=t) for a,b,t in lines],indent=2))
async def main():
 for i,(_,_,t) in enumerate(lines):
  p=R/f'voice-{i}.mp3'
  if not p.exists():await edge_tts.Communicate(t,voice='en-US-AriaNeural',rate='+8%',pitch='+4Hz',receive_timeout=30).save(str(p))
  print('Narration',i,flush=True)
asyncio.run(main())
