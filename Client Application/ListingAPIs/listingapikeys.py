import os, re, json
from urllib2 import Request, urlopen
from urllib import quote
root = 'F:\\Movies'

def findMovieIds(files):
	titles = []
	years = []
	for name in files:
		filename, extension = os.path.splitext(name)
		if extension in ['.mkv', '.mp4', '.avi', '.m4v']:
			flag = False
			matches = re.findall(r"([\s\d]*)([\sA-Za-z'+-.]+)([\d]*)([\sA-Za-z'+-.]*)([\(\[]*[\d][\d][\d][\d][\)\]]*)", filename)
			for match in matches:
				title=(match[0].replace('.',' ').strip()+" "+match[1].replace('.',' ').strip()+" "+match[2].replace('.',' ').strip()+" "+match[3].replace('.',' ').strip()).replace('.',' ').strip()
				year=match[4].replace('(',' ').replace(')',' ').replace('[',' ').replace(']',' ').strip()
				if int(year)>1000 and int(year)<3000:
					titles.append(title)
					years.append(year)
					flag = True
					break
			if not flag:
				matches = re.findall(r"([\s\d]*)([\sA-Za-z'+-.]+)", filename)
				for match in matches:
					title = (match[0].replace('.',' ').strip()+" "+match[1].replace('.',' ').strip()).strip()
					year = None
					if title.lower() not in ['sample', 'silver', 'du', 'esd-hies', 'kkbb', 'extratorrentrg']:
						if ' br' in title.lower():
							title = title.lower().replace('br','').strip()
						if ' rip' in title.lower():
							title = title.lower().replace('rip','').strip()
						if ' yify' in title.lower():
							title = title.lower().replace('yify','').strip()
						if ' x' in title.lower():
							title = title.lower().replace('x','').strip()
						if 'target-' in title.lower():
							title = title[title.find('-')+1:title.find('-', title.find('-')+1)].strip()
						if 'dvdrip' in title.lower():
							title = title[0:title.lower().find('dvdrip')].strip()
						if 'hrspk' in title.lower():
							title = title[0:title.lower().find('hrspk')-1].strip()
						titles.append(title)
						years.append(year)
					break
	removablestrings = ['extended', 'unrated', 'directors cut', 'director\'s cut', 'final cut']
	for i in range(len(titles)):
		if years[i]=='1080':
			if '19' in titles[i]:
				years[i] = titles[i][titles[i].find('19'):titles[i].find('19')+4]
				titles[i] = titles[i][0:titles[i].find('19')].strip()
			elif '20' in titles[i]:
				years[i] = titles[i][titles[i].find('20'):titles[i].find('20')+4]
				titles[i] = titles[i][0:titles[i].find('20')].strip()
		for remstring in removablestrings:
			if remstring in titles[i].lower():
				titles[i] = titles[i][0:titles[i].lower().find(remstring)].strip()

	movieids = []
	for i in range(len(titles)):
		movieSearchUrl = "https://api.themoviedb.org/3/search/movie?api_key=72380f72d2ac93525738d2ef104c283d&"
		headers = {"Accept": "application/json"}
		if years[i] != None:
			url = movieSearchUrl+"query="+quote(titles[i])+"&year="+years[i]
		else:
			url = movieSearchUrl+"query="+quote(titles[i])
		request = Request(url, headers=headers)
		response_body = urlopen(request).read()
		data = json.loads(response_body)
		if data["total_results"] != 0:
			movieids.append(data["results"][0]["id"])
		else:
			movieids.append(None)
	return (titles, years, movieids)

filelist = []
x=0
for path, subdirs, files in os.walk(root):
    for name in files:
    	if os.stat(os.path.join(path, name))[6]>500000000:
    		filelist.append(name)
    		x = x +1
    if x==60:
    	break
y = findMovieIds(filelist)
print y[0]
print y[1]
print y[2]