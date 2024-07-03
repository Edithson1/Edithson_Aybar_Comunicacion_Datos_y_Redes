import boto3
from botocore.exceptions import ClientError

def crear_cola_sqs(nombre):
    try:
        # Crear un cliente de SQS
        sqs = boto3.client('sqs')
        # Crear la cola SQS
        response = sqs.create_queue(
            QueueName=nombre
        )
        return response['QueueUrl']
    except ClientError as e:
        print(f"Error al crear la cola: {e}")

def enviar_mensajes_a_cola(queue_url, mensajes):
    try:
        # Crear un cliente de SQS
        sqs = boto3.client('sqs')
        for mensaje in mensajes:
            # Enviar el mensaje a la cola SQS
            response = sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=mensaje
            )
            print(f"Mensaje enviado a la cola: {response['MessageId']}")
    except ClientError as e:
        print(f"Error al enviar el mensaje a la cola: {e}")

def procesar_enviar_a_s3(mensaje):
    bucket_name = 'proyecto-datos'
    object_key = f'mensaje_{mensaje["MessageId"]}.txt'  # Nombre único para cada mensaje

    s3 = boto3.client('s3')
    try:
        # Subir el mensaje como archivo en S3
        response = s3.put_object(
            Body=mensaje['Body'].encode('utf-8'),  # Convertir el mensaje a bytes
            Bucket=bucket_name,
            Key=object_key
        )
        print(f"Mensaje enviado a S3: {object_key}")
    except ClientError as e:
        print(f"Error al enviar el mensaje a S3: {e}")

def leer_y_procesar_mensajes(queue_url):
    try:
        # Crear un cliente de SQS
        sqs = boto3.client('sqs')
        while True:
            # Recibir mensajes de la cola SQS
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=20
            )
            mensajes = response.get('Messages', [])
            if not mensajes:
                print("No hay mensajes en la cola.")
                continue
            for mensaje in mensajes:
                print(f"Mensaje recibido: {mensaje['Body']}")
                # Procesar el mensaje enviándolo a S3
                procesar_enviar_a_s3(mensaje)

    except ClientError as e:
        print(f"Error al leer o procesar mensajes: {e}")

if __name__ == "__main__":
    nombre_cola = 'MiColaSQS'

    # Crear la cola SQS
    queue_url = crear_cola_sqs(nombre_cola)
    
    # Enviar un mensaje a la cola SQS
    if queue_url:
        mensajes = [
            'Mensaje 1 para la cola SQS',
            'Mensaje 2 para la cola SQS',
            'Mensaje 3 para la cola SQS'
        ]
        enviar_mensajes_a_cola(queue_url, mensajes)
    if queue_url:
        leer_y_procesar_mensajes(queue_url)