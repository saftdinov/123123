
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги")

    class Meta:
        ordering = ["name"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    date_of_birth = models.DateField(
        null=True, blank=True, verbose_name="Дата рождения"
    )
    date_of_death = models.DateField(
        null=True, blank=True, verbose_name="Дата смерти"
    )

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.pk)])

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Language(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Введите язык книги"
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Язык"
        verbose_name_plural = "Языки"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        related_name="books",
        verbose_name="Автор"
    )

    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Язык"
    )

    summary = models.TextField(
        max_length=1000,
        help_text="Краткое описание книги",
        verbose_name="Описание"
    )

    isbn = models.CharField("ISBN", max_length=13, unique=True)

    genre = models.ManyToManyField(
        Genre,
        help_text="Выберите жанры",
        verbose_name="Жанры"
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.pk)])


class BookInstance(models.Model):
    LOAN_STATUS = (
        ("m", "На обслуживании"),
        ("o", "Выдана"),
        ("a", "Доступна"),
        ("r", "Зарезервирована"),
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.RESTRICT,
        related_name="instances",
        verbose_name="Книга"
    )

    imprint = models.CharField(
        max_length=200,
        verbose_name="Издательство / данные экземпляра"
    )

    due_back = models.DateField(
        null=True,
        blank=True,
        verbose_name="Вернуть до"
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        default="m",
        verbose_name="Статус"
    )

    class Meta:
        ordering = ["due_back"]
        verbose_name = "Экземпляр книги"
        verbose_name_plural = "Экземпляры книг"

    def __str__(self):
        return f"{self.id} — {self.book.title}"
