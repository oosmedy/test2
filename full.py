import requests

url = "https://sedayezende.ir/"
cookies = {'PHPSESSID': '9olesjraphcramjc2b11g7elns'}
headers = {
    'Host': 'sedayezende.ir',
    'Content-Length': '53',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99", "Google Chrome";v="109"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://sedayezende.ir',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://sedayezende.ir/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}
data = {'domain': 'Digikala.com', 'submitAddNewScore': '1', 'score': '20'}
l=0
while True:
 response = requests.post(url, headers=headers, cookies=cookies, data=data)
 print(l)
 l+=1
