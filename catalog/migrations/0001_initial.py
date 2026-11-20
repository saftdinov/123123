from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=100, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=100, verbose_name="Фамилия")),
                ("date_of_birth", models.DateField(blank=True, null=True, verbose_name="Дата рождения")),
                ("date_of_death", models.DateField(blank=True, null=True, verbose_name="Дата смерти")),
            ],
            options={"ordering": ["last_name", "first_name"], "verbose_name": "Автор", "verbose_name_plural": "Авторы"},
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(help_text="Введите жанр книги", max_length=200)),
            ],
            options={"ordering": ["name"], "verbose_name": "Жанр", "verbose_name_plural": "Жанры"},
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Название")),
                ("summary", models.TextField(help_text="Краткое описание книги", max_length=1000, verbose_name="Описание")),
                ("isbn", models.CharField(max_length=13, unique=True, verbose_name="ISBN")),
                ("author", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="books", to="catalog.author", verbose_name="Автор")),
                ("genre", models.ManyToManyField(help_text="Выберите жанры", to="catalog.genre", verbose_name="Жанры")),
            ],
            options={"ordering": ["title"], "verbose_name": "Книга", "verbose_name_plural": "Книги"},
        ),
        migrations.CreateModel(
            name="BookInstance",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("imprint", models.CharField(max_length=200, verbose_name="Издательство / данные экземпляра")),
                ("due_back", models.DateField(blank=True, null=True, verbose_name="Вернуть до")),
                ("status", models.CharField(choices=[("m", "На обслуживании"), ("o", "Выдана"), ("a", "Доступна"), ("r", "Зарезервирована")], default="m", max_length=1, verbose_name="Статус")),
                ("book", models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name="instances", to="catalog.book", verbose_name="Книга")),
            ],
            options={"ordering": ["due_back"], "verbose_name": "Экземпляр книги", "verbose_name_plural": "Экземпляры книг"},
        ),
    ]
