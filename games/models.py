from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



from django.db import models

class GameDeveloper(models.Model):
    name = models.CharField(max_length=255)
    founded_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



from django.db import models

class Platform(models.TextChoices):
    PC = 'pc', 'PC'
    PLAYSTATION = 'playstation', 'PlayStation'
    XBOX = 'xbox', 'Xbox'
    NINTENDO = 'nintendo', 'Nintendo'
    MAC = 'mac', 'Mac'
    LINUX = 'linux', 'Linux'
    ANDROID = 'android', 'Android'
    IOS = 'ios', 'iOS'
    WEB = 'web', 'Web'



class Game(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField()
    description = models.TextField()
    platform = models.CharField(max_length=20, choices=Platform.choices)

    def __str__(self):
        return self.title



class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.game.title} - {self.user.username}"




