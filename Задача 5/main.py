def password_level(password, confirm_password):
  while True:
      # Проверка совпадения пароля и подтверждения пароля
      if password != confirm_password:
          return "Пароль и подтверждение пароля не совпадают"

      # Проверка длины пароля
      if len(password) <= 7:
          return "Недопустимый пароль\n"
      # Проверка наличия букв
      has_letters = any(c.islower() for c in password) or any(c.isupper() for c in password)
    
      # Проверка наличия букв разного регистра
      has_upper_and_lower = any(c.islower() for c in password) and any(c.isupper() for c in password)

      # Проверка наличия цифр
      has_digits = any(c.isdigit() for c in password)

      # Проверка требований
      if has_upper_and_lower and has_digits:
          return "Надежный пароль"
      elif has_upper_and_lower or has_letters and has_digits:
          return "Слабый пароль\n"
      else:
          return "Ненадежный пароль\n"

# Пример использования
while True:
  user_password = input("Введите пароль: ")
  confirm_password = input("Подтвердите пароль: ")

  result = password_level(user_password, confirm_password)
  print(result)

  if result == "Надежный пароль":
      break
