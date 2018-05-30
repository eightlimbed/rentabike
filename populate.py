#!/usr/bin/python3

from models import *

# States
California = '63b0cabe-f6ae-465d-b796-0d67de778659'
Oregon = 'b398346-f04b-4210-b5d1-87fc4a7977a0'

# Cities
Portland = '86a56ba5-7c97-413d-bc8a-f7f7adace335'
SF = 'a3c45ddb-4ce6-47c5-8e76-be8910beec5d'

# Users
Ronnie = '397d3642-f1aa-4317-96fa-78fb6f3730ba'
Michael = '69738e94-1e9e-4f0b-9b9b-4cc4393394bf'

# create categories
cat1 = Category(name='Fixed Gear')
cat1.save()
cat2 = Category(name='Cruiser')
cat2.save()
cat3 = Category(name='Road')
cat3.save()
cat4 = Category(name='Mountain')
cat4.save()


# create bikes
b1 = Bike(city_id=Portland, user_id=Ronnie,
          img_url='https://image.ibb.co/jdYg5y/parcour_s.jpg',
          name='Parcour Classic',
          description='This fixed gear bike is a smooth ride. The lightweight \
                  frame makes it easy to take off and get going.\
                  Excellent for cruising around Portland!',
          price_per_day=15)

b1.categories.append(cat1)
b1.save()

b2 = Bike(city_id=SF, user_id=Michael,
          img_url='https://image.ibb.co/iNdQXd/083d81e8b74ddc1d1739e15ad687edb7.jpg',
          name='Dayton Fixie with Water Guard',
          description='This is an excellent fixie with a rain guard over the \
                  back tire for those rainy San Francisco days. I provide \
                  helmets to anyone who rents one of my bikes!',
          price_per_day=20)
b2.categories.append(cat1)
b2.save()

b3 = Bike(city_id=SF, user_id=Michael,
        img_url='https://image.ibb.co/dk5uQy/scott_scale_jr_24_disc_2018_350x225.jpg',
          name='Scott Wildabeast-45XL Mountain Bike',
          description='This is a heavy-duty mountain bike that is suitable to \
          take on dirt hills. It is equipped with a sturdy, yet flexible \
          suspension system so you can catch some air and land smoothly.',
          price_per_day=10)
b3.categories.append(cat4)
b3.save()

b4 = Bike(city_id=Portland, user_id=Ronnie,
        img_url='https://image.ibb.co/gsDjsd/941f09ae757c540186b1ac72458bcef2.jpg',
          name='Vintage City Cruiser',
          description='Old-fashioned cruiser that has a European look and feel.\
          You\'ll be cruising around Portland and someone might stop you and say, "Nice bike!"',
          price_per_day=5)
b4.categories.append(cat2)
b4.save()

b5 = Bike(city_id=SF, user_id=Ronnie,
        img_url='https://image.ibb.co/f2b9Qy/610_rent_a_bike_netherlands_trek_5_2_ultgra.jpg',
          name='High Performance Trek RidgeMaster 6000',
          description='You will never lose a race when you\'re riding this baby.\
          This bike is nearly brand new and still has great traction. Speed past\
          the stiff San Francisco traffic and leave all your worries behind',
          price_per_day=40)
b5.categories.append(cat3)
b5.save()

b6 = Bike(city_id=SF, user_id=Michael,
        img_url='https://image.ibb.co/icyvyJ/65187.jpg',
          name='Specialized XRT-667',
          description='If you\'re looking for a high performance road bike to \
          battle the hills of SF, look no further! The Specialized XRT-667 is \
          one of the highest regarded road bikes on the market.',
          price_per_day=65)
b6.categories.append(cat3)
b6.save()

storage.save()
print('OK')
