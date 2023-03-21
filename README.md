# Password Generator / Generador de contraseñas

---

## English
This is a **random password generator** developed with **Python 3.10** and **PyQt6**.

### Directory Structure
- `main.py`: Main file to start the application.
- `gen_pass/`: Directory containing the password_generator.py module.
- `gen_pass/__init__.py`: Initialization file for the password_generator module.
- `gen_pass/password_generator.py`: Module for the random password generator.
- `ui/`: Directory containing the main_window.py module.
- `ui/__init__.py`: Initialization file for the main_window module.
- `ui/main_window.py`: Module for the graphical user interface.

- ### Usage
To run the application, simply run the main.py file with **Python 3.10**:

`python3.10 main.py`

The application will display a window with a field to enter the **_password length_** and a button to generate a **_random password_**. The generated password will be displayed in the window.

### Input validation
Basic validation has been added to ensure that the user enters a valid password length. The length must be a positive integer greater than or equal to 4 characters. If an invalid length is entered, a warning message will be displayed in the application.

### Credits
This project was developed by `Kenny Escalante`.

---

## Español
Este es un **generador de contraseñas aleatorias** desarrollado con **Python 3.10** y **PyQt6**.

### Estructura de archivos y directorios
- `main.py`: Archivo principal para iniciar la aplicación.
- `gen_pass/`: Directorio que contiene el módulo password_generator.py.
- `gen_pass/__init__.py`: Archivo de inicialización para el módulo password_generator.
- `gen_pass/password_generator.py`: Módulo para el generador de contraseñas aleatorias.
- `ui/`: Directorio que contiene el módulo main_window.py.
- `ui/__init__.py`: Archivo de inicialización para el módulo main_window.
- `ui/main_window.py`: Módulo para la interfaz gráfica de usuario.

### Uso
Para ejecutar la aplicación, simplemente ejecute el archivo main.py con **Python 3.10**:

`python3.10 main.py`

La aplicación mostrará una ventana con un campo para ingresar la **_longitud de la contraseña_** y un botón para generar una **_contraseña aleatoria_**. La contraseña generada se mostrará en la ventana.

### Validación de entrada
Se ha agregado una validación básica para asegurarse de que el usuario ingrese una longitud de contraseña válida. La longitud debe ser un número entero positivo mayor o igual a 4 caracteres. Si se ingresa una longitud no válida, se mostrará un mensaje de advertencia en la aplicación.

### Créditos
Este proyecto fue desarrollado por `Kenny Escalante`.
