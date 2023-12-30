from django.urls import path
from frontend import views

urlpatterns=[
    path('',views.homepg,name="homepg"),
    path('product/',views.product,name="product"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('service/',views.service,name="service"),
    path('insertcontact/',views.insertcontact,name="insertcontact"),
    path('singledish/<int:proid>/',views.singledish,name="singledish"),
    path('dishcategory/<cat_name>/',views.dishcategory,name="dishcategory"),
    path('registration/',views.registration,name="registration"),
    path('registerdata/',views.registerdata,name="registerdata"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('logoutuser/',views.logoutuser,name="logoutuser"),

    path('insertcart/',views.insertcart,name="insertcart"),
    path('cartpg/',views.cartpg,name="cartpg"),
    path('deletedish/<int:proid>/',views.deletedish,name="deletedish"),
    path('checkoutorder/',views.checkoutorder,name="checkoutorder"),
    path('bookingevent/',views.bookingevent,name="bookingevent"),
    path('bookingdata/',views.bookingdata,name="bookingdata"),
    path('confirmorder/',views.confirmorder,name="confirmorder"),

    path('dish_search/',views.dish_search,name="dish_search"),

    path('eventspg/',views.eventspg,name="eventspg"),
    path('endpage/',views.endpage,name="endpage"),
    path('deletealldish/',views.deletealldish,name="deletealldish"),

]