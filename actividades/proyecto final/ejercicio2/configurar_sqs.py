import boto3
from botocore.exceptions import ClientError

def crear_cola_sqs(nombre, visibility_timeout = 60, message_retention_period = 86400, delay_seconds = 10):
    try:
        # Crear un cliente de SQS
        sqs = boto3.client('sqs')
        # Crear la cola SQS con configuraciones personalizadas
        response = sqs.create_queue(
            QueueName=nombre,
            Attributes={
                'VisibilityTimeout': str(visibility_timeout),  # Tiempo de visibilidad en segundos
                'MessageRetentionPeriod': str(message_retention_period),  # Retención de mensajes en segundos
                'DelaySeconds': str(delay_seconds)  # Tiempo de espera inicial para mensajes en segundos
            }
        )
        print(f"Cola creada: {response['QueueUrl']}")
        return response['QueueUrl']
    except ClientError as e:
        print(f"Error al crear la cola: {e}")
        return None
        
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


def recibir_y_eliminar_mensajes(queue_url):
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
                print("No hay más mensajes en la cola.")
                break

            for mensaje in mensajes:
                # indicar que el mensaje a sido recibido
                print(f"Mensaje recibido: {mensaje['Body']}")
                
                # Eliminar el mensaje después de procesarlo
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=mensaje['ReceiptHandle']
                )
                print("Mensaje eliminado de la cola.")
    except ClientError as e:
        print(f"Error al recibir o eliminar mensajes: {e}")


#creacion de las colas con diferentes politicas
sqs_urls = []
colas = [
        {'nombre': 'Cola1', 'visibility_timeout': 30, 'message_retention_period': 86400, 'delay_seconds': 0},
        {'nombre': 'Cola2', 'visibility_timeout': 45, 'message_retention_period': 172800, 'delay_seconds': 5},
        {'nombre': 'Cola3', 'visibility_timeout': 60, 'message_retention_period': 345600, 'delay_seconds': 10}
]

for cola in colas:
    sqs_urls.append(cola['nombre'], cola['visibility_timeout'], cola['message_retention_period'], cola['delay_seconds']))
for queue_url in sqs_urls:
    # Enviar un mensaje a la cola SQS
    if queue_url:
        mensajes = [
                'Mensaje 1 para la cola SQS',
                'Mensaje 2 para la cola SQS',
                'Mensaje 3 para la cola SQS'
        ]
        enviar_mensajes_a_cola(queue_url, mensajes)
        leer_y_procesar_mensajes(queue_url)
