import requests
import sys
import re

if __name__ == "__main__":
    assert(len(sys.argv) == 4)
    handle = sys.argv[1]
    indexPath = sys.argv[2]


    hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
    html = requests.get('https://raw.githubusercontent.com/ChenWendi2001/ChenWendi2001/master/README.md',headers = hea)
    html = html.text
   
    html = re.findall(r"(?<=<!\-\-START_SECTION:waka\-\->)[\s\S]*(?=<!\-\-END_SECTION:waka\-\->)",html)[0]
    print(html)
    
    with open(indexPath, "r") as index:
        content = index.read()
        
    newContent = re.sub(r"(?<=<!\-\-START_SECTION:waka\-\->)[\s\S]*(?=<!\-\-END_SECTION:waka\-\->)", f"\n{html}\n", content)
    print(newContent)

    with open(indexPath, "w") as index:
        index.write(newContent)