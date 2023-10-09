from django.contrib.auth.models import AbstractUser
from django.db import models


# # Create your models here.
class scUser(AbstractUser):
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)
    community = models.CharField(max_length=100, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='scuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='scuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


CATEGORIES = [
    ('Tools', 'Tools'),
    ('Wedding', 'Wedding'),
    ('Baby', 'Baby'),
    ('Costumes', 'Costumes'),
    ('Electronics', 'Electronics'),
    ('Childrens', 'Childrens'),
    ('Sporting_Goods', 'Sporting Goods'),
    ('Books_and_Media', 'Books and Media'),
    ('Party_and_Event_Supplies', 'Party and Event Supplies'),
    ('Arts_and_Crafts', 'Arts and Crafts'),
    ('Outdoor_Gear', 'Outdoor Gear'),
    ('Musical_Instruments', 'Musical Instruments'),
    ('Other', 'Other'),
]

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORIES)
    itemowner = models.ForeignKey('scUser', related_name='items', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='items_photos', blank=True, null=True)
    active = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    loan_terms = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return f"{self.name}"
    
class Trade(models.Model):
    item = models.ForeignKey('Item', related_name='trades', on_delete=models.CASCADE)
    borrower = models.ForeignKey('scUser', related_name='trades', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    borrow_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    returned = models.BooleanField(default=False)
    return_notes = models.TextField(blank=True, null=True)
    photo_before = models.ImageField(upload_to='trade_photos', blank=True, null=True)
    photo_after = models.ImageField(upload_to='trade_photos', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

