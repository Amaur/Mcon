from django.conf.urls import include, url,patterns
from rest_framework import routers
from .views import (Index,dinar_list,dinar_detail,DinarViewSet,ItemViewSet,DinarList,DinarItem,DinDetail,Detail,AddDin ,AddItem,DinExcept,DeleteList,
                    DeleteItem)

router = routers.DefaultRouter()
router.register(r'dinar',  DinarViewSet)
#router.register(r'period', PeriodViewSet)
router.register(r'itens',  ItemViewSet)

urlpatterns = patterns('apps.con.views',
    (r'^',include(router.urls)),
    (r'^index$',Index),
    (r'^addDin$',AddDin),
    (r'^addItem/(?P<pk>[0-9]+)$',AddItem),
    (r'^detail/(?P<id>[0-9]+)$',Detail),
    (r'^dinars/$', dinar_list),
    (r'^dinar_detail/(?P<pk>[0-9]+)$', dinar_detail),
    (r'^dinarlist/$', DinarList),
    (r'^dinaritem/$', DinarItem),
    (r'^dindetail/(?P<id>[0-9]+)$', DinDetail),
    (r'^dinexcept/(?P<id>[0-9]+)$', DinExcept),
    (r'^dellist/(?P<id>[0-9]+)$', DeleteList),
    (r'^delitem/(?P<id>[0-9]+)$', DeleteItem),
)
