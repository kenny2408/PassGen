def validate_password_length(length_str):
    if not length_str.isdigit():
        return 'La longitud de la contraseña debe ser un número entero positivo'

    length = int(length_str)
    if length < 4:
        return 'La longitud de la contraseña debe tener al menos 4 caracteres'

    return None
