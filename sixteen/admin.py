from import_export.admin import ImportExportModelAdmin

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

class TypeAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ["name"]
    ordering = ("id",)


class FunctionAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ["name"]
    ordering = ("id",)


class GroupAdmin(ImportExportModelAdmin):
    list_display = ("id", "category", "name", "description")
    search_fields = ["name"]
    ordering = ("id",)


class TypeFunctionAdmin(ImportExportModelAdmin):
    list_display = ("id", "type_id", "function_id", "hierarchy")
    ordering = ("id",)


class TypeGroupAdmin(ImportExportModelAdmin):
    list_display = ("id", "type_id", "group_id")
    ordering = ("id",)


class QuestionAdmin(ImportExportModelAdmin):
    list_display = ("id", "category", "question_sentence")
    ordering = ("id",)


class ChoiceAdmin(ImportExportModelAdmin):
    list_display = ("id", "question_id", "choice_sentence", "point")
    ordering = ("id",)


class AnswerAdmin(ImportExportModelAdmin):
    list_display = ("id", "question_id", "choice_id", "type_id")
    search_fields = ["type_id"]
    ordering = ("id",)


class AnimeAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "character_name", "type_id")
    ordering = ("id",)


# ================================= 動物 ===============================================

class AnimalResultAdmin(ImportExportModelAdmin):
    list_display = ("id", "type_id", "name", "head", "description", "img")
    list_editable = ("name", "head", "description", "img")
    search_fields = ["type_id"]
    ordering = ("id",)


# ================================= ポケモン ===============================================

class PokemonResultAdmin(ImportExportModelAdmin):
    list_display = ("id", "type_id", "name", "head", "description", "img")
    list_editable = ("name", "head", "description", "img")
    search_fields = ["type_id"]
    ordering = ("id",)


class PokemonAdmin(ImportExportModelAdmin):
    list_display = ("id", "character_name", "type")
    list_editable = ("character_name", "type")
    ordering = ("id",)


# ================================= RPG ===============================================

class RpgResultAdmin(ImportExportModelAdmin):
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
