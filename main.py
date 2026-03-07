import webbrowser
import datetime
import random


def open_website(url):
    webbrowser.open(url)
    return "Открываю сайт"


def get_date():
    return datetime.datetime.now().strftime("%d.%m.%Y")


def search_google(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)
    return f"Ищу в Google: {query}"


def search_youtube(query):
    query = query.replace(" ", "+")
    url = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(url)
    return f"Ищу на YouTube: {query}"


def flip_coin():
    return random.choice(["Орёл", "Решка"])


# словарь команд
commands = {
    "как дела": lambda: "У меня всё отлично!",
    "открой гугл": lambda: open_website("https://www.google.com/"),
    "открой новости": lambda: open_website("https://tengrinews.kz/"),
    "открой ютуб": lambda: open_website("https://www.youtube.com/"),
    "включи музыку": lambda: open_website("https://open.spotify.com/"),
    "кино": lambda: open_website("https://kinogo.support/"),
    "какая сегодня дата": lambda: f"Сегодня: {get_date()}",
    "монетка": lambda: flip_coin(),
    "команды": lambda:(
    "Команды:\n"
    "1. как дела\n"
    "2. открой гугл\n"
    "3. открой новости\n"
    "4. открой ютуб\n"
    "5. включи музыку\n"
    "6. кино\n"
    "7. какая сегодня дата\n"
    "8. найти... (в гугл)\n"
    "9. найти... (в ютуб)\n"
    "10. монетка\n"
    "11. команды\n"
    "12. выход"
)
}


def respond(question):
    question = question.lower()

    if question.startswith("найди "):
        query = question.replace("найди ", "")
        return search_google(query)

    if question.startswith("ютуб "):
        query = question.replace("ютуб ", "")
        return search_youtube(query)


    for command in commands:
        if command in question:
            return commands[command]()

    return "Я не понимаю запрос."


if __name__ == "__main__":
    print("Mika запущен. Напишите 'выход' для завершения.\n"
          "Привет! чем могу помочь?")

    while True:
        user_input = input("Вы: ")

        if user_input.lower() == "выход":
            print("Mika выключена.")
            break

        response = respond(user_input)
        print("Mika:", response)