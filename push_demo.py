import requests, base64, os

token_line = open(r"C:\Users\82578\.git-credentials").read().strip()
token = token_line.split(":")[-1].split("@")[0]

OWNER, REPO = "TheeTarnished", "paper-super-reviewer"
API = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"
H = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

def get_sha(path):
    r = requests.get(f"{API}/{path}", headers=H, timeout=15)
    return r.json().get("sha") if r.status_code == 200 else None

def push(path):
    fpath = r"C:\Users\82578\Desktop\paper-super-reviewer" + "\\" + path.replace("/","\\")
    if not os.path.exists(fpath):
        print(f"  SKIP {path}")
        return
    content = base64.b64encode(open(fpath,'rb').read()).decode()
    sha = get_sha(path)
    body = {"message": f"Update {path}", "content": content}
    if sha: body["sha"] = sha
    r = requests.put(f"{API}/{path}", headers=H, json=body, timeout=30)
    ok = 'content' in r.json()
    print(f"  {'✅' if ok else '❌'} {path}")

# Push everything
push("README.md")
push("SKILL.md")
push("demo/RESNET_REVIEW.md")
push("templates/review_report_template.md")

print(f"\nhttps://github.com/{OWNER}/{REPO}")
