from django.core.management.base import BaseCommand, CommandError
from companydata.models import Company
from django.conf import settings
from pprint import pprint as pp
from termcolor import cprint
import csv
import os
os.system('color')
from tqdm import tqdm

class Command(BaseCommand):
    help = "Import data from CSV file to the database"

    def handle(self, *args, **options):
        
        cprint(f'\nProcessing CSV file, grab a beer!', 'green', attrs=['reverse'])

        num_lines = sum(1 for line in open('prhdata.csv'))
        with tqdm(total=num_lines) as pbar:
            with open('prhdata.csv', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                line_count = 0
                for row in csv_reader:
                    if line_count != 0:
                        Company.objects.create(name=row[0], business_id=row[1], company_form=row[2], business_line=row[3],
                                                registration_date=row[5], address=row[6], postcode=row[7], city=row[8])
                        line_count += 1
                        pbar.update(1)
                    else:
                        line_count += 1

        pbar.close()
        cprint(f'\nProcessed {line_count} lines :)', 'green', attrs=['reverse'])