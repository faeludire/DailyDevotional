# DailyDevotional
This project scrapes the latest devotional from http://apostolicfaith.org/daily-devotional and tweets updates everyday.

## To run an instance of this app, you need:

#### Clone the Repo
- The code is hosted at https://github.com/faeludire/DailyDevotional.git
- Check out the latest development version:
    ```
    $ git clone https://github.com/faeludire/DailyDevotional.git
    $ cd DailyDevotional/
    ```

- To install libraries, run:

    ```
    $ pip install -r requirements.txt
    ```
- Create `credentials.py` in `DailyDevotional/`
- `credentials.py` holds your own Twitter API Keys

    ```
    credentials.py
    consumer_key = "YOUR-CONSUMER-KEY-HERE"
    consumer_secret = "YOUR-CONSUMER-SECRET-HERE"
    access_token = "YOUR-TOKEN-HERE"
    access_token_secret = "YOUR-TOKEN-SECRET-HERE"
    ```

- To start the app run:

    ```
    $ python3 daily_devotional.py
    ```
