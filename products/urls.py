
from django.urls import path
from products.views.prodcuts_logic import (
    ProductListViewSet,
    ProductCreateView,
    ProductRetUpDesViewSet,

    ProductSingleView,
)

from products.views.products_init_logic import (
    CategoriesViewSet, 
    CategoriesUpdateDelete, 

    SubCategoriesListView, 
    SubCategoryCreateView,
    SubCategorySingleView,
    SubCategoryUpdateView,
    SubCategoryDeleteView,

    BrandView,
    BrandUpdateDelete,
    
    CountryView,
    CountryUpdateDelete,
     
)

from products.views.product_review_logic import (
    ProducReviewtListView, 
    ProductReviewCreateView,
    ProductReviewRetrieveView, 
    ProductReviewEditView,
    ProductReviewDeleteView
)


from products.views.slider_logic import (
    SliderListView, 
    SliderSingleView,
    SliderCreateView,
    SliderEditView,
    SliderDeleteView
)


from products.views.feature_products_logic import (
    Banner_createView,
    Banner_ListView,
    Banner_SingleView,
    Banner_update_deleteView,

    BannerProducts_createView,
    BannerProducts_SingleView,
    BannerProducts_DeleteView,
    BannerListView,
)

from products.views.discount_product_logic import (
    Discountproducts_list_view,
    Discountproducts_Single_view,
    Discountproducts_Create_view,
    # Discountproducts_Update_view,
    Discountproducts_Delete_view,
)

from products.views.damage_products_logic import (
    AddDamageProductsView,
    DamageProductsView,
    DamageProductsListView,
    DamageProductsUpdateView,
    DamageProductsDeleteeView,
    DamageProductsSingleView

)
urlpatterns = []


urlpatterns_category = [
    path('categories/', CategoriesViewSet.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoriesUpdateDelete.as_view(), 
        name='categories_update_delete'),

    path('sub_categories/list/', SubCategoriesListView.as_view(), name='sub_categories_list'),
    path('subcategory/create/', SubCategoryCreateView.as_view(), name='sub_category_create'),
    path('sub_categories/single/<int:pk>/', SubCategorySingleView.as_view(),
        name='sub_categories_update_delete'),
    path('sub_category/update/<int:pk>/',SubCategoryUpdateView.as_view()),
    path('sub_category/delete/<int:pk>/',SubCategoryDeleteView.as_view()),
]

urlpatterns_product = [ 
    
    path('product/', ProductListViewSet.as_view(), name='products' ),
    path('product/create/',ProductCreateView.as_view(), name='product_create' ),
    path('product/update-delete/<int:pk>/',ProductRetUpDesViewSet.as_view(), 
        name='products_delete_update' ),
    path('product/single/<int:pk>/',ProductSingleView.as_view()),
    
]


urlpatterns_brand_countries = [ 
    path('brand/', BrandView.as_view(), name='brand' ),
    path('brand/<int:pk>/', BrandUpdateDelete.as_view(), name='brand_update_delete' ),
    path('countries/', CountryView.as_view(), name='country' ),
    path('countries/<int:pk>/', CountryUpdateDelete.as_view(), name='country_update_delete' ),
]


urlpatterns_productsReview = [ 
    path('review/',ProducReviewtListView.as_view()),
    path('review/create/',ProductReviewCreateView.as_view()),
    path('review/view/<int:pk>/', ProductReviewRetrieveView.as_view()),
    path('review/update/<int:pk>/',ProductReviewEditView.as_view()),
    path('review/delete/<int:pk>/',ProductReviewDeleteView.as_view()),
]

urlpatterns_slider = [ 
    path('slider/',SliderListView.as_view()),
    path('slider/create/',SliderCreateView.as_view()),
    path('slider/view/<int:pk>/', SliderSingleView.as_view()),
    path('slider/update/<int:pk>/',SliderEditView.as_view()),
    path('slider/delete/<int:pk>/',SliderDeleteView.as_view()),
]

urlpatterns_banner_products = [ 
    path('banners/list/',Banner_ListView.as_view()),
    path('banners/create/',Banner_createView.as_view()),
    path('banners/single/view/<int:pk>/',Banner_SingleView.as_view()),
    path('banners/action/<int:pk>/',Banner_update_deleteView.as_view()),

    path('banners/product/create/',BannerProducts_createView.as_view()),
    path('banners/product/single/view/<int:pk>/',BannerProducts_SingleView.as_view()),
    path('banners/product/delete/<int:pk>/',BannerProducts_DeleteView.as_view()),

    path("banner/product/list/", BannerListView.as_view()),
]

urlpatterns_discount_products = [ 
    path('discount/products/list/',Discountproducts_list_view.as_view()),
    path('discount/products/single/view/<int:pk>/',Discountproducts_Single_view.as_view()),

    path('discount/products/create/',Discountproducts_Create_view.as_view()),
    # path('discount/products/edit/view/<int:pk>/',Discountproducts_Update_view.as_view()),
    path('discount/products/dekete/<int:pk>/',Discountproducts_Delete_view.as_view()),

]

urlpatterns_damage_products = [ 
    path('damage/add/', AddDamageProductsView.as_view()),

    path('damage/products/create/', DamageProductsView.as_view()),
    path('damage/products/list/',DamageProductsListView.as_view()), 
    path('damage/products/single/view/<int:pk>/',DamageProductsSingleView.as_view()),
    path('damage/products/update/<int:pk>/',DamageProductsUpdateView.as_view()), 
    path('damage/products/delete/<int:pk>/',DamageProductsDeleteeView.as_view()), 
    
]

urlpatterns += urlpatterns_category
urlpatterns += urlpatterns_product
urlpatterns += urlpatterns_brand_countries
urlpatterns += urlpatterns_productsReview
urlpatterns += urlpatterns_slider
urlpatterns += urlpatterns_banner_products
urlpatterns += urlpatterns_discount_products

urlpatterns += urlpatterns_damage_products