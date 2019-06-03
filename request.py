# importing the requests library 
import requests 
 
  
# sending post request and saving response as response object 
r = requests.post(url = "http://127.0.0.1:8000/notex/deleteUser/?password=helloxsss&username=skullcrusherss") 
  
# extracting response text  
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)