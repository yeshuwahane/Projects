from plyer import notification
import time

while 1:
    if __name__ == '__main__':
        notification.notify(
            title='Drink Water',
            message="Drinking enough water each day is crucial for many reasons: to regulate body temperature, keep joints lubricated, prevent infections, deliver nutrients to cells, and keep organs functioning properly.",
            app_icon= None ,
            timeout = 5,
        )
        time.sleep(60*60)