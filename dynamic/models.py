from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255,
        choices=(
            ("TextField", "TextField"),
            ("IntegerField", "IntegerField"),
            ("DecimalField", "DecimalField"),
            ("DateField", "DateField"),
            ("DateTimeField", "DateTimeField"),
            ("BooleanField", "BooleanField"),
        ),
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "fields"


def create_model(name, fields=None, app_label="", module="", options=None):
    """
    Create a model class dynamically
    """

    class DynamicModel(models.Model):
        class Meta:
            abstract = True

    class Meta:
        # Using type('Meta', ...) gives a dictproxy error during model creation
        managed = False

    if app_label:
        # app_label must be set using the Meta inner class
        setattr(Meta, "app_label", app_label)

    # Update Meta with any options that were provided
    if options is not None:
        for key, value in options.items():
            setattr(Meta, key, value)

    # Set up a dictionary to simulate declarations within a class
    attrs = {"__module__": module, "Meta": Meta}

    # Add in any fields that were provided
    if fields:
        attrs.update(fields)

    # Create the class, which automatically triggers ModelBase processing
    model = type(name, (DynamicModel,), attrs)

    return model


# fields = {
#     "name": models.CharField(max_length=255),
#     "description": models.TextField(),
#     "price": models.DecimalField(max_digits=5, decimal_places=2),
# }

# options = {
#     "ordering": ["name"],
# }

# MyDynamicModel = create_model("MyDynamicModel", fields, "myapp", options=options)
# MyDynamicModel.objects.create(
#     name="product1", description="This is a product1", price=9.99
# )

# items = MyDynamicModel.objects.all()

# from myapp.models import OtherModel

# # Get the fields from other model
# other_model_fields = OtherModel._meta.get_fields()

# # Create fields dictionary
# fields = {}
# for field in other_model_fields:
#     if isinstance(field, models.CharField):
#         fields[field.name] = models.CharField(max_length=field.max_length)
#     elif isinstance(field, models.IntegerField):
#         fields[field.name] = models.IntegerField()
#     # Add other field types as needed

# options = {
#     'ordering': ['name'],
# }

# MyDynamicModel = create_model('MyDynamicModel', fields, 'myapp', options=options)
