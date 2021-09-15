import csv
import os
import sys

import django

sys.path.append('D:/Dev/api_yamdb/api_yamdb')
os.environ['DJANGO_SETTINGS_MODULE'] = 'api_yamdb.api_yamdb.settings'
django.setup()

from users.models import User
from reviews.models import Review, Title, Category, Genre, Comment, TitleGenre

with open('D:/Dev/api_yamdb/api_yamdb/static/data/users.csv', newline='',
          encoding='utf-8') as csv_file:
    table = csv.reader(csv_file, delimiter=',')
    obj_list = []
    for row in table:
        if row[0] != 'id':
            obj = User(
                id=row[0],
                username=row[1],
                email=row[2],
                role=row[3],
                bio=row[4],
                first_name=row[5],
                last_name=row[6]
            )
            obj_list.append(obj)
    User.objects.bulk_create(obj_list)

with open('D:/Dev/api_yamdb/api_yamdb/static/data/category.csv', newline='',
          encoding='utf-8') as csv_file:
    table = csv.reader(csv_file, delimiter=',')
    obj_list = []
    for row in table:
        if row[0] != 'id':
            obj = Category(
                id=row[0],
                name=row[1],
                slug=row[2]
            )
            obj_list.append(obj)
    Category.objects.bulk_create(obj_list)

with open('D:/Dev/api_yamdb/api_yamdb/static/data/titles.csv', newline='',
          encoding='utf-8') as csv_file:
    table = csv.reader(csv_file, delimiter=',')
    obj_list = []
    for row in table:
        if row[0] != 'id':
            obj = Title(
                id=row[0],
                name=row[1],
                year=row[2],
                category_id=row[3]
            )
            obj_list.append(obj)
    Title.objects.bulk_create(obj_list)

with open('D:/Dev/api_yamdb/api_yamdb/static/data/genre.csv', newline='',
          encoding='utf-8') as csv_file:
    table = csv.reader(csv_file, delimiter=',')
    obj_list = []
    for row in table:
        if row[0] != 'id':
            obj = Genre(
                id=row[0],
                name=row[1],
                slug=row[2]
            )
            obj_list.append(obj)
    Genre.objects.bulk_create(obj_list)

with open('D:/Dev/api_yamdb/api_yamdb/static/data/genre_title.csv', newline='',
          encoding='utf-8') as csv_file:
    table = csv.reader(csv_file, delimiter=',')
    obj_list = []
    for row in table:
        if row[0] != 'id':
            obj = TitleGenre(
                id=row[0],
                title_id=row[1],
                genre_id=row[2]
            )
            obj_list.append(obj)
    TitleGenre.objects.bulk_create(obj_list)

with open('D:/Dev/api_yamdb/api_yamdb/static/data/review.csv', newline='',
          encoding='utf-8') as csv_file:
    table = csv.reader(csv_file, delimiter=',')
    obj_list = []
    for row in table:
        if row[0] != 'id':
            obj = Review(
                id=row[0],
                title_id=row[1],
                text=row[2],
                author_id=row[3],
                score=row[4],
                pub_date=row[5]
            )
            obj_list.append(obj)
    Review.objects.bulk_create(obj_list)

with open('D:/Dev/api_yamdb/api_yamdb/static/data/comments.csv', newline='',
          encoding='utf-8') as csv_file:
    table = csv.reader(csv_file, delimiter=',')
    obj_list = []
    for row in table:
        if row[0] != 'id':
            obj = Comment(
                id=row[0],
                review_id=row[1],
                text=row[2],
                author_id=row[3],
                pub_date=row[4]
            )
            obj_list.append(obj)
    Comment.objects.bulk_create(obj_list)
