from pathlib import Path
import json,subprocess,wave,math,concurrent.futures
import numpy as np
from PIL import Image,ImageDraw,ImageFont
import imageio_ffmpeg
R=Path(__file__).resolve().parent; FF=imageio_ffmpeg.get_ffmpeg_exe(); S=R.parent/'tutorial-output/DenClick-Tutorial.mp4'; scenes=json.loads((R/'script.json').read_text())
W,H=1920,1080; teal='#087d80'; navy='#123b4a'; bg='#f3faf9'; coral='#ff885f'
def font(n,bold=False):return ImageFont.truetype('/usr/share/fonts/truetype/lato/Lato-'+('Bold' if bold else 'Regular')+'.ttf',n)
logo=Image.open(R.parent/'public/logo.png').convert('RGBA');logo=logo.crop(logo.getbbox())
def putlogo(im,x,y,w):
 l=logo.resize((w,round(w*logo.height/logo.width)),Image.Resampling.LANCZOS);im.alpha_composite(l,(x,y))
def center(d,text,y,size=38,fill=navy):
 f=font(size,True);d.text(((W-d.textlength(text,font=f))/2,y),text,font=f,fill=fill)
def lines(d,text,maxwidth,size):
 out=[];s='';f=font(size)
 for word in text.split():
  if d.textlength((s+' '+word).strip(),font=f)>maxwidth:out.append(s);s=word
  else:s=(s+' '+word).strip()
 if s:out.append(s)
 return out
cats=['ONE CLINIC. ONE PLACE.','MEET DENCLICK','PATIENT RECORDS','DIGITAL DENTAL CHART','APPOINTMENTS','TREATMENTS & PAYMENTS','CLINIC MANAGEMENT','DATA PROTECTION','LET’S GET STARTED']
for i,s in enumerate(scenes):
 im=Image.new('RGBA',(W,H),bg);d=ImageDraw.Draw(im)
 d.ellipse((1500,-320,2170,350),fill='#e3f3ee');d.ellipse((-240,840,300,1380),fill='#e6f4f2')
 putlogo(im,80,45,245);d.text((W-80-d.textlength(cats[i],font=font(21,True)),63),cats[i],font=font(21,True),fill=teal)
 if s['source'] is not None:
  d.text((130,125),s['heading'],font=font(56,True),fill=navy)
  d.rounded_rectangle((123,201,1797,891),radius=20,fill='#cce1df')
  d.rounded_rectangle((130,194,1790,884),radius=16,fill='white')
  for j,c in enumerate([coral,'#f3c85d','#68c1a2']):d.ellipse((150+j*21,205,160+j*21,215),fill=c)
  d.rounded_rectangle((135,222,1784,879),radius=6,fill=(0,0,0,0))
 else:
  if i in [1,8]:
   center(d,'YOUR CLINIC, CONNECTED.' if i==1 else 'LESS ADMIN. MORE TIME FOR PATIENTS.',245,30,teal)
   putlogo(im,410,352,1100)
   center(d,s['heading'],620,49)
   if i==1:
    labels=['Patient records','Appointments','Payments','Clinic insights']
    for j,label in enumerate(labels):
     x=218+j*380;d.rounded_rectangle((x,725,x+345,801),radius=38,fill='white',outline='#c7e2dd',width=2);d.text((x+(345-d.textlength(label,font=font(28,True)))/2,746),label,font=font(28,True),fill=teal)
   else:
    d.rounded_rectangle((590,718,1330,814),radius=48,fill=teal);center(d,'Message us for a free demo',743,38,'white')
  else:
   d.ellipse((800,210,1120,530),fill='#d9eee7')
   d.arc((879,270,1041,430),180,360,fill=teal,width=18);d.rounded_rectangle((851,343,1069,480),radius=24,fill=teal)
   d.ellipse((946,380,974,408),fill='white');d.rectangle((955,397,965,432),fill='white')
   center(d,s['heading'],574,64);center(d,'Encrypted patient details & uploaded files',674,39,teal)
   center(d,'Built-in protection for your clinic’s sensitive information.',756,29,navy)
 caption=s['narration'].replace('Den Click','DenClick').replace('G Cash','GCash').replace('H M O','HMO')
 ls=lines(d,caption,1650,34)
 for n,line in enumerate(ls):
  f=font(34);d.text(((W-d.textlength(line,font=f))/2,922+n*43),line,font=f,fill=navy)
 d.text((80,1040),'DenClick • Dental Clinic Management',font=font(18),fill='#537777')
 txt='Actual app • Sample records';d.text((W-80-d.textlength(txt,font=font(18)),1040),txt,font=font(18),fill='#537777')
 im.save(R/f'overlay-{i}.png')

