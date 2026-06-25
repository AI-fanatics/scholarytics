import requests,base64,os,glob

t=open(r'C:\Users\82578\.git-credentials').read().strip().split(':')[-1].split('@')[0]
H={'Authorization':f'token {t}','Accept':'application/vnd.github.v3+json'}
API='https://api.github.com/repos/TheeTarnished/paper-super-reviewer/contents'
BASE=r'C:\Users\82578\Desktop\paper-super-reviewer'

files=[]
for root,dirs,fnames in os.walk(BASE):
    for f in fnames:
        if '.git' in root: continue
        fp=os.path.join(root,f)
        rel=os.path.relpath(fp,BASE).replace('\\','/')
        files.append((rel,fp))

for rel,fp in sorted(files):
    c=base64.b64encode(open(fp,'rb').read()).decode()
    r=requests.get(f'{API}/{rel}',headers=H,timeout=15)
    sha=r.json().get('sha') if r.status_code==200 else None
    body={'message':f'v3.0: 12-skill family','content':c}
    if sha: body['sha']=sha
    rr=requests.put(f'{API}/{rel}',headers=H,json=body,timeout=30)
    ok='content' in rr.json()
    print(f"  {'✅' if ok else '❌'} {rel}")

print(f"\nhttps://github.com/TheeTarnished/paper-super-reviewer")
