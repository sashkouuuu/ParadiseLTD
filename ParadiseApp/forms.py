from django.forms import Form, ChoiceField, Select, CharField, TextInput, IntegerField, NumberInput


class CreateRoll(Form):
    producer = CharField(label="Производитель", max_length=20,  widget=TextInput(attrs={'class': "mat-input form-control"}))
    batch = IntegerField(label="Партия",
                         widget=NumberInput(attrs={'class': "mat-input form-control"}))
    number= IntegerField(label="Номер",
                         widget=NumberInput(attrs={'class': "mat-input form-control"}))
    size = CharField(label="Размер", max_length=20,
                         widget=TextInput(attrs={'class': "mat-input form-control"}))
    coating = CharField(label="Покрытие", max_length=20,
                         widget=TextInput(attrs={'class': "mat-input form-control"}))
    hardness = CharField(label="Твердость", max_length=20,
                         widget=TextInput(attrs={'class': "mat-input form-control"}))
    net = IntegerField(label="Нетто",
                         widget=NumberInput(attrs={'class': "mat-input form-control"}))
    gross = IntegerField(label="Брутто",
                         widget=NumberInput(attrs={'class': "mat-input form-control"}))

