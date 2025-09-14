from django.http import HttpResponse
from datetime import datetime, timedelta
import datetime


def display_time(request):
    now = datetime.datetime.now()
    ahead = now + timedelta(hours=4)
    before = now - timedelta(hours=4)
#
    time = f"""<h1>Time table</h1>
    <p>Current time is {now}<p>
        <p>4 Hour ahead the current time {ahead}</p>
       <p>4 Before ahead the current time{before}</p>
    """
    return HttpResponse(time)


def twentyfour(request):
    rightnow = datetime.datetime.now()
    twentyFourAhead = rightnow+timedelta(hours=24)
    twentyFourBefore = rightnow-timedelta(hours=24)

    hour = f"""<h1>Current Time table</h1>
    <p>Current time is {rightnow}<p>
        <p>24 Hour ahead the current time {twentyFourAhead}</p>
       <p>24 Hour Before the current time{twentyFourBefore}</p>
       """
    return HttpResponse(hour)
