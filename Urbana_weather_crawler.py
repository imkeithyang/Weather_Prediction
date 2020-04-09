import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 


#Create File, write headaer
filename = 'Urbana_Hitorical_Weather.csv'
f = open(filename, "w")
headers = "Day,Temperature_High,High_Time,Temperature_Low,Low_Time,Temperature_Mean,Precipitation,Snowfall\n"
f.write(headers)

for year in range (2014,2019):
	print ("year: " + str(year))
	year_num = str(year)
	for i in range (1,13): 
		month_num = str(i)
		if year == 2014 and i < 10: continue
		if i < 10: month_num = "0" + month_num
		print("month: " + month_num)
		url = 'https://www.isws.illinois.edu/statecli/urbana/urbana-monthly-' + str(year) +'_files/sheet0' + month_num + '.htm'
		#Open up connection
		uclient = uReq(url); page_html =  uclient.read();
		uclient.close()
		
		page_soup = soup(page_html, 'html.parser')
		
		#grab each news updates
		items = page_soup.findAll("tr", {'height': "18"})
	
		for item in items[2:33]:
			if "Avg" in item.getText(): continue
			if "est" in item.getText(): continue
			tags = item.findAll("td")
	
			data = []
			for tag in tags:
				data.append(tag.text)
			if len(data[0]) < 2: 
				data[0] = "0" + data[0]
			if " " not in data[2]:
				s = data[2]
				temp = s[:len(s) - 2] + " " + s[len(s) - 2:]
				data[2] = temp
			if " " not in data[4]:
				s = data[4]
				temp = s[:len(s) - 2] + " " + s[len(s) - 2:]
				data[4] = temp

			data[0] = year_num + '-' + month_num + '-' + data[0]
			f.write(data[0] + ',' + data[1] + ',' +  data[2] + ','+  data[3] + ',' + data[4] + ',' + data[5] + ',' + data[9].replace("T", "0.0") + ',' + data[10].replace("T", "0.0") + '\n')
		if year == 2018:
			items = page_soup.findAll("tr", {'height': "17"})
			items.insert(35, page_soup.find("tr", {'height': "18"}))
			for item in items[6:36]:
				if "Avg" in item.getText(): continue
				if "est" in item.getText(): continue
				tags = item.findAll("td")
				data = []
				for tag in tags:
					data.append(tag.text)
				if len(data[0]) < 2: 
					data[0] = "0" + data[0]
				if " " not in data[2]:
					s = data[2]
					temp = s[:len(s) - 2] + " " + s[len(s) - 2:]
					data[2] = temp
				if " " not in data[4]:
					s = data[4]
					temp = s[:len(s) - 2] + " " + s[len(s) - 2:]
					data[4] = temp

				data[0] = year_num + '-' + month_num + '-' + data[0]
				f.write(data[0] + ',' + data[1] + ',' +  data[2] + ','+  data[3] + ',' + data[4] + ',' + data[5] + ',' + data[9].replace("T", "0.0") + ',' + data[10].replace("T", "0.0") + '\n')
f.close()