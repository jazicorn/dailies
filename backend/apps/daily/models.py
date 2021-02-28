from django.db import models

# Resources
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models

# To-do List
class Daily(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(max_length = 200, blank=True, null=True)
    completed = models.BooleanField(default=False)
    # slug = models.SlugField(unique=True, max_length=255)
    
    # list dailies by date created
    class Meta:
        ordering = ['created', 'modified']

    # get url for list
    # def get_absolute_url(self):
    #    return reverse('daily_detail_view', args=[self.slug])

    # save when updated tite of list
    # def save(self, *args, **kwargs):
    #    if not self.slug:
    #        self.slug = slugify(self.title)
    #    super(Post, self).save(*args, **kwargs)


    def __str__(self): 
        return self.title

# User Profile
# class Profile(models.Model):
#    id = models.BigAutoField(primary_key=True)
    
