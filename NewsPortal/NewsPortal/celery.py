import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# app.conf.beat_schedule = {
#        'send_weekly_news': {
#            'task': 'news.tasks.send_weekly_news',
#            'schedule': crontab(day_of_week='mon', hour=8),
#        },
#    }
