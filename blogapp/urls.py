from django.urls import path
from . import views

# URLconfのURLパターンをぎゃくびき用にアプリ名を登録
app_name = 'blogapp'

# URLパターン登録用リスト
urlpatterns = [
    # http(s)://ホスト名/以下パスが''(無し)の場合
    # viewsモジュールのIndexViewを実行
    # URLパターン名'index'
    path('', views.IndexView.as_view(), name='index'),
    
    # 問い合わせページURL
    path(
        # 問い合わせページURL
        'contact/',
        # viewsモジュールのContactViewを実行
        views.ContactView.as_view(),
        # URLパターン名を'contact'
        name='contact'
        ),
    
    # リクエストされたURLが「blog-detail/レコードid/」の場合
    # viewsモジュールのBlogDetailを実行
    # URLパターン名'blog-detail'
    
    path(
        # 詳細ページのURL「blog-detail/レコードid/」
        'blog-detail/<int:pk>/',
        # viewsモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        # URLパターン名前を'blog_detail'
        name='blog_detail'
        ),
        # Scienceカテゴリ一覧ページURL
    path(
        # scienceのカテゴリの一覧ページURL
        'science-list/',
        # viewsモジュールのDailylifeViewを実行
        views.ScienceView.as_view(),
        # URLパターン名
        name='science_list'
        ),
    path(
        # dailylifeのカテゴリの一覧ページURL
        'dailylife-list/',
        # viewsモジュールのDailylifeViewを実行
        views.DailylifeView.as_view(),
        # URLパターン名
        name='dailylife_list'
        ),
    # musicカテゴリの一覧ページURL
    path(
        # musicのカテゴリの一覧ページURL
        'music-list/',
        # viewsモジュールのDailylifeViewを実行
        views.MusicView.as_view(),
        # URLパターン名
        name='music_list'
        ),
]