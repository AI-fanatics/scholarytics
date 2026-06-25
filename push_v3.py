import requests,base64,os
t=open(r'C:\Users\82578\.git-credentials').read().strip().split(':')[-1].split('@')[0]
H={'Authorization':f'token {t}','Accept':'application/vnd.github.v3+json'}
API='https://api.github.com/repos/TheeTarnished/paper-super-reviewer/contents'
BASE=r'C:\Users\82578\Desktop\paper-super-reviewer'
for f in ['SKILL.md','README.md']:
    fp=os.path.join(BASE,f)
    c=base64.b64encode(open(fp,'rb').read()).decode()
    r=requests.get(f'{API}/{f}',headers=H,timeout=15)
    sha=r.json().get('sha') if r.status_code==200 else None
    body={'message':f'v3.0: 6-agent architecture','content':c}
    if sha: body['sha']=sha
    rr=requests.put(f'{API}/{f}',headers=H,json=body,timeout=30)
    print('✅' if 'content' in rr.json() else '❌',f)
print('https://github.com/TheeTarnished/paper-super-reviewer')
