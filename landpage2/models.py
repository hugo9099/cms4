from django.db import models

# Create your models here.


class LeadType(models.Model):
    type = models.IntegerField('Booberdoo Lead Type ID')
    name = models.CharField(max_length=50)
    specs = models.URLField(max_length=200, null=True)

    class Meta:
        ordering = ['type']

    def __unicode__(self):
        return '{} - {}'.format(self.type, self.name)


class LandPageVersion(models.Model):
    lpver = models.IntegerField('Landing Page Version', primary_key=True)
    name = models.CharField(max_length=50)
    # look = models.ImageField()
    description = models.TextField()
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.lpver, self.name)


class Campaign(models.Model):
    lead_type = models.ForeignKey(LeadType, related_name='campaigns')
    name = models.CharField(max_length=45, blank=True, null=True)
    creation_date = models.DateTimeField('Date Created', null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    LP_version = models.ForeignKey(LandPageVersion, help_text='Landing Page Version', default=1)
    default_src = models.CharField(max_length=45, blank=True, null=True)
    default_affref = models.CharField(max_length=45, blank=True, null=True)

    # phone number  fields
    phone_number = models.IntegerField('Phone Number', default=1)
    index_phone_header = models.BooleanField(default=1)
    index_phone_footer = models.BooleanField(default=1)
    form_phone_header = models.BooleanField(default=1)
    form_phone_footer = models.BooleanField(default=1)
    thankyou_phone_header = models.BooleanField(default=1)
    thankyou_phone_footer = models.BooleanField(default=1)

    # Questions in long form
    self_emp = models.BooleanField('Are You Self Employed', default=1)
    insured = models.BooleanField('', default=1)
    spouse = models.BooleanField(default=1)
    no_of_children = models.BooleanField(default=1)
    est_income = models.BooleanField(default=1)
    affordable = models.BooleanField(default=1)
    hospitalized = models.BooleanField(default=1)
    physician = models.BooleanField(default=1)
    prescription = models.BooleanField(default=1)
    previously_denied = models.BooleanField(default=1)
    ss_disabled = models.BooleanField(default=1)
    pregnant = models.BooleanField(default=1)
    health = models.BooleanField(default=1)
    household_size = models.BooleanField(default=1)
    expected_income = models.BooleanField(default=1)
    click_agree_terms_cond = models.BooleanField(default=1)
    affil_contact = models.BooleanField(default=1)

    def __str__(self):
        return self.name




