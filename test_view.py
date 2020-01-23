from django.urls import reverse
from rest_framework import status


def test_some(django_app, admin_user):
    url = reverse('test-view')
    r = django_app.get(url, user=admin_user)
    assert r.status_code == status.HTTP_200_OK
