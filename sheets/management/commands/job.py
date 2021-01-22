from django.core.management.base import BaseCommand, CommandError
from sheets.models import Deals, Commits
import sys
sys.stdout = open('file.txt', 'w')

class Command(BaseCommand):
  help = 'Testing Cron Jobs in Django'
  
  def handle(self, *args, **options):
    queryset_deals = Deals.objects.all()
    queryset_commits = Commits.objects.all()

    for d in queryset_deals:
      self.stdout.write(self.style.SUCCESS(d.id))

    self.stdout.write(self.style.SUCCESS('Successfully wrote deals'))

    for c in queryset_commits:
      self.stdout.write(self.style.SUCCESS(c.id))

    self.stdout.write(self.style.SUCCESS('Successfully wrote commits'))