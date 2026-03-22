import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    "const startParam = tg?.initDataUnsafe?.start_param || '';",
    "const _urlParams = new URLSearchParams(window.location.search);\nconst startParam = tg?.initDataUnsafe?.start_param || _urlParams.get('start') || _urlParams.get('startapp') || '';"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done!")
