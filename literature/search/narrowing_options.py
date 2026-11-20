"""Narrowing options (2026-11-20): counts unique records per option from the existing v1.1 exports.
Run from literature/screening:  python ../search/narrowing_options.py   (needs sr_work/ and sr_work/citation_counts.json)
Exploratory analysis for Frank's choice; it does not change sr_work."""
import json, re, collections
ident=json.load(open('sr_work/identification.json'))
raw=json.load(open('sr_work/raw_records.json'))
uniq=json.load(open('sr_work/records.json'))['unique']
fileof=[]
for f in ident['files']: fileof += [f['file'].split('_')[0]] * f['records']
assert len(fileof)==len(raw)
for u in uniq: u['rounds']={fileof[i] for i in u['members']}
FIX_STRICT={'R1b','R2a','R2b','R4b'}
def txt(u): return (u['title']+' '+(u['abstract'] or '')).lower()
FIN=re.compile(r'financ|invest|stock|portfolio|banking|\bbank|trading|\bmarket|economic|credit|robo-advis|wealth|fintech')
KNOW=re.compile(r'factual|knowledge|\bfacts?\b|memoriz|memoris')
UNC=re.compile(r'uncertaint|confiden|calibrat|entropy|hedg|abstain|abstention|i don.?t know')
SURV=re.compile(r'\b(survey|review|overview|tutorial|position paper|taxonomy)\b')
def report(fixset):
    fixed=[u for u in uniq if u['rounds']&fixset]
    rest=[u for u in uniq if not (u['rounds']&fixset)]
    print(f"fixed ({'+'.join(sorted(fixset))}): {len(fixed)} unique; remaining R1a/R3-only: {len(rest)}",
          collections.Counter(frozenset(u['rounds']) for u in rest).most_common(6))
    r1=[u for u in rest if 'R1a' in u['rounds']]; r3=[u for u in rest if 'R3' in u['rounds']]
    opts={
     'O1 2026 only': lambda u: u['year']=='2026',
     'O2 bridge: R1a needs knowledge/finance term, R3 needs uncertainty/finance term':
        lambda u: (('R1a' in u['rounds'] and (KNOW.search(txt(u)) or FIN.search(txt(u)))) or
                   ('R3' in u['rounds'] and (UNC.search(txt(u)) or FIN.search(txt(u))))),
     'O2 + 2026 only': lambda u: u['year']=='2026' and ((('R1a' in u['rounds'] and (KNOW.search(txt(u)) or FIN.search(txt(u)))) or ('R3' in u['rounds'] and (UNC.search(txt(u)) or FIN.search(txt(u)))))),
     'survey-titled only': lambda u: bool(SURV.search(u['title'].lower())),
    }
    for k,f in opts.items():
        keep=[u for u in rest if f(u)]
        print(f"  {k}: +{len(keep)} (R1a {sum('R1a' in u['rounds'] for u in keep)}, R3 {sum('R3' in u['rounds'] for u in keep)}) -> total {len(fixed)+len(keep)}")
    return fixed, rest
report(FIX_STRICT)
report(FIX_STRICT|{'R4a'})

print("\n=== citation-based options ===")
C=json.load(open('sr_work/citation_counts.json'))['cited_by_count']
def c(u): return C.get(u['id'], 0)
fixed, rest = [u for u in uniq if u['rounds']&FIX_STRICT], [u for u in uniq if not u['rounds']&FIX_STRICT]
r4a_only=[u for u in rest if u['rounds']=={'R4a'} or u['rounds']=={'R1a','R4a'}]
r13=[u for u in rest if u['rounds']&{'R1a','R3'}]
for t25,t26 in ((10,3),(20,5),(30,8),(50,10)):
    keep=[u for u in r13 if SURV.search(u['title'].lower()) or c(u)>=(t25 if u['year']=='2025' else t26)]
    print(f"  O3 surveys + cited >= {t25} (2025) / >= {t26} (2026): +{len(keep)} (R1a {sum('R1a' in u['rounds'] for u in keep)}, R3 {sum('R3' in u['rounds'] for u in keep)})")
print("R4a-only records:", len(r4a_only))
print("\n=== what drives the fixed part ===")
for rnd in ('R1b','R2a','R2b','R4b'):
    us=[u for u in uniq if rnd in u['rounds']]
    print(rnd, len(us), "2026:", sum(u['year']=='2026' for u in us), "no abstract:", sum(not u['abstract'] for u in us),
          "survey-titled:", sum(bool(SURV.search(u['title'].lower())) for u in us),
          "has unc term:", sum(bool(UNC.search(txt(u))) for u in us), "only this round:", sum(u['rounds']=={rnd} for u in us))
