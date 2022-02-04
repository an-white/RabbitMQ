import sys

import pika


def new_task():
    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    message = ' '.join(sys.argv[1:]) or "niu tas"

    channel = conn.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
                          )

    print(" [x] Sent %r" % message)
    conn.close()


if __name__ == '__main__':
    new_task()
