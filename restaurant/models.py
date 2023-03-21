from django.db import models

class User(models.Model):
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Client(models.Model):
    name=models.CharField(max_length=30)
    card_number=models.CharField(max_length=20)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Worker(models.Model):
    name=models.CharField(max_length=20)
    position=models.CharField(max_length=30)
    user=models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name



class Ingredient(models.Model):
    name=models.CharField(max_length=30)
    extra_price=models.IntegerField()

    def __str__(self):
        return self.name


class Food(models.Model):
    name=models.CharField(max_length=20)
    start_price=models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    ingredient=models.ManyToManyField(Ingredient,related_name='orders')
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE)
    order_date_time=models.DateTimeField()

    def __str__(self):
        return f'{self.food} - {self.order_date_time}'

