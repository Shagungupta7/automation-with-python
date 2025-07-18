import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import dotenv

now = datetime.datetime.now()

#email content placeholder
content = ''

#extracting hacker news stoiries

def extract_news(url):
    print("Extracting Hacker news Stories...")
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n'+'<br>' + '-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    stories = soup.find_all('tr', class_='athing')

    for i, story in enumerate(stories):
        titleline = story.find('span', class_='titleline')
        if titleline and titleline.a:
            title = titleline.a.text.strip()
            link = titleline.a['href']
            cnt += f"{i+1}. <a href='{link}'>{title}</a><br>\n"

    return cnt

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>--------<br>')
content += ('<br><br>End of Message')

#send email

print('Composing Email...')

#update email details

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = dotenv.EMAIL_USERNAME
TO = dotenv.EMAIL_USERNAME
PASS = dotenv.EMAIL_PASS

msg = MIMEMultipart()

msg['Subject'] = 'Top news Stories HN [Automated Email]' + '' + str(now.day) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Intiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1) #to see error msg, set 1 otherwise set 0(this helps in debugging)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()

