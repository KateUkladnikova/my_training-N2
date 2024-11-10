# Дополнительное практическое задание по модулю: "Классы и объекты."
# Задание "Свой YouTube"
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео,
# авторизации и регистрации пользователя и т.д.

from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.logged_in = False
        self.current_user = None
    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.logged_in = True
                self.current_user = user
                break
            return self.current_user
    def register(self, nickname, password, age):
        is_exist = False
        i = 0
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                is_exist = True
                break
            elif nickname == user.nickname and hash(password) != user.password:
                print(f"Пользователь {nickname} уже существует")
                i = 1
                break
        if not is_exist:
            self.users.append(User(nickname, password, age))
            if i != 1:
                self.current_user = User(nickname, password, age)
    def log_out(self):
        self.current_user = None
    def add(self, *args):
        for video in args:
            if isinstance(video, Video) and self.videos.__contains__(video):
                continue
            else:
                self.videos.append({'title': video.title})
    def get_videos(self, poiskovoe_slovo):
        spisok_nazvaniy_videos_so_slovom = [video['title'] for video in self.videos if poiskovoe_slovo.lower() in video['title'].lower()]
        return spisok_nazvaniy_videos_so_slovom
    def watch_video(self, video_title):
        # if not self.logged_in:
        if not self.users:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        if self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            self.current_video = None
            return
        for i in range(0,len(self.videos)):
            if video_title in list(self.videos[i].values())[0]:
                print(f"Начало воспроизведения видео: {video_title}")
                for second in range(1, 11):
                    print(f"Секунда воспроизведения: {second}")
                    sleep(1)
                print("Конец видео")
                self.current_video = None

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
