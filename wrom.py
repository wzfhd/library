import requests
from bs4 import BeautifulSoup

# 发送HTTP请求获取网页内容
url = 'https://example.com'
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 提取所需数据
# 以下是一些示例操作，你可以根据具体网页结构和需求进行修改
title = soup.title.text
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text = link.text
    print(f"Link: {href}, Text: {text}")

# 进一步处理数据或保存数据到文件等
# ...

