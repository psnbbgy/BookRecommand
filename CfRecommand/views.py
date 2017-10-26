#!/usr/bin/python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse 
import json
#from json import loads, dumps

# Create your views here.
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

# Create your views here.
def hello(request):
  context          = {}
  context['hello'] = 'Hello World!'
  return render(request, 'hello.html', context)

def predict(request):
  book_list = []
  book_list.append('wa')
  book_list.append('wa')
  book_list.append('wa')
  books = ''
  if request.method == 'POST':
    books = request.POST.get('books')
    #book_list = get_cur_id(books)
    #book_list = recommand(get_cur_id(books))
  books = ''.join(book_list)
  result = {'result': books}
  return HttpResponse(json.dumps(result))

# cur fav: reader's favourite book
def recommand(cur_fav):
  book_score = dict()
  book_list = []
  for id_str in OriginRecommandList.objects.all():
    b_ids = id_str.split(' ')
    single_fav = []
    for b_id in b_ids:
      single_fav.append(int(b_id))
    single_score = 0
    for cur_id in cur_fav:
      if cur_id in single_fav:
        single_score = single_score + 1
    single_score = single_score / len(single_fav)
    for single_id in single_fav:
      if single_id not in book_score:
        book_score[single_id] = 0
      book_score[single_id] = book_score[single_id] + single_score
  sort_score = collections.OrderedDict(sorted(book_score.items(),key=lambda t:t[1]))
  i = 0
  for key, value in sort_score.items():
    book_list.append(BookIds.objects.get(book_id = key).book_name)
    i = i + 1
  book_res = []
  i = 0
  for book in book_list:
    if i < 10:
      book_res.append(book)
  # user_fav.append(cur_fav) new book's id must write into db
  return book_res

# get specify book ID
# cur_name: user's favourite book
def get_cur_id(cur_name):
  cur_fav = []
  cur_names = cur_name.split('，')
  return cur_names
  for single_book in cur_names:
    # if new book name is error, how to do
    single_id, is_create = BookIds.objects.get_or_create(book_name = single_book)
    if is_create:
      single_id.book_id = BookIds.objects.count()
      single_id.save()
    cur_fav.append(single_id.book_id)
  cur_fav.sort()
  return cur_fav

