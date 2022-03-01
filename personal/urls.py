from django.urls import path

from .views import (
    renderHome,
    renderAcademics,
    renderContact,
    renderHappenings,
    renderOpportunities,
    renderPeople,
    renderLabs,
    renderPlacements,
    renderResearch,
    sendImages,
)

urlpatterns = [
    path('', renderHome, name='home'),
    path('academics/', renderAcademics, name='academics'),
    path('contact/', renderContact, name='contact'),
    path('happenings/', renderHappenings, name='happenings'),
    path('research', renderResearch, name='research'),
    path('labs', renderLabs, name='labs'),
    path('placements', renderPlacements, name='placements'),
    path('opportunities', renderOpportunities, name='opportunities'),
    path('people', renderPeople, name='people'),
    path('sendImages', sendImages, name='sendImages'),
]