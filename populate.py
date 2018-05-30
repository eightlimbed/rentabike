#!/usr/bin/python3

from models import *

# create states
s1 = State(name='Washington')
s1.save()

# create cities and link them to states
c1 = City(state_id=s1.id, name='Seattle')
c1.save()

# create users
u1 = User(email='michael@google.com', password='123',
          first_name='Michael', last_name='Jordan')
u1.save()

# create bikes
b1 = Bike(city_id=c1.id, user_id=u1.id,
          img_url='https://image.ibb.co/bPqpWT/fixed1.jpg',
          name='Harmonix Fixie',
          description='This fixed gear bike is a smooth ride. The lightweight \
                  carbon frame makes it easy to take off and get going.\
                  Excellent for cruising around Seattle!',
          price_per_day=35)
b1.save()

# create categories
cat1 = Category(name='Fixie')
cat1.save()

# link bike with categories
b1.categories.append(cat1)

storage.save()
print('OK')
