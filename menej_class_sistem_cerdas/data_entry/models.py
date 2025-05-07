from django.db import models
from django import forms
from datetime import date

# Model Pengguna
class Pengguna(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address_1 = models.TextField()
    address_2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=20, help_text='Enter your city')
    state = models.TextField()
    zip_code = models.CharField(max_length=7)
    tanggal_join = models.DateField(auto_now=True)

    def __str__(self):
        return self.email  # Tampilkan email di dropdown dan admin

# Model Konten
class Content(models.Model):
    author = models.ForeignKey(Pengguna, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    set_view = models.BooleanField(default=False)
    article = models.TextField()

    def __str__(self):
        return f"Konten oleh {self.author.email}"  # Tampilkan email author di admin
