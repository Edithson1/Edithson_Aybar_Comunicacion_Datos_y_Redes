import uuid
import datetime


# ServicioIAM para gestionar usuarios, roles y credenciales temporales
class ServicioIAM:
    def __init__(self):
        self.usuarios = {}
        self.grupos = {}
        self.politicas = {}
        self.roles = {}
        self.credenciales_temporales = {}

    def crear_rol(self, nombre_rol, politicas):
        self.roles[nombre_rol] = [nombre_rol, politicas]
        print(f"Rol '{nombre_rol}' creado.")

    def asumir_rol(self, nombre_usuario, nombre_rol):
        if nombre_usuario in self.usuarios and nombre_rol in self.roles:
            rol = self.roles[nombre_rol]
            credenciales = self.generar_credenciales_temporales()
            expiracion = datetime.datetime.now() + datetime.timedelta(hours=1)
            print(expiracion)
            self.credenciales_temporales[credenciales['clave_acceso']] = {
                'usuario': nombre_usuario,
                'rol': nombre_rol,
                'expiracion': expiracion,
                'politicas': rol[1]
            }
            return credenciales
        else:
            print(f"Error: Usuario '{nombre_usuario}' o rol '{nombre_rol}' no existe.")
            return None

    def generar_credenciales_temporales(self):
        return {
            'clave_acceso': str(uuid.uuid4()),
            'clave_secreta': str(uuid.uuid4()),
            'token_sesion': str(uuid.uuid4())
        }

    def verificar_permiso(self, clave_acceso, accion):
        if clave_acceso in self.credenciales_temporales:
            info_cred = self.credenciales_temporales[clave_acceso]
            if datetime.datetime.now() > info_cred['expiracion']:
                print(f"Error: Las credenciales para la clave de acceso '{clave_acceso}' han expirado.")
                return False
            for politica in info_cred['politicas']:
                if accion in politica[1]:
                    return True
        print(f"Permiso denegado para la acción '{accion}' con clave de acceso '{clave_acceso}'.")
        return False

# ConsolaIAM para gestionar usuarios y roles
class ConsolaIAM:
    def crear_usuario(self, servicio_iam, nombre_usuario):
        servicio_iam.usuarios[nombre_usuario] = {'politicas': [], 'mfa_habilitado': False}
        print(f"Usuario '{nombre_usuario}' creado.")

    def crear_rol(self, servicio_iam, nombre_rol, politicas):
        servicio_iam.crear_rol(nombre_rol, politicas)

    def asumir_rol(self, servicio_iam, nombre_usuario, nombre_rol):
        credenciales = servicio_iam.asumir_rol(nombre_usuario, nombre_rol)
        if credenciales:
            print(f"Usuario '{nombre_usuario}' asumió el rol '{nombre_rol}'. Credenciales temporales: {credenciales}")
            return credenciales

# Inicialización y pruebas
servicio_iam = ServicioIAM()
consola_iam = ConsolaIAM()

# Crear usuario, roles y políticas
consola_iam.crear_usuario(servicio_iam, "alice")
politica_admin = ["AdminPolicy", ["s3:ListBucket", "ec2:StartInstances"]]
politica_desarrollador = ["DeveloperPolicy", ["s3:PutObject", "ec2:StopInstances"]]

servicio_iam.politicas["AdminPolicy"] = politica_admin
servicio_iam.politicas["DeveloperPolicy"] = politica_desarrollador

consola_iam.crear_rol(servicio_iam, "RolAdmin", [politica_admin])
consola_iam.crear_rol(servicio_iam, "RolDesarrollador", [politica_desarrollador])

# Usuario asume rol y verifica permisos
credenciales = consola_iam.asumir_rol(servicio_iam, "alice", "RolAdmin")
if credenciales:
    clave_acceso = credenciales['clave_acceso']
    print("Verificando permisos para 's3:ListBucket':")
    servicio_iam.verificar_permiso(clave_acceso, "s3:ListBucket")
    print("Verificando permisos para 'ec2:StopInstances':")
    servicio_iam.verificar_permiso(clave_acceso, "ec2:StopInstances")
