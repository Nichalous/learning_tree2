
import re
def filter_hkeys():
  workingset = []
  with open('/tmp/nick-files.txt') as f:
    for line in f:
      if 'C:' in line:
        workingset.append(line)
  return workingset
def extract_pathname(lines):
  newset = []
  for l in lines:
    m = re.search('(C:.*)', l)
    if m:
      newset.append(m.group(1))
  return newset

if __name__ == '__main__':
   workingset = filter_hkeys()
   workingset = extract_pathname(workingset)
   with open('/tmp/nick-files-2.txt', 'w') as f:
         for p in workingset:
            f.write(p+'\n')
