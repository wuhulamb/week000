# generate pages/week000.md
import os
import re
x = os.listdir('_posts')
week000 = []
for _ in x:
    m = re.search('.*?week\d{3}\\.md', _)
    if m:
        week000.append(m.group())
week000.sort(reverse=True)

front_matter = ['---\n', 'layout: page\n', 'title: Week000\n', 'permalink: /week000/\n', '---\n', '\n']
with open('pages/week000.md', 'w') as w:
    w.writelines(front_matter)
    for _ in week000:
        with open('_posts/' + _, 'r') as f:
            start, end = False, False
            count = 0
            for line in f:
                if not start and re.match('## 本期回顾.*', line):
                    start = True
                if not end and re.match('## 下期安排.*', line):
                    end = True
                if start and not end:
                    count += 1
                    if count == 1:
                        week = re.search('.*?(week\d{3})\\.md', _).group(1)
                        line = re.match('## 本期回顾(.*)', line).group(1)
                        line = '## [%s]({{ "p/%s/" | relative_url }})%s\n' %(week, week, line)
                    w.write(line)
print('week000.md has been generated')