src=collections.Counter()
for u in fixed: src[tuple(u['sources'])]+=1
print("fixed by source:", src)
# R2a: share mentioning uncertainty/confidence/risk/consistency
R2a=[u for u in uniq if 'R2a' in u['rounds']]
CONC=re.compile(UNC.pattern+r'|consisten|reliab|hallucinat|\brisk')
print("R2a with uncertainty/consistency/reliability/hallucination/risk term:", sum(bool(CONC.search(txt(u))) for u in R2a))
R1b=[u for u in uniq if 'R1b' in u['rounds']]
print("R1b sources:", collections.Counter(tuple(u['sources']) for u in R1b))
import random
print("sample R1b OA-only titles:"); [print("  -", u['title'][:110]) for u in random.Random(1).sample([u for u in R1b if u['sources']==['OpenAlex']],8)]
print("sample R2a titles:"); [print("  -", u['title'][:110]) for u in random.Random(2).sample(R2a,8)]

print("\n=== LLM term in title for R1b/R2a/R2b (R4b complete) ===")
LT=re.compile(r'\bllms?\b|language model|chatgpt|\bgpt|chatbot|generative ai|\bgenai\b', re.I)
def keep_fixed(u, rule):
    if 'R4b' in u['rounds']: return True
    return any(r in u['rounds'] for r in ('R1b','R2a','R2b')) and rule(u)
for name, rule in (("LLM term in title", lambda u: bool(LT.search(u['title']))),):
    kf=[u for u in uniq if keep_fixed(u, rule)]
    print(name, "-> fixed part", len(kf), {r: sum(r in u['rounds'] for u in kf) for r in ('R1b','R2a','R2b','R4b')})
    ids={u['id'] for u in kf}
    seed='R01687'
    for oname, f in (("O2 bridge", lambda u: (('R1a' in u['rounds'] and (KNOW.search(txt(u)) or FIN.search(txt(u)))) or ('R3' in u['rounds'] and (UNC.search(txt(u)) or FIN.search(txt(u)))))),
                     ("O2 bridge + 2026", lambda u: u['year']=='2026' and (('R1a' in u['rounds'] and (KNOW.search(txt(u)) or FIN.search(txt(u)))) or ('R3' in u['rounds'] and (UNC.search(txt(u)) or FIN.search(txt(u)))))),
                     ("O3 surveys + cited>=20/5", lambda u: SURV.search(u['title'].lower()) or c(u)>=(20 if u['year']=='2025' else 5)),
                     ("O3 surveys + cited>=50/10", lambda u: SURV.search(u['title'].lower()) or c(u)>=(50 if u['year']=='2025' else 10))):
        add=[u for u in uniq if u['id'] not in ids and u['rounds']&{'R1a','R3'} and not u['rounds']&{'R4a'} and f(u)]
        print(f"   + {oname}: +{len(add)} -> {len(kf)+len(add)} (R4a not included; R4a-only = {len(r4a_only)})")

print("\n=== combinations aiming at 200-400 ===")
O3s=lambda u: SURV.search(u['title'].lower()) or c(u)>=(50 if u['year']=='2025' else 10)
O2=lambda u: (('R1a' in u['rounds'] and (KNOW.search(txt(u)) or FIN.search(txt(u)))) or ('R3' in u['rounds'] and (UNC.search(txt(u)) or FIN.search(txt(u)))))
CONC=re.compile(UNC.pattern+r'|consisten|reliab|hallucinat|\brisk')
combos={
 "X: R1b/R2 LLM-in-title, R2a also needs uncertainty/consistency/risk term; R4b all; R1a/R3 O3-strict":
   lambda u: 'R4b' in u['rounds'] or (('R1b' in u['rounds'] or 'R2b' in u['rounds']) and LT.search(u['title'])) or ('R2a' in u['rounds'] and LT.search(u['title']) and CONC.search(txt(u))) or (u['rounds']&{'R1a','R3'} and O3s(u)),
 "Y: R1b/R2 LLM-in-title and 2026 only; R4b all; R1a/R3 O3-strict":
   lambda u: 'R4b' in u['rounds'] or (u['rounds']&{'R1b','R2a','R2b'} and LT.search(u['title']) and u['year']=='2026') or (u['rounds']&{'R1a','R3'} and O3s(u)),
 "Z: R2 + R4b complete; R1b LLM-in-title; R1a/R3 O3-strict; (R1b is direction 4 only)":
   lambda u: u['rounds']&{'R4b','R2a','R2b'} or ('R1b' in u['rounds'] and LT.search(u['title'])) or (u['rounds']&{'R1a','R3'} and O3s(u)),
}
for k,f in combos.items():
    keep=[u for u in uniq if f(u)]
    r4=[u for u in uniq if u['rounds']=={'R4a'} and (LT.search(u['title']) and O3s(u))]
    print(f"{k}\n   -> {len(keep)} unique (+{len(r4)} if R4a gets O3-strict too); per round:",
          {r: sum(r in u['rounds'] for u in keep) for r in ('R1a','R1b','R2a','R2b','R3','R4a','R4b')}, "seed in:", any(u['id']=='R01687' for u in keep))
