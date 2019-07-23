import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

from blog.models import Post
from faker import Faker

from django.utils import timezone
fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        
        #fake_name = fakegen.name().split()
        #fake_lastname = fake_name[1]
        #fake_firstname = fake_name[0]
        #fake_email = fakegen.email()
        #user = User.objects.get_or_create(first_name=fake_firstname,
        #        last_name=fake_lastname,
        #        email=fake_email)

        fake_user = fakegen.name().split()[1]
        fake_text = fakegen.text()
        fake_title = fakegen.text()[:30]
        fake_date= fakegen.date()

        post = Post.objects.get_or_create(author=fake_user, text=fake_text, title=fake_title, published_date=fake_date)

if __name__  == '__main__':
    print("Populationg database")
    populate(5)
    print("Complete")
