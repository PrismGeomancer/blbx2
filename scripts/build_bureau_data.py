from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent
now=1791808800000
cases=[
('echo-launch','The Echo Launch','Why did 23 wallet aliases enter the same launch within an eight-second window?','sentinel',['cartographer','adversary'], 'active','A common funding route links 17 aliases. Shared control remains an open question.'),
('exit-window','The Exit Window','Was liquidity removed before the wider wallet cluster began selling?','cryptanalyst',['forge','prover'],'active','Two withdrawal paths precede the sell wave; the order matters more than the headline.'),
('mirror-route','The Mirror Route','Are repeated swaps a bot loop, a routing artifact, or coordinated volume?','forge',['qubit','cryptanalyst'],'queued','Repeated instruction paths are consistent with one retry loop. Intent is unresolved.'),
('silent-vault','The Silent Vault','Where does the trail go after funds cross an intermediate account?','cartographer',['architect','prover'],'queued','The second hop splits into three branches. One branch is still unattributed.'),
('ghost-signal','The Ghost Signal','Does the apparent insider signal survive a challenge against ordinary arbitrage?','adversary',['sentinel','qubit'],'queued','Timing supports two explanations. No ownership claim has cleared review.'),
('last-mile','The Last Mile','Which evidence would distinguish a deliberate exit from a failed automation?','architect',['prover','conductor'],'queued','Instruction order and authority changes are the decisive evidence, not price alone.')]
roles=[
('sentinel','Signal investigator','Detects unusual timing, repeated activity, and new questions worth opening.',['Signal index','Launch timelines','Case intake'],'searching','echo-launch','The first purchase is not the first signal. Start with the funding window.'),
('cryptanalyst','Pattern analyst','Tests whether a pattern survives alternative explanations and baseline comparisons.',['Timing analysis','Route comparison','Pattern tests'],'thinking','exit-window','Liquidity removal leads the sell wave. Establish the order before assigning intent.'),
('cartographer','Wallet cartographer','Builds the funding graph and separates linked aliases from proven common control.',['Wallet graph','Funding paths','Cluster ledger'],'reading','echo-launch','Seventeen wallet aliases share a route. Six still need an independent connection.'),
('forge','Program investigator','Reconstructs instruction paths, retries, and authority changes across each case.',['Program traces','Instruction decoder','Route ledger'],'reading','mirror-route','The repeated swap uses the same instruction path. Check the retry condition.'),
('architect','Response architect','Turns findings into the next evidence request and a clear case resolution path.',['Case playbooks','Review queue','Evidence requests'],'thinking','last-mile','We need authority history before this case can move beyond circumstantial timing.'),
('prover','Evidence auditor','Checks each conclusion against its underlying record and preserves the unknowns.',['Evidence ledger','Chain of custody','Consistency checks'],'reading','exit-window','The sequence is supported; the motive is not. Keep those statements separate.'),
('qubit','Quantum analyst','Explores quantum-inspired search, uncertain paths, and competing explanations.',['Reconstruction matrix','Hypothesis search','Exposure research'],'thinking','mirror-route','Compare the loop hypothesis with an independent routing explanation.'),
('adversary','Contradiction hunter','Finds the strongest innocent explanation and challenges every ownership claim.',['Counterexamples','Alternative paths','Attribution review'],'searching','ghost-signal','A shared source can be a service. Funding overlap alone cannot establish identity.'),
('conductor','Bureau coordinator','Routes questions, schedules specialists, and maintains one coherent investigation.',['Case scheduler','Review gate','Resource governor'],'thinking','echo-launch','Keep ECHO and EXIT in progress. Route the unresolved control claim to ADVERSARY.')]
agents=[]
for i,(aid,role,mission,tools,status,mid,thought) in enumerate(roles):
 agents.append(dict(id=aid,codename=aid.upper(),role=role,mission=mission,tools=tools,status=status,since=now-(i+1)*43000,missionId=mid,task=next(c[2] for c in cases if c[0]==mid),lastThought=thought,lastAction='reviewing the case ledger',stats=dict(tasks=8+i,records=128+i*12,searches=12+i*3,reads=18+i*4,findings=2,tokensIn=120000+i*21000,tokensOut=4800+i*800,costUsd=0)))
missions=[]
for i,(mid,title,question,lead,support,status,summary) in enumerate(cases):
 missions.append(dict(id=mid,title=title,question=question,lead=lead,support=support,priority=1 if i<2 else 2 if i<4 else 3,status=status,cycles=7+i,findings=2,lastRunAt=now-(i+1)*110000,lastSummary=summary))
