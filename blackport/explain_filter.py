import re
"""
1)change opacity of wm
2)copy filter.py into #Explain_Filter.py
3) RE module
parse
   .1)workingset
   .2)workingset.append()
   .3)newset
   .4)newset.append(m.group(1))

7)create a ## version of filter.py
"""
####################################################

def filter_hkeyes():
   workingset = []
   with open('/tmp/nick-files.txt') as f:
      for line in f:
         if 'C:' in line:
## .append
            workingset.append(line)
         return workingset
def extract_pathname(lines):
##explain dictionary newset
   newset = []
   for l in lines:
##re in re.search "c:" matches the c and : characters literatly
##re in re.search '.*' == any charcter except newline
      m - re.search('(c:.*', l)
##searches workinset for case of m
##explain .append(m.group(1))
      if m:
         newset.append(m.group(1))
   return newset

##explain __name__ == '__main__': Python files can act as either reusable modules, or as standalone programs.

if __name__ == '__main__':
   workingset = filter_hkeyes()
   workingset = extract_pathname(workingset)
   with open('/tmp/nick-files-2.txt', 'w') as f:
         for p in workingset:
            f.write(p+'\n')
