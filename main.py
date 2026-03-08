import webbrowser
import datetime
import random
import time


# хранилища данных
reminders = {}
diary = {}

SECRET_PASSWORD = "1234"


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

# сохраниение Напоминаний
def add_reminder(date_time, text):

    with open("reminders.txt", "a", encoding="utf-8") as file:
        file.write(f"{date_time} | {text}\n")

    return "Напоминание сохранено"


def list_reminders():

    try:
        with open("reminders.txt", "r", encoding="utf-8") as file:
            data = file.read()

        if data == "":
            return "Напоминаний нет"

        return "Список напоминаний:\n" + data

    except FileNotFoundError:
        return "Файл напоминаний ещё не создан."



def check_reminders():

    try:
        with open("reminders.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

        for line in lines:
            if "|" in line:
                date, text = line.strip().split(" | ")

                if date == now:
                    print("🔔 НАПОМИНАНИЕ:", text)

    except FileNotFoundError:
        pass


def add_diary(date, text):

    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(f"{date} | {text}\n")

    return "Запись сохранена"


def get_diary(date):

    try:
        with open("diary.txt", "r", encoding="utf-8") as file:

            for line in file:
                if date in line:
                    return line

        return "Записей на эту дату нет"

    except FileNotFoundError:
        return "Дневник пока пуст."


# словарь команд
commands = {
    "как дела": lambda: "У меня всё отлично!",
    "открой гугл": lambda: open_website("https://www.google.com/"),
    "нейросети": lambda: open_website("https://chat.openai.com/"),
    "открой новости": lambda: open_website("https://tengrinews.kz/"),
    "открой ютуб": lambda: open_website("https://www.youtube.com/"),
    "открой твич": lambda: open_website("https://www.twitch.tv/"),
    "открой гитхаб": lambda: open_website("https://github.com/"),
    "включи музыку": lambda: open_website("https://open.spotify.com/"),
    "кино": lambda: open_website("https://kinogo.support/"),
    "какая сегодня дата": lambda: f"Сегодня: {get_date()}",
    "монетка": lambda: flip_coin(),
    "список напоминаний": lambda: list_reminders(),
    "команды": lambda:(
    "Команды:\n"
    "1. как дела\n"
    "2. открой гугл\n"
    "3. нейросети\n"
    "4. открой новости\n"
    "5. открой ютуб\n"
    "6. открой твич\n"
    "7. открой гитхаб\n"
    "8. включи музыку\n"
    "9. кино\n"
    "10. какая сегодня дата\n"
    "11. найти... (в гугл)\n"
    "12. найти... (в ютуб)\n"
    "13. монетка\n"
    "14. напомни\n"
    "15. список напоминаний\n"
    "16. дневник\n"
    "17. что я делал\n"
    "18. особо засекречено\n"
    "19. команды\n"
    "20. выход"
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

    # добавление напоминания
    if question == "напомни":
        date = input("Введите дату и время (дд.мм.гггг чч:мм): ")
        text = input("Что напомнить: ")

        add_reminder(date, text)
        return "Напоминание сохранено"

    # дневник
    if question == "дневник":
        date = input("Введите дату: ")
        text = input("Что вы делали: ")

        return add_diary(date, text)

    # просмотр дневника
    if question == "что я делал":
        date = input("Введите дату: ")
        return get_diary(date)

    # секретная команда
    if question == "особо засекречено":

        password = input("Введите пароль: ")

        if password == SECRET_PASSWORD:
            return "Доступ разрешён. Добро пожаловать в секретный раздел."
        else:
            return "Неверный пароль."

    for command in commands:
        if command in question:
            return commands[command]()

    return "Я не понимаю запрос."


if __name__ == "__main__":
    print("Mika запущен. Напишите 'выход' для завершения.\n"
          "Напишите 'команды' чтобы увидеть список")

    while True:
        check_reminders()

        user_input = input("Вы: ")

        if user_input.lower() == "выход":
            print("Mika выключена.")
            break

        response = respond(user_input)
        print("Mika:", response)