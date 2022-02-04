manual message acknowlewdgemtns se asegura que el mensaje enviado nunca se pierda ya sea porque no se pudo procesar el
mensaje o porque el receptor no lo recibio correctamente

para evitar un aumento del consumo de memoria por omitir basic_ack sudo rabbitmqctl list_queues name messages_ready
messages_unacknowledged

por defecto la cola asignara todas las tareas a todos los workers que existen esto puede causar que uno de los workers
se quede con una lista de mensajes sin procesar se debe setear un prefetch_count=1 para evitar que los workers tengan
mas de 1 tarea asignada a la vez

tamaño de las colas si todos los workers se ocupan durante mucho tiempo la cola se puede llenar