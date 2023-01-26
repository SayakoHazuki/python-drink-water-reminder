from plyer import notification
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

interval = int(config['SETTINGS']['interval'])

notification.notify(
    app_name="Drink Water Reminder",
    title="Drink Water Reminder",
    message="Drink Water Reminder has been started."
)

while __name__ == '__main__':
    time.sleep(interval * 60)
    notification.notify(
        app_name="Drink Water Reminder",
        title="Drink Water",
        message=f"It has been {interval} minutes since you last drank water."
    )
