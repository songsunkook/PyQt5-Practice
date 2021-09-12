#import requests
import urllib.request
url = "https://streaming.copyright.or.kr:1935/upload/encoding/video/2021/09/618941eb12af4503862c273cc0423868_media1.mp4"
savename = "dd.mp4"

urllib.request.urlretrieve(url,savename)
print("저장완료")


#mem=requests.get(url).content

#with open(savename,"wb") as f:
#  f.write(mem)
#  print("저장완료!")