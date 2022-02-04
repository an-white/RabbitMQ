import pika

"""
estableciendo conexion con RabbitMQ server
"""
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = conn.channel()

"""
crear el recipiente de una cola
"""

channel.queue_declare(queue="hello")

"""
enviar info a la cola, el routing_key es el nombre de la cola y el body es la informacion que recibe dicha cola
"""
channel.basic_publish(exchange="", routing_key="hello", body="ola kiazez")
print("[x] Envio 'hola'")

"""
asegurarse que el buffer fue limpiado y el mensaje fue entregado
"""

conn.close()
