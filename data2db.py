#!/usr/bin/env python
#coding:utf-8
 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookRecommand.settings")
 
'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
 
import django
import collections
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
 
from CfRecommand.models import OriginRecommandList
from CfRecommand.models import BookIds
 
#把爬来的数据存进数据库
def load_data(file_name):
  book_ids = dict()
  user_fav = [[]]
  id = 1
  input_book = open(file_name)
  for line in input_book:
    cur_fav = []
    lines = line.split(' ')
    for book in lines:
      if len(book) != 0 and not(book in book_ids):
        book_ids[book] = id
        id = id + 1
      cur_fav.append(book_ids[book])
    cur_fav.sort()
    user_fav.append(cur_fav)
  for book, b_id in book_ids.items():
    books_pack, is_create = BookIds.objects.get_or_create(book_name = book)
    books_pack.book_id = b_id
    books_pack.save()
  OriginRecommandList.objects.all().delete()
  user_num = 1
  for re_books in user_fav:
    book_id_str = ''
    for book_id in re_books:
      single_str = str(book_id)
      book_id_str = book_id_str + single_str
    OriginRecommandList.objects.get_or_create(user_id = user_num, books = book_id_str)
  return

if __name__ == '__main__':
  load_data('youshu_10000.log')
  print 'Done'


