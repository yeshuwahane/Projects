from pynotifier import Notification
import time
while 1:
    if __name__ == '__main__':
        Notification(title="Drink Water",
                     description="The importance of hydration. Drinking enough water each day is crucial for many reasons: to regulate body temperature, keep joints lubricated, prevent infections, deliver nutrients to cells, and keep organs functioning properly. Being well-hydrated also improves sleep quality, cognition, and mood.",
                     icon_path='glass.png',
                     duration= 15,
                     urgency=Notification.URGENCY_CRITICAL).send()
        time.sleep(60*60)