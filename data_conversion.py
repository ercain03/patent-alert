import django
django.setup()
# from drugs.models import Drug
from drugs.models import Drug
# file_path = open('sample_dict.txt', 'r')


def conversion():
    """Convert from JSON into database."""
    with open('sample_dict.txt', 'r') as sample_file:
        lst = eval(sample_file.read())
        for data in lst:
            print(data)
            dmodel = Drug(**data)
            dmodel.save()

if __name__ == '__main__':
    conversion()
