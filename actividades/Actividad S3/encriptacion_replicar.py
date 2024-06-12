from cryptography.fernet import Fernet
import copy
import os

class EncryptedReplicatedObjectStorage:
    def __init__(self, key):
        self.cipher = Fernet(key)
        self.buckets = {}
        
    #crear buckes
    def create_bucket(self, name):
        self.buckets[name] = {}

    #Almacenar y encriptar contenido de un archivo de un bucket
    def put_object(self, bucket, key, data):
        datos_encriptados = self.cipher.encrypt(data.encode())
        if bucket in self.buckets:
            self.buckets[bucket][key] = datos_encriptados
            print("data encriptada: "+str(datos_encriptados))

    #obtener el contenido de un archivo de un bucket
    def get_object(self, bucket, key):
        datos_encriptados = self.buckets.get(bucket, {}).get(key, None)
        if datos_encriptados is not None:
            return self.cipher.decrypt(datos_encriptados).decode()
        return "archivo "+key+" no encontrado en el "+ bucket

    #replicar la informacion de un bucket en otro
    def replicate(self, source_bucket, target_bucket):
        if source_bucket in self.buckets and target_bucket in self.buckets:
            self.buckets[target_bucket] = copy.deepcopy(self.buckets[source_bucket])
        else:
            print("no se a encontrado el "+source_bucket*int(source_bucket not in self.buckets) + target_bucket*int(target_bucket not in self.buckets)+" en la lista de buckets")

# Ejemplo de uso
clave = Fernet.generate_key()
almacenamiento = EncryptedReplicatedObjectStorage(clave)

# Crear buckets
almacenamiento.create_bucket('bucket1')
almacenamiento.create_bucket('bucket2')
archivo = {'nombre': 'file1.txt', 'data':'¡Hola, almacenamiento encriptado y replicado!'}

# Almacenar y encriptar datos en bucket1
almacenamiento.put_object('bucket1', archivo['nombre'], archivo['data'])

# Replicar datos de bucket1 a bucket2
almacenamiento.replicate('bucket1', 'bucket2')

# Recuperar y desencriptar datos de ambos buckets
print(almacenamiento.get_object('bucket1', 'file1.txt'))  # Output: '¡Hola, almacenamiento encriptado y replicado!'
print(almacenamiento.get_object('bucket2', 'file1.txt'))  # Output: '¡Hola, almacenamiento encriptado y replicado!'



# Obtener el directorio de trabajo actual
directorio_actual = os.getcwd()
print("Directorio actual:", directorio_actual)
