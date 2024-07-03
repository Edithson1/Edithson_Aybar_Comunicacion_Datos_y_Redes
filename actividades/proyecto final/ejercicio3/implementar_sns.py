import boto3
from botocore.exceptions import ClientError

def crear_topico_sns(nombre):
    sns = boto3.client('sns')
    try:
        response = sns.create_topic(Name=nombre)
        topic_arn = response['TopicArn']
        print(f"Tópico creado con ARN: {topic_arn}")
        return topic_arn
    except ClientError as e:
        print(f"Error al crear el tópico: {e}")
        return None

def suscribir_email_a_topico(topic_arn, email_address):
    sns = boto3.client('sns')
    try:
        response = sns.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint=email_address
        )
        subscription_arn = response['SubscriptionArn']
        print(f"Suscripción por correo electrónico creada con ARN: {subscription_arn}")
        return subscription_arn
    except ClientError as e:
        print(f"Error al suscribir por correo electrónico: {e}")
        return None

def suscribir_http_a_topico(topic_arn, endpoint_url):
    sns = boto3.client('sns')
    try:
        response = sns.subscribe(
            TopicArn=topic_arn,
            Protocol='http',
            Endpoint=endpoint_url
        )
        subscription_arn = response['SubscriptionArn']
        print(f"Suscripción HTTP/S creada con ARN: {subscription_arn}")
        return subscription_arn
    except ClientError as e:
        print(f"Error al suscribir HTTP/S: {e}")
        return None
        
def enviar_mensaje_sns(topic_arn, mensaje):
    sns = boto3.client('sns')
    try:
        response = sns.publish(
            TopicArn=topic_arn,
            Message=mensaje
        )
        message_id = response['MessageId']
        print(f"Mensaje enviado correctamente con ID: {message_id}")
        return message_id
    except ClientError as e:
        print(f"Error al enviar mensaje: {e}")
        return None



nombre_topico = 'MiTopicoSNS'

# Crear el tópico en SNS
topic_arn = crear_topico_sns(nombre_topico)

# Ejemplo de suscripción por correo electrónico
email_address = 'akuntsueharu@gmail.com'
suscripcion_email_arn = suscribir_email_a_topico(topic_arn, email_address)

# Ejemplo de suscripción HTTP/S
endpoint_url = 'https://2pgrq3u54a.execute-api.us-east-1.amazonaws.com'
suscripcion_http_arn = suscribir_http_a_topico(topic_arn, endpoint_url)

mensaje = 'Hola, este es un mensaje de prueba enviado a través de SNS.'
# Enviar mensaje al tópico
enviar_mensaje_sns(topic_arn, mensaje)


