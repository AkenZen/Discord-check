import requests
import time

def check_discord_tokens_from_file(file_path, output_path, delay):
    working_tokens = []

    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines()]

            for token in tokens:
                if not token:
                    continue

                headers = {
                    'Authorization': f'{token}'
                }

                try:
                    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)

                    if response.status_code == 200:
                        user_data = response.json()
                        print(f"Токен {token}: действителен. Информация о пользователе:")
                        print(f"Имя пользователя: {user_data['username']}#{user_data['discriminator']}")
                        print(f"ID пользователя: {user_data['id']}")
                        working_tokens.append(token)
                    else:
                        print(f"Токен {token}: Ошибка: {response.status_code}. Пожалуйста, проверьте токен.")

                except Exception as e:
                    print(f"Токен {token}: Произошла ошибка при отправке запроса: {e}")

                time.sleep(float(delay))  # Задержка в секундах

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    print("\nРабочие токены:")
    print("\n".join(working_tokens))

    # Запись
    try:
        with open(output_path, 'w') as output_file:
            output_file.write("\n".join(working_tokens))
        print(f"\nРабочие токены сохранены в файл: {output_path}")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")

if __name__ == "__main__":
    file_path = input("Введите полный путь к файлу с токенами (txt файл):\n")
    output_path = input("Введите полный путь к файлу для сохранения рабочих токенов (txt файл):\n")
    delay = input("Введите время задержки между запросами в секундах (0, если не нужна задержка):\n")
    check_discord_tokens_from_file(file_path, output_path, delay)
