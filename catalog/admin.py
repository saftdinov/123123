
from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    search_fields = ("first_name", "last_name")
    list_filter = ("date_of_birth",)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "language", "display_genre")
    list_filter = ("genre", "author", "language")
    search_fields = ("title", "author__last_name")
    inlines = [BookInstanceInline]

    @admin.display(description="Жанры")
    def display_genre(self, obj):
        return ", ".join(genre.name for genre in obj.genre.all())


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "imprint", "status", "due_back")
    list_filter = ("status", "due_back")
    search_fields = ("book__title",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