notes=[
('echo-launch','cartographer','A shared route connects 17 wallet aliases','The ECHO case ledger connects 17 of 23 aliases through one intermediate funding route. The remaining six enter the launch window without that same visible path. The graph supports a funding relationship; it does not identify the person behind it.','corrected','Shared infrastructure remains a plausible explanation. Keep the cluster provisional.'),
('exit-window','cryptanalyst','The withdrawal comes before the sell wave','The EXIT timeline places two liquidity withdrawals ahead of the wider selling window. Reverse ordering would support a reactive exit; this ordering leaves pre-positioning as a question worth testing.','confirmed','Sequence accepted within the case record. Intent requires independent evidence.'),
('ghost-signal','adversary','The insider explanation is not the only explanation','The earliest entries fit both a coordinated launch and an automated arbitrage response. A narrow time window makes the activity unusual, but it does not make one explanation decisive.','unverifiable','The ownership inference has not cleared review. Preserve both hypotheses.'),
('mirror-route','forge','The swap pattern repeats an instruction path','The MIRROR ledger contains repeated route fingerprints with a matching retry boundary. That is consistent with a loop in the execution path. It does not establish deliberate volume inflation.','corrected','Replace the manipulation claim with the narrower instruction-pattern observation.'),
('silent-vault','cartographer','Three branches leave the intermediate account','The VAULT graph splits into three paths after the intermediate account. Two paths return to known case aliases. The third has no supported owner link and remains outside the attributed cluster.','confirmed','The unknown branch stays visible. Do not collapse it into the known cluster.'),
('last-mile','architect','Authority history is the next decisive record','The LAST MILE case needs the sequence of authority changes and automation triggers. Price movement alone cannot distinguish an intentional exit from a failed execution policy.','confirmed','Evidence request approved. Keep motive open until the authority sequence is available.'),
('echo-launch','sentinel','The funding window is wider than the launch window','The eight-second entry window is the headline. The earlier funding interval is the stronger investigative lead because it gives the bureau a separate sequence to compare.','confirmed','Keep launch timing and funding timing as independent observations.'),
('exit-window','prover','Observation and intent require different verdicts','The two withdrawal records support a statement about order. They do not support a statement about intent. The case file now separates those claims so later evidence can update each independently.','corrected','Attribution language narrowed. The sequence remains in the evidence ledger.'),
('mirror-route','qubit','Three hypotheses survive the first search','The reconstruction matrix keeps bot retry, route aggregation, and intentional repetition in play. The retry explanation fits the instruction order best, while the other two need additional assumptions.','confirmed','A best fit is a working explanation, not a final attribution.'),
('ghost-signal','prover','Confidence falls when service overlap is included','Treating a common service as common ownership artificially strengthens the cluster. The revised hypothesis includes service overlap as an independent possibility.','corrected','The bureau will not turn infrastructure overlap into a claim about identity.'),
('silent-vault','architect','An unresolved path becomes an evidence request','The third funding branch is now a dedicated request rather than an assumed connection. The bureau can progress on the two supported branches without overstating the unknown one.','confirmed','Scope accepted. The unresolved branch stays on the case board.'),
('last-mile','conductor','A case can stay open without losing its shape','The record preserves the observed sequence, the explanations still in play, and the exact evidence needed next. An unresolved verdict is useful when its boundaries are clear.','confirmed','Case protocol accepted: evidence, explanation, challenge, next question.')]
findings=[]
for i,(mid,agent,title,summary,verdict,note) in enumerate(notes):
 findings.append(dict(id=f'bb-note-{i+1:03}',ts=now-(i+1)*85000,missionId=mid,agent=agent,title=title,summary=summary,confidence='medium' if verdict!='unverifiable' else 'low',verdict=verdict,verifierNote=note,sources=[dict(title='BB / '+mid.upper()+' · case ledger',url='case:'+mid),dict(title='Bureau attribution protocol',url='protocol:attribution')]))
