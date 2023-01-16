actor_films = {
  "links": {
    "next": "null",
    "previous": "null"
  },
  "count": 10,
  "results": [
    [
      {
        "imdb_id": "tt1201607",
        "title": "Harry Potter and the Deathly Hallows: Part 2",
        "rating": 8.1
      },
      [
        {
          "role": "Harry Potter",
          "actor": {
            "imdb_id": "nm0705356",
            "name": "Daniel Radcliffe"
          }
        }
      ]
    ],
    [
      {
        "imdb_id": "tt0304141",
        "title": "Harry Potter and the Prisoner of Azkaban",
        "rating": 7.9
      },
      [
        {
          "role": "Harry Potter",
          "actor": {
            "imdb_id": "nm0705356",
            "name": "Daniel Radcliffe"
          }
        }
      ]
    ],
    [
      {
        "imdb_id": "tt0926084",
        "title": "Harry Potter and the Deathly Hallows: Part 1",
        "rating": 7.7
      },
      [
        {
          "role": "Harry Potter",
          "actor": {
            "imdb_id": "nm0705356",
            "name": "Daniel Radcliffe"
          }
        }
      ]
    ],
    [
      {
        "imdb_id": "tt0330373",
        "title": "Harry Potter and the Goblet of Fire",
        "rating": 7.7
      },
      [
        {
          "role": "Harry Potter",
          "actor": {
            "imdb_id": "nm0705356",
            "name": "Daniel Radcliffe"
          }
        }
      ]
    ],
    [
      {
        "imdb_id": "tt0241527",
        "title": "Harry Potter and the Sorcerer's Stone",
        "rating": 7.6
      },
      [
        {
          "role": "Harry Potter",
          "actor": {
            "imdb_id": "nm0705356",
            "name": "Daniel Radcliffe"
          }
        }
      ]
    ],
    [
      {
        "imdb_id": "tt0417741",
        "title": "Harry Potter and the Half-Blood Prince",
        "rating": 7.6
      },
      [
        {
          "role": "Harry Potter",
          "actor": {
            "imdb_id": "nm0705356",
            "name": "Daniel Radcliffe"
          }
        }
      ]
    ],
    [
      {
        "imdb_id": "tt0373889",
        "title": "Harry Potter and the Order of the Phoenix",
        "rating": 7.5
      },
      [
        {
          "role": "Harry Potter",
          "actor": {
            "imdb_id": "nm0705356",
            "name": "Daniel Radcliffe"
          }
        }
      ]
    ],
    [
      {
        "imdb_id": "tt0295297",
        "title": "Harry Potter and the Chamber of Secrets",
        "rating": 7.4
      },
      [
        {
          "role": "Harry Potter",
          "actor": {
            "imdb_id": "nm0705356",
            "name": "Daniel Radcliffe"
          }
        }
      ]
    ],
    [
      {
        "imdb_id": "tt4034354",
        "title": "Swiss Army Man",
        "rating": 7
      },
      [
        {
          "role": "Manny",
          "actor": {
            "imdb_id": "nm0705356",
            "name": "Daniel Radcliffe"
          }
        }
      ]
    ],
    [
      {
        "imdb_id": "tt5797184",
        "title": "Escape from Pretoria",
        "rating": 6.8
      },
      [
        {
          "role": "Tim Jenkin",
          "actor": {
            "imdb_id": "nm0705356",
            "name": "Daniel Radcliffe"
          }
        }
      ]
    ]
  ]
}

def new_func_5(rating_input):
  for i in range(len(actor_films['results'])):
    if actor_films['results'][i][0]['rating'] >= rating_input:
      print(actor_films['results'][i][0]['title'], actor_films['results'][i][0]['rating'], sep=', ')
    elif int(rating_input) > 10:
      return("Ви ввели рейтинг більше 10-ти")
    else:
      return("Нажаль, таких фільмів більше не існує")


#Пробуем записать в аргумент фуннкции разные варианты:
new_func_5(1)