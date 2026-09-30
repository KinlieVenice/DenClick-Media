from pathlib import Path
import asyncio,json,sys
import edge_tts
R=Path(__file__).resolve().parent
lines=[
(.2,11.9,"A familiar face walks into your clinic. You remember the patient, but where's their record? Cards to search, another notebook to check for their balance."),
(12.1,21.4,"With Den Click, that visit starts differently. Type their name to bring up their profile, ready to pick up where you left off."),
(21.5,27,"Supporting records stay close, too. Open their X-rays and referral forms."),
(27.1,32.9,"Before treatment begins, check their dental chart to see what needs attention."),
(33.1,36.9,"Their next appointment is right there, too."),
(37.1,47,"For installment payments, enter the amount your patient has paid today, then save it to their record. Their remaining balance updates automatically."),
(47.1,50,"Sensitive details and files are encrypted."),
(50,57.9,"Beyond each visit, see your all-time receivables: how much patients still owe your clinic, together in one place."),
(58,65.9,"Check HMO claims still awaiting payment, including pending and submitted claims, so you know what needs following up."),
(66,69.9,"Keep everyday clinic expenses organized, too."),
(70,73.9,"Monitor supplies and see when stock runs low."),
(74,84.9,"For accountability, the activity log shows who viewed patient records, created entries, or made changes, with timestamps you can review."),
(85,94.9,"There's a one-time payment option, with no required monthly subscription. More time for your patients. Message us for a free demo.")]
lines=[(a+12 if i>=2 else a,b+12 if i>=2 else b,t) for i,(a,b,t) in enumerate(lines)]
lines.append((21.5,33.48,"Take Paolo's braces treatment. Open the history to review each visit, from fitting to later adjustments. The dentist's notes show what changed, how the patient felt, and what to check next time."))
(R/'narration.json').write_text(json.dumps([dict(start=a,end=b,text=t) for a,b,t in lines],indent=2))
async def main():
 for i,(_,_,t) in enumerate(lines):
  if len(sys.argv)>1 and str(i) not in sys.argv[1:]:continue
  words=[]
  stream=edge_tts.Communicate(t,voice='en-US-AvaMultilingualNeural',rate='+0%',pitch='+0Hz',boundary='WordBoundary',receive_timeout=30)
  with (R/f'voice-{i}.mp3').open('wb') as output:
   async for chunk in stream.stream():
    if chunk['type']=='audio':output.write(chunk['data'])
    elif chunk['type']=='WordBoundary':words.append(chunk)
  (R/f'voice-{i}-words.json').write_text(json.dumps(words,indent=2))
  print('Narration',i,flush=True)
asyncio.run(main())
