
### Rest api using classes

### installations

```
pip install django
django-admin startporject <app-name>
pip install djangorestframework
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

--------------------

### Model creation
```py
# Creating company model
class Company(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    about = models.TextField()
    type=models.CharField(max_length=100, choices=(
        ('IT', 'IT'), ('NON IT', 'NON IT'), ('Mobile Phones', 'Mobile Phones')
    ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
```

### Serializer to serialize the data : 
```py
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = '__all__'
```

### use model view set to create all api's 
- the ModelViewSet class provides all the basic features like : `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
- But you can create your own custom function to render customized data or data in a particular manner, you can use : `@action` decorator for this
```python
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)
            serializer = EmployeeSerializer(employees, many=True, context={'request': request})
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
```

### lastly create routs with default router

```python
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet

router = DefaultRouter()

router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path("", include(router.urls))
]
```

-------------

### customizing admin dashboard fields
restapi/api/admin.py
```py
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'active', 'location', 'added_date')
    search_fields = ('name', 'location')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
    search_fields = ('name', 'email')
    list_filter = ('company',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
```


## Permission and Renderers
restapi/restapi/settings.py
```py

REST_FRAMEWORK = {
    # Permissions:
    # - Authenticated users: Permissions come from `django.contrib.auth` (add, change, delete, view).
    # - Unauthenticated users: Can only **read** (GET, HEAD, OPTIONS).
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],

    # Renderers:
    # - Only JSON responses are enabled.
    # - Browsable API (HTML UI) is disabled.
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
```

## customizing admin dashboard
1. install django-jazzmin
```py
pip install -U django-jazzmin
```

2. add to your apps
```py
INSTALLED_APPS = [
    'jazzmin',
    
    # other apps
]
```
3. ready to run
4. customization : [Django-jazzmin documentation](https://django-jazzmin.readthedocs.io/configuration/)
```py
JAZZMIN_SETTINGS = {
     "site_title": "Rest API Admin",
    'show_ui_builder' : True,
    ### other propertis available on docs
}
```

5. customized jazzmin dashboard : `restapi/restapi/settings.py`
```py

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-white",
    "accent": "accent-orange",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-orange",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "sketchy",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": False
} 
```