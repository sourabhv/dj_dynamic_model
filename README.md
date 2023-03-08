# dj_dynamic_model

Minimal dynamic model in django example


## How to use

1. Run migrations and create tables
   
   ```sh
   ./manage.py migrate
   ```
2. Add all the fields you need in the `fields` model, with one of the following type:
   
   - `TextField`
   - `IntegerField`
   - `DecimalField`
   - `DateField`
   - `DateTimeField`
   - `BooleanField`
   
   (You can add more in `Field` model)

3. Run this command to recreate the dynamic model (it will drop the previous model first 
   ```sh
   ./manage.py make_dynamic_model
   ```
