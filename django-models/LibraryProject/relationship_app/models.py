from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max)
    
    def __str__(self):
        return self.name

#books models here 
class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")
    
    def __str__(self):
        return self.title

#create the library model
class Library(models.Model):
    name= models.CharField(max_length=250)
    books = models.ManyToManyField(Book,related_name="libraries")
    
    def __str__(self):
        return self.name
#create the librarian model

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library,on_delete=models.CASCADE,related_name="librarian")
    
    def __str__(self):
        return self.name