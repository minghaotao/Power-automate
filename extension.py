import pandas as pd
import requests
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import os
from slacker import Slacker
import json

current_day = datetime.today()
filt_week = (current_day - timedelta(days=7)).strftime('%Y-%m-%d')


def load_json():
    with open("your cred.json", 'r') as f:
        cred = json.load(f)
        return cred


def slack_bot():
    cred = load_json()
    bot = Slacker(cred["slack_token_staff"])
    channel = "your channel"
    bot_name = "your bot name"

    bot.chat.post_message(channel, as_user=bot_name,
                          text=f"Extension Request Reprots -  {filt_week}")

    bot.files.upload(channels=channel, file_='upload file from your local server/assignment-extensions.png')


def extension_requests():
    url = f'your public google sheet url'
    r = requests.get(url)
    with open('/home1/e/edtao/data_reports/extension_report/extension.csv', 'wb') as f:
        f.write(r.content)

    df = pd.read_csv("read file from your local server/extension.csv")

    filt_week = (current_day - timedelta(days=7)).strftime('%Y-%m-%d')
    df = df.loc[df["submission_time"] >= filt_week]
    current_week = df.groupby(["Course_number"]).agg({'status': 'value_counts'})["status"].unstack().fillna(0)
    print(current_week)

    ax = current_week.plot.bar(fontsize=9, figsize=(7, 6), rot=0)

    for patch in ax.patches:
        ax.text(
            patch.get_x(),
            patch.get_height() + 1,
            " {:,}".format(int(patch.get_height())),
            fontsize=10,
            color='dimgrey'
        )

    plt.title(f"Assignment Extension for the week of {filt_week}")

    plt.tight_layout()

    plt.savefig('save file to your local server/assignment-extensions.png')

    plt.show()

    print(df)


if __name__ == '__main__':
    extension_requests()
    slack_bot()
