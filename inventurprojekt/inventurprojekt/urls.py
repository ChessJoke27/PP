from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from inventory.views import OrderListView, OrderCreateView, CalendarView, ProductListView, ProductCreateView

urlpatterns = [
    path('', CalendarView.as_view(), name='home'),
    path('inventar/', TemplateView.as_view(template_name='inventory.html'), name='inventory'),
    path('auftraege/', OrderListView.as_view(), name='orders'),
    path('auftraege/neu/', OrderCreateView.as_view(), name='order-create'),
    path('kalender/', CalendarView.as_view(), name='calendar'),
    path('produkte/', ProductListView.as_view(), name='products'),
    path('produkte/neu/', ProductCreateView.as_view(), name='product-create'),
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
