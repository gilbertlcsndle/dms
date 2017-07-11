import os

from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='files/')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return os.path.basename(self.file.name)
    
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.file.path):
            os.remove(self.file.path)

        super(File, self).delete(*args, **kwargs)