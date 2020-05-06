"""ltm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
import sro.views as sro_views
import revoffice.views as rev_views

urlpatterns = [
    path('index', views.index),
    path('homepage', views.homepage, name="homepage"),
    path('search_land_details', rev_views.search_land_details, name="search"),
    path('sro_homepage', sro_views.sro_homepage, name="sro_homepage"),  
    path('rev_homepage', rev_views.rev_homepage, name="rev_homepage"),
	path('application_form', views.application_form, name="application_form"),
	path('apply_to_sro', sro_views.receive_application),
    path('display_applications', sro_views.display_pending_applicaitons, name="display_applications"),
    path('process_application', sro_views.process_application, name="process_application"),
    path('send_appn_to_rev', sro_views.send_appn_to_rev, name="send_appn_to_rev"),
    path('get_tempblock_at_rev', rev_views.get_block_at_rev, name='get_tempblock_at_rev'),
    path('print_blockqueue', rev_views.print_BlockQueue, name="print_blockqueue"),
    path('get_top_hash', rev_views.get_top_hash, name="get_top_hash"),
    path('ladle', rev_views.blockchain_ladle, name="ladle"),
    path('append_the_ledger', rev_views.append_the_ledger, name="append_the_ledger"),
    path('admin/', admin.site.urls)
]
 