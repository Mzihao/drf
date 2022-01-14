import user_agents
from django.shortcuts import redirect
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

swagger_info = openapi.Info(
    title="Swagger API",
    default_version='v1',
    description="""
                这是一个`Django Rest Framework`和`Swagger`的demo.
                The `swagger-ui` view can be found [here](/cached/swagger).
                The `ReDoc` view can be found [here](/cached/redoc).
                The swagger YAML document can be found [here](/cached/swagger.yaml).
                The swagger JSON document can be found [here](/cached/swagger.json).
                You can login using the pre-existing `admin` user with password `passwordadmin`.
                """,
    # terms_of_service="https://www.google.com/policies/terms/",
    # contact=openapi.Contact(email="contact@snippets.local"),
    # license=openapi.License(name="BSD License"),
)

SchemaView = get_schema_view(
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)


def root_redirect(request):
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = user_agents.parse(user_agent_string)

    if user_agent.is_mobile:
        schema_view = 'cschema-redoc'
    else:
        schema_view = 'cschema-swagger-ui'

    return redirect(schema_view, permanent=True)


urlpatterns = [
    path('pumpkin/', admin.site.urls),
    path('', include('index.urls')),
    re_path(r'^swagger(?P<format>.json|.yaml)$', SchemaView.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path(r'redoc-old/', SchemaView.with_ui('redoc-old', cache_timeout=0), name='schema-redoc-old'),
    re_path(r'^cached/swagger(?P<format>.json|.yaml)$', SchemaView.without_ui(cache_timeout=None), name='cschema-json'),
    path('cached/swagger/', SchemaView.with_ui('swagger', cache_timeout=None), name='cschema-swagger-ui'),
    path('cached/redoc/', SchemaView.with_ui('redoc', cache_timeout=None), name='cschema-redoc'),
    re_path(r'^$', root_redirect),
]
