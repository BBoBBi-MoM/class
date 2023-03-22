#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
#%%
html_example =''''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <div id="link">
        <a class="external_link", href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link", href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link", href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''
#%%
soup = BeautifulSoup(html_example,'html.parser')
#print(soup.title)
#print(soup.title.text)
print("title태그의 내용",soup.title.get_text())
# %%
print('title태그의 상위 태그:',soup.title.parent)
# %%
print('body 태그:',soup.body)
# %%
print(':',soup.a.get('href'))
# %%
soup.find('div').a['href']
# %%
div_html = soup.find('div')
div_text = div_html.text
# %%
#href_link = soup.find('a',{'class':'iternal_link'})
href_link = soup.find('a',class_ = 'internal_link')
print(href_link.text)
# %%
print('href_link.attrs: ', href_link.attrs)
# %%
span_tag = soup.find('sapn')
#%%
table = '''
<table>
<tr class="passed a b c" id="row1 example"><td>t1</td></tr>
<tr class="failed" id="row2"><td>t2</td></tr>
</table>
'''
soup1 = BeautifulSoup(table,'html.parser')
for row in soup1.find_all('tr'):
    print(row.attrs)
# %%
div_tags = soup.find_all('div')
print('div_tag_length:',len(div_tags))
for div in div_tags:
    print('-'*45)
    print(div.text.replace('\n',','))
#%%
links = soup.find_all('a')
for link in links:
    print('-'*45)
    print('url:{0},text:{1}'.format(link['href'],link.text))
#%%
link_tag = soup.find_all('a',{'class':['external_link','internal_link']})
#%%
p_tags = soup.find_all('p',{'id':['first','third']})
for p in p_tags:
    print(p.text)
#%%
a = [1,2,3,4,5]
b = list(map((lambda x:x**2),a))
(lambda x: x**2)(3)
# %%
find_example = soup.find('div').find('p').text
select_one_example = soup.select_one('div>p').text
print(find_example)
print(select_one_example)
# %%
head = soup.select_one('head')
print(head)
print('-'*45)
h1 = soup.select_one('h1')
print(h1)
print('-'*45)
footer = soup.select_one('h1#footer')
print(footer)
print('-'*45)
class_link = soup.select_one('a.internal_link')
print(class_link)
# %%
link1 = soup.select_one('div#link > a.external_link')
print(link1.text)
# %%
link2 = soup.select_one('div#link a.external_link')
# %%
h1_all = soup.select('h1')
# %%
url_links = soup.select('a')
for link in url_links:
    print(link['class'])
# %%
div_urls = soup.select('div#class1 > a')
print(div_urls)
# %%
