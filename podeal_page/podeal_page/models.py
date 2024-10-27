from django.db import models

class Locations(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    location_name = models.CharField(max_length=255)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'

    def __str__(self):
        return f'{self.location_name} (User: {self.user})'


class Referrals(models.Model):
    user = models.OneToOneField('User', models.CASCADE, primary_key=True)
    invited_user = models.ForeignKey('User', models.CASCADE, db_column='invited_user', related_name='referrals_invited_user_set')
    score_for_invite = models.IntegerField(blank=True, null=True)
    is_accepted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referrals'

    def __str__(self):
        return f'Referral from {self.user} to {self.invited_user}'


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'team'

    def __str__(self):
        return self.team_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_surname = models.CharField(max_length=255, blank=True, null=True)
    team = models.ForeignKey(Team, models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    custom_id = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return f'{self.user_name} {self.user_surname} (Role: {self.role})'


class UserAdditionalInfo(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    course = models.IntegerField()
    specialty = models.CharField(max_length=255)
    english_level = models.CharField(max_length=50, blank=True, null=True)
    another_language_level = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_additional_info'

    def __str__(self):
        return f'{self.user} - {self.specialty}'
