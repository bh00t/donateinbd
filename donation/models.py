from django.db import models
from django.contrib.auth.models import User

# Create your models here.


ACCOUNT_TYPE_CHOICES=(
    ('Donor','Donor'),
    ('Donee','Donee'),
)
from django_countries.data import COUNTRIES

class UserProfile(models.Model):


    user = models.OneToOneField(User)

    # account_type = models.CharField(max_length=40,blank=True)

    contact_no = models.CharField(max_length=40, null=True, blank = True)
    street_no = models.CharField(max_length=40, null=True, blank = True)
    street_address = models.CharField(max_length=40, null=True, blank = True)
    city = models.CharField(max_length=40, null=True, blank = True)
    country = models.CharField(max_length=40, null=True, blank = True,choices=sorted(COUNTRIES.items(),key=lambda country:country[1]),default='Bangladesh')
    donor_donee_type = models.CharField(max_length=40, null=True, blank = True,choices=ACCOUNT_TYPE_CHOICES)

    # person_file = models.FileField(upload_to='%Y/%M/%D', blank = True)
    image = models.ImageField(upload_to="%Y/%M/%D",blank=True)
    occupation = models.CharField(max_length=40, null=True, blank = True)

    # org_identification_doc = models.FileField(upload_to='%Y/%M/%D', blank = True)

    description = models.CharField(max_length=40, null=True, blank = True)
    website = models.CharField(max_length=400, null=True, blank = True)

    donation_make_count = models.IntegerField(default=0)
    donation_take_count = models.IntegerField(default=0)


    def get_full_name(self):

        full_name = self.user.first_name + " " + self.user.last_name

        if len(full_name) == 1 :
            return self.user.username
        return full_name







POST_DONATION_TYPE = (
    ('money' , 'Money'),
    ('goods' , 'Goods'),
)

POST_TYPE = (
    ('make donation','Make donation'),
    ('take donation','Take donation'),
)

POST_SECTOR = (
    ('education',"Education"),
    ('medication','Medication'),
    ('relief','Relief'),
    ('employment','Employment'),
    ('innovative projects','Innovative projects'),
)

FEEDBACK_VERIFICATION = (
    ('verified','verified'),
    ('unverified','unverified'),

)

class Post(models.Model):

    user = models.ForeignKey(UserProfile)

    post_header = models.TextField()
    post_detail = models.TextField()
    post_date = models.DateField(auto_now=True)
    post_type = models.CharField(max_length=100,choices=POST_TYPE)
    post_amount = models.TextField()
    post_sector = models.CharField(max_length=100,choices=POST_SECTOR)
    post_donation_type = models.CharField(max_length=100,choices=POST_DONATION_TYPE)
    post_donation_method = models.CharField(max_length=100)
    post_rating = models.IntegerField(default=5)

class Message(models.Model):

    sender = models.ForeignKey(User)
    receiver = models.CharField(max_length=100, blank=True)
    sender_full_name = models.CharField(max_length=100,blank=True)
    content = models.TextField()
    event_time = models.TimeField(auto_now=True)
    file = models.FileField(upload_to='message/%Y/%M/%D', null=True)


class ProfileFeedback(models.Model):

    user = models.ForeignKey(User)
    message = models.TextField()
    feedback_sender = models.CharField(max_length=100)
    event_time = models.TimeField(auto_now=True)


class PostFeedback(models.Model):

    post = models.ForeignKey(Post)
    message = models.TextField()
    feedback_sender = models.CharField(max_length=100)
    event_time = models.TimeField(auto_now=True)
    verified = models.CharField(max_length=100,choices=FEEDBACK_VERIFICATION, default="unverified")


