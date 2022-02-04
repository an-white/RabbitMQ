import os
import sys
import time

import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b"."))
    print("[x] Done")
    """
    debe añadirse siempre
    """
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    """
    añadir durabilidad de los mensajes enviados que pueden quedar perdidos por crashes 
    de rabbit
    al definir una cola no se puede modificar su contenido sus parametros ya que arroja 
    un error
    """

    channel.queue_declare(queue='task_queue', durable=True)

    """
    auto_ack=True apaga el manual message acknowlewdgemtns 
    """
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='hello', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        """
        a la espera de nuevos mensajes
        """
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
