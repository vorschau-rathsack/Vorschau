# Fügt in jede Entwurf-Seite (Websiten/<Firma>/*.html, ausser index.html) die Handy-Ansicht ein, falls sie fehlt.
import glob, re
TAG='<script src="../../assets/geraet.js"></script>'
n=0
for f in glob.glob('Websiten/*/*.html'):
    if f.endswith('/index.html'): continue
    s=open(f,encoding='utf-8').read()
    if 'geraet.js' in s: continue
    s2,k=re.subn(r'(<head[^>]*>)',r'\1'+TAG,s,count=1,flags=re.I)
    if not k: continue
    open(f,'w',encoding='utf-8').write(s2); n+=1; print('ergänzt:',f)
print(n,'Datei(en) ergänzt')
