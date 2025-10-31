from django.urls import path

from apps.branches import views

urlpatterns = [
    path("", views.BranchListCreateView.as_view(), name="branch-list"),
    path("<int:pk>/", views.BranchDetailView.as_view(), name="branch-detail"),
]