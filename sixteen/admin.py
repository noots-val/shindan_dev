from .models import Type
from .models import Function
from .models import Group
from .models import TypeFunction
from .models import TypeGroup
from .models import Anime
from .models import Question
from .models import Choice
from .models import Answer
from .models import AnimalResult
from .models import PokemonResult
from .models import Pokemon
from .models import RpgResult
from django.contrib import admin


# ================================= 16タイプ共通 ===============================================

class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ["name"]
    ordering = ("id",)


class FunctionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ["name"]
    ordering = ("id",)


class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "name", "description")
    search_fields = ["name"]
    ordering = ("id",)


class TypeFunctionAdmin(admin.ModelAdmin):
    list_display = ("id", "type_id", "function_id", "hierarchy")
    ordering = ("id",)


class TypeGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "type_id", "group_id")
    ordering = ("id",)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "question_sentence")
    ordering = ("id",)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "question_id", "choice_sentence", "point")
    ordering = ("id",)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question_id", "choice_id", "type_id")
    search_fields = ["type_id"]
    ordering = ("id",)


class AnimeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "character_name", "type_id")
    ordering = ("id",)


# ================================= 動物 ===============================================

class AnimalResultAdmin(admin.ModelAdmin):
    list_display = ("id", "type_id", "name", "head", "description", "img")
    list_editable = ("name", "head", "description", "img")
    search_fields = ["type_id"]
    ordering = ("id",)


# ================================= ポケモン ===============================================

class PokemonResultAdmin(admin.ModelAdmin):
    list_display = ("id", "type_id", "name", "head", "description", "img")
    list_editable = ("name", "head", "description", "img")
    search_fields = ["type_id"]
    ordering = ("id",)


class PokemonAdmin(admin.ModelAdmin):
    list_display = ("id", "character_name", "pokemon_result")
    search_fields = ["pokemon_result"]
    ordering = ("id",)


# ================================= RPG ===============================================

class RpgResultAdmin(admin.ModelAdmin):
    list_display = ("id", "type_id", "name", "head", "description", "img")
    list_editable = ("name", "head", "description", "img")
    search_fields = ["type_id"]
    ordering = ("id",)


admin.site.register(Type, TypeAdmin)
admin.site.register(Function, FunctionAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(TypeFunction, TypeFunctionAdmin)
admin.site.register(TypeGroup, TypeGroupAdmin)
admin.site.register(Anime, AnimeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(AnimalResult, AnimalResultAdmin)
admin.site.register(PokemonResult, PokemonResultAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(RpgResult, RpgResultAdmin)