def render(i):
 s=scenes[i];dur=s['end']-s['start'];p=R/f'scene-{i}.mp4'
 cmd=[FF,'-hide_banner','-loglevel','error','-y']
 if s['source'] is not None:
  # All source captions sit outside this central crop.
  shots={2:[(654,4),(1179,4)],5:[(784,4.5),(800,4.5)],6:[(1479,3.5),(1736,3.5)]}.get(i)
  prefix='';src='0:v';overlay=1
  if shots:
   for at,length in shots:cmd+=['-ss',str(at),'-t',str(length),'-i',str(S)]
   prefix='[0:v]setpts=PTS-STARTPTS[a];[1:v]setpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=1:a=0[src];';src='src';overlay=2
  else:cmd+=['-ss',str(s['source']),'-i',str(S)]
  cmd+=['-loop','1','-i',str(R/f'overlay-{i}.png')]
  crop='crop=1280:490:0:110,scale=1650:630,pad=1920:1080:135:236' if i==6 else 'crop=1280:510:0:90,scale=1650:658,pad=1920:1080:135:222'
  filt=prefix+f'[{src}]{crop}:color=0xf3faf9,setsar=1[v];[v][{overlay}:v]overlay=0:0,fade=t=in:st=0:d=0.18:color=0xf3faf9,fade=t=out:st={dur-.18}:d=0.18:color=0xf3faf9[out]'
 else:
  cmd+=['-loop','1','-i',str(R/f'overlay-{i}.png')]
  filt=f'[0:v]scale=1920:1080,zoompan=z=1.008+0.00006*on:x=iw/2-iw/zoom/2:y=ih/2-ih/zoom/2:d=1:s=1920x1080:fps=25,fade=t=in:st=0:d=0.18:color=0xf3faf9,fade=t=out:st={dur-.18}:d=0.18:color=0xf3faf9[out]'
 cmd+=['-filter_complex',filt,'-map','[out]','-t',str(dur),'-r','25','-an','-c:v','libx264','-preset','fast','-crf','20','-pix_fmt','yuv420p','-threads','2',str(p)]
 subprocess.run(cmd,check=True);print('Rendered scene',i,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(render,range(len(scenes))))
(R/'concat.txt').write_text('\n'.join(f"file 'scene-{i}.mp4'" for i in range(len(scenes))))
# Voice is mixed at a consistent level, with quiet original cheerful music.
SR=24000;N=60*SR;voice=np.zeros(N,dtype=np.float32);intervals=[];report=[]
for i,s in enumerate(scenes):
 cmd=[FF,'-v','error','-i',str(R/f'voice-{i}.mp3'),'-af','silenceremove=start_periods=1:start_threshold=-48dB:start_silence=0.04,areverse,silenceremove=start_periods=1:start_threshold=-48dB:start_silence=0.04,areverse','-f','f32le','-ac','1','-ar',str(SR),'-']
 raw=subprocess.check_output(cmd);a=np.frombuffer(raw,dtype='<f4').copy();available=s['end']-s['start']-.35;speed=max(1,len(a)/SR/available)
 if speed>1.2:raise RuntimeError(f'Voice {i} too rushed: {speed}')
 if speed>1:
  a=np.frombuffer(subprocess.check_output([FF,'-v','error','-f','f32le','-ac','1','-ar',str(SR),'-i','-','-af',f'atempo={speed}','-f','f32le','-'],input=a.tobytes()),dtype='<f4').copy()
 active=a[np.abs(a)>.01];a*=min(3,.15/max(.001,float(np.sqrt(np.mean(active**2)))));a*=min(1,.85/max(.001,float(np.max(np.abs(a)))))
 start=round((s['start']+.15)*SR);voice[start:start+len(a)]=a;intervals.append((start/SR,(start+len(a))/SR));report.append(dict(scene=i,duration=len(a)/SR,speed=speed))
 # Write subtitle timecodes for each complete narration scene.
raw=subprocess.check_output([FF,'-v','error','-i',str(R.parent/'tutorial-output/audio/DenClick-background-original.wav'),'-af','atempo=1.18','-f','f32le','-ac','2','-ar',str(SR),'-'])
bg=np.frombuffer(raw,dtype='<f4').reshape(-1,2);bg=np.tile(bg,(math.ceil(N/len(bg)),1))[:N].copy();bg*=.026/max(.001,float(np.sqrt(np.mean(bg**2))))
t=np.arange(N)/SR;duck=np.ones(N)
for a,b in intervals:
 e=np.minimum(np.clip((t-(a-.12))/.12,0,1),np.clip((b+.25-t)/.25,0,1));duck=np.minimum(duck,1-.7*e)
fade=np.minimum(np.clip(t/.5,0,1),np.clip((60-t)/.7,0,1));mix=(voice[:,None]+bg*duck[:,None])*fade[:,None]
assert np.max(np.abs(mix))<1
with wave.open(str(R/'soundtrack.wav'),'wb') as f:f.setparams((2,2,SR,0,'NONE','not compressed'));f.writeframes((mix*32767).astype('<i2').tobytes())
(R/'timing-check.json').write_text(json.dumps(report,indent=2))
subprocess.run([FF,'-v','error','-y','-f','concat','-safe','0','-i',str(R/'concat.txt'),'-i',str(R/'soundtrack.wav'),'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-t','60','-movflags','+faststart','-metadata','title=DenClick — Your Clinic, Connected','-metadata','comment=Actual app footage with fictional sample records. Synthesized English narration and original instrumental music.',str(R/'DenClick-60s-Demo.mp4')],check=True)
print('Finished:',R/'DenClick-60s-Demo.mp4',flush=True)
