from __future__ import absolute_import
from celery import shared_task
#from celery.task.schedules import crontab
from scripts.pingatma import ping_ip
#from celery.decorators import periodic_task
import subprocess
import platform


@shared_task
def ping_ip():
    ping_ip()


"""
@periodic_task(
    run_every=(crontab(minute='*/0.2')), #12 saniyede 1 atacak
    name="ping_ip",
    ignore_result=True
)
def ping_ip():
    ping_ip()



def ping_ip(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False

if __name__ == '__main__':
    current_ip_address = ['127.0.0.1', '10.64.25.35', '10.0.2.15', '192.168.56.101']
    for each in current_ip_address:
        if ping_ip(each):
            print(f"{each} is available")
        else:
            print(f"{each} is not available")
"""