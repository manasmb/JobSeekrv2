
from flask import Flask, render_template, request, redirect, url_for, flash,session
from authlib.common.security import generate_token
from authlib.integrations.flask_client import OAuth

import requests


from bs4 import BeautifulSoup
import re
app = Flask(__name__)

oauth = OAuth(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs', methods=['GET','POST'])
def jobs():
    URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+(%22data%22+OR+%22analyst%22)+US+Python+(%22Intern%22+OR+%22Internship%22)&sca_esv=581602149&rlz=1C1RXQR_enIN973IN973&sxsrf=AM9HkKkZia_9G9XsCQtTucNyjc6sZc7QBw:1700201257908&source=lnt&tbs=qdr:w&sa=X&ved=2ahUKEwiwupigr8qCAxUJGlkFHZWuCHUQpwV6BAgBEAk&biw=1920&bih=945&dpr=1'

    role = 'Data Analyst'
    skill = 'Python'
    if request.method=='POST':
        role = request.form.get('role')
        skill = request.form.get('skill')
        URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+%22ROLE%22+%22(US)+OR+(United+states)%22+SKILL+%22(Intern)+OR+(Internship)%22&sca_esv=576140894&sxsrf=AM9HkKlILxCrhS6DSvta8vIMXbBU58x7pw:1698180369525&source=lnt&tbs=qdr:TIME&sa=X&ved=2ahUKEwj1jMLtxo-CAxXYD1kFHXpxD1oQpwV6BAgBEAg&biw=1872&bih=912&dpr=1'
        URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+ROLE+internship+United+States+US+SKILL&sca_esv=576140894&sxsrf=AM9HkKnsclYm6PewKze55SEGdHUUEoEyyw:1698182424439&source=lnt&tbs=qdr:TIME&sa=X&ved=2ahUKEwil9a_Bzo-CAxXTMVkFHVQwB80QpwV6BAgBEAg&biw=1872&bih=912&dpr=1'
        URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+Role+SKILL+internship+OR+intern+United+States&sca_esv=576140894&sxsrf=AM9HkKmX1L3SERNYiWn-8PFpqHb5XK_GwQ:1698183507591&source=lnt&tbs=qdr:w&sa=X&ved=2ahUKEwi1xu7F0o-CAxUfKFkFHWJrCXwQpwV6BAgBEAk&biw=1872&bih=912&dpr=1'
        URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+%22ROLE%22+%22(US)+OR+(United+states)%22+SKILL+%22(Intern)+OR+(Internship)%22&sca_esv=576140894&sxsrf=AM9HkKlILxCrhS6DSvta8vIMXbBU58x7pw:1698180369525&source=lnt&tbs=qdr:TIME&sa=X&ved=2ahUKEwj1jMLtxo-CAxXYD1kFHXpxD1oQpwV6BAgBEAg&biw=1872&bih=912&dpr=1'
        URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+%22ROLE%22+US+%22+SKILL+%22(Internship)+OR+(Intern)%22&sca_esv=583240805&rlz=1C1RXQR_enIN973IN973&sxsrf=AM9HkKmoqu9oqngMc_3OHT-esuYdMhn6Aw:1700200290916&source=lnt&tbs=qdr:w&sa=X&ved=2ahUKEwjk-IvTq8qCAxX0F1kFHY4pDxMQpwV6BAgBEAk&biw=1920&bih=945&dpr=1#ip=1'
        URL = 'https://www.google.com/search?q=site%3Amyworkdayjobs.com+%7C+site%3Alever.co+%7C+site%3Agreenhouse.io+ROLE+US+SKILL+%28%22Intern%22+OR+%22Internship%22%29&sca_esv=581602149&rlz=1C1RXQR_enIN973IN973&biw=1920&bih=945&tbs=qdr%3Ad&sxsrf=AM9HkKmKZ3vfw2OwbpfzxUlisESkbIu8vQ%3A1700200561998&ei=cQBXZezDPO2f5NoPqOCCoAI&ved=0ahUKEwiswK3UrMqCAxXtD1kFHSiwACQQ4dUDCBA&uact=5&oq=site%3Amyworkdayjobs.com+%7C+site%3Alever.co+%7C+site%3Agreenhouse.io+data+analyst+US+Python+%28%22Intern%22+OR+%22Internship%22%29&gs_lp=Egxnd3Mtd2l6LXNlcnAibXNpdGU6bXl3b3JrZGF5am9icy5jb20gfCBzaXRlOmxldmVyLmNvIHwgc2l0ZTpncmVlbmhvdXNlLmlvIGRhdGEgYW5hbHlzdCBVUyBQeXRob24gKCJJbnRlcm4iIE9SICJJbnRlcm5zaGlwIilIAFAAWABwAHgAkAEAmAEAoAEAqgEAuAEDyAEA-AEB4gMEGAAgQQ&sclient=gws-wiz-serp'
        if len(role.split()) > 1:
            URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+(%22ROLE1%22+OR+%22ROLE2%22)+US+Python+(%22Intern%22+OR+%22Internship%22)&sca_esv=581602149&rlz=1C1RXQR_enIN973IN973&sxsrf=AM9HkKkZia_9G9XsCQtTucNyjc6sZc7QBw:1700201257908&source=lnt&tbs=qdr:w&sa=X&ved=2ahUKEwiwupigr8qCAxUJGlkFHZWuCHUQpwV6BAgBEAk&biw=1920&bih=945&dpr=1'
            word1 = role.split()[0]
            word2 = role.split()[1]
            URL = URL.replace("ROLE1", word1)
            URL = URL.replace("ROLE2", word2)
        else: 
            URL = 'https://www.google.com/search?q=site%3Amyworkdayjobs.com+%7C+site%3Alever.co+%7C+site%3Agreenhouse.io+ROLE+US+SKILL+%28%22Intern%22+OR+%22Internship%22%29&sca_esv=581602149&rlz=1C1RXQR_enIN973IN973&biw=1920&bih=945&tbs=qdr%3Ad&sxsrf=AM9HkKmKZ3vfw2OwbpfzxUlisESkbIu8vQ%3A1700200561998&ei=cQBXZezDPO2f5NoPqOCCoAI&ved=0ahUKEwiswK3UrMqCAxXtD1kFHSiwACQQ4dUDCBA&uact=5&oq=site%3Amyworkdayjobs.com+%7C+site%3Alever.co+%7C+site%3Agreenhouse.io+data+analyst+US+Python+%28%22Intern%22+OR+%22Internship%22%29&gs_lp=Egxnd3Mtd2l6LXNlcnAibXNpdGU6bXl3b3JrZGF5am9icy5jb20gfCBzaXRlOmxldmVyLmNvIHwgc2l0ZTpncmVlbmhvdXNlLmlvIGRhdGEgYW5hbHlzdCBVUyBQeXRob24gKCJJbnRlcm4iIE9SICJJbnRlcm5zaGlwIilIAFAAWABwAHgAkAEAmAEAoAEAqgEAuAEDyAEA-AEB4gMEGAAgQQ&sclient=gws-wiz-serp'
            URL = URL.replace("ROLE", role)
        URL = URL.replace("SKILL", skill)
        URL = URL.replace("TIME", 'w')
    # URL = 'https://www.google.com/search?q=site%3Amyworkdayjobs.com+%7C+site%3Alever.co+%7C+site%3Agreenhouse.io+%22Data%22+%22%28US%29+OR+%28United+states%29%22+Python+%22%28Intern%29+OR+%28Internship%29%22&sca_esv=576140894&sxsrf=AM9HkKmy_EkC0_l5hPGHiBu7w8hz6YPqVQ%3A1698164748218&ei=DPA3ZfvADPKx5NoPh--HCA&ved=0ahUKEwj79tjUjI-CAxXyGFkFHYf3AQEQ4dUDCBA&uact=5&oq=site%3Amyworkdayjobs.com+%7C+site%3Alever.co+%7C+site%3Agreenhouse.io+%22Data%22+%22%28US%29+OR+%28United+states%29%22+Python+%22%28Intern%29+OR+%28Internship%29%22&gs_lp=Egxnd3Mtd2l6LXNlcnAifnNpdGU6bXl3b3JrZGF5am9icy5jb20gfCBzaXRlOmxldmVyLmNvIHwgc2l0ZTpncmVlbmhvdXNlLmlvICJEYXRhIiAiKFVTKSBPUiAoVW5pdGVkIHN0YXRlcykiIFB5dGhvbiAiKEludGVybikgT1IgKEludGVybnNoaXApIkgAUABYAHAAeACQAQCYAQCgAQCqAQC4AQPIAQD4AQL4AQHiAwQYACBB&sclient=gws-wiz-serp#ip=1'

    page = requests.get(URL)

    # print(page.text)
    soup = BeautifulSoup(page.content, "html.parser")
    soup
    results = soup.find(id="egMi0 kCrYT")

    heading_object = soup.find_all('a')
    urls = []
    # Iterate through the object
    # and print it as a string.
    for info in heading_object:
        text = info.getText()
        # print(str(info))
        info = str(info)
        url_pattern = r'href="/url\?q=(https?://[^&]+)&'
        url_match = re.search(url_pattern, info)
        each_job = []
        if (url_match) and ((str(text) != 'Learn more')) and ((str(text) != 'Sign in')):
            # print(text)
            extracted_url = url_match.group(1)

            # print("Extracted URL:", )
            each_job.append(text)
            each_job.append(extracted_url)
            print("------")
            urls.append(each_job)
    all_data = []
    for url in urls:
        # print(url)
        each_job = []
        if 'greenhouse' in str(url[1]):

            page = requests.get(url[1])

            # print(page.text)
            soup = BeautifulSoup(page.content, "html.parser")

            job_title = soup.find("h1", {"class": "app-title"})
            if job_title != None:
                job_title = job_title.getText().strip()

                company_name = soup.find("span", {"class": "company-name"})
                company_name = company_name.getText().strip()
                location = soup.find("div", {"class": "location"})
                location = location.getText().strip()
                listing = job_title+" " +company_name+ " " +location
            else:
                listing = 'This job is no longer available but you can search for other jobs on their site!'
            each_job.append(listing)
            each_job.append(url[1])
            all_data.append(each_job)
        else:
            each_job.append(url[0])
            each_job.append(url[1])
            all_data.append(each_job)
            

    # all_data = [['SkillBridge Intern at Skylight United States', 'https://boards.greenhouse.io/skylighthq/jobs/4239496005%3Fgh_jid%3D4239496005'], ['2024 Long-Term Operations Internship at United States Golf Association Lancaster, PA', 'https://boards.greenhouse.io/unitedstatesgolfassociation/jobs/6966547002'], ['People Internship - Summer 2024 at Pagaya New York, NY', 'https://boards.greenhouse.io/pagaya/jobs/5784515003'], ['Long-Term USWO Championship Administration Intern at United States Golf Association Lancaster, PA', 'https://boards.greenhouse.io/unitedstatesgolfassociation/jobs/6929848002'], ['2024 U.S. Open Marketing Internship at United States Golf Association Pinehurst, North Carolina', 'https://boards.greenhouse.io/unitedstatesgolfassociation/jobs/7005038002'], ['2024 USSO Long-Term Championship Administration Internship at United States Golf Association Newport, RI', 'https://boards.greenhouse.io/unitedstatesgolfassociation/jobs/6981244002'], ['2024 Cybersecurity Summer Internship at Schonfeld New York, New York, United States', 'https://boards.greenhouse.io/schonfeld/jobs/5452804']]

    
    return render_template('jobs.html', job_list = all_data, role = role, skill = skill)

@app.route('/google/')
def google():

    GOOGLE_CLIENT_ID = '326367558877-otku242huvrbm6ho9fs4l6i9vf4p5vuc.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'

    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    print(redirect_uri)
    session['nonce'] = generate_token()
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])



@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    # user = oauth.google.parse_id_token(token)
    print(user['email'], user['name'])
    user_name = user['name']

    return redirect(url_for('jobs'))
