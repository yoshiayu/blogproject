from django.shortcuts import render

# Create your views here.

# django.views.generic.baseからListViewをインポート
from django.views.generic import ListView, DetailView
# BlogPostをインポート
from .models import BlogPost
# django.views.genericからFormViewをインポート
from django.views.generic import FormView
# django.urlからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからContactFormをインポート
from .forms import ContactForm
# django.cintribからmessagesをインポート
from django.contrib import messages
# django.core.mailをモジュールからEmailMessageをインポート
from django.core.mail import EmailMessage

# index.htmlをレンダリング
class IndexView(ListView):
    '''トップページビュー
    投稿記事を一覧表示するのでListViewを継承
    Attributes:
        template_name:レンダリングテンプレート
        context_object_name:object_listキーの別名を設定
        queryset:テータベースのクエリ
    '''
    # index.htmlをレンダリング
    template_name = 'index.html'
    # object_listキーの別名を設定
    context_object_name = 'orderby_records'
    # モデルBlogPostのオブジェクトにobject_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並べ替える
    queryset = BlogPost.objects.order_by('-posted_at')
    
    paginate_by = 4

class BlogDetail(DetailView):
    '''詳細ページのビュー
    投稿記事の詳細を表示するのでDetailViewを継承する
    Attributes:
        template_name:レンダリングテンプレート
        Model:モデルのクラス
    '''
    # post.htmlをレンダリング
    template_name ='post.html'
    # ラクス変数modelにモデルBlogPostを設定
    model = BlogPost

class ScienceView(ListView):
    '''科学（science）カテゴリ記事一覧表示
    
    '''
    # science_list.htmlをレンダリング
    template_name ='science_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_list_キーの別名を設定
    context_object_name = 'science_records'
    # categoly='science'のレコードを抽出し
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='science').order_by('-posted_at')
    # 1ページに表示するレコード件数
    paginate_by = 2

class DailylifeView(ListView):
    '''日常（dailylife）カテゴリ記事一覧表示
    
    '''
    # dailylife_list.htmlをレンダリング
    template_name ='dailylife_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_list_キーの別名を設定
    context_object_name = 'dailylife_records'
    # categoly='dailylife'のレコードを抽出し
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='dailylife').order_by('-posted_at')
    # 1ページに表示するレコード件数
    paginate_by = 2

class MusicView(ListView):
    '''音楽（music）カテゴリ記事一覧表示
    
    '''
    # music_list.htmlをレンダリング
    template_name ='music_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_list_キーの別名を設定
    context_object_name = 'music_records'
    # categoly='music'のレコードを抽出し
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='music').order_by('-posted_at')
    # 1ページに表示するレコード件数
    paginate_by = 2

class ContactView(FormView):
    '''問い合わせページを表示
    フォームで入力されたデータを取得し、メールの作成と送信
    '''
    # contact.htmlをレンダリング
    template_name = 'contact.html'
    # クラス変数form_classにform.pyw゛定義したContactFormを設定
    form_class = ContactForm
    # 送信完了後にリダイレクトするページ
    success_url = reverse_lazy('blogapp:contact')
    
    def form_valid(self, form):
        '''FormViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したデータがPostされたときに呼ばれるメール送信を行う
        
        parameters:
            form(object): ContactFormのオブジェクト
        Return:
            HttpResponseRedirectのオブジェクト
            オブジェクトをインスタンス化するとsucceaa_urlで
            設定されているURLにリダイレクト
        '''
        # フォームに入力されたデータをフィールド名を指定し取得
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        # メールタイトルの書式を設定
        subject = 'お問い合せ: {}'.format(title)
        # フォームの入力データの書式を設定
        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)
            # メール送信元のアドレス
        from_email = 'yoshiayu19771106@gmail.com'
            # 送信先のメールアドレス
        to_list = ['yoshiayu19771106@gmail.com']
            # EmailMessageオブジェクト生成
        message = EmailMessage(subject=subject,
                              body=message,
                              from_email=from_email,
                              to=to_list,
                              )
            # EmailMessageクラスのsend()でメールサーバーからメールを送信
        message.send()
            # 送信完了後に表示するメッセージ
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
            # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)