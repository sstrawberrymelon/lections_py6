# Написать платформу для прослушивания музыки
# 1) Класс Пользователь с юзернеймом, возраст, эл. почтой и подпиской(по дефолту - Без подписки,
# если подписка не оформлена, то с каждым прослушиванием появялется реклама, спам), 
# плейлист(по дефолту - пустой список). Можно дополнительно еще пароль сделать, 
# с валидацией, вся информация должна быть приватной.
# Нужно провалидировать все данные(почту на наличие @, пароль, возраст)
# - Метод для оформления подписки, для добавления в пейлист песни, 
# - метод для прослушивания песни, 
# - метод который прослушивает весь плейлист по очередно
# 2) Класс жанр в названием
# 3) Класс музыка с названием, автором, жанром, длительностью
# 4) Класс работник, который наследуется от Пользователя, но у него есть доп 
# атрибут - роль (например админ), и платформа где он работает
# 5) Класс платформа для прослушивания музыки, например - Spotify, у 
# которого должны быть списки песен, жанры, список пользователей с полпиской и без
# - методы для  просмотра всех песен,
# - методы для просмотра песен по определенному жанру,
# - метод для оформления подписки у пользователя, если
# - метод для поиска песни по названию
# - метод для добавления определенной песни в плейлист пользователя
# - метод удаления, добавления песни, жанра из списка Платформы, которую может сделать 
# только админ этой платформы
# - метод блокировки, удаления пользователя, если это потребуется
class User: 
    subsc = 'no'
    def __init__(self, user, age, email ,password) -> None:
        if self.set_user(user):
            self.user = user 
        if self.set_age(age):
            self.age = age 
        if self.set_email(email):
            self.email = email 
        if self.set_password(password):
            self.__password = password 
        self.subsc = False
        self.playlist = []
        
    def __str__(self) -> str:
        return f'User:{self.user}\nAge:{self.age}\nEmail:{self.email}'

           
    def set_user(self, user): 
            if not isinstance(user, str): 
                print('Name must be str object!')
            else:
                self.__user = user

    
    def set_age(self, age): 
            if not isinstance(age, int) or not 0 <=age < 150:  
                print('Invalid value for age!')
            else:
                self.__age = age 


    from string import ascii_letters, digits
    symbols = '!@#$%^&*()_-+=<>?/,. '
    def set_password(self, password): 
        if len(password) in range(8, 16) and [i for i in password if i in self.symbols] and [i for i in password if i in self.ascii_letters] and [i for i in password if i in self.digits]:
                print('Ваш пароль успешен') 
                return True
        else: 
                raise ValueError('Неправильный пароль')


    def set_email(self,email): 
    
        for i in email: 
            if i == '@':
                print('Почта принята!')
                return True
        raise ValueError('Неправильная почта')
                
                

    

    
         
class Genre:
    def __init__(self, name) -> None:
          self.name = name 
        
    def __repr__(self) -> str:
        return f'Жанр:{self.name}'
    
class Music:
    def __init__(self, name, author, genre ,duration ) -> None:
          self.name = name 
          self.author = author 
          self.genre = genre 
          self.duration = duration 
    def __repr__(self) -> str:
        return f'Song name:{self.name},Author:{self.author},Genre:{self.genre},Duration:{self.duration}'
    

class Worker(User): 
    def __init__(self, user, age, email, password,role, platform ) -> None:
          super().__init__(user, age, email, password)
          self.role = role 
          self.platform = platform 
    def __repr__(self) -> str:
        return f'User:{self.user}\nAge:{self.age}\nEmail:{self.email}\nRole:{self.role}\nPlatform:{self.platform}'
    
class Platform:
    def __init__(self,name, playlist , genre, userlist_sub=[], userlist_nosub=[]) -> None:
        self.name = name
        self.playlist = playlist
        self.genre = [genre]
        self.userlist_nosub = userlist_nosub
        self.userlist_sub = userlist_sub
    
    def platfrom_music(self): 
        for i in self.playlist:
            print(i.name)

    def platfrom_genre(self): 
        for i in self.genre:
              print(i.name)
        

    def subscription(self):
        self.subsc = True 
        return 'Подписка оформлена!Теперь вы можете добавлять вашу любимую музыку в плейлист!'
    
    def add_music_to_playlist(self, music, user): 
        if user.subsc == True:
            user.playlist.append(music)
            print(f'Ваша песня {music} добавлена в vash плейлист')

    def find_song(self,fname):
        self.fname = fname
        for i in self.playlist: 
            if fname in i.name:
                print(fname)


    def listen_music(self, music ): 
        self.music = music 
        print(f'Прослушиваем {music.name}')

    def listen_to_playlist(self):
        
        for i in self.playlist:
            print(f'Прослушиваем:{i}...')


    def delete_song(self, song):
        if Worker.role == 'admin': 
            for i in self.playlist: 
                if i == song: 
                     self.playlist.remove(song)

        return f'{song} deleted!'
    
    def delete_genre(self, genre): 
        if Worker.role == 'admin': 
            for i in self.genre: 
                if i == genre: 
                     self.genre.remove(genre)
        

        
                
              
user = User('lemon',12, 'lemon12@gmial.com','@lemon121212')
user2 = Worker('apple',13, 'admin@gmail.com', 'sdfdsfWdf!21', 'admin','Spotify')

user.set_user('lemon')
user.set_age(12)
user.set_email('lemon12@gmial.com')
user.set_password('@lemon121212')

genre = Genre('R&B')
genre2 = Genre('Hip Hop')

music1 = Music('Mic Drop','BTS','HipHop','3:34')
music2 = Music('AirPlane pt.2','BTS','Latino','4:12')
music3 = Music('Black Swan','BTS','Classic','2:34')

print(music1)
print(music2)
print(music3)



spotify = Platform('Spotify',[music3, music2, music1],genre,user2,user)

spotify.add_music_to_playlist(music1, user)
spotify.add_music_to_playlist(music2, user)
spotify.add_music_to_playlist(music3, user)

spotify.platfrom_music()
spotify.platfrom_genre()
spotify.subscription()
spotify.find_song('Black Swan')
spotify.listen_music(music2)
spotify.listen_to_playlist()








         
        

                
    
              


    
    
          

    