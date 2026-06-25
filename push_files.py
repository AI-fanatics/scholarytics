import requests, json, base64, os, glob

token_line = open(r"C:\Users\82578\.git-credentials").read().strip()
token = token_line.split(":")[-1].split("@")[0]

OWNER = "TheeTarnished"
REPO = "paper-super-reviewer"
API = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"
HEADERS = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

REPO_DIR = r"C:\Users\82578\Desktop\paper-super-reviewer"
files = []
for root, dirs, filenames in os.walk(REPO_DIR):
    for f in filenames:
        if '.git' in root: continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, REPO_DIR).replace('\\', '/')
        if rel.startswith('create_repo.py'): continue
        files.append((path, rel))

for path, rel in sorted(files):
    content = base64.b64encode(open(path, 'rb').read()).decode()
    resp = requests.put(
        f"{API}/{rel}",
        headers=HEADERS,
        json={"message": f"Add {rel}", "content": content}
    )
    status = resp.json()
    if 'content' in status:
        print(f"  ✅ {rel}")
    else:
        print(f"  ❌ {rel}: {status.get('message', 'unknown')}")

print(f"\nDone! {len(files)} files pushed.")
print(f"https://github.com/{OWNER}/{REPO}")
