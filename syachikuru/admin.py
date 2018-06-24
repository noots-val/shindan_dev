from .models import Answer
from .models import Candidate
from .models import Characteristic
from .models import Choice
from .models import Question
from .models import Result
from django.contrib import admin


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "choice")
    search_fields = ["candidate"]
    ordering = ("id",)


class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "result", "name", "sex", "age", "profession")
    search_fields = ["name"]
    ordering = ("id",)


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ("id", "characteristic_type", "description")
    search_fields = ["characteristic_type"]
    ordering = ("id",)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "choice_sentence", "point")
    search_fields = ["question"]
    ordering = ("id",)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question_sentence", "characteristic")
    search_fields = ["characteristic"]
    ordering = ("id",)


class ResultAdmin(admin.ModelAdmin):
    list_display = ("id", "level", "type", "img", "description")
    search_fields = ["product_title"]
    ordering = ("id",)


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)
