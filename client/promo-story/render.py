from pathlib import Path
import json,subprocess,math,wave,concurrent.futures
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import imageio_ffmpeg
R=Path(__file__).resolve().parent;FF=imageio_ffmpeg.get_ffmpeg_exe();W,H=1920,1080;FPS=25
marks={x['name']:x['time'] for x in json.loads((R/'capture-markers.json').read_text())['marks']}
V=R/'raw/story-Paolo-returning-patient-story/video.webm'
NAVY='#163c43';TEAL='#087d80';BG='#f4f8f7'
def font(s,b=False):return ImageFont.truetype('/usr/share/fonts/truetype/lato/Lato-'+('Bold' if b else 'Regular')+'.ttf',s)
def label(im,t,lock=False):
 d=ImageDraw.Draw(im);f=font(48,True);w=d.textlength(t,font=f);pad=78 if lock else 34;x=(W-w-pad-34)/2;y=20
 if lock:
  d.arc((x+29,y+19,x+52,y+46),180,360,fill=NAVY,width=3);d.rounded_rectangle((x+25,y+35,x+56,y+60),radius=5,fill=NAVY)
 d.text((x+pad,y+10),t,font=f,fill=NAVY)
 return im
# Planned time, source, in, source duration, crop, editorial label. Still holds are explicit.
main=(270,35,1290,726);modal=(435,65,730,770)
shots=[]
def shot(a,b,src,at=0,length=None,crop=None,text='',motion=False):shots.append(dict(a=a,b=b,src=str(src),at=at,length=length or b-a,crop=crop,text=text,motion=motion))
shot(0,2.8,R/'assets/clinic-opening.png',text='hook',motion=True)
shot(2.8,5.4,R/'assets/clinic-opening.png',crop=(700,230,920,518),motion=True)
shot(5.4,7,R/'assets/patient-card.png',motion=True)
shot(7,10.2,V,marks['search-start']+.05,marks['profile']-marks['search-start']-.5,main,'A few clicks away.')
shot(10.2,14.4,R/'profile.png',crop=main)
shot(14.4,18,V,marks['history']-.65,3.6,main,'Patient history')
shot(18,21,V,marks['attachments']-.6,3,main)
shot(21,25,R/'security.png',crop=main,text='Protected with encryption')
shot(25,27,V,marks['chart']-.6,2,main,'Digital dental chart')
shot(27,29,V,marks['tooth']-.7,1.4,(300,15,1250,855))
shot(29,34,R/'tooth.png',crop=modal)
shot(34,36,V,marks['appointments']-.5,2,main,'Next appointment')
shot(36,37.4,R/'calendar.png',crop=(285,80,940,750))
shot(37.4,40,R/'appointment-detail.png',crop=(380,55,840,780))
shot(40,42,R/'balance-before.png',crop=main,text='Payments & installments')
shot(42,44,V,marks['payment-form']+.15,2,(405,20,790,860))
shot(44,44.6,V,marks['payment-confirm']-.7,.6,(400,20,800,860))
shot(44.6,45.2,V,marks['payment-confirm']+.15,.6,(400,20,800,860))
shot(45.2,48,R/'balance-after.png',crop=main,text='Remaining balance: ₱500')
shot(48,52,V,marks['dashboard']+.2,4,main,'Your clinic. Organized.')
shot(52,55,R/'dashboard.png',crop=main,text='Built for small dental clinics')
# Calm closing frame, the actual logo over a subdued actual dashboard.
logo=Image.open(R.parent/'public/logo.png').convert('RGBA');logo=logo.crop(logo.getbbox());logo.thumbnail((820,280),Image.Resampling.LANCZOS)
for name,cta in [('offer',False),('cta',True)]:
 im=Image.open(R/'dashboard.png').convert('RGB').resize((W,H),Image.Resampling.LANCZOS).filter(ImageFilter.GaussianBlur(12)).convert('RGBA');im=Image.alpha_composite(im,Image.new('RGBA',(W,H),(245,249,247,230)));im.alpha_composite(logo,((W-logo.width)//2,280));d=ImageDraw.Draw(im)
 def center(t,y,size,fill=NAVY):
  f=font(size,True);d.text(((W-d.textlength(t,font=f))/2,y),t,font=f,fill=fill)
 if cta:center('Message us for a free demo.',650,58,TEAL)
 else:center('One-time payment option',610,55);center('No required monthly subscription',702,43,TEAL)
 im.save(R/f'{name}.png')
shot(55,58,R/'offer.png');shot(58,60,R/'cta.png')
assert shots[0]['a']==0 and shots[-1]['b']==60
assert all(x['b']==y['a'] for x,y in zip(shots,shots[1:]))
(R/'edit-timeline.json').write_text(json.dumps(shots,indent=2))

def render(i):
 s=shots[i];dur=s['b']-s['a'];still=Path(s['src']).suffix.lower()=='.png';cmd=[FF,'-v','error','-y','-filter_complex_threads','1']
 if still:cmd+=['-loop','1','-framerate','25','-i',s['src']]
 else:cmd+=['-ss',str(s['at']),'-t',str(s['length']),'-i',s['src']]
 overlay=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(overlay)
 if s['text']=='hook':
  # Gentle translucent wash only behind the opening words.
  for y in range(420):d.line((0,y,850,y),fill=(8,25,25,int(55*(1-y/420))))
  d.text((95,100),'Still searching through\npatient cards?',font=font(68,True),fill='white',spacing=13)
 elif s['text']:label(overlay,s['text'],s['text']=='Protected with encryption')
 overlay.save(R/f'text-{i}.png');cmd+=['-loop','1','-i',str(R/f'text-{i}.png')]
 c=s['crop'];crop=f'crop={c[2]}:{c[3]}:{c[0]}:{c[1]},' if c else ''
 filters=crop+f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0xf4f8f7,setsar=1'
 if s['motion']:filters+=f",zoompan=z=1.015+0.00012*on:x=iw/2-iw/zoom/2:y=ih/2-ih/zoom/2:d=1:s={W}x{H}:fps=25"
 if not still:filters+=f",setpts={(dur/s['length']):.8f}*(PTS-STARTPTS),tpad=stop_mode=clone:stop_duration=1"
 if s['text'] and s['text']!='hook':filters+=',scale=1706:960,pad=1920:1080:(ow-iw)/2:120:color=0xf4f8f7'
 fc=f'[0:v]{filters}[v];[v][1:v]overlay=0:0,format=yuv420p[out]'
 cmd+=['-filter_complex',fc,'-map','[out]','-an','-t',str(dur),'-r','25','-c:v','libx264','-crf','19','-preset','fast','-threads','2',str(R/f'cut-{i:02}.mp4')]
 subprocess.run(cmd,check=True);print('Rendered',i,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:list(p.map(render,range(len(shots))))
(R/'concat.txt').write_text('\n'.join(f"file 'cut-{i:02}.mp4'" for i in range(len(shots))))
# Original bright 104 BPM score: major triads, soft plucks and gentle percussion.
SR=48000;N=60*SR;music=np.zeros((N,2),np.float32);fx=np.zeros_like(music);voice=np.zeros(N,np.float32);rng=np.random.default_rng(29)
def add(arr,at,sound,pan=0):
 k=round(at*SR);sound=sound[:max(0,min(len(sound),N-k))]
 if not len(sound):return
 arr[k:k+len(sound),0]+=sound*math.sqrt((1-pan)/2);arr[k:k+len(sound),1]+=sound*math.sqrt((1+pan)/2)
def piano(at,midi,amp=.06,length=1,pan=0):
 t=np.arange(round(length*SR))/SR;f=440*2**((midi-69)/12);env=(1-np.exp(-t*220))*np.exp(-t*5)*np.minimum(1,(length-t)/.1)
 sound=(np.sin(2*np.pi*f*t)+.32*np.sin(2*np.pi*f*2*t)+.12*np.sin(2*np.pi*f*3*t))*env*amp
 add(music,at,sound.astype('float32'),pan)
beat=60/104;chords=[[48,60,64,67],[53,60,65,69],[48,60,64,67],[55,62,67,71]]
for bar in range(26):
 start=bar*4*beat;ch=chords[bar%4]
 for j in range(8):
  at=start+j*beat/2
  if at>=58:continue
  piano(at,ch[1+j%3]+(12 if j in [3,7] else 0),.028 if at<7 else .045,.85,(j%3-1)*.25)
 if start<7 or start>=58:continue
 for j in [0,2]:piano(start+j*beat,ch[0],.07,.65)
 for j in range(4):
  at=start+j*beat
  if at>=58:continue
  t=np.arange(int(.16*SR))/SR
  if j%2==0:
   kick=np.sin(2*np.pi*(65*t+35*.025*(1-np.exp(-t/.025))))*np.exp(-t*28)*(1-np.exp(-t*250))*.055
   add(music,at,kick.astype('float32'))
  else:
   noise=rng.normal(0,1,len(t));tap=np.convolve(noise,np.ones(5)/5,'same')*np.exp(-t*48)*.027
   add(music,at,tap.astype('float32'),.12)
  t=np.arange(int(.06*SR))/SR;noise=rng.normal(0,1,len(t));shaker=np.diff(noise,prepend=0)*np.sin(np.pi*t/.06)**2*.005
  add(music,at+beat/2,shaker.astype('float32'),-.25)
for j,n in enumerate([48,60,64,67,72]):piano(58+j*.045,n,.05,2)
for at in [2.85,4.25,5.45]:
 t=np.arange(int(.42*SR))/SR;noise=rng.normal(0,1,len(t));soft=np.convolve(noise,np.ones(7)/7,'same');env=np.sin(np.pi*t/.42)**2*(.6+.4*np.sin(2*np.pi*17*t)**2);add(fx,at,(soft*env*.026).astype('float32'),-.1)
for at in [7.3,7.46,7.63,7.8,8.01,8.2,8.38,9.65,27.35,35.2,42.35,42.55,42.75,44.15,44.76]:
 t=np.arange(int(.025*SR))/SR;s=(rng.normal(0,1,len(t))*.4+np.sin(2*np.pi*900*t)*.3)*np.exp(-t*240)*.022;add(fx,at,s.astype('float32'))
for at,n in [(45.3,72),(45.44,76)]:
 t=np.arange(int(.32*SR))/SR;f=440*2**((n-69)/12);add(fx,at,(np.sin(2*np.pi*f*t)*np.exp(-t*12)*(1-np.exp(-t*100))*.026).astype('float32'))
items=json.loads((R/'narration.json').read_text());report=[];intervals=[]
for i,e in enumerate(items):
 raw=subprocess.check_output([FF,'-v','error','-i',str(R/f'voice-{i}.mp3'),'-af','silenceremove=start_periods=1:start_threshold=-48dB:start_silence=0.02,areverse,silenceremove=start_periods=1:start_threshold=-48dB:start_silence=0.05,areverse','-f','f32le','-ac','1','-ar',str(SR),'-'])
 a=np.frombuffer(raw,dtype='<f4').copy();duration=len(a)/SR
 assert duration<=e['end']-e['start']+.08,(i,duration,e['end']-e['start'])
 active=a[np.abs(a)>.01];a*=min(3,.12/max(.001,float(np.sqrt(np.mean(active**2)))));a*=min(1,.8/max(.001,float(np.max(np.abs(a)))))
 k=round(e['start']*SR);voice[k:k+len(a)]=a;intervals.append((e['start'],e['start']+duration));report.append({**e,'actualDuration':duration,'speed':1})
t=np.arange(N)/SR;duck=np.ones(N)
for a,b in intervals:
 env=np.minimum(np.clip((t-a+.15)/.15,0,1),np.clip((b+.3-t)/.3,0,1));duck=np.minimum(duck,1-.65*env)
music*=.024/max(.001,float(np.sqrt(np.mean(music**2))));fade=np.minimum(np.clip(t/1.5,0,1),np.clip((60-t)/.6,0,1));mixed=voice[:,None]+music*duck[:,None]*fade[:,None]+fx
assert np.max(np.abs(mixed))<1
with wave.open(str(R/'mix.wav'),'wb') as f:f.setparams((2,2,SR,0,'NONE','not compressed'));f.writeframes((mixed*32767).astype('<i2').tobytes())
(R/'audio-check.json').write_text(json.dumps(report,indent=2))
# Short phrase subtitles, supplied separately so they do not crowd the clean master.
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
srt=[];idx=1
for e in report:
 words=e['text'].replace('Den Click','DenClick').split();groups=[words[j:j+7] for j in range(0,len(words),7)];at=e['start']
 for g in groups:
  end=at+e['actualDuration']*len(g)/len(words);srt+= [str(idx),f'{stamp(at)} --> {stamp(end)}',' '.join(g),''];idx+=1;at=end
(R/'DenClick-Story.srt').write_text('\n'.join(srt))
subprocess.run([FF,'-v','error','-y','-f','concat','-safe','0','-i',str(R/'concat.txt'),'-i',str(R/'mix.wav'),'-map','0:v','-map','1:a','-c:v','copy','-af','loudnorm=I=-16:TP=-1:LRA=9','-c:a','aac','-b:a','192k','-ar','48000','-t','60','-movflags','+faststart','-metadata','title=DenClick — A Few Clicks Away','-metadata','comment=Fictional patient data. Generated opening stills with camera motion; actual DenClick screen recording. Synthesized English narration and original music and sound design.',str(R/'DenClick-Story-60s.mp4')],check=True)
print('FINAL',R/'DenClick-Story-60s.mp4',flush=True)
