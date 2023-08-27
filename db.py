import sqlite3
from random import randint

def create():
    '''Создает базу данных и таблицу
    questions где будут храниться все вопросы и ответы
    на приложение "викторина"'''
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        surname VARCHAR,
        number_phone VARCHAR)''')
    conn.commit()
    cursor.close()
    conn.close()

def insert_db():
    '''Вставляет вопросы в базу данных'''
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    questions = [
        ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
        ('Каким станет зелёный утёс, если упадёт в Красное море?', 'Мокрым', 'Красным', 'Не изменится', 'Фиолетовым'),
        ('Какой рукой лучше размешивать чай?', 'Ложкой', 'Правой', 'Левой', 'Любой'),
        ('Что не имеет длины, глубины, ширины, высоты, а можно измерить?', 'Время', 'Глупость', 'Море', 'Воздух'),
        ('Когда сетью можно вытянуть воду?', 'Когда вода замёрзла', 'Когда нет рыбы', 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Парашют', 'Облако')
    ]
    cursor.executemany('''INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', questions)
    conn.commit()
    cursor.close()
    conn.close()

def clear_db():
    '''Удаляет таблицу из базы данных'''
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS questions''')
    cursor.execute('''DROP TABLE IF EXISTS contacts''')
    conn.commit()
    cursor.close()
    conn.close()

def get_random_question():
    '''Функция возвращает 1 случайное поле
    с вопросом, ответом и 3 неправильных ответа'''
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM questions''')
    all_data = cursor.fetchall()
    result = all_data[randint(0, len(all_data)-1)]
    conn.commit()
    cursor.close()
    conn.close()
    return result

def is_correct_answer(id, answer):
    '''
    Принимает ID вопроса и ответ пользователя
    Возвращает True если правильный, False если
    неправильный.
    '''
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT answer FROM questions WHERE id == ?''', [id])
    ans = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    if answer == ans[0]:
        return True
    else:
        return False

def insert_contact(name, phone):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO contacts (surname, number_phone) VALUES (?, ?)''', [name, phone])
    conn.commit()
    cursor.close()
    conn.close()