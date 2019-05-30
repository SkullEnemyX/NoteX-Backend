from rest_framework import serializers
from .models import Authentication,NoteApp
from rest_framework import serializers

class AuthSerializer(serializers.ModelSerializer):

    class Meta:
            model = Authentication
            fields = ('__all__')

class NoteSerializer(serializers.ModelSerializer):
    # embedded_field = serializers.SerializerMethodField()
    class Meta:
            model = NoteApp
            field = ('__all__')
            
    # def get_embedded_field(self, obj):
    #     return_data = None
    #     if type(obj.embedded_field) == list:
    #         embedded_list = []
    #         for item in field:
    #             embedded_dict = item.__dict__
    #             for key in list(embedded_dict.keys()):
    #                 if key.startswith('_'):
    #                     embedded_dict.pop(key)
    #             embedded_list.append(embedded_dict)
    #         return_data = embedded_list
    #     else:
    #         embedded_dict = field.__dict__
    #         for key in list(embedded_dict.keys()):
    #             if key.startswith('_'):
    #                 embedded_dict.pop(key)
    #         return_data = embedded_dict
    #     return return_data