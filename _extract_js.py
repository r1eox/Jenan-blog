import re, sys
with open('dashboard.html', encoding='utf-8') as f:
    html = f.read()
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
js = '\n'.join(scripts)
with open('_check.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('extracted', len(scripts), 'scripts, total chars:', len(js))
