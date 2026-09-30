# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: story.spec.js >> Paolo returning patient story
- Location: story-capture/story.spec.js:13:1

# Error details

```
TimeoutError: locator.boundingBox: Timeout 15000ms exceeded.
Call log:
  - waiting for locator('main').getByRole('button', { name: 'Medical Info', exact: true })

```

# Page snapshot

```yaml
- generic [ref=e3]:
  - navigation [ref=e4]:
    - generic [ref=e5]:
      - button "Toggle menu" [ref=e6]
      - generic [ref=e8]:
        - img "DenClick" [ref=e9]
        - paragraph [ref=e10]: Clinical Management
    - button "Search patients..." [ref=e12]
    - generic [ref=e17]:
      - link "Dashboard" [ref=e18] [cursor=pointer]:
        - /url: /
      - link "Appointments" [ref=e25] [cursor=pointer]:
        - /url: /appointments
      - link "Patients" [ref=e29] [cursor=pointer]:
        - /url: /patients
      - link "Treatments" [ref=e36] [cursor=pointer]:
        - /url: /treatments
      - link "Finance" [ref=e42] [cursor=pointer]:
        - /url: /finance
      - link "Expenses" [ref=e46] [cursor=pointer]:
        - /url: /expenses
      - link "Inventory" [ref=e51] [cursor=pointer]:
        - /url: /inventory
      - link "Dentists" [ref=e57] [cursor=pointer]:
        - /url: /dentists
      - link "Users" [ref=e71] [cursor=pointer]:
        - /url: /users
      - link "Activity Log" [ref=e76] [cursor=pointer]:
        - /url: /activity-log
      - link "Settings" [ref=e81] [cursor=pointer]:
        - /url: /settings
    - generic [ref=e86]:
      - link "C Clinic Admin" [ref=e87] [cursor=pointer]:
        - /url: /account
        - generic [ref=e88]: C
        - paragraph [ref=e90]: Clinic Admin
      - button "Log out" [ref=e91]
  - main [ref=e95]:
    - generic [ref=e96]:
      - button "Back" [ref=e97]
      - generic [ref=e100]:
        - generic [ref=e101]:
          - generic [ref=e102]: P
          - generic [ref=e103]:
            - heading "Paolo Cruz" [level=1] [ref=e104]
            - paragraph [ref=e105]: 0917 000 0000
        - generic [ref=e106]:
          - button "Print Summary" [ref=e107]
          - button "Export Record" [ref=e112]
          - button "Add Appointment" [ref=e116]
          - button "Edit" [ref=e118]
      - generic [ref=e122]:
        - button "Overview" [ref=e123]
        - button "Medical Info" [ref=e127]
        - button "Appointments" [ref=e131]
        - button "Treatments" [ref=e134]
        - button "Odontogram" [ref=e139]
        - button "Attachments" [ref=e143]
      - generic [ref=e146]:
        - generic [ref=e147]:
          - heading "Overview" [level=3] [ref=e148]
          - button "Edit" [ref=e149]
        - generic [ref=e153]:
          - generic [ref=e154]:
            - generic [ref=e155]: Contact number
            - paragraph [ref=e156]: 0917 000 0000
          - generic [ref=e157]:
            - generic [ref=e158]: Date of birth
            - paragraph [ref=e159]: —
        - generic [ref=e160]:
          - generic [ref=e161]: Address
          - paragraph [ref=e162]: Sample address, Quezon City
        - generic [ref=e163]:
          - generic [ref=e164]:
            - generic [ref=e165]: HMO provider
            - paragraph [ref=e166]: —
          - generic [ref=e167]:
            - generic [ref=e168]: HMO member ID
            - paragraph [ref=e169]: —
```

# Test source

