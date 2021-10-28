from django.db import models

# Create your models here.
class Tblassets(models.Model):
    assettype = models.SmallIntegerField(db_column='assetType', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        if self.identifier == None:
            return str(self.firstname) + ' ' + str(self.lastname)
        else:
            return str(self.identifier)

    class Meta:
        managed = False
        db_table = 'tblassets'


class Tblbadges(models.Model):
    badgeid = models.IntegerField(db_column='badgeID', blank=True, null=True)  # Field name made lowercase.
    asset = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='asset', blank=True, null=True)
    lastbatterychange = models.DateTimeField(db_column='lastBatteryChange', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.badgeid) + ', ' + str(self.asset)
    class Meta:
        managed = False
        db_table = 'tblbadges'


class Tbllocationdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    nodeid = models.IntegerField(db_column='nodeID', blank=True, null=True)  # Field name made lowercase.
    badgeid = models.IntegerField(db_column='badgeID', blank=True, null=True)  # Field name made lowercase.
    stampedtime = models.DateTimeField(db_column='stampedTime', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        r = Tblnodes.objects.filter(nodeid=self.nodeid)
        a = Tblbadges.objects.filter(badgeid=self.badgeid)
        if len(a) > 0 and len(r) > 0:
            return str(a[0].asset) + ', Room ' + str(r[0].room) + ' on ' + str(self.stampedtime)
        else:
            return str(self.nodeid) + ',' + str(self.badgeid) + ',' + str(self.stampedtime)
    class Meta:
        managed = False
        db_table = 'tbllocationdata'


class Tblnodes(models.Model):
    nodeid = models.IntegerField(db_column='nodeID', unique=True, blank=True, null=True)  # Field name made lowercase.
    room = models.ForeignKey('Tblrooms', models.DO_NOTHING, db_column='room', blank=True, null=True)
    firingsequence = models.IntegerField(db_column='firingSequence', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.nodeid) + ', ' + str(self.room)
    class Meta:
        managed = False
        db_table = 'tblnodes'


class Tblrooms(models.Model):
    designator = models.CharField(max_length=255, blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.designator)

    class Meta:
        managed = False
        db_table = 'tblrooms'