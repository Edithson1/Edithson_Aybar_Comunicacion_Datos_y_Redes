**Repaso de computación en la Nube y servicios AWS Temas: IAM, S3**

**La consola de AWS IAM Pregunta:**

**Describe las diferentes secciones de la consola de AWS IAM y cómo se utilizan para gestionar identidades y permisos.**

Permite gestionar el acceso a recursos de AWS. Con IAM, se puede crear y administrar usuarios y grupos,usa permisos para permitir o denegar acceso a recursos de AWS.

**Consola de administración basada en web:** Es un servicio que brinda una interfaz de usuario que está disponible a través del navegador, esto permite crear y gestionar usuarios, grupos, roles y políticas

**Interfaz de línea de comandos:** Es una herramienta que permite ejecutar comandos desde una consola, su uso es muy interesante puesto que se pueden optimizar tareas, más que todo se utilizan para script y flujos de trabajo

**Los SDK:** Brindan todo tipo de código, como python, Java, Node,js entre otros. Es perfecto para utilizarlo de manera programática en servicios de AWS para poder hacer configuraciones de recursos, gestionar los permisos o integrar servicios

**Diferencias clave entre usuarios IAM y Grupos IAM Pregunta:**

**Compara y contrasta las diferencias clave entre usuarios IAM y grupos IAM, incluyendo sus usos y mejores prácticas.**

**DIferencias claves:**

**usos:**

Por un lado, los usuarios IAM se le asignan a una persona o entidad para que pueda acceder a la consola de AWS, realizar tareas administrativas, desarrollo, monitoreo, etc.Esto al otorgarles permisos personalizados al utilizar políticas, dependiendo de la actividad que va a realizar el usuario.

Mientras que los grupos IAM son asignados a grupos de usuarios que realizan funciones similares, como desarrolladores, administradores de bases de datos, equipo de soporte, etc., los cuales comparten políticas de acceso, de esta manera ajilizando el proceso de asignación de permisos.

**Mejores practicas:**

En cuanto a las mejores prácticas, las diferencias entre usuarios y grupos IAM en AWS se reflejan en cómo se gestionan y se aplican estas prácticas a cada uno: Para los usuarios IAM, se enfoca en aplicar el principio de menor privilegio a nivel individual y en la rotación regular de credenciales para garantizar la seguridad de las cuentas. Mientras tanto, para los grupos IAM, la centralización de permisos facilita la aplicación del principio de menor privilegio y garantiza una gestión coherente de permisos mediante la definición de políticas a nivel de grupo, lo que simplifica la administración y reduce el riesgo de errores de configuración.

Crear usuarios

- Hemos creado usuarios para Alice, Bob y Charlie en la consola de IAM de AWS.

Definimos Políticas:

- Definimos una política "DeveloperPolicy" que permite el uso de EC2 y S3 para los desarrolladores.
- También he creado una política "SysAdminPolicy" que otorga acceso completo a la infraestructura para los administradores de sistemas.

  Asignar Políticas:

- Hemos asignado la política "DeveloperPolicy" a Alice para que tenga los permisos necesarios como desarrolladora.
- Asimismo, he asignado la política "SysAdminPolicy" a Bob y a Charlie para que tengan acceso completo como administradores.

  Crear Roles:

- Hemos creado un rol llamado "RolAdmin, RolDesarrollador" que permite el acceso temporal a CloudWatch logs.

  Verificar Permisos:

- El sistema verifica los permisos antes de permitir que un usuario asuma un rol. Por ejemplo, si Alice intenta asumir un rol que no tiene permitido, se le negará el acceso.
