import schedule
import time

def job():
    print("Scheduler is working.")

schedule.every(5).seconds.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
    print("testing")

