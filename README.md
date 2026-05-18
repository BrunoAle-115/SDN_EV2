# Proyecto Redes EV2: Monitor Astronómico Automatizado

## 1. Contexto y Narrativa
* **Stakeholder:** Educador o divulgador científico de astronomía.
* **Propuesta de Valor (Problema/Solución):** Un divulgador científico necesita obtener diariamente la imagen astronómica del día (APOD) de la NASA junto con su resumen técnico para preparar su material de clases. Esta aplicación automatiza la consulta a la API de la NASA, procesa los datos relevantes y entrega un reporte limpio en consola, ahorrando tiempo de búsqueda manual.

## 2. Guía de Configuración
Para que la aplicación funcione, es estrictamente necesario configurar la siguiente variable de entorno:
* `API_KEY_NASA`: Llave de autenticación proporcionada por api.nasa.gov.

**Ejemplo de configuración en Linux:**
`export API_KEY_NASA="tu_llave_aqui"`

## 3. Instrucciones de Ejecución
Este proyecto utiliza Docker para su contenerización. Para construir y ejecutar la imagen de forma automatizada, utilice el script proporcionado:

1. Otorgue permisos de ejecución al script:
   `chmod +x build_app.sh`
2. Ejecute el script (asegúrese de exportar su API_KEY_NASA previamente, o el script usará la de DEMO_KEY definida internamente):
   `./build_app.sh`