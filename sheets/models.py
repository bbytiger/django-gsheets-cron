from django.db import models

def get_deleted_deal():
  return Deals.objects.get_or_create(id="deleted")[0]

class Deals(models.Model):
  id = models.TextField(unique=True, primary_key=True)
  ItemDescription = models.TextField(null=True)
  ItemURL = models.TextField(null=True)
  Price = models.FloatField(null=True)
  PricePaying = models.FloatField(null=True)
  Comment = models.TextField(null=True)
  QTYPerOrder = models.IntegerField(null=True)
  QTYWanted = models.IntegerField(null=True)
  QTYCommitted = models.IntegerField(null=True)
  QTYRemaining = models.IntegerField(null=True)
  Filled = models.TextField(null=True)
  Completed = models.BooleanField(null=True)
  DateCreated = models.TextField(null=True)
  DateCompleted = models.TextField(null=True)

  class Meta:
    db_table = "deals"

class Commits(models.Model):
  id = models.TextField(unique=True, primary_key=True)
  CommittedDate = models.TextField(null=True)
  VendorEmail = models.TextField(null=True)
  VendorName = models.TextField(null=True)
  VendorPhone = models.TextField(null=True)
  Deal = models.ForeignKey(Deals, related_name="deal_commits", on_delete=models.SET(get_deleted_deal), null=True)
  ItemDescription = models.TextField(null=True)
  ItemURL = models.TextField(null=True)
  QTYCommitted = models.IntegerField(null=True)

  class Meta:
    db_table = "commits"

class CommitsLog(models.Model):
  id = models.TextField(unique=True, primary_key=True)
  RelatedCommit = models.ForeignKey(Commits, related_name="commit_history", on_delete=models.PROTECT, null=True)
  CommittedDate = models.TextField(null=True)
  VendorEmail = models.TextField(null=True)
  VendorName = models.TextField(null=True)
  VendorPhone = models.TextField(null=True)
  ItemDescription = models.TextField(null=True)
  ItemURL = models.TextField(null=True)
  QTYCommitted = models.IntegerField(null=True)
  
  class Meta:
    db_table = "commits_log"
