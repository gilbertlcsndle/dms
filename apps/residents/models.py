from django.db import models

class Resident(models.Model):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    CIVIL_STATUS_CHOICES = (
        ('s', 'Single'),
        ('m', 'Married'),
        ('w', 'Widowed'),
        ('se', 'Separated'),
        ('d', 'Divorced'),
    )
    EDUC_ATTAIN_CHOICES = (
        ('col', 'College'),
        ('hs', 'High school'),
        ('elem', 'Elementary'),
    )
    STATUS_CHOICES = (
        ('act', 'Active'),
        ('dec', 'Decease'),
        ('tr', 'Transferred'),
    )

    # personal
    photo = models.ImageField(blank=True, upload_to='residents/')
    fname = models.CharField(verbose_name='first name', max_length=50)
    mname = models.CharField(verbose_name='middle name', max_length=50)
    lname = models.CharField(verbose_name='last name', max_length=50)
    bdate = models.DateField(verbose_name='date of birth')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')
    spouse = models.ForeignKey('self', blank=True, null=True)
    children = models.IntegerField(blank=True, default=0)
    civil_status = models.CharField(default='', max_length=50, choices=CIVIL_STATUS_CHOICES)
    occupation = models.CharField(blank=True, max_length=50)
    educational_attainment = models.CharField(
        null = True,
        max_length = 50,
        choices = EDUC_ATTAIN_CHOICES,
        default=''
    )
    status = models.CharField(
        choices = STATUS_CHOICES, 
        max_length = 50, 
        default = 'act'
    )

    # contact
    address = models.CharField(max_length=50, default='Dili, Bauang La Union')
    phone_number = models.CharField(blank=True, max_length=50)

    # household
    common_garbage_disposal = models.CharField(blank=True, max_length=50)
    source_of_water_supply = models.CharField(blank=True, max_length=50)
    toilet_type = models.CharField(blank=True, max_length=50)
    common_agri_products = models.CharField(
        verbose_name = 'common agri-products', 
        blank = True, 
        max_length = 50
    )
    kinds_of_animals = models.CharField(blank=True, max_length=50)
    type_of_dwelling_unit = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return '{0}, {1} {2}'.format(self.lname, self.fname, self.mname)