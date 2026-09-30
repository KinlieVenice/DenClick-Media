from pathlib import Path
import json, math, subprocess, wave, concurrent.futures, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg
R=Path(__file__).resolve().parent; OLD=R.parent/'promo-story'; FF=imageio_ffmpeg.get_ffmpeg_exe()
W,H,FPS=1920,1080,30
NAVY='#123f45';TEAL='#087d80';LIME='#dcf792';CREAM='#f5f8f3'
CAP=R/'referral-capture'
V=next((CAP/'raw').glob('*/video.webm'))
def font(n,bold=True):return ImageFont.truetype('/usr/share/fonts/truetype/lato/Lato-'+('Bold' if bold else 'Regular')+'.ttf',n)
def text(im,words,xy,size=76,fill=NAVY):ImageDraw.Draw(im).text(xy,words,font=font(size),fill=fill,spacing=15)
def center(im,words,y,size=76,fill=NAVY):
 d=ImageDraw.Draw(im);x=(W-d.textlength(words,font=font(size)))/2;d.text((x,y),words,font=font(size),fill=fill)
def logo(im,y=170,width=720):
 l=Image.open(R.parent/'public/logo.png').convert('RGBA');l=l.crop(l.getbbox());l.thumbnail((width,260),Image.Resampling.LANCZOS);im.alpha_composite(l,((W-l.width)//2,y))
def save(im,name):p=R/(name+'.png');im.save(p);return p
# Graphic overlays are composed for this film; all software interactions use the real capture.
def overlay(lines,kicker=None):
 im=Image.new('RGBA',(W,H));
 if kicker:text(im,kicker,(106,112),30,LIME)
 for words,y,color in lines:text(im,words,(100,y),100,color)
 return im
# Opening photographs remain the existing generated cinematic recreation.
for name,lines,kicker in [
 ('problem-cards',[('Patient records.',350,'white'),('Still on cards?',472,LIME)],'A PATIENT RETURNS.'),
 ('problem-search',[('Time spent',350,'white'),('searching.',472,LIME)],'ONE NAME. STACKS OF CARDS.'),
 ('problem-missing',[('And sometimes…',350,'white'),('records go missing.',472,LIME)],'WHEN THE RECORD ISN’T THERE.')]:
 im=Image.new('RGBA',(W,H),(8,28,31,130));im.alpha_composite(overlay(lines,kicker));save(im,name)
# A clearly fictional payment notebook, drawn as a motion graphic.
im=Image.new('RGBA',(W,H),'#eae8df');d=ImageDraw.Draw(im)
d.rounded_rectangle((970,115,1820,975),radius=16,fill='#fffdf2')
for y in range(270,910,82):d.line((1010,y,1770,y),fill='#b7cfcc',width=2)
d.line((1090,140,1090,950),fill='#e8b4a4',width=2)
text(im,'PAYMENT NOTEBOOK',(1130,170),30);text(im,'Paolo Cruz',(1130,280),47)
for words,y in [('Treatment   ₱1,000',380),('Paid                 ₱300',465),('Balance           ₱700',550),('Today              ₱200',635),('New balance       ?',750)]:text(im,words,(1130,y),38)
text(im,'Installments?',(95,355),87);text(im,'More manual',(95,466),76);text(im,'tracking.',(95,562),94,TEAL)
text(im,'ANOTHER NOTEBOOK TO UPDATE.',(100,230),27,TEAL)
save(im,'notebook')
# Reveal and ending use the actual logo and restrained kinetic typography.
for name in ['reveal','offer','monthly','payoff','cta']:
 im=Image.new('RGBA',(W,H),CREAM);d=ImageDraw.Draw(im)
 if name=='reveal':
  logo(im,290,1040);center(im,'A few clicks changes everything.',680,62)
 elif name=='offer':
  logo(im,105,600);center(im,'One-time payment',420,110);center(im,'option available',565,76,TEAL)
 elif name=='monthly':
  logo(im,105,600);center(im,'No required',370,103);center(im,'monthly subscription.',510,103)
  d.line((345,658,1575,658),fill=TEAL,width=9)
 elif name=='payoff':
  logo(im,105,600);center(im,'Less searching.',410,110);center(im,'More caring.',545,110,TEAL)
 else:
  logo(im,105,600);center(im,'Your clinic. Organized.',415,96);center(im,'Message us for a free demo.',610,70,TEAL)
 save(im,name)
for name in ['offer','monthly','payoff','cta']:
 im=Image.open(R/(name+'.png')).convert('RGBA');im.paste((0,0,0,0),(0,0,W,335));save(im,name+'-words')
base=Image.new('RGBA',(W,H),CREAM);logo(base,105,600);save(base,'closing-base')
shots=[]
def shot(a,b,source,start=0,length=None,c0=(0,0,1600),c1=None,graphic=None,label=None):
 shots.append(dict(a=a,b=b,source=str(source),start=start,length=length or b-a,c0=c0,c1=c1 or c0,graphic=graphic,label=label))
photo=OLD/'assets/clinic-opening.png';card=OLD/'assets/patient-card.png'
shot(0,3.5,photo,c0=(0,0,1600),c1=(40,22,1500),graphic='problem-cards')
shot(3.5,5.8,photo,c0=(550,170,1050),c1=(580,190,990),graphic='problem-search')
shot(5.8,7.8,card,c0=(0,0,1600),c1=(65,35,1470),graphic='problem-missing')
shot(7.8,12,R/'notebook.png',c0=(0,0,1920))
shot(12,14.5,R/'reveal.png',c0=(0,0,1920),c1=(35,20,1850))
# Camera paths are source coordinates. Ease into each action, then hold the result.
shot(14.5,18.3,V,2.8,3.8,c0=(265,30,1290),c1=(282,65,920),label='Search a name.')
shot(18.3,21.5,V,6.6,3.2,c0=(280,40,1240),c1=(280,100,1100),label='Their history. Right here.')
shot(21.5,24.6,V,10.0,3.1,c0=(280,95,1260),c1=(285,160,1100))
shot(24.6,27,V,14.6,2.4,c0=(280,100,1250))
shot(27,29.5,V,23.3,2.5,c0=(275,90,1250),c1=(400,255,1080),label='See the treatment history.')
shot(29.5,33,V,26.1,3.5,c0=(400,220,1080),c1=(390,40,870))
shot(33,34.7,V,33.8,1.7,c0=(275,85,1270))
shot(34.7,37,V,41.3,2.3,c0=(285,85,1220),c1=(365,180,1000))
shot(37,39,V,53.8,2,c0=(280,80,1270),c1=(275,65,1320),label='Installments, made clear.')
shot(39,41,V,55.6,2.2,c0=(425,360,760),c1=(420,395,800))
shot(41,42,V,59.7,1.3,c0=(405,425,820))
shot(42,42.8,V,63.0,.8,c0=(415,425,800))
shot(42.8,44,V,64.9,1.2,c0=(420,235,800))
shot(44,45.5,V,68.2,1.5,c0=(650,90,900),c1=(880,65,720),label='Remaining balance: ₱500')
shot(45.5,50,V,73.7,4.5,c0=(270,20,1290),c1=(285,35,1250),label='Sensitive details & files, encrypted.')
shot(50,52.6,R/'closing-base.png',c0=(0,0,1920),graphic='offer-words')
shot(52.6,55,R/'closing-base.png',c0=(0,0,1920),graphic='monthly-words')
shot(55,57.4,R/'closing-base.png',c0=(0,0,1920),graphic='payoff-words')
shot(57.4,60,R/'closing-base.png',c0=(0,0,1920),graphic='cta-words')
# Re-map the existing edit to the refreshed capture's recorded scene markers.
old_marks={m['name']:m['time'] for m in json.loads((R/'capture-markers.json').read_text())['marks']}
new_marks={m['name']:m['time'] for m in json.loads((CAP/'capture-markers.json').read_text())['marks']}
anchors={5:'search-start',6:'profile',7:'history',8:'attachments',9:'chart',10:'tooth',11:'appointments',12:'appointment-detail',13:'balance-before',14:'payment-form',15:'payment-filled',16:'payment-confirm',17:'payment-confirm',18:'balance-after',19:'dashboard'}
for i,name in anchors.items():shots[i]['start']+=new_marks[name]-old_marks[name]
# Show the fuller list and all three real thumbnails without clipping their edges.
shots[7]['c0']=shots[7]['c1']=(0,0,1600)
shots[8]['c0']=(270,110,1250);shots[8]['c1']=(285,145,1170)
# Drive the key visual reveals from actual spoken-word timestamps.
voice_lines=json.loads((R/'narration.json').read_text());voice_trim={}
for i in range(len(voice_lines)):
 raw=subprocess.check_output([FF,'-v','error','-i',str(R/f'voice-{i}.mp3'),'-f','f32le','-ac','1','-ar','48000','-'])
 data=np.frombuffer(raw,dtype='<f4');voice_trim[i]=max(0,np.flatnonzero(np.abs(data)>.002)[0]-480)/48000
word_times={}
for i,e in enumerate(voice_lines):
 word_times[i]=[{**w,'at':e['start']+w['offset']/1e7-voice_trim[i]} for w in json.loads((R/f'voice-{i}-words.json').read_text())]
def cue(i,word):return next(w['at'] for w in word_times[i] if w['text'].lower().strip('.,?!')==word.lower())
def frame(t):return round(t*FPS)/FPS
shots[2]['b']=shots[3]['a']=frame(cue(0,'notebook'))
shots[5]['b']=shots[6]['a']=frame(cue(1,'profile'))
shots[20]['b']=shots[21]['a']=frame(cue(7,'no'))
shots[21]['b']=shots[22]['a']=frame(cue(7,'More'))
shots[22]['b']=shots[23]['a']=frame(cue(7,'Message'))
attachment_at=frame(cue(2,'X-rays')-.65)
shots[7]['b']=attachment_at;shots[8]['a']=attachment_at
shots[8]['start']=new_marks['attachments']-.65;shots[8]['length']=shots[8]['b']-shots[8]['a']
# Show the entered amount, save action, then a confirmed balance at their spoken cues.
save_at=frame(cue(5,'save'));balance_at=frame(cue(5,'remaining'))
shots[13]['b']=shots[14]['a']=frame(cue(5,'enter'))
shots[14]['b']=shots[15]['a']=save_at-1.2
shots[15]['b']=shots[16]['a']=save_at-.5
shots[16]['b']=shots[17]['a']=save_at+.3
shots[17]['b']=shots[18]['a']=balance_at
shots[18]['start']=new_marks['balance-after'];shots[18]['b']=47;shots[18]['length']=47-balance_at
shots[19]['a']=47;shots[19]['length']=3
assert shots[14]['b']-shots[14]['a']>.65
assert shots[17]['b']>shots[17]['a']
sync={'attachmentsMention':cue(2,'X-rays'),'attachmentsCut':attachment_at,'saveMention':cue(5,'save'),'remainingBalanceMention':cue(5,'remaining'),'remainingBalanceCut':balance_at}
(R/'sync-timing.json').write_text(json.dumps(sync,indent=2))
assert shots[0]['a']==0 and shots[-1]['b']==60 and all(x['b']==y['a'] for x,y in zip(shots,shots[1:]))
(R/'edit-timeline.json').write_text(json.dumps(shots,indent=2))
def render(i):
 s=shots[i];dur=s['b']-s['a'];still=Path(s['source']).suffix=='.png';cmd=[FF,'-v','error','-y','-filter_complex_threads','1']
 if still:cmd+=['-loop','1','-framerate',str(FPS),'-i',s['source']]
 else:cmd+=['-ss',str(s['start']),'-t',str(s['length']),'-i',s['source']]
 label=Image.new('RGBA',(W,H))
 if s['graphic']:label=Image.open(R/(s['graphic']+'.png')).convert('RGBA')
 elif s['label']:center(label,s['label'],23,45)
 labelpath=save(label,f'overlay-{i}');cmd+=['-loop','1','-i',str(labelpath)]
 # Oversampling makes the source-coordinate camera move smooth at small increments.
 srcw=Image.open(s['source']).width if still else 1600
 fac=3200/srcw
 x,y,w=s['c0'];xx,yy,ww=s['c1'];ease=f'(min(on/{max(1,round(min(1.2,dur*.5)*FPS))},1)^2*(3-2*min(on/{max(1,round(min(1.2,dur*.5)*FPS))},1)))'
 zoom=f'3200/({w*fac}+({(ww-w)*fac})*{ease})';cx=f'{x*fac}+({(xx-x)*fac})*{ease}';cy=f'{y*fac}+({(yy-y)*fac})*{ease}'
 filt=f"fps={FPS},scale=3200:-2,zoompan=z='{zoom}':x='{cx}':y='{cy}':d=1:s={W}x{H}:fps={FPS}"
 if not still:filt+=f',setpts={(dur/s["length"]):.8f}*(PTS-STARTPTS),tpad=stop_mode=clone:stop_duration=1'
 if s['label']:filt+=',scale=1742:980,pad=1920:1080:(ow-iw)/2:100:color=0xf5f8f3'
 # Text arrives with a small rise and fade; the screen capture stays readable.
 fc=f'[0:v]{filt},setsar=1[v];[1:v]format=rgba,fade=t=in:st=0:d=0.16:alpha=1[o];[v][o]overlay=0:y=16*exp(-12*t),format=yuv420p[out]'
 cmd+=['-filter_complex',fc,'-map','[out]','-an','-t',str(dur),'-r',str(FPS),'-c:v','libx264','-crf','17','-preset','fast','-threads','2',str(R/f'cut-{i:02}.mp4')]
 subprocess.run(cmd,check=True);print('Rendered',i,flush=True)
if '--audio-only' not in sys.argv:
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(render,range(len(shots))))
(R/'concat.txt').write_text('\n'.join(f"file 'cut-{i:02}.mp4'" for i in range(len(shots))))
# 120 BPM original upbeat score. Layers enter at the reveal and rise into the CTA.
SR=48000;N=60*SR;rng=np.random.default_rng(47);music=np.zeros((N,2),np.float32);fx=np.zeros_like(music);voice=np.zeros(N,np.float32)
def add(dst,at,sound,pan=0):
 k=round(at*SR)
 if k>=N:return
 sound=sound[:N-k];dst[k:k+len(sound),0]+=sound*math.sqrt((1-pan)/2);dst[k:k+len(sound),1]+=sound*math.sqrt((1+pan)/2)
def tone(at,midi,amp=.04,length=.7,pan=0,bass=False):
 t=np.arange(int(length*SR))/SR;f=440*2**((midi-69)/12)
 sig=np.sin(2*np.pi*f*t)+.24*np.sin(2*np.pi*f*2*t)+.13*np.sin(2*np.pi*f*3*t)
 env=(1-np.exp(-t*250))*np.exp(-t*(4 if bass else 6))*np.minimum(1,(length-t)/.07)
 add(music,at,(sig*env*amp).astype('float32'),pan)
chords=[[48,60,64,67],[53,60,65,69],[48,60,64,67],[55,62,67,71]]
for bar in range(30):
 at=bar*2;ch=chords[bar%4];energy=.45 if at<12 else (1.2 if at>=50 else 1)
 for tick in [0,.75,1.5]:
  for j,n in enumerate(ch[1:]):tone(at+tick+j*.018,n,.033*energy,.65,(j-1)*.3)
 for tick in [0,.5,1,1.75]:tone(at+tick,ch[0]-(12 if tick==0 else 0),.075*energy,.48,bass=True)
 if at>=12:
  for j,n in enumerate([ch[1]+12,ch[2]+12,ch[3]+12,ch[2]+12]):
   if bar%2==0 or at>=50:tone(at+j*.5+.25,n,.019*(1.3 if at>=50 else 1),.5,.2)
 for j in range(4):
  hit=at+j*.5
  if hit>=59.5:continue
  t=np.arange(int(.22*SR))/SR
  kick=np.sin(2*np.pi*(52*t+52*.028*(1-np.exp(-t/.028))))*np.exp(-t*23)*(1-np.exp(-t*400))*.10*energy
  add(music,hit,kick.astype('float32'))
  if j%2 and at>=12:
   noise=rng.normal(0,1,len(t));clap=np.convolve(noise,np.ones(4)/4,'same')*np.exp(-t*27)*(.5+.5*np.cos(t*170)**2)*.055
   add(music,hit,clap.astype('float32'),.05)
  for dt in [.0,.25]:
   t=np.arange(int(.055*SR))/SR;noise=rng.normal(0,1,len(t));hat=np.diff(noise,prepend=0)*np.exp(-t*85)*(1-np.exp(-t*600))*.007*energy
   add(music,hit+dt,hat.astype('float32'),-.3 if dt else .3)
# Brief lifts into product reveal and final offer; a bright ending chord.
for at in [11.55,49.55]:
 t=np.arange(int(.4*SR))/SR;noise=rng.normal(0,1,len(t));whoosh=np.convolve(noise,np.ones(15)/15,'same')*np.sin(np.pi*t/.4)**2*.035;add(fx,at,whoosh.astype('float32'))
for j,n in enumerate([48,60,64,67,72]):tone(59.35+j*.025,n,.07,.65,(j-2)*.15)
# Paper rustle in the problem scene.
for at in [1.3,3.6,5.9]:
 t=np.arange(int(.3*SR))/SR;noise=rng.normal(0,1,len(t));paper=np.convolve(noise,np.ones(7)/7,'same')*np.sin(np.pi*t/.3)**2*.045;add(fx,at,paper.astype('float32'))
# Use actual captured mouse/keyboard events, transformed through each edit's timing.
events=json.loads((CAP/'pointer-events.json').read_text());mapped=[]
for s in shots:
 if s['source']!=str(V):continue
 for e in events:
  if e['type'] not in ['click','key'] or not s['start']<=e['time']<s['start']+s['length']:continue
  at=s['a']+(e['time']-s['start'])*(s['b']-s['a'])/s['length'];mapped.append(dict(type=e['type'],time=at,sourceTime=e['time']))
  t=np.arange(int(.045*SR))/SR
  click=(rng.normal(0,1,len(t))*.35+np.sin(2*np.pi*1100*t)*.4)*np.exp(-t*145)*(.062 if e['type']=='click' else .035)
  add(fx,at,click.astype('float32'))
for at,n in [(balance_at+.1,76),(balance_at+.23,79)]:
 t=np.arange(int(.35*SR))/SR;sig=np.sin(2*np.pi*(440*2**((n-69)/12))*t)*np.exp(-t*10)*(1-np.exp(-t*180))*.045;add(fx,at,sig.astype('float32'))
(R/'sound-events.json').write_text(json.dumps(mapped,indent=2))
report=[];intervals=[]
for i,e in enumerate(json.loads((R/'narration.json').read_text())):
 raw=subprocess.check_output([FF,'-v','error','-i',str(R/f'voice-{i}.mp3'),'-f','f32le','-ac','1','-ar',str(SR),'-']);a=np.frombuffer(raw,dtype='<f4').copy();nz=np.flatnonzero(np.abs(a)>.002);a=a[max(0,nz[0]-480):min(len(a),nz[-1]+1440)]
 duration=len(a)/SR;assert duration<=e['end']-e['start']+.05,(i,duration,e)
 active=a[np.abs(a)>.012];a*=min(3,.14/max(.001,float(np.sqrt(np.mean(active**2)))));a*=min(1,.8/max(.001,float(np.max(np.abs(a)))))
 k=round(e['start']*SR);voice[k:k+len(a)]=a;intervals.append((e['start'],e['start']+duration));report.append({**e,'actualDuration':duration,'playbackSpeed':1})
t=np.arange(N)/SR;duck=np.ones(N)
for a,b in intervals:
 env=np.minimum(np.clip((t-a+.09)/.09,0,1),np.clip((b+.2-t)/.2,0,1));duck=np.minimum(duck,1-.56*env)
music*=.048/np.sqrt(np.mean(music**2));fade=np.minimum(np.clip(t/.15,0,1),np.clip((60-t)/.18,0,1));mixed=voice[:,None]+music*duck[:,None]*fade[:,None]+fx
assert np.max(np.abs(mixed))<1
with wave.open(str(R/'mix.wav'),'wb') as f:f.setparams((2,2,SR,0,'NONE','not compressed'));f.writeframes((mixed*32767).astype('<i2').tobytes())
(R/'audio-check.json').write_text(json.dumps(report,indent=2))
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
srt=[];index=1
for i,e in enumerate(report):
 words=word_times[i]
 for j in range(0,len(words),6):
  group=words[j:j+6];at=group[0]['at'];end=group[-1]['at']+group[-1]['duration']/1e7
  srt.extend([str(index),f'{stamp(at)} --> {stamp(end)}',' '.join(w['text'] for w in group).replace('Den Click','DenClick'),'']);index+=1
(R/'DenClick-Energetic-60s.srt').write_text('\n'.join(srt))
(R/'DenClick-Energetic-60s.vtt').write_text('WEBVTT\n\n'+'\n'.join(line.replace(',', '.') if '-->' in line else line for line in srt))
subprocess.run([FF,'-v','error','-y','-f','concat','-safe','0','-i',str(R/'concat.txt'),'-i',str(R/'mix.wav'),'-map','0:v','-map','1:a','-c:v','copy','-af','loudnorm=I=-15:TP=-1:LRA=7','-c:a','aac','-b:a','256k','-ar','48000','-t','60','-movflags','+faststart',str(R/'DenClick-Energetic-60s.mp4')],check=True)
print('FINAL',R/'DenClick-Energetic-60s.mp4',flush=True)
