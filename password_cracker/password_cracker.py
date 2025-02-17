import itertools
import string
import math

# Функция для расчета времени и энтропии
# Function to calculate time and entropy
def calculate_time_and_entropy(password, charset):
    # Длина пароля / Password length
    password_length = len(password)
    
    # Количество возможных комбинаций / Number of possible combinations
    total_combinations = len(charset) ** password_length
    
    # Предположим, что система может проверять 1 миллион комбинаций в секунду
    # Assume the system can check 1 million combinations per second
    combinations_per_second = 1_000_000
    
    # Время в секундах / Time in seconds
    time_seconds = total_combinations / combinations_per_second
    
    # Преобразуем время в тысячелетия, века, годы, месяцы, дни, часы, минуты и секунды
    # Convert time to millennia, centuries, years, months, days, hours, minutes, and seconds
    millennia = time_seconds // (1000 * 365 * 24 * 3600)
    time_seconds %= (1000 * 365 * 24 * 3600)
    centuries = time_seconds // (100 * 365 * 24 * 3600)
    time_seconds %= (100 * 365 * 24 * 3600)
    years = time_seconds // (365 * 24 * 3600)
    time_seconds %= (365 * 24 * 3600)
    months = time_seconds // (30 * 24 * 3600)
    time_seconds %= (30 * 24 * 3600)
    days = time_seconds // (24 * 3600)
    time_seconds %= (24 * 3600)
    hours = time_seconds // 3600
    time_seconds %= 3600
    minutes = time_seconds // 60
    seconds = time_seconds % 60
    
    # Расчет энтропии в битах / Calculate entropy in bits
    entropy_bits = math.log2(total_combinations)
    
    return int(millennia), int(centuries), int(years), int(months), int(days), int(hours), int(minutes), int(seconds), entropy_bits

# Функция для определения набора символов на основе пароля
# Function to determine the character set based on the password
def get_charset_from_password(password):
    charset = set()
    for char in password:
        if char in string.ascii_lowercase:
            charset.update(string.ascii_lowercase)
        if char in string.ascii_uppercase:
            charset.update(string.ascii_uppercase)
        if char in string.digits:
            charset.update(string.digits)
        if char in string.punctuation:
            charset.update(string.punctuation)
    return ''.join(sorted(charset))

# Основная функция / Main function
def main():
    # Выбор языка / Language selection
    print("Выберите язык / Select language:")
    print("1. Русский / Russian")
    print("2. English")
    language_choice = input("Введите номер / Enter the number: ")

    # Устанавливаем тексты в зависимости от выбора языка
    # Set texts based on language choice
    if language_choice == '1':
        # Русский язык / Russian language
        mode_prompt = "Выберите режим:"
        mode_option1 = "1. Оценить время для пароля заданной длины и сложности"
        mode_option2 = "2. Оценить время для введенного пароля"
        length_prompt = "Введите длину пароля:"
        lowercase_prompt = "Использовать строчные буквы? (y/n):"
        uppercase_prompt = "Использовать заглавные буквы? (y/n):"
        digits_prompt = "Использовать цифры? (y/n):"
        special_prompt = "Использовать специальные символы? (y/n):"
        password_prompt = "Введите пароль для проверки:"
        no_charset_message = "Не выбран ни один набор символов!"
        no_password_message = "Пароль не содержит символов, которые можно использовать для перебора!"
        result_message = "Время на расшифровку пароля: {} тысячелетий, {} веков, {} лет, {} месяцев, {} дней, {} часов, {} минут, {} секунд"
        entropy_message = "Энтропия пароля: {:.2f} бит"
        invalid_choice_message = "Неверный выбор. Пожалуйста, выберите 1 или 2."
    elif language_choice == '2':
        # Английский язык / English language
        mode_prompt = "Select mode:"
        mode_option1 = "1. Estimate time for a password of given length and complexity"
        mode_option2 = "2. Estimate time for an entered password"
        length_prompt = "Enter password length:"
        lowercase_prompt = "Use lowercase letters? (y/n):"
        uppercase_prompt = "Use uppercase letters? (y/n):"
        digits_prompt = "Use digits? (y/n):"
        special_prompt = "Use special characters? (y/n):"
        password_prompt = "Enter password to check:"
        no_charset_message = "No character set selected!"
        no_password_message = "The password does not contain any characters that can be used for brute force!"
        result_message = "Time to crack the password: {} millennia, {} centuries, {} years, {} months, {} days, {} hours, {} minutes, {} seconds"
        entropy_message = "Password entropy: {:.2f} bits"
        invalid_choice_message = "Invalid choice. Please select 1 or 2."
    else:
        print("Неверный выбор языка / Invalid language choice.")
        return

    print(mode_prompt)
    print(mode_option1)
    print(mode_option2)
    choice = input("Введите номер / Enter the number: ")
    
    if choice == '1':
        # Режим 1: Оценка времени для пароля заданной длины и сложности
        # Mode 1: Estimate time for a password of given length and complexity
        password_length = int(input(length_prompt))
        use_lowercase = input(lowercase_prompt).lower() == 'y'
        use_uppercase = input(uppercase_prompt).lower() == 'y'
        use_digits = input(digits_prompt).lower() == 'y'
        use_special = input(special_prompt).lower() == 'y'
        
        # Формирование набора символов / Forming the character set
        charset = ''
        if use_lowercase:
            charset += string.ascii_lowercase
        if use_uppercase:
            charset += string.ascii_uppercase
        if use_digits:
            charset += string.digits
        if use_special:
            charset += string.punctuation
        
        if not charset:
            print(no_charset_message)
            return
        
        # Расчет времени и энтропии / Calculate time and entropy
        millennia, centuries, years, months, days, hours, minutes, seconds, entropy_bits = calculate_time_and_entropy('a' * password_length, charset)
        
        # Вывод результата / Output the result
        print(result_message.format(millennia, centuries, years, months, days, hours, minutes, seconds))
        print(entropy_message.format(entropy_bits))
    
    elif choice == '2':
        # Режим 2: Оценка времени для введенного пароля
        # Mode 2: Estimate time for an entered password
        password = input(password_prompt)
        
        # Определяем набор символов на основе пароля / Determine the character set based on the password
        charset = get_charset_from_password(password)
        
        if not charset:
            print(no_password_message)
            return
        
        # Расчет времени и энтропии / Calculate time and entropy
        millennia, centuries, years, months, days, hours, minutes, seconds, entropy_bits = calculate_time_and_entropy(password, charset)
        
        # Вывод результата / Output the result
        print(result_message.format(millennia, centuries, years, months, days, hours, minutes, seconds))
        print(entropy_message.format(entropy_bits))
    
    else:
        print(invalid_choice_message)

if __name__ == "__main__":
    main()
