import boto3
import json
from botocore.exceptions import ClientError

#funcion para obtener el arn del topico a partir del nombre 
def obtener_url_arn(nombre_topico):
    sns = boto3.client('sns')
    try:
        response = sns.list_topics()
        topicos = response['Topics']
        for topico in topicos:
            if nombre_topico in topico['TopicArn']:
                return topico['TopicArn']
        return None
    except Exception as e:
        print(f"Error al buscar el tópico por nombre: {e}")
        return None

#funcion para suscribir sqs a topico de sns
def suscribir_cola_sqs_a_topico_sns(topic_arn, queue_arn):
    sns = boto3.client('sns')
    try:
        response = sns.subscribe(
            TopicArn=topic_arn,
            Protocol='sqs',
            Endpoint=queue_arn
        )
        subscription_arn = response['SubscriptionArn']
        print(f"Suscripción de la cola SQS al tópico SNS creada con ARN: {subscription_arn}")
        return subscription_arn
    except ClientError as e:
        print(f"Error al suscribir la cola SQS al tópico SNS: {e}")
        return None

# Función para publicar un mensaje en un tópico de SNS
def publicar_mensaje_sns(topic_arn, message):
    sns = boto3.client('sns')
    try:
        response = sns.publish(
            TopicArn=topic_arn,
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )
        print(f"Mensaje publicado en el tópico SNS con ID de mensaje: {response['MessageId']}")
        return response['MessageId']
    except Exception as e:
        print(f"Error al publicar mensaje en SNS: {e}")
        return None

# Función para recibir mensajes de una cola SQS
def recibir_mensajes_sqs(queue_url):
    sqs = boto3.client('sqs')
    try:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=5
        )
        messages = response.get('Messages', [])
        if messages:
            for message in messages:
                body = json.loads(message['Body'])
                print(f"Mensaje recibido de la cola SQS: {body}")
                # Eliminar el mensaje de la cola después de procesarlo
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
        else:
            print("No se recibieron mensajes de la cola SQS.")
    except Exception as e:
        print(f"Error al recibir mensajes de la cola SQS: {e}")





topic_arn = obtener_url_arn('MiTopicoSNS')
sqs = boto3.client('sqs')
try:
    response = sqs.list_queues()
    colas = response.get('QueueUrls', [])
    for queue_url in colas:
        response = sqs.get_queue_attributes(
                    QueueUrl=queue_url,
                    AttributeNames=['QueueArn']
                )
        queue_arn = response['Attributes']['QueueArn']
        suscribir_cola_sqs_a_topico_sns(topic_arn, queue_arn)
    mensaje = {'message': 'Este es un mensaje de prueba para SNS y SQS'}
    message_id = publicar_mensaje_sns(topic_arn, mensaje)
    for queue_url in colas:
        recibir_mensajes_sqs(queue_url)
except Exception as e:
    print(f"Error al buscar la cola por nombre: {e}")
