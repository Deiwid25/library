
Este proyecto es una API para la gestión de libros, construida con FastAPI y Docker. Permite realizar operaciones CRUD sobre libros, gestionar datos y proporcionar documentación interactiva de la API.

## Instrucciones de instalación

1. **Clonar el repositorio**

   Primero, debes clonar el proyecto desde GitHub:

   ```bash
   git clone https://github.com/Deiwid25/library.git
   cd library
   ```


2. **Construir las imágenes de Docker**


```bash
docker-compose build
```

3. **Levantar los contenedores con Docker Compose**


```bash
docker-compose up -d
```


4. **Acceder a la documentación de la API**

Una vez que los contenedores estén corriendo, puedes acceder a la documentación interactiva de la API en:

http://localhost:8000/docs


Preguntas Adicionales
1. **¿Cómo manejarías la autenticación y autorización en la API?**
Para manejar la autenticación y autorización en la API, implementaría el uso de JSON Web Tokens (JWT) para la autenticación de usuarios. El proceso sería:
Crear un endpoint de inicio de sesión donde el usuario proporcione sus credenciales.
Verificar las credenciales y generar un JWT.
Utilizar un middleware que verifique la validez del JWT en cada solicitud a los endpoints protegidos.
Para la autorización, asignar roles o permisos a los usuarios y asegurarse de que solo los usuarios con permisos adecuados puedan acceder a ciertos recursos.

2. **¿Qué estrategias utilizarías para escalar la aplicación?**

Usar Docker y Kubernetes para crear múltiples instancias de la aplicación y distribuir la carga entre ellas.
Implementar una base de datos escalable y replicada (como PostgreSQL con réplicas) para distribuir el tráfico de lectura y escritura.
Utilizar un sistema de caché como Redis para almacenar resultados de consultas frecuentes y mejorar el rendimiento.
Implementar un balanceador de carga (como Nginx o HAProxy) para distribuir las solicitudes de manera eficiente.

3. **¿Cómo implementarías la paginación en los endpoints que devuelven listas de libros?**
ya se encuentra implementada, con los parametros, skip y limit en la url de lsitar libros, puedes consultar en la documentacion 

4. **¿Cómo asegurarías la seguridad de la aplicación (protección contra inyecciones SQL, XSS, etc.)?**

Protección contra inyecciones SQL: Utilizaría un ORM como SQLAlchemy para manejar las consultas de la base de datos de forma segura, evitando el uso de consultas SQL sin procesar que puedan ser vulnerables a inyecciones. (esta ya se usa en el diseño actual)
Protección contra XSS: Aseguraría que cualquier entrada de usuario sea validada y escapada antes de ser mostrada en la interfaz de usuario. Esto se puede hacer utilizando librerías que validen el contenido antes de ser mostrado en el frontend.
Cifrado de contraseñas: Las contraseñas de los usuarios se almacenarían utilizando un algoritmo seguro de hashing (como bcrypt) para evitar que las contraseñas en texto claro sean expuestas en caso de una brecha de seguridad.
Uso de HTTPS: Aseguraría que todas las comunicaciones entre el cliente y el servidor se realicen sobre HTTPS, cifrando la información transmitida.