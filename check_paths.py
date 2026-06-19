import os, re
root = r'c:\xampp1\htdocs\xampp\Myntra-CE\Myntra-master'
errors = []
for dirpath, dirnames, filenames in os.walk(root):
    for fn in filenames:
        if fn.lower().endswith('.html'):
            path = os.path.join(dirpath, fn)
            rel_dir = os.path.dirname(path)
            with open(path, 'r') as f:
                text = f.read()
            for match in re.findall(r'(?:src|href)=["\"]([^"\"]+)["\"]', text):
                if match.startswith('http://') or match.startswith('https://') or match.startswith('mailto:') or match.startswith('#'):
                    continue
                if match.startswith('data:'):
                    continue
                target = os.path.normpath(os.path.join(rel_dir, match.replace('/', os.sep)))
                if not os.path.exists(target):
                    errors.append((path, match, target))
print('errors=%d' % len(errors))
for p,m,t in errors:
    print(p + ' -> ' + m + ' -> ' + t)
