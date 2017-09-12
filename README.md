This is a Telegram bot is build for Python 3.5+.  It the way it was
designed, it requires a PostgreSQL database.

# Installation

1. Install the requirements

```pip3.6 install -r requirements.txt```

2. Create the Telegram bot as per the [instructions](https://core.telegram.org/bots#6-botfather).

3. Copy `secrets.template.py` to `secrets.py`.

4. Fill the variables in `secrets.py`.

5. Set-up the database:

```
CREATE TABLE messages(
   message_id           BIGINT PRIMARY KEY NOT NULL,
   message_date         BIGINT NOT NULL,
   chat_id              BIGINT NOT NULL,
   content_type         CHAR(20) NOT NULL,
   is_deleted           BOOLEAN NOT NULL
);
```

6. Run `python3 listen.py`

7. Schedule `python3 delete.py` to run as a cronjob every minute.