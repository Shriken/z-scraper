#!/usr/bin/python

import requests
import os

r = False

while not r:
	r = requests.get('http://stuycs-softdev.github.io/assignments.html')

t = r.text
t = t.replace('&#8217;', "'")
t = t[t.find('<h1>Assignments</h1>'):]
t = t[:t.find('</div>') - 9]

def numAssignments(page):
	count = 0
	lastHomeworkFound = False

	while not lastHomeworkFound:
		findString = 'hw-%i-github.html'%(count+1)
		index = page.find(findString)
		lastHomeworkFound = (index == -1)

		if not lastHomeworkFound:
			count += 1

	return count

lastCount = 0

if 'lastCount' in os.listdir('.'):
	f = open('lastCount')
	text = f.read()

	lastCount = int(text)
else:
	f = open('lastCount', 'w')

	lastCount = 0
	f.write(str(lastCount))

count = numAssignments(t)

if lastCount == count:
	print "Nothing new. Carry on jubilantly."
else:
	print "There's a new assignment! Check out the page."

	f = open('lastCount', 'w')
	f.write(str(count));

