from celery import Celery


app = Celery('tasks',broker='amqp://rael:alse21@localhost/', backend='amqp')

@app.task
def add(x,y):
	return x+y