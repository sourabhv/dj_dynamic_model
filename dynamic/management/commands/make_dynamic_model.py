from django.core.management.base import BaseCommand, CommandError
from django.db import models, connections, utils
from dynamic.models import create_model, Field


def type_to_dj_field(type: str) -> models.Field:
    if type == "TextField":
        return models.TextField()
    elif type == "IntegerField":
        return models.IntegerField()
    elif type == "DecimalField":
        return models.DecimalField()
    elif type == "DateField":
        return models.DateField()
    elif type == "DateTimeField":
        return models.DateTimeField()
    elif type == "BooleanField":
        return models.BooleanField()
    else:
        raise CommandError(f"Unknown type: {type}")

class Command(BaseCommand):
    help = "Make a dynamic model"

    def handle(self, *args, **kwargs):
        connection = connections["default"]

        field_items = Field.objects.all()

        fields = {
            field.name: type_to_dj_field(field.type)
            for field in field_items
        }
        options = {
            "ordering": ["name"],
            "db_table": "myapp_dynamic_model",
        }
        DynamicModel = create_model(
            "DynamicModel",
            fields=fields,
            app_label="myapp",
            options=options,
        )
        # https://docs.djangoproject.com/en/4.2/ref/schema-editor/#create-model
        with connection.schema_editor() as schema_editor:
            try:
                schema_editor.delete_model(DynamicModel)
            except utils.OperationalError:
                pass
            schema_editor.create_model(DynamicModel)
