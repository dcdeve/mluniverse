# Prediccion de clima Ws (Version dev.0.1)

Este servicio web se usa para obtener la prediccion climatica en Ferengi, Betasoide, Vulcano.

## Metodos disponibles

**Resumen**
----
  _Se usa para obtener el clima de un dia en especifico._

* **Url**

  _http://dcdev.pythonanywhere.com/_

* **Methodo:**


  `GET`

* **Llamada de ejemplo:**

    ```sh
    ~$ wget -qO- http://dcdev.pythonanywhere.com/
    ```

* **Respuesta exitosa:**

    **Content:**
    `{
    "error": false,
    "sequia": 40,
    "pico_lluvia": {
        "dia": 3168,
        "perimetro": 6262.300354242006
    },
    "null": 2299,
    "optimo": 40,
    "total_dias": 3600,
    "lluvia": 1181
    }`

* **Respuesta no exitosa:**

    **Content:**
    `{
    "errorList": [
        "La base de datos no ha sido generada."
    ],
    "error": "true"
    }`

**clima**
----
  _Se usa para obtener el clima de un dia en especifico._

* **Url**

  _http://dcdev.pythonanywhere.com/clima_

* **Methodo:**


  `GET`

*  **URL Params**


   **Requerido:**

   `dia=[integer]`

* **Llamada de ejemplo:**

    ```sh
    ~$ wget -qO- http://dcdev.pythonanywhere.com/clima?dia=68
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

**generar (Desactivado mientras se crea en multithread)**
----
  _Se usa para generar el pronostico que se consulta en el metodo clima._

* **Url**

  _http://dcdev.pythonanywhere.com/generar_

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
    ~$ wget -qO- http://dcdev.pythonanywhere.com/generar?dias=71
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
