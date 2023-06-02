
# Página web de Bruno Diferente

Esta es una página web simple que muestra videos aleatorios del canal de YouTube de Bruno Diferente al iniciar. También cuenta con un botón para cargar un video diferente cada vez que se hace clic en él. La aplicación está desarrollada en Django y utiliza la API de YouTube para obtener los videos.

## Configuración

1.  Clona el repositorio a tu máquina local:
```bash
    git clone https://github.com/tu-usuario/repo.git
    cd repo
```
2.  Crea y activa un entorno virtual    
 ```bash    
    python3 -m venv venv
    source venv/bin/activate
   ```
3.  Instala las dependencias del proyecto:
```bash
    pip install -r requirements.txt
```
5.  Obtén una clave de API de YouTube:
    
    -   Visita el [Centro de Desarrolladores de Google](https://console.developers.google.com/).
    -   Crea un nuevo proyecto (si aún no tienes uno).
    -   Activa la API de YouTube para tu proyecto.
    -   Obtén una clave de API válida para acceder a la API de YouTube.
6.  Configura la clave de API en la aplicación:
    
    -   Crea un archivo `.env` en el directorio raíz del proyecto.
        
    -   Agrega la siguiente línea al archivo `.env` y reemplaza `<TU_CLAVE_DE_API>` con tu clave de API de YouTube:  
 ```bash        
YOUTUBE_API_KEY=<TU_CLAVE_DE_API>
``` 
        

## Uso

1.  Inicia el servidor de desarrollo de Django:
    
     ```bash
    python manage.py runserver
    ``` 
    
2.  Abre tu navegador web y visita la siguiente URL: `http://localhost:8000`
    
3.  La página web se cargará y mostrará automáticamente un video aleatorio del canal de YouTube de Bruno Diferente.
    
4.  Si deseas ver un video diferente, haz clic en el botón "Picale" y se cargará un nuevo video aleatorio.
    

## Contribución

Si deseas contribuir a este proyecto, siéntete libre de abrir un "issue" para discutir tus ideas o enviar una solicitud de extracción con tus mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT.

----------

¡Diviértete viendo los videos de Bruno Diferente en esta página web! Si tienes alguna pregunta o problema, no dudes en contactar al desarrollador del proyecto.
