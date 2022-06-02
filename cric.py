# JAI BAJARANG BALI

#manitianajay45

#give me some sunshine,give me some rain,give me some little more chance to grow up once again


# https://www.cricbuzz.com/

'''
download these module first:

pip install notify-py
pip install requests
pip install webbrowsers
pip install beautifulsoup4

'''
from time import sleep
from notifypy import Notify

notification = Notify()


import requests
import webbrowser
from bs4 import BeautifulSoup

url="https://www.cricbuzz.com"

page=requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='match_menu_container')

elem= results.find_all('ul',class_='cb-col cb-col-100 videos-carousal-wrapper')
for elem in elem:
    matches=elem.find_all('li',class_='cb-col cb-col-25 cb-mtch-blk cb-vid-sml-card-api videos-carousal-item cb-carousal-item-large cb-view-all-ga')
matches_name=[]
for matches in matches:
    ls=[]
    ls.append(matches.find('a')['title'])
    ls.append(matches.text)  
    ls.append(matches.find('a')['href'])
    matches_name.append(ls)
# print(matches_name)
ind=0
for i in range(0,len(matches_name)):
    ind+=1
    print(ind," ",matches_name[i][0])

print("select match no whichever you want")
ind=int(input())
print("open this link to watch scorecard:-")
match_url=url+matches_name[ind-1][2]
print(match_url)
while(True):
    specific_match=requests.get(match_url)
    specific_match_soup=BeautifulSoup(specific_match.content,'html.parser')
    # print(specific_match_soup)
    options=specific_match_soup.find(id='matchCenter')
    # print(options)

    team_details=options.find('div',class_='cb-col-100 cb-col cb-col-scores')
    more_options=options.find_all('a',class_='cb-nav-tab')
    # print(more_options)

    score_board=more_options[1]['href']
    score_board= url + score_board
    # score_board_link=score_board[1].find_all('a')['href']
    print(score_board)

    notification.title = matches_name[ind-1][0]
    notification.message = matches_name[ind-1][1]
    notification.send(block=False)
    if(team_details is None):
        if 'won' in matches_name[ind-1][1]  or  'drawn' in matches_name:
            print("match has finished:")
            print(matches_name[ind-1][1])
        else:
            print("match yet not started")
            print(matches_name[ind-1][1])

    else:
        print(team_details.text)
        print("would you like to want full scorecard??")
        print("if yes then press 1 otherwise press number")
        ch=int(input())

        if(ch==1):
            # print(score_board)
            webbrowser.open(score_board)
        else:
            pass
    sleep(600) #notification time
        

