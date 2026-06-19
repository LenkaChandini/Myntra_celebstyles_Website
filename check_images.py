import os
import re
root = r'c:\xampp1\htdocs\xampp\Myntra-CE\Myntra-master'
html_path = os.path.join(root, 'Homepages', 'Celebstyles.html')
with open(html_path, 'r') as f:
    text = f.read()
refs = set(re.findall(r'src=["\"]\.\./images/([^"\"]+)["\"]', text))
files = set(os.listdir(os.path.join(root, 'images')))
print('refs=%s' % sorted(refs))
print('files=%s' % sorted(files))
print('missing=%s' % sorted(refs - files))
print('extra=%s' % sorted(files - refs))
