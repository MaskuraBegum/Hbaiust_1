from django.shortcuts import render,redirect, get_object_or_404
from app_cover.models import CoverPage

def cover_page(request):
    covers = CoverPage.objects.all()
    context = {
        'covers': covers,
        'message': 'This is FBVs'
    }
    return render(request, 'covers/cover_page.html', context)