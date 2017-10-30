# Prediccion de clima Ws (Version dev.0.1)

Este servicio web se usa para obtener la prediccion climatica en Ferengi, Betasoide, Vulcano.

## Metodos disponibles

**clima**
----
  _Se usa para obtener el clima de un dia en especifico._

* **Url**

  _http://localhost/clima_

* **Methodo:**


  `GET`

*  **URL Params**


   **Requerido:**

   `dia=[integer]`

* **Llamada de ejemplo:**

    ```sh
    ~$ wget -qO- http://localhost/clima?dia=68
    ```

* **Respuesta exitosa:**

    **Content:**
    `{
    "clima": "lluvia",
    "dia": 68
    }`

* **Respuesta no exitosa:**

    **Content:**
    `{
    "error": "true",
    "errorList": [
        "El dia seleccionado no ha sido generado."
    ]
    }`

**generar**
----
  _Se usa para generar el pronostico que se consulta en el metodo clima._

* **Url**

  _http://localhost/generar_

* **Methodo:**


  `GET`

*  **URL Params**


   **Requerido:**

   `dias=[integer]`
   *OR*
   `anios=[integer]`

   **Opcional:**
   `planeta=[string]`

   * **Admitidos:**
        `Ferengi` | `Vulcano` | `Betasoide`

* **Llamada de ejemplo:**

    ```sh
    ~$ wget -qO- http://localhost:8081/generar?dias=71
    ```

* **Respuesta exitosa:**

    **Content:**
    `{
    "lluvia": 11,
    "optimo": 2,
    "pico_lluvia": {
        "perimetro": 6230.14485411762,
        "dia": 70
    },
    "null": 57,
    "error": false,
    "total_dias": 71,
    "sequia": 1
    }`

* **Respuesta no exitosa:**

    **Content:**
    `{
    "error": "true",
    "errorList": []
    }`