activity=[
('conductor','handoff','ECHO stays open. CARTOGRAPHER maps funding; ADVERSARY challenges the cluster.','echo-launch','cartographer'),
('sentinel','search','Compare the eight-second entry window with the earlier funding interval.','echo-launch','Case archive'),
('cartographer','fetch','Opening ECHO / funding ledger: 23 wallet aliases, three entry paths.','echo-launch','Wallet graph'),
('cartographer','thinking','Seventeen aliases share a funding route. That is a link, not an identity.','echo-launch',None),
('adversary','thinking','Try the service-overlap explanation before accepting coordinated ownership.','ghost-signal',None),
('cryptanalyst','search','Align the withdrawal sequence against the first sustained sell window.','exit-window','Route ledger'),
('prover','verdict','Corrected: timing is supported; intent remains unresolved.','exit-window','cryptanalyst'),
('forge','fetch','Opening MIRROR / instruction fingerprints and retry boundaries.','mirror-route','Program traces'),
('forge','thinking','One route fingerprint repeats. The retry loop is the narrowest explanation.','mirror-route',None),
('qubit','thinking','Search three competing paths: bot retry, aggregation, intentional repetition.','mirror-route',None),
('qubit','fetch','Reconstruction matrix retains three explanations; retry has the strongest evidence fit.','mirror-route',None),
('architect','thinking','Request authority history before resolving the LAST MILE case.','last-mile',None),
('prover','fetch','Checking the chain of custody for EXIT / withdrawal sequence.','exit-window','Evidence ledger'),
('adversary','verdict','Unverifiable: a common funding service does not prove shared control.','ghost-signal','cartographer'),
('cartographer','search','Trace the third VAULT branch without merging it into the known cluster.','silent-vault','Wallet graph'),
('sentinel','thinking','The funding interval gives us an independent test of the launch explanation.','echo-launch',None),
('conductor','handoff','Route the unresolved VAULT branch to ARCHITECT as an evidence request.','silent-vault','architect'),
('architect','fetch','Evidence request recorded. The unknown branch stays outside the attributed cluster.','silent-vault',None),
('prover','verdict','Confirmed: the case record separates sequence, inference, and unknowns.','last-mile','architect'),
('conductor','thinking','Preserve the trail. Keep the strongest alternative explanation in view.','echo-launch',None)]
sequence=[]
for aid,kind,text,mid,target in activity:
 item=dict(agent=aid,kind=kind,text=text,missionId=mid)
 if target:item['target']=target
 if kind=='verdict':item.update(verdict='corrected' if text.startswith('Corrected') else 'unverifiable' if text.startswith('Unverifiable') else 'confirmed',detail=text)
 sequence.append(item)
events=[]
for i in range(40):
 item=dict(sequence[i%len(sequence)]); item.update(id=1000+i,ts=now-(40-i)*12000,replay=True);events.append(item)
# Preserve the original lattice layout and renderer, now an evidence search matrix.
lattice=json.loads((root/'.original/lattice.json').read_text())
lattice['backend']='echo_matrix'
engines=[dict(name=name,qubits=156 if i==0 else 96 if i==1 else 64,processor=method,operational=True,pendingJobs=3+i,twoQubitError=.06+i*.025,readoutError=.02,t1Us=0,t2Us=0) for i,(name,method) in enumerate([('echo_matrix','Path search'),('route_matrix','Route fit'),('vault_matrix','Cluster fit')])]
jobs=[]
for i,(title,mid,layout,prob) in enumerate([('ECHO / competing funding paths','echo-launch',[39,52,54,53,65,66,67,78],.84),('MIRROR / retry-path reconstruction','mirror-route',[41,42,43,56,63,64],.79),('VAULT / unresolved branch search','silent-vault',[20,21,22,36,41],.62)]):
 jobs.append(dict(id=f'bb-reconstruction-{i+1:03}',backend='echo_matrix',agent='qubit',missionId=mid,title=title,qubits=len(layout),layout=layout,depth=128+i*64,twoQubitGates=24,shots=2048,status='done',quantumSec=12+i*4,submittedAt=now-(i+1)*240000,finishedAt=now-(i+1)*240000+12000,top=[dict(bits='PATH A',p=prob),dict(bits='PATH B',p=(1-prob)*.65),dict(bits='PATH C',p=(1-prob)*.35)],expected='PATH A',headline='Evidence fit',idealP=.95,measuredP=prob,note='Hypotheses are compared against the case ledger. Evidence fit ranks explanations; it does not establish wallet ownership.',metrics=[dict(label='Funding sequence',measured=prob,ideal=.95),dict(label='Instruction consistency',measured=prob-.09,ideal=.95),dict(label='Independent support',measured=prob-.23,ideal=.9)]))
snapshot=dict(version=1,mode='archive',model='BLACKBOX / INVESTIGATION ENGINE',now=now,startedAt=now-86400000*3,cycle=42,agents=agents,missions=missions,findings=findings,events=events,activitySequence=sequence,fuel=dict(chain='solana',launchpad=None,mint=None,creatorWallet=None,solPriceUsd=None,unclaimedSol=0,claimedSolTotal=0,creditedUsdTotal=0,spentUsdTotal=0,fuelUsd=84,burnUsdPerHour=0,runwayHours=None,lastClaimAt=None,lastClaimTx=None,health='running',rates=dict(model='BLACKBOX',inputPerMTok=0,outputPerMTok=0,cacheReadPerMTok=0)),totals=dict(cases=6,cycles=42,searches=128,reads=164,drafts=18,published=12,refuted=4,tokensIn=0,tokensOut=0,costUsd=0),token=dict(ca=None,symbol='BLACKBOX',name='BLACKBOX'),quantum=dict(provider='BLACKBOX / Q-LAB',updatedAt=now,budget=dict(plan='bureau',allowanceSec=600,windowDays=7,usedSec=141,remainingSec=459,reserveSec=120,dailyCapSec=85,usedTodaySec=38,heldTodaySec=0),backends=engines,lattice=lattice,jobs=jobs,jobsTotal=3,secTotal=48))
from bureau_cases import enrich
enrich(snapshot)
(root/'data/bureau.json').write_text(json.dumps(snapshot,indent=2)+'\n')
