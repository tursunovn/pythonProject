<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>

<div class ="container">
    <nav class="navbar navbar-expand-lg navbar-grey bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">DJANGO</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Главная</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">О сайте</a>
        </li>

        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">О разработчике</a>
        </li>
      </ul>
      <ul class="navbar-nav">
        <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Поиск..." aria-label="Search">
        <button class="btn btn-outline-primary" type="submit">Найти</button>
        </form>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Войти</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Зарегестрироваться</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
             data-bs-toggle="dropdown" aria-expanded="false">
              Привет Пользователь!
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Моя страница</a></li>
            <li><a class="dropdown-item" href="#">Добавить статью</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Выход</a></li>
          </ul>
        </li>
      </ul>

    </div>
  </div>
</nav>


  <h1>Список статей</h1>


  <div class = "d-flex justify-content-between">
    <div class = "col-3">
      <div class="list-group">
          <a href="{% url 'index' %}" class="list-group-item list-group-item-action">Все статьи</a>
          {% for category in categories %}
          <a href="{% url 'category_list' category.pk %}" class="list-group-item list-group-item-action">{{ category.title }}</a>

          {% endfor %}
      </div>
    </div>

    <div class = "col-8">
      {% for article in articles %}
      <div class="card">
        <div class="card-header">
              {{ article.category }}
        </div>
          <div class="card-body">
            <h5 class="card-title">{{ article.title }}</h5>
            <p class="card-text">{{ article.content| linebreaks|truncatewords:20 }}</p>
            <p class="card-text">{{ article.created_at }}</p>
            <a href="#" class="btn btn-primary">Подробнее</a>
          </div>
      </div>
      {% endfor %}
    </div>



  </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
