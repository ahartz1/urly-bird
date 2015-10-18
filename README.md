# URLy Bird

### A Website to Shorten, Save, and Share URLs

* `localhost/` shows the most recent saved URLs
* `localhost/worms/worm_id` for each link's page
* `localhost/birds/bird_id` for each user's page

### System Requirements

* You will need to have **Python&nbsp;3** installed on your machine or have access to a Python&nbsp;3 interpreter. See [Python's site](https://www.python.org/) for details.

* Copy this repo to your computer; the below assumes you have kept the default folder name as `urly-bird`.

* You will need to make sure that you have a virtual environment running Python&nbsp;3 in the folder that you made in the above step. [See this site for details if you're not familiar.](http://docs.python-guide.org/en/latest/dev/virtualenvs/) **Complete this step before attempting the below.**

* Using your favorite command line program (e.g., Terminal on Mac&nbsp;OS&nbsp;X), install the requirements file in your virtual environment: `pip install -r requirements.txt`.

* **To create some fake data**, you will need to run some shell commands. Navigate to the `urly-bird/urlybird` folder and confirm that you see the `manage.py` file. Then run the following lines **in order**. (Note that creating the clickstodb takes ~40 minutes on a 2015 MacBookPro.)
```
$ python manage.py migrate
$ python manage.py userstodb
$ python manage.py wormstodb
$ python manage.py clickstodb
$ python manage.py updatenumclicks
```

* **Running the site** requires more command line. Navigate to `urly-bird/urlybird` and enter `python manage.py runserver` This will take over the current command-line program's window until you stop the server. Kill the process by pressing `Ctrl+C` or quitting the command-line program entirely.

### Recent Worms
Located at `localhost/`, where `localhost` is the location of your Django server.

### Bird Pages
Users on this site are referred to as "birds." Located at `localhost/birds/bird_id`, where `localhost` is the location of your django server and `bird_id` is the user_id. These are more easily accessed through the interface by logging in (to see your own bird page) or by clicking on another bird's name.

### Worm Pages
Located at `localhost/worms/worm_id`, where `localhost` is the location of your Django server and `worm_id` is the number associated with that worm. These are more easily accessed through the interface by clicking on the info buttons throughout the site.
