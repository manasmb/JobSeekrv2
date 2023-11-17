from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs', methods=['GET','POST'])
def jobs():
    URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+%22ROLE%22+%22(US)+OR+(United+states)%22+SKILL+%22(Intern)+OR+(Internship)%22&sca_esv=576140894&sxsrf=AM9HkKlILxCrhS6DSvta8vIMXbBU58x7pw:1698180369525&source=lnt&tbs=qdr:TIME&sa=X&ved=2ahUKEwj1jMLtxo-CAxXYD1kFHXpxD1oQpwV6BAgBEAg&biw=1872&bih=912&dpr=1'
    role = 'Data Scientist'
    skill = 'Python'
    if request.method=='POST':
        role = request.form.get('role')
        skill = request.form.get('skill')
        URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+%22ROLE%22+%22(US)+OR+(United+states)%22+SKILL+%22(Intern)+OR+(Internship)%22&sca_esv=576140894&sxsrf=AM9HkKlILxCrhS6DSvta8vIMXbBU58x7pw:1698180369525&source=lnt&tbs=qdr:TIME&sa=X&ved=2ahUKEwj1jMLtxo-CAxXYD1kFHXpxD1oQpwV6BAgBEAg&biw=1872&bih=912&dpr=1'
        URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+ROLE+internship+United+States+US+SKILL&sca_esv=576140894&sxsrf=AM9HkKnsclYm6PewKze55SEGdHUUEoEyyw:1698182424439&source=lnt&tbs=qdr:TIME&sa=X&ved=2ahUKEwil9a_Bzo-CAxXTMVkFHVQwB80QpwV6BAgBEAg&biw=1872&bih=912&dpr=1'
        URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+Role+SKILL+internship+OR+intern+United+States&sca_esv=576140894&sxsrf=AM9HkKmX1L3SERNYiWn-8PFpqHb5XK_GwQ:1698183507591&source=lnt&tbs=qdr:w&sa=X&ved=2ahUKEwi1xu7F0o-CAxUfKFkFHWJrCXwQpwV6BAgBEAk&biw=1872&bih=912&dpr=1'
        URL = 'https://www.google.com/search?q=site:myworkdayjobs.com+%7C+site:lever.co+%7C+site:greenhouse.io+Role+SKILL+United+States&sca_esv=576140894&sxsrf=AM9HkKmX1L3SERNYiWn-8PFpqHb5XK_GwQ:1698183507591&source=lnt&tbs=qdr:w&sa=X&ved=2ahUKEwi1xu7F0o-CAxUfKFkFHWJrCXwQpwV6BAgBEAk&biw=1872&bih=912&dpr=1'

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
