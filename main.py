import requests
import os

banner = """
      ,gg,        ,gggg,   ,ggggggggggg,              ,ggg,  ,ggggggggggg,     ,ggggggg,  ,ggggggggggg,   
     i8""8i     ,88""""""88""""""Y8,           dP""8I dP""""""""" """""""""88""""""Y8, 
     `8,,8'    d8"     `Y8Yb,  88      `8b          dP   88 Yb,  88      `8b d8'    a  Y8Yb,  88      `8b 
      `88'    d8'   8b  d8 `"  88      ,8P         dP    88  `"  88      ,8P 88     "Y8P' `"  88      ,8P 
      dP"8,  ,8I    "Y88P'     88aaaad8P"         ,8'    88      88aaaad8P"  `8baaaa          88aaaad8P"  
     dP' `8a I8'               88""""Yb,          d88888888      88"""""    ,d8P""""          88""""Yb,   
    dP'   `Ybd8                88     "8b   __   ,8"     88      88         d8"               88     "8b  
_ ,dP'     I8Y8,               88      `8i dP"  ,8P      Y8      88         Y8,               88      `8i 
"888,,____,dP`Yba,,_____,      88       Yb,Yb,_,dP       `8b,    88         `Yba,,_____,      88       Yb,
a8P"Y88888P"   `"Y8888888      88        Y8 "Y8P"         `Y8    88           `"Y8888888      88        Y8
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                                                                                                                           
"""
print(banner)
print("\n A TOOL BY SAM")
def infinite_tsukinomi():
    os.system("mover.bat")
# URL of the website to scrape
infinite_tsukinomi()
url = input("Enter full URL: ")
file = input("Enter file name (for ex: index.html): ")
response = requests.get(url)

f = open(file, "a")
f.write(response.text)
f.close()
