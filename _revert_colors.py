# -*- coding: utf-8 -*-
"""
يُعيد ألوان dashboard.html و jenan-erp.html إلى الأصل (أزرق/بنفسجي)
مع الحفاظ على قسم JenanPro الذهبي في dashboard.html
"""
import os

BASE = r'c:\Users\JEN21\OneDrive\سطح المكتب\بايثون\jenan-biz'

# ══════════════════════════════════════════
# 1. jenan-erp.html — فقط CSS (الأصل أزرق بنفسجي)
#    الأنماط الـ HTML تبقى ذهبية (شعار + كلمة "برو")
# ══════════════════════════════════════════
ERP_CSS_REVERTS = [
    # :root variables
    ('  --accent:   #c9a227;',          '  --accent:   #6366f1;'),
    ('  --accent2:  #a07c1e;',          '  --accent2:  #4f46e5;'),
    ('  --accent-bg: rgba(201,162,39,.12);', '  --accent-bg: rgba(99,102,241,.12);'),
    # .splash-logo CSS
    ('  background: linear-gradient(135deg, #a07c1e, #7a5c10);',
     '  background: linear-gradient(135deg, #4f46e5, #7c3aed);'),
    ('  box-shadow: 0 0 60px rgba(201,162,39,.5);',
     '  box-shadow: 0 0 60px rgba(99,102,241,.5);'),
    # @keyframes pulse-logo
    ('  0%, 100% { box-shadow: 0 0 30px rgba(201,162,39,.35); transform: scale(1); }',
     '  0%, 100% { box-shadow: 0 0 30px rgba(99,102,241,.35); transform: scale(1); }'),
    ('  50%       { box-shadow: 0 0 70px rgba(201,162,39,.65); transform: scale(1.04); }',
     '  50%       { box-shadow: 0 0 70px rgba(99,102,241,.65); transform: scale(1.04); }'),
    # .splash-title
    ('  background: linear-gradient(135deg, #e5c55a, #d4af37);',
     '  background: linear-gradient(135deg, #818cf8, #a78bfa);'),
    # .splash-loader-bar
    ('background: linear-gradient(90deg, #c9a227, #d4af37);',
     'background: linear-gradient(90deg, #6366f1, #a78bfa);'),
]

erp_path = os.path.join(BASE, 'jenan-erp.html')
with open(erp_path, 'r', encoding='utf-8') as f:
    erp = f.read()

for old, new in ERP_CSS_REVERTS:
    if old in erp:
        erp = erp.replace(old, new)
        print(f'  ERP OK: {old[:50]}')
    else:
        print(f'  ERP MISS: {old[:50]}')

with open(erp_path, 'w', encoding='utf-8') as f:
    f.write(erp)
print('✓ jenan-erp.html done\n')

# ══════════════════════════════════════════
# 2. dashboard.html — كل الذهبي → أزرق
#    ماعدا: قسم CSS #navgrp-growth
#           وقسم HTML navgrp-growth
# ══════════════════════════════════════════
GOLD_TO_BLUE = [
    ('rgba(201,162,39,', 'rgba(78,115,194,'),
    ('rgba(122,92,16,',  'rgba(30,58,138,'),
    ('#c9a227',          '#4E73C2'),
    ('#a07c1e',          '#3558A8'),
    ('#7a5c10',          '#1E3A8A'),
    ('#e5c55a',          '#7B9ED4'),
    ('#d4af37',          '#6896D8'),
    ('#f0d060',          '#93B4E8'),
    ('#fdf8e8',          '#EEF2FC'),
]

# حدود قسم CSS الخاص بـ JenanPro
CSS_PROTECT_START = '/* ══ JenanPro قسم خاص — أسود ذهبي احترافي ══ */'
CSS_PROTECT_END   = '\n@media(max-width:900px){'

# حدود قسم HTML الخاص بـ JenanPro
HTML_PROTECT_START = '<!-- ══ JenanPro ══ -->'
HTML_PROTECT_END   = '<!-- ══ تقاريري ووثائقي ══ -->'

dash_path = os.path.join(BASE, 'dashboard.html')
with open(dash_path, 'r', encoding='utf-8') as f:
    dash = f.read()

# إيجاد مواضع الحماية
c_s = dash.find(CSS_PROTECT_START)
c_e = dash.find(CSS_PROTECT_END, c_s)
h_s = dash.find(HTML_PROTECT_START)
h_e = dash.find(HTML_PROTECT_END, h_s)

print(f'CSS block:  [{c_s}:{c_e}]')
print(f'HTML block: [{h_s}:{h_e}]')

if -1 in (c_s, c_e, h_s, h_e):
    print('WARN: ماركر غير موجود!')

# تقسيم الملف إلى أجزاء (محمية / قابلة للتعديل)
regions = sorted([(c_s, c_e), (h_s, h_e)], key=lambda x: x[0])
result = ''
prev = 0
for rs, re in regions:
    # الجزء قبل المنطقة المحمية → نُطبّق الاستبدال
    chunk = dash[prev:rs]
    for gold, blue in GOLD_TO_BLUE:
        chunk = chunk.replace(gold, blue)
    result += chunk
    # المنطقة المحمية → نُبقيها كما هي
    result += dash[rs:re]
    prev = re
# ما تبقى بعد آخر منطقة محمية → نُطبّق الاستبدال
chunk = dash[prev:]
for gold, blue in GOLD_TO_BLUE:
    chunk = chunk.replace(gold, blue)
result += chunk

with open(dash_path, 'w', encoding='utf-8') as f:
    f.write(result)
print('✓ dashboard.html done')
