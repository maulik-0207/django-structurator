"""
@shared_task(name='any_name')
def add(x, y): # add.delay(10, 20)
    return x + y

@shared_task(bind=True, max_retries=3) 
def fetch_data(self, url): # fetch_data.delay("http://example.com/api/data")
    try:
        response = requests.get(url)
        return response.json()
    except Exception as exc:
        self.retry(exc=exc, countdown=2**self.request.retries)
    

Execution Methods:
--> Using `delay`:
        add.delay(10, 20)

--> Using `apply_async`:
        fetch_data.apply_async(eta= django.utils.timezone.now() + datetime.timedelta(seconds=30))
        fetch_data.apply_async(countdown=10) # Executes after 10 seconds
"""
from celery import shared_task
# Create your tasks here.

