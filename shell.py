from restaurant.models import*

user1=User.objects.create(email='nikname21@gmail.com',password='defender42')
user2=User.objects.create(email='altywa1998@gmail.com',password='nono34')
client1=Client.objects.create(name='Azat',card_number='4147565798789009',user=user1)
worker1=Worker.objects.create(name='АлтынайАлиева',position='операторкассы',user=user2)
shawerma=Food.objects.create(name='шавурма',start_price=50)
hamburger=Food.objects.create(name='гамбургер',start_price=25)
chees=Ingredient.objects.create(name='сыр',extra_price=10)
chicken=Ingredient.objects.create(name='курица',extra_price=70)
meat=Ingredient.objects.create(name='говядина',extra_price=80)
salat=Ingredient.objects.create(name='салат',extra_price=15)
fri=Ingredient.objects.create(name='фри',extra_price=15)
order1=Order.objects.create(food=shawerma,client=client1,worker=worker1,order_date_time='2023-01-0114:02')

order1
order1.ingredient.set([chees,fri,salat])
order2=Order.objects.create(food=hamburger,worker=worker1,client=client1,order_date_time='2023-09-0106:45')

order2
order2.ingredient.set([chicken,salat])


order2.food.start_price
25
order1.food.start_price
50

order1.food.start_price+order2.food.start_price
75
