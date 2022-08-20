from django.db import models

# Create your models here.

class BlogPost(models.Model):

    # カテゴリに設定する項目を入れ子のタプルとして定義
    # タプルの第1要素はモデルが使用する値、第2要素は管理サイトの選択メニューに表示する文字列
    CATEGORY = (('science', '科学について'), ('dailylife', '日常について'), ('music', '音楽について'))
    
    # タイトル用フィールド
    title = models.CharField(
        verbose_name = 'タイトル', # フィールドタイトル
        max_length=200 # 最大文字数200
        )
    # 本文フィールド
    content = models.TextField(
        verbose_name= '本文' # フィールドタイトル
        )
    # 投稿日時フィールド
    posted_at = models.DateTimeField(
        verbose_name='カテゴリ', # フィールドタイトル
        auto_now_add=True # 日時自動追加
        )
    #　カテゴリーフィールド
    category = models.CharField(
        verbose_name= 'カテゴリ', # フィールドタイトル
        max_length=50, choices=CATEGORY # 最大文字数50
        )
      
    def __str__(self):
          '''Django管理サイトでデータを表示する際に識別名として投稿記事のタイトルを表示するために必要
          Returns(str):投稿記事のタイトル
          '''
          return self.title
