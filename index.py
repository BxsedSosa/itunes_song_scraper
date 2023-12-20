import xml.etree.ElementTree as ET

tree = ET.parse(r'itunes_song_scraper\Library.xml')
root = tree.getroot()

myfile = open(r'itunes_song_scraper\songs.txt','w', encoding='utf-8')

for dict in root.iter('dict'):
  x =(dict[5].text, dict[3].text)
  myfile.writelines(str(x))

myfile.close()
print('done')
  