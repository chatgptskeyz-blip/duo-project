"""
ПРОСТЕЙШИЙ СЕРВЕР НА FLASK
Автор: Егор
"""

# ========== ЧАСТЬ 1: ИМПОРТЫ ==========
# Пока не устанавливаем flask, просто пишем код
# Когда установишь flask - раскомментируй эти строки
# from flask import Flask, jsonify
# from flask_cors import CORS

# ========== ЧАСТЬ 2: ИМИТАЦИЯ FLASK ==========
# Создаём классы-заглушки чтобы код работал БЕЗ установки Flask

class FakeFlask:
    def __init__(self, name):
        self.name = name
        self.routes = {}
    
    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator
    
    def run(self, debug=True, port=5000):
        print(f"🚀 Сервер запущен на порту {port}")
        print("👉 Если бы Flask был установлен, сервер работал бы здесь:")
        print(f"   http://localhost:{port}")
        print("\n📡 Доступные маршруты:")
        for path in self.routes:
            print(f"   • http://localhost:{port}{path}")
        print("\n⏸️  Пока это имитация. Установи Flask для реальной работы.")

# Создаём фейковый Flask
app = FakeFlask(__name__)

# Фейковый jsonify
def jsonify(data):
    import json
    return json.dumps(data, indent=2, ensure_ascii=False)

# Фейковый CORS
class CORS:
    def __init__(self, app):
        pass

CORS(app)  # Просто для совместимости с кодом

# ========== ЧАСТЬ 3: НАШИ МАРШРУТЫ (ОСНОВНАЯ ЧАСТЬ) ==========

# Маршрут 1: Главная страница
@app.route('/')
def home():
    """Главная страница сервера"""
    return "👋 Привет! Я Егор, и это мой первый бэкенд-сервер!\n\n" \
           "📌 Используй эти маршруты:\n" \
           "   /api/hello - приветствие\n" \
           "   /api/about - информация о нас\n" \
           "   /api/team - наша команда\n" \
           "\n🚀 Чтобы сервер заработал, установи Flask командой:\n" \
           "   pip install flask flask-cors"

# Маршрут 2: Приветствие API
@app.route('/api/hello')
def say_hello():
    """API для получения приветствия"""
    response = {
        "message": "Привет от бэкенд-сервера!",
        "status": "success",
        "author": "Егор",
        "time": "сейчас",
        "instructions": "Это JSON ответ. Фронтенд (Артем) будет получать такие данные."
    }
    return jsonify(response)

# Маршрут 3: Информация о проекте
@app.route('/api/about')
def about_project():
    """Информация о нашем проекте"""
    project_info = {
        "project_name": "Duo Project",
        "description": "Совместный проект двух разработчиков",
        "backend": {
            "developer": "Егор",
            "tech": "Python Flask",
            "status": "в разработке"
        },
        "frontend": {
            "developer": "Артем",
            "tech": "HTML/CSS/JavaScript",
            "status": "в разработке"
        },
        "repository": "https://github.com/ваш-аккаунт/duo-project"
    }
    return jsonify(project_info)

# Маршрут 4: Команда проекта
@app.route('/api/team')
def team():
    """Список участников команды"""
    team_members = [
        {
            "id": 1,
            "name": "Егор",
            "role": "Бэкенд-разработчик",
            "responsibilities": [
                "Создание API",
                "Работа с базой данных",
                "Логика сервера"
            ],
            "skills": ["Python", "Flask", "Git", "SQL"]
        },
        {
            "id": 2,
            "name": "Артем",
            "role": "Фронтенд-разработчик",
            "responsibilities": [
                "Интерфейс пользователя",
                "Взаимодействие с API",
                "Адаптивный дизайн"
            ],
            "skills": ["HTML", "CSS", "JavaScript", "React"]
        }
    ]
    return jsonify(team_members)

# Маршрут 5: Тестовый POST запрос (для будущего)
@app.route('/api/test-post')
def test_post():
    """Пример для POST запросов"""
    return jsonify({
        "message": "Этот эндпоинт принимает POST запросы",
        "example_data": {
            "username": "Egor",
            "action": "create",
            "data": {"title": "Новая задача", "completed": False}
        },
        "note": "Артем будет отправлять сюда данные с фронтенда"
    })

# ========== ЧАСТЬ 4: ЗАПУСК СЕРВЕРА ==========
if __name__ == '__main__':
    print("=" * 50)
    print("🎯 БЭКЕНД ПРОЕКТ 'DUO PROJECT'")
    print("   Разработчик: Егор")
    print("=" * 50)
    
    # Пытаемся импортировать настоящий Flask
    try:
        # Если Flask установлен - используем его
        from flask import Flask, jsonify
        from flask_cors import CORS
        
        print("✅ Flask обнаружен! Запускаю реальный сервер...")
        
        # Пересоздаём app с настоящим Flask
        app = Flask(__name__)
        CORS(app)
        
        # Переопределяем маршруты для настоящего Flask
        # (код остаётся тот же, только теперь с настоящим Flask)
        
        @app.route('/')
        def home_real():
            return home()
        
        @app.route('/api/hello')
        def say_hello_real():
            return say_hello()
        
        @app.route('/api/about')
        def about_project_real():
            return about_project()
        
        @app.route('/api/team')
        def team_real():
            return team()
        
        @app.route('/api/test-post')
        def test_post_real():
            return test_post()
        
        # Запускаем настоящий сервер
        app.run(debug=True, port=5000, host='0.0.0.0')
        
    except ImportError:
        # Если Flask не установлен - используем фейковый
        print("⚠️  Flask не установлен. Запускаю режим имитации...")
        print("📦 Чтобы сервер заработал, установи Flask:")
        print("   pip install flask flask-cors")
        print("\n" + "=" * 50)
        
        # Запускаем фейковый сервер
        app.run(debug=True, port=5000)