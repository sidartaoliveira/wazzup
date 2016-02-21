from yowsup.demos.sendclient import *
import gearman
from time import sleep

credentials = ('551199998888','XXXXXXXXXXXXXX+')

gm_worker = gearman.GearmanWorker(['localhost:4730'])

def task_listener_send_wazzup(gearman_worker, gearman_job):
  messages = [ gearman_job.data ]
  sleep(0.05)
  try:
    app = YowsupSendStack(credentials, messages, False)
    app.start()
  except KeyboardInterrupt:
    pass
  return GearmanJobRequest.JOB_COMPLETE

gm_worker.set_client_id('wazzup-worker')
gm_worker.register_task('wazzup', task_listener_send_wazzup)

gm_worker.work()