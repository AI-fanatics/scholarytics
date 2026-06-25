import requests

token_line = open(r"C:\Users\82578\.git-credentials").read().strip()
token = token_line.split(":")[-1].split("@")[0]

OWNER, REPO = "TheeTarnished", "paper-super-reviewer"
API = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"
H = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

# Delete helper scripts — not part of the skill
for f in ["push_files.py","push3.py","push2.py","create_repo.py","push_final.py","cleanup.py","push_clean.py"]:
    r = requests.get(f"{API}/{f}", headers=H, timeout=15)
    if r.status_code == 200:
        sha = r.json()["sha"]
        dr = requests.delete(f"{API}/{f}", headers=H, 
            json={"message":f"Remove build script","sha":sha}, timeout=15)
        print(f"  {'✅' if dr.status_code==200 else '❌'} {f}")
    else:
        print(f"  ⚪ {f} (not on GitHub)")
