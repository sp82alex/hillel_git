def new_func_imdb_rank(imdb_rank):
  #в переменную записываем искомый ранк
  our_rank = 8.5
  #далее через цикл смотрим какие фильмы выше по рейтингу, чем 8,5
  for i in range(len(imdb_rank)):
    if float(imdb_rank[i]['rating']) > our_rank:
      #в новую переменную a записываем эти фиьмы
      a = (imdb_rank[i]['title'], imdb_rank[i]['rating'])
      #с помощью sorted и lambda сортируем фильмы
      print(sorted(a, key = lambda x: x[1]))

#выводим результат
new_func_imdb_rank(imdb_rank)






#создаем функцию, которая будет принмиать как аргумент название фильма, цикл проверяет, есть ли данный фильм в imdb_rank и если да, то возвращает ссылку на трейлер
def my_film(film_input):
  for i in range(len(imdb_rank)):
    if imdb_rank[i]['title'] == film_input:
      return(imdb_rank[i]['trailer'])




#обьявляем новую функции, аргументом выступает искомый режиссер
def our_director(input_director):
  #создаем новый список
  director_list = []
  #добавляем в него самих режиссеров, их фильмы и рейтинг
  for i in range(len(imdb_rank)):
    for b in range(len(imdb_rank[i]['director'])):
      director_list.append([imdb_rank[i]['director'][b], imdb_rank[i]['title'], imdb_rank[i]['rank']])
      #проверяем, есть ли искомый режиссер в нашем списке и выводим всего его найденные фильмы
      if director_list[i][b] == input_director:
        print(director_list[i])