```ts
  1   | import { test, expect } from '@playwright/test';
  2   | import { createRequire } from 'node:module';
  3   | import fs from 'node:fs';
  4   | import path from 'node:path';
  5   | import { serverEnv } from '../playwright.config.js';
  6   | const require=createRequire(import.meta.url);
  7   | Object.assign(process.env,serverEnv);
  8   | const {PrismaClient}=require('../../server/node_modules/@prisma/client');
  9   | const {encryptedPatientData,encryptText}=require('../../server/src/lib/patientCrypto');
  10  | const db=new PrismaClient();
  11  | const out=path.resolve(process.env.STORY_OUTPUT || 'promo-story');
  12  | fs.mkdirSync(out,{recursive:true});
  13  | test('Paolo returning patient story',async({page})=>{
  14  |  const zero=Date.now(); const marks=[];
  15  |  const mark=async(name)=>{marks.push({name,time:(Date.now()-zero)/1000});console.log(name,marks.at(-1).time);fs.writeFileSync(path.join(out,'capture-markers.json'),JSON.stringify({marks},null,2));await page.screenshot({path:path.join(out,`${name}.png`)});};
  16  |  const hold=ms=>page.waitForTimeout(ms);
> 17  |  const click=async(loc)=>{const b=await loc.boundingBox();if(b){await page.mouse.move(b.x+b.width/2,b.y+b.height/2,{steps:24});await hold(120);}await loc.click();await hold(450);};
      |                                             ^ TimeoutError: locator.boundingBox: Timeout 15000ms exceeded.
  18  |  const admin=await db.user.findUnique({where:{email:'admin@clinic.test'}});const dentist=await db.user.findUnique({where:{email:'maria@clinic.test'}});const branch=await db.branch.findFirst({where:{isDefault:true}});
  19  |  const patient=await db.patient.create({data:{...encryptedPatientData({name:'Paolo Cruz',contact:'0917 000 0000',address:'Sample address, Quezon City',allergies:'Penicillin\nLatex',medicalHistory:'Previous dental treatment reviewed\nMedical questionnaire updated at follow-up'}),branchId:branch.id,createdById:admin.id,updatedById:admin.id}});
  20  |  const catalog=await db.treatmentCatalogItem.findFirst({where:{name:'Braces Installation (Metal)'}});const past=new Date(Date.now()-14*86400000);
  21  |  const treatment=await db.treatmentCase.create({data:{patientId:patient.id,catalogItemId:catalog.id,totalPrice:45000,dentistId:dentist.id,branchId:branch.id,createdAt:new Date(Date.now()-104*86400000),createdById:admin.id,updatedById:admin.id}});
  22  |  const visitNotes=[
  23  |   'Braces fitted. Baseline photos reviewed; care instructions recorded.',
  24  |   'First adjustment: archwire changed. Patient reported mild soreness after the previous visit.',
  25  |   'Second adjustment: ligatures replaced. Alignment progress reviewed; comfort checked.',
  26  |   'Latest adjustment: archwire reviewed and ligatures replaced. Check alignment and comfort at the next visit.'
  27  |  ];
  28  |  for(let i=0;i<visitNotes.length;i++){
  29  |   const date=new Date(Date.now()-(104-i*30)*86400000);
  30  |   const visit=await db.appointment.create({data:{patientId:patient.id,dentistId:dentist.id,branchId:branch.id,startsAt:date,durationMinutes:30,status:'COMPLETED',createdById:admin.id}});
  31  |   await db.invoice.create({data:{treatmentCaseId:treatment.id,amount:i?1500:15000,method:'Cash',appointmentId:visit.id,dentistId:dentist.id,branchId:branch.id,note:visitNotes[i],createdAt:date,createdById:admin.id}});
  32  |  }
  33  |  // A returning patient's sample history: ten cases across multiple visits.
  34  |  const historyNames=['Oral Prophylaxis (Cleaning)','Dental X-Ray (Panoramic)','Fluoride Treatment','Dental Sealant','Braces Consultation','Dental X-Ray (Periapical)','Dental Filling (Composite)','Teeth Whitening','Oral Prophylaxis (Cleaning)'];
  35  |  for (let i=0;i<historyNames.length;i++){
  36  |   const item=await db.treatmentCatalogItem.findFirstOrThrow({where:{name:historyNames[i]}});
  37  |   const date=new Date(Date.now()-(45+i*40)*86400000);
  38  |   const c=await db.treatmentCase.create({data:{patientId:patient.id,catalogItemId:item.id,totalPrice:item.defaultPrice,status:'CLOSED',dentistId:dentist.id,branchId:branch.id,createdAt:date,createdById:admin.id,updatedById:admin.id}});
  39  |   await db.invoice.create({data:{treatmentCaseId:c.id,amount:item.defaultPrice,method:i%2?'GCash':'Cash',dentistId:dentist.id,branchId:branch.id,note:'Completed visit — fictional demo history.',createdAt:date,createdById:admin.id}});
  40  |  }
  41  |  expect(await db.treatmentCase.count({where:{patientId:patient.id}})).toBe(10);
  42  |  await db.patientTooth.create({data:{patientId:patient.id,toothNumber:16,status:'FILLING',isMiddleShade:true,notes:encryptText('Composite filling completed. Review at follow-up.'),createdById:admin.id,updatedById:admin.id}});
  43  |  await db.toothHistory.create({data:{patientId:patient.id,toothNumber:16,status:'FILLING',isMiddleShade:true,notes:encryptText('Composite filling completed. Review at follow-up.'),changedById:admin.id,changedAt:past}});
  44  |  const next=new Date();next.setDate(next.getDate()+1);next.setHours(10,0,0,0);
  45  |  await db.appointment.create({data:{patientId:patient.id,dentistId:dentist.id,branchId:branch.id,startsAt:next,durationMinutes:30,createdById:admin.id}});
  46  |  for (let i=0;i<1;i++){
  47  |   const when=new Date(Date.now()-(14+i*40)*86400000);when.setHours(10+i%3,0,0,0);
  48  |   await db.appointment.create({data:{patientId:patient.id,dentistId:dentist.id,branchId:branch.id,startsAt:when,durationMinutes:30,status:'COMPLETED',createdById:admin.id}});
  49  |  }
  50  |  expect(await db.appointment.count({where:{patientId:patient.id}})).toBe(6);
  51  |  for (const [i,name] of ['Sofia Reyes','Miguel Santos','Bea Mendoza'].entries()){
  52  |   const hmoPatient=await db.patient.create({data:{...encryptedPatientData({name,hmoProvider:['Maxicare','Medicard','Intellicare'][i],hmoMemberId:'DEMO-HMO-'+(i+1)}),branchId:branch.id,createdById:admin.id}});
  53  |   const amount=[1500,2500,4000][i];const c=await db.treatmentCase.create({data:{patientId:hmoPatient.id,catalogItemId:(await db.treatmentCatalogItem.findFirstOrThrow({where:{name:"Dental Filling (Composite)"}})).id,totalPrice:amount,status:"CLOSED",dentistId:dentist.id,branchId:branch.id,createdById:admin.id}});
  54  |   await db.invoice.create({data:{treatmentCaseId:c.id,amount,method:'HMO/Insurance',claimStatus:i?'SUBMITTED':'PENDING',dentistId:dentist.id,branchId:branch.id,createdById:admin.id}});
  55  |  }
  56  |  await page.goto('/login');await page.getByLabel('email').fill('admin@clinic.test');await page.getByLabel('password',{exact:true}).fill('changeme123');await page.getByRole('button',{name:/login/i}).click();await expect(page).not.toHaveURL(/login/);
  57  |  const attachmentAssets=[['panoramic-xray.jpg','Panoramic X-ray — sample'],['sample-referral-form.png','Referral form — sample'],['dental-model.jpg','Treatment reference — sample']];
  58  |  for (const [name,title] of attachmentAssets){
  59  |   const result=await page.request.post('/api/attachments',{multipart:{ownerType:'PATIENT',ownerId:patient.id,title,notes:'Illustrative sample for a fictional demo patient. Not a clinical record of this person.',file:{name,mimeType:name.endsWith('.png')?'image/png':'image/jpeg',buffer:fs.readFileSync(path.resolve('promo-energy/assets',name))}}});expect(result.status()).toBe(201);
  60  |  }
  61  |  await page.addStyleTag({content:'html{scroll-behavior:auto!important}*{caret-color:#087d80}'});
  62  |  // Restrained pointer and click ring, recorded into the actual UI.
  63  |  await page.evaluate((zero)=>{
  64  |   window.storyEvents=[];
  65  |   const s=document.createElement('style');
  66  |   s.textContent='.story-cursor{position:fixed;width:29px;height:36px;z-index:2147483646;pointer-events:none;filter:drop-shadow(0 2px 3px #163c4355)}.story-click{position:fixed;width:34px;height:34px;border:3px solid #09a9a680;border-radius:50%;z-index:2147483645;pointer-events:none;transform:translate(-50%,-50%);animation:storyclick .4s ease-out forwards}@keyframes storyclick{to{opacity:0;transform:translate(-50%,-50%) scale(1.8)}}';document.head.append(s);
  67  |   const c=document.createElement('div');c.className='story-cursor';c.style.left='-100px';c.innerHTML='<svg viewBox="0 0 29 36"><path d="M2 2 L2 28 L9 22 L15 34 L21 31 L15 20 L25 20 Z" fill="#163c43" stroke="white" stroke-width="2.4" stroke-linejoin="round"/></svg>';document.body.append(c);
  68  |   addEventListener('mousemove',e=>{c.style.left=e.clientX+'px';c.style.top=e.clientY+'px';window.storyEvents.push({type:'move',time:(Date.now()-zero)/1000,x:e.clientX,y:e.clientY})});
  69  |   addEventListener('mousedown',e=>{window.storyEvents.push({type:'click',time:(Date.now()-zero)/1000,x:e.clientX,y:e.clientY});const r=document.createElement('div');r.className='story-click';r.style.left=e.clientX+'px';r.style.top=e.clientY+'px';document.body.append(r);setTimeout(()=>r.remove(),450)});
  70  |   addEventListener('keydown',e=>{window.storyEvents.push({type:'key',time:(Date.now()-zero)/1000,key:e.key.length===1?'character':e.key})});
  71  |  },zero);
  72  |  const main=page.locator('main');const nav=n=>page.locator('nav').getByRole('link',{name:n,exact:true});
  73  |  await click(nav('Patients'));await mark('search-start');await click(main.getByPlaceholder('Search patients...'));await main.getByPlaceholder('Search patients...').pressSequentially('Paolo Cruz',{delay:125});await hold(500);await mark('search-result');await click(main.getByText('Paolo Cruz',{exact:true}).first());await hold(700);await mark('profile');await hold(900);
  74  |  await click(main.getByRole('button',{name:'Medical Info',exact:true}));await expect(main.getByText('Penicillin',{exact:true})).toBeVisible();await expect(main.getByText('Latex',{exact:true})).toBeVisible();await mark('medical-info');await hold(4500);
  75  |  if(process.env.MEDICAL_INSERT){
  76  |   await click(main.getByRole('button',{name:'Treatments',exact:true}));await mark('medical-to-treatments');await hold(3500);
  77  |   fs.writeFileSync(path.join(out,'pointer-events.json'),JSON.stringify(await page.evaluate(()=>window.storyEvents),null,2));
  78  |   fs.writeFileSync(path.join(out,'capture-markers.json'),JSON.stringify({marks,patientId:patient.id},null,2));await db.$disconnect();return;
  79  |  }
  80  | 
  81  |  await click(main.getByRole('button',{name:'Treatments',exact:true}));await expect(main.locator('a[href^="/treatment-cases/"]')).toHaveCount(10);await mark('history');await hold(3500);
  82  |  if(process.env.TREATMENT_INSERT){
  83  |   await mark('treatment-sequence-start');
  84  |   await click(main.getByText('Braces Installation (Metal)',{exact:false}).first());await mark('treatment-open');await page.mouse.move(1280,465,{steps:20});await hold(3400);
  85  |   await page.mouse.move(1260,670,{steps:20});
  86  |   for(let i=0;i<8;i++){await page.mouse.wheel(0,35);await hold(65);}
  87  |   await mark('treatment-earlier');await hold(3900);
  88  |   for(let i=0;i<8;i++){await page.mouse.wheel(0,-35);await hold(45);}
  89  |   await click(main.getByRole('button',{name:'Back',exact:true}));await hold(250);
  90  |   await click(main.getByRole('button',{name:'Attachments',exact:true}));await mark('treatment-attachments');await hold(4000);
  91  |   fs.writeFileSync(path.join(out,'pointer-events.json'),JSON.stringify(await page.evaluate(()=>window.storyEvents),null,2));await db.$disconnect();return;
  92  |  }
  93  |  await click(main.getByText('Braces Installation (Metal)',{exact:false}).first());await mark('braces-open');await hold(3000);
  94  |  await main.getByText(visitNotes[3],{exact:true}).scrollIntoViewIfNeeded();await mark('braces-history');await hold(5000);
  95  |  await main.getByText(visitNotes[0],{exact:true}).scrollIntoViewIfNeeded();await mark('braces-earlier');await hold(5000);
  96  |  await page.goBack();await hold(600);
  97  | 
  98  |  await click(main.getByRole('button',{name:'Attachments',exact:true}));await expect(main.locator('img[src^="/api/attachments/"]')).toHaveCount(3);await expect.poll(()=>main.locator('img[src^="/api/attachments/"]').evaluateAll(imgs=>imgs.every(img=>img.complete&&img.naturalWidth>0))).toBe(true);await mark('attachments');await hold(2500);
  99  |  await click(main.getByRole('button',{name:'Overview',exact:true}));await mark('security');await hold(4000);
  100 |  await click(main.getByRole('button',{name:'Odontogram',exact:true}));await mark('chart');await hold(1700);await click(main.getByRole('cell',{name:'16',exact:true}).first());await mark('tooth');await hold(4500);await click(page.getByRole('button',{name:'Close',exact:true}).first());
  101 |  await click(main.getByRole('button',{name:'Appointments',exact:true}));await mark('appointments');await hold(2200);
  102 |  await click(nav('Appointments'));await hold(1000);await mark('calendar');await hold(2200);
  103 |  const ev=main.locator('.fc-event',{hasText:'Paolo Cruz'}).first();await expect(ev).toBeVisible();await click(ev);await mark('appointment-detail');await hold(2800);await click(page.getByRole('button',{name:'Close',exact:true}).first());
  104 |  await click(nav('Patients'));await main.getByPlaceholder('Search patients...').fill('Paolo Cruz');await click(main.getByText('Paolo Cruz',{exact:true}).first());await click(main.getByRole('button',{name:'Treatments',exact:true}));await click(main.getByText('Braces Installation (Metal)',{exact:false}).first());await hold(900);await mark('balance-before');await hold(1800);await click(main.getByRole('button',{name:/new billing/i}));await mark('payment-form');await click(page.getByPlaceholder(/Balance due/));await page.getByPlaceholder(/Balance due/).pressSequentially('1500',{delay:190});
  105 |  const method=page.locator('form#billing-form').getByRole('button',{name:'Cash',exact:true});await click(method);await click(page.getByRole('button',{name:'GCash',exact:true}).last());await page.getByPlaceholder('What was done today...').fill('Adjustment completed. Progress and comfort reviewed; recheck alignment next visit.');await mark('payment-filled');await hold(1600);
  106 |  await click(page.getByRole('button',{name:'Save Billing',exact:true}));await mark('payment-confirm');await click(page.locator('.swal2-confirm'));await expect(page.locator('.swal2-icon-success')).toBeVisible();await hold(300);await click(page.locator('.swal2-confirm'));await hold(700);await mark('balance-after');await expect(main.getByText('₱24,000',{exact:true}).first()).toBeVisible();await hold(3200);
  107 |  await click(nav('Dashboard'));await click(main.getByRole('button',{name:'Month',exact:true}).first());await page.mouse.move(40,870);await mark('dashboard');await hold(8000);
  108 |  await click(nav('Finance'));await click(main.getByRole('button',{name:'Outstanding Balance',exact:true}));await expect(main.getByText(/all time, not affected/)).toBeVisible();await mark('receivables');await hold(9500);
  109 |  await click(main.getByRole('button',{name:'HMO Claims',exact:true}));await expect(main.getByText(/3 claims to follow up worth/)).toBeVisible();await mark('hmo-claims');await hold(9500);
  110 |  await click(nav('Expenses'));await mark('expenses');await hold(6000);
  111 |  await click(nav('Inventory'));await mark('inventory');await hold(6000);
  112 |  // Generate genuine CREATE, UPDATE and VIEW audit events through the normal API.
  113 |  const expense=await page.request.post('/api/expenses',{data:{date:new Date().toISOString(),category:'Dental supplies',amount:850,note:'Demo clinic supplies'}});expect(expense.status()).toBe(201);
  114 |  const updated=await page.request.put('/api/patients/'+patient.id,{data:{address:'Sample address, Quezon City'}});expect(updated.ok()).toBe(true);
  115 |  await page.request.get('/api/patients/'+patient.id);
  116 |  await click(nav('Activity Log'));await expect(main.locator('tbody tr').first()).toBeVisible();await mark('activity-log');await hold(12000);
  117 |  fs.writeFileSync(path.join(out,'pointer-events.json'),JSON.stringify(await page.evaluate(()=>window.storyEvents),null,2));
```