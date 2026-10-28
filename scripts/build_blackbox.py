from pathlib import Path
import json,re
root=Path(__file__).resolve().parent.parent
source=(root/'.original/index-WL105mLy.js').read_text()
# Keep React, Framer Motion, canvas renderers and the original interaction system.
start=source.index('var Ef=')
lib,app=source[:start],source[start:]
replacements={
'HASHWALL':'BLACKBOX','Hashwall':'Blackbox','HASHWALL home':'BLACKBOX home',
'Quantum threat research':'Solana incident bureau','re: @drakefjustin, 2026-10-07':'EST. 2026 · EVERY TRACE MATTERS',
'Bunker':'Black','Mode':'Box',
'The quantum breakthrough that breaks ':'Nine agents. ',
'Bitcoin’s signatures':'Every transaction',
' is getting closer.':' leaves evidence.',
' Claude agents race Q-Day ':' investigators follow the money ',
'. They track every new paper and qubit estimate, run their own experiments on IBM quantum computers, and hunt for the solutions, and the breakthrough, that keep Bitcoin’s keys safe. Creator fees from the HASHWALL coin on pump.fun fund the compute.':'. Wallet clusters. Echo launches. Vanishing liquidity. The bureau reconstructs unusual activity on Solana, challenges every explanation, and follows each case until the evidence holds.',
'Watch the agents live ':'Enter mission control ',
'Inside the quantum lab':'Explore the quantum lab',
'Until launch, this console runs a demo of the agents\' workflow.':'The bureau follows the evidence. Every case has a chain of custody.',
'Preview: until launch, the console runs a demo of the agents’ workflow.':'BLACKBOX · SOLANA INCIDENT BUREAU',
'On air':'Bureau online','Live':'Control','Missions':'Cases','Research missions':'Case missions','Lab notebook':'Evidence archive',
'Skip to the live swarm':'Skip to mission control',
'Live swarm map: CONDUCTOR at the core, the agents on the ring, and the sources they read on the outer ring.':'Bureau swarm map: CONDUCTOR at the core, nine investigators and their evidence sources.',
'Live graph: CONDUCTOR at the core, eight agents on the ring, and the source sites they read on the outer ring.':'Investigation graph: CONDUCTOR at the core, eight specialist agents and their evidence sources.',
'Live swarm map':'Bureau swarm map',
'Every agent works in the open. Watch them think, search, read and argue, live.':'Nine specialists. Nine perspectives. Follow their working notes, evidence trails, and competing explanations.',
'Every entry survived ADVERSARY, who tries to refute each draft before it goes out.':'Case notes, evidence trails, and competing explanations. ADVERSARY challenges the conclusions before they enter the archive.',
'Quantum experimenter':'Quantum analyst',
'Runs small experiments on real IBM quantum computers to measure how far today’s hardware is from breaking ECDSA.':'Explores quantum-inspired search and competing explanations in the reconstruction lab.',
'IBM Quantum · Open plan':'Reconstruction matrix',
'Qiskit · Aer simulator':'Hypothesis search',
'Estimated at Claude API list prices':'Bureau resource allocation',
'Choosing the most overdue mission.':'Routing the next investigation.',
'Every mission is in flight.':'Every case has an investigator.',
'Q-Day, ':'Evidence, ',
'How close is the quantum breakthrough that breaks Bitcoin’s signatures? QUBIT tests it on real IBM quantum computers, one experiment at a time.':'Reconstruct the incident before you reach a verdict. QUBIT explores competing paths through the evidence; PROVER checks the assumptions. The quantum lab is the bureau’s engine for difficult questions.',
'Quantum link · ':'Quantum matrix · ',
'IBM Quantum':'BLACKBOX / Q-LAB',
'QPU time':'Search budget',
'QPU time used on the whole IBM account, as IBM reports it':'Reconstruction budget allocated to the current case',
'IBM account':'Case allocation',
'Backends':'Reconstruction engines','Chip':'Method','Qubits':'Nodes','Queue':'Pending',
'Median two-qubit gate error, latest calibration':'Unresolved evidence fraction','2Q err':'Unknown',
' QPU job log':' Reconstruction log',' measured ':' evidence fit ',' ideal':' target',
' QPU-s so far':' search-s allocated','No QPU jobs yet.':'No reconstructions yet.',
'— QPU-s':'— search-s','QPU not used':'Search pending','QPU':'Q-LAB',
'Quantum link':'Quantum matrix','Online':'Ready','Chip map':'Evidence matrix','No chip data yet.':'No matrix data yet.',
' Live swarm map':' Bureau swarm map',' q × ':' nodes × ','Compute (est.)':'Resources','On mission':'On case',
'No findings yet. The first cycle is still running.':'The evidence archive is opening.',
'Agent activity is broadcast with a delay and may include replays of recent sessions.':'Case activity is sequenced from the bureau archive.',
'Nothing here attacks real keys.':'Evidence before attribution.',
}
# Text-only substitutions do not rename CSS classes or data keys.
for old,new in replacements.items():
 app=app.replace('`'+old+'`','`'+new+'`')
app=app.replace('`${ap(e)} Claude agents tracking the quantum threat to Bitcoin’s signatures, in the open. Every pulse below is a real step one of them took.`','`${ap(e)} investigators. One shared evidence graph. Follow the paths, inspect the case files, and watch the bureau challenge its own conclusions.`')
app=app.replace('`IBM account · ${e.windowDays} days`','`Case window · ${e.windowDays} days`')
app=app.replace('`${m?.qubits??l.coords.length} qubits`','`${m?.qubits??l.coords.length} evidence nodes`')
app=app.replace('`${e.backend} chip, ${l.length} qubits','`${e.backend} matrix, ${l.length} evidence nodes')
app=app.replace('`qubit ${e}`','`evidence node ${e}`')
app=app.replace('`${e.qubits} qubits × ${e.shots.toLocaleString','`${e.qubits} nodes × ${e.shots.toLocaleString')
app=app.replace('`${Wg(e.quantumSec)} QPU-s`','`${Wg(e.quantumSec)} search-s`')
app=app.replace('`IBM job ${e.id}`','`Reconstruction ${e.id}`')
app=app.replace('`HW-${String(np.indexOf(e)+1)','`BB-${String(np.indexOf(e)+1)')
# Remove every network dependency from the retained application's data layer.
a=app.index('function Xf()'); b=app.index('function Zf()',a)
app=app[:a]+'''function Xf(){
 if(globalThis.__blackboxLoad)return;
 globalThis.__blackboxLoad=true;
 fetch('./data/bureau.json').then(r=>{if(!r.ok)throw Error('Case archive unavailable');return r.json()}).then(data=>{
  globalThis.__blackboxData=data;
  const now=Date.now();const delta=now-data.now;
  for(const agent of data.agents)agent.since+=delta;
  data.startedAt+=delta;data.now=now;data.quantum.updatedAt=now;
  for(const event of data.events)event.ts+=delta;
  for(const finding of data.findings)finding.ts+=delta;
  for(const mission of data.missions)mission.lastRunAt+=delta;
  for(const job of data.quantum.jobs){job.submittedAt+=delta;if(job.finishedAt)job.finishedAt+=delta;}
  Jf({type:'snapshot',data});Vf=Date.now();
  let index=0,id=data.events[data.events.length-1].id;
  const advance=()=>{
   if(document.hidden){setTimeout(advance,2000);return;}
   const item=data.activitySequence[index++];
   if(!item){for(const agent of jf.snap.agents)Jf({type:'agent',data:{...agent,status:'idle',task:'Case archive reviewed',lastAction:'Review complete',since:Date.now()}});return;}
   const event={...item,id:++id,ts:Date.now(),replay:true};
   Jf({type:'event',data:event});Vf=Date.now();
   const mission=jf.snap.missions.find(m=>m.id===item.missionId);
   if(mission&&item.missionUpdate)Jf({type:'mission',data:{...mission,...item.missionUpdate,lastRunAt:Date.now()}});
   const current=jf.snap.agents.find(a=>a.id===item.agent);
   if(current)Jf({type:'agent',data:{...current,missionId:item.missionId,task:mission?.question??current.task,status:item.kind==='search'?'searching':item.kind==='thinking'?'thinking':item.kind==='verdict'?'verifying':item.kind==='draft'?'writing':'reading',since:Date.now(),lastThought:item.text,lastAction:item.text}});
   setTimeout(advance,data.activitySequence[index]?.delayMs??13000);
  };
  setTimeout(advance,data.activitySequence[0]?.delayMs??13000);
  setInterval(()=>{Vf=Date.now();Jf({type:'ping',data:{now:Date.now()}})},15000);

 }).catch(error=>{globalThis.__blackboxLoad=false;Yf('offline');console.error(error)});
}''' +app[b:]
a=app.index('async function tp('); b=app.index('var np=',a)
app=app[:a]+'''async function tp(e,t=200){return (jf.snap?.events??globalThis.__blackboxData?.events??[]).filter(x=>x.agent===e).slice(-t)}''' +app[b:]
app=app.replace('Af=`https://hashwall-swarm-production.up.railway.app`.replace(/\\/$/,``)??``','Af=``')
# Retain the entire black/white/yellow spectrum in procedural canvas drawing too.
colors={'#ffb224':'#22c55e','#ffcf73':'#6ee7a0','#c8f169':'#22c55e','#ff7aa8':'#ffffff','#78c6ff':'#dedede','#6cf0c8':'#6ee7a0','#f0d49a':'#efefef','#b7a2ff':'#c8c8c8','#e47aff':'#a7f3c4','#ff6a3d':'#16a34a','#ff4a36':'#22c55e','#eee6d6':'#f5f5f5','#c9bfad':'#c7c7c7','#8f8676':'#969696','#7a7264':'#7a7a7a','#0b0a08':'#040a07','#15130f':'#0e1a13'}
for old,new in colors.items(): app=app.replace(old,new)
for old,new in {'255,178,36':'34,197,94','238,230,214':'245,245,245','11,10,8':'4,10,7','13,12,9':'9,18,13','#5d564b':'#666666'}.items(): app=app.replace(old,new)
app=app.replace('[`Resources`,e?.costUsd,`var(--amber)`,!0]', '[`Case files`,e?.cases,`var(--amber)`]')
app=app.replace('children:`Tokens`','children:`Records`').replace('rh(i.stats.tokensIn+i.stats.tokensOut)','rh(i.stats.records)')
app=app.replace('children:`Compute`','children:`Review`').replace('children:[`≈`,nh(i.stats.costUsd)]','children:[`Open`]')
app=app.replace('`Live transcript`','`Case transcript`').replace(' live transcript`',' case transcript`')
# Source labels used by the retained swarm renderers.
for old,new in {'arxiv.org':'Case archive','eprint.iacr.org':'Evidence ledger','mempool.space':'Wallet graph','github.com':'Program traces','notes.ethereum.org':'Route notes','bitcoin-risq-list.projecteleven.com':'Cluster map','IBM':'Q-LAB'}.items():
 app=app.replace('`'+old+'`','`'+new+'`')
# Keep the original hero, motion wrappers, control room, lab, agents, missions and findings.
app=app.replace('(0,z.jsx)(xp,{})','(0,z.jsx)(BBIdentity,{})').replace('(0,z.jsx)(F_,{})','(0,z.jsx)(BBFuel,{})').replace('(0,z.jsx)(L_,{})','(0,z.jsx)(BBFooter,{})')
app=app.replace('(0,z.jsx)(Xg,{chip:g})','(0,z.jsx)(BBPrinciples,{chip:g})')
app=app.replace('(0,z.jsx)(zp,{})','(0,z.jsx)(BBLogo,{})')
app=app.replace('(0,z.jsx)(cg,{})','(0,z.jsx)(BBCases,{})')
app=app.replace('(0,z.jsx)(BBPrinciples,{chip:g})','(0,z.jsxs)(z.Fragment,{children:[(0,z.jsx)(BBPrinciples,{chip:g}),(0,z.jsx)(BBReconstructionCases,{})]})')
app=app.replace('className:`msn-card__h`,id:`msn-${e.id}-h`,children:e.title','className:`msn-card__h`,id:`msn-${e.id}-h`,children:(0,z.jsx)(BBCaseLink,{mission:e})')
app=app.replace('className:`msn-q__t`,children:e.title','className:`msn-q__t`,children:(0,z.jsx)(BBCaseLink,{mission:e})')
app=app.replace('(0,z.jsx)(`p`,{className:`msn-card__q`,children:e.question})','(0,z.jsx)(BBCaseMeta,{mission:e}),(0,z.jsx)(`p`,{className:`msn-card__q`,children:e.question})')
app=app.replace('if(!lg(e))return','if(e.startsWith(`case:`))return(0,z.jsx)(BBCaseLink,{missionId:e.slice(5),label:t??`Open case dossier ↗`});if(!lg(e))return')
app=app.replace('children:hg.test(e.url)?','children:(hg.test(e.url)||e.url.startsWith(`case:`))?')
app=app.replace('className:`qlab-job__t`,children:e.title','className:`qlab-job__t`,children:(0,z.jsxs)(z.Fragment,{children:[e.title,(0,z.jsx)(BBCaseLink,{missionId:e.missionId,label:`Open case ↗`})]})')
app=app.replace('if(i-n.updatedAt>18e5)','if(jf.snap?.mode!==`archive`&&i-n.updatedAt>18e5)')
app=app.replace('`Pending`','`Case queue`').replace('cooldown:`Cooldown`','cooldown:`Reviewed`')
app=app.replace('`The swarm, `','`The bureau, `')
# A persistent Twitter entry is shared by desktop and mobile navigation.
app=app.replace('children:Lp.map(e=>','children:[...Lp,{href:BBTwitter,label:`Twitter ↗`}].map(e=>')
app=app.replace('href:e.href,children:e.label','href:e.href,children:e.label')
extra=(root/'scripts/blackbox-components.js').read_text()
render=app.rfind('(0,Df.createRoot)')
app=app[:render]+extra+'\n'+app[render:]
(root/'blackbox-app.js').write_text(lib+app)
css=(root/'.original/index-sFjYehkM.css').read_text()
for old,new in colors.items():css=css.replace(old,new)
for old,new in {'#ff8a7a':'#6ee7a0','#120d02':'#021208','#080705':'#06100a','#100e0b':'#08110c','#1c1914':'#14231b','#17140f':'#0b150f','#eee6d6':'#f5f5f5','#a8a08f':'#9e9e9e'}.items():css=css.replace(old,new)
(root/'blackbox-base.css').write_text(css)
