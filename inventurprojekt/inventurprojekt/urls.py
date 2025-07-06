from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from inventory.views import OrderListView, OrderCreateView, CalendarView

urlpatterns = [
    path('', CalendarView.as_view(), name='home'),
    path('inventar/', TemplateView.as_view(template_name='inventory.html'), name='inventory'),
    path('auftraege/', OrderListView.as_view(), name='orders'),
    path('auftraege/neu/', OrderCreateView.as_view(), name='order-create'),
    path('kalender/', CalendarView.as_view(), name='calendar'),
    path('produkte/', TemplateView.as_view(template_name='products.html'), name='products'),
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
