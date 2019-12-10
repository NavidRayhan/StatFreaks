from lxml import html
import requests
from sqlite3 import connect

conn = connect("international_transactions.db")
cursor = conn.cursor()
conn.commit()


def insert_transactions(year): 
    """
        program to webscape data from realGM pages and insert it into sqlite3 database
        inserts on a year by year basis based on url
        param; year to look up specific url 
        return; None
    """    
    page = requests.get("https://basketball.realgm.com/international/transactions/20{0}".format(year))
    tree = html.fromstring(page.content)
    arrOfDates = tree.xpath('//div[@class="portal widget fullpage"]')

    for i in range(len(arrOfDates)):        
        date = arrOfDates[i].getchildren()[0].text_content()
        player = arrOfDates[i].getchildren()[1].find('li').findall('a')[0].text_content() # Player
        
        try:
            team1 = arrOfDates[i].getchildren()[1].find('li').findall('a')[2].text_content() # New Team
            team2 = arrOfDates[i].getchildren()[1].find('li').findall('a')[1].text_content() # Old team
        except:
            team1 = arrOfDates[i].getchildren()[1].find('li').findall('a')[1].text_content()
            team2 = None 

        action = arrOfDates[i].getchildren()[1].find('li').text_content()
        
        if 'has signed' in action:
            action = 'has signed with ' + team1
        else:
            action = 'has left ' + team1
        
        # manipulating teams based on if there is a prev team or not 
        if team2:
            newTeam = team2
            prevTeam = team1
        else:
            newTeam = team1
            prevTeam = None

        with conn:
            cursor.execute("""INSERT INTO International_Transactions VALUES(?,?,?,?,?,?)""",
                            (None, player, date, action, prevTeam, newTeam))

# fills database with every transaction from 2012 to 2020
for i in range(12,21):
    insert_transactions(i)
