from django.urls import path
from delivery import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('category/',views.category,name="category"),
    path('insert/',views.insert,name="insert"),
    path('catdisplay/',views.catdisplay,name="catdisplay"),
    path('editcat/<int:dataid>/',views.editcat,name="editcat"),
    path('updatecat/<int:dataid>/',views.updatecat,name="updatecat"),
    path('deletecat/<int:dataid>/',views.deletecat,name="deletecat"),

    path('dish/',views.dish,name="dish"),
    path('productdata/',views.productdata,name="productdata"),
    path('prodisplay/',views.prodisplay,name="prodisplay"),
    path('editprod/<int:dataid>/',views.editprod,name="editprod"),
    path('update/<int:dataid>/',views.update,name="update"),
    path('delete/<int:dataid>/',views.delete,name="delete"),


    path('loginpage/',views.loginpage,name="loginpage"),
    path('logindetails/',views.logindetails,name="logindetails"),
    path('logoutpage/',views.logoutpage,name="logoutpage"),

    path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact"),
    path('displaycontact/',views.displaycontact,name="displaycontact"),


    path('addeventpg/',views.addeventpg,name="addeventpg"),
    path('insertevents/',views.insertevents,name="insertevents"),
    path('displayevent/',views.displayevent,name="displayevent"),
    path('editpg/<int:dataid>/',views.editpg,name="editpg"),
    path('updateevent/<int:dataid>/',views.updateevent,name="updateevent"),


    path('displaybookingpg/',views.displaybookingpg,name="displaybookingpg"),
    path('bookingdelete/<int:dataid>/',views.bookingdelete,name="bookingdelete"),
]