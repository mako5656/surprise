from django.db import models
from django.core import validators


class Item(models.Model):

    BUDGET_CHOICES = (
        (0, '1001~2000'),
        (1, '2001~3000'),
        (2, '3001~4000'),
        (3, '4001~5000'),
        (4, '5001~6000'),
    )

    AREA_CHOICES = (
        (0, '名古屋駅'),
        (1, '栄駅'),
    )

    shop_name = models.CharField(
        verbose_name='店名',
        max_length=200,
    )
    urls = models.TextField(
        verbose_name='URL',
        max_length=300,
    )
    address = models.TextField(
        verbose_name='住所',
        max_length=300,
    )
    genre_name = models.TextField(
        verbose_name='店のジャンルやキャッチコピー1',
        max_length=300,
    )
    genre_catch = models.TextField(
        verbose_name='店のジャンルやキャッチコピー2',
        max_length=300,
    )
    catch = models.TextField(
        verbose_name='店のジャンルやキャッチコピー3',
        max_length=300,
    )
    image_url = models.TextField(
        verbose_name='画像のURL',
        max_length=300,
    )
    insta_tag_name = models.TextField(
        verbose_name='インスタのタグ名',
        max_length=300,
    )
    budget = models.IntegerField(
        verbose_name='予算',
        choices=BUDGET_CHOICES,
        default=1
    )
    budget_str = models.TextField(
        verbose_name='予算str',
        max_length=300,
    )
    area = models.IntegerField(
        verbose_name='エリア',
        choices=AREA_CHOICES,
        default=1
    )
    area_str = models.TextField(
        verbose_name='エリアstr',
        max_length=300,
    )
    map_shop = models.TextField(
        verbose_name='ショップの位置情報',
        max_length=300,
    )
    map_station = models.TextField(
        verbose_name='駅の位置情報',
        max_length=300,
    )

    good = models.IntegerField(
        verbose_name='エリア',
        default=0
    )

    # 管理サイト上の表示設定
    # def __str__(self):
    #     return self.shop_name
    #
    # class Meta:
    #     verbose_name = 'アイテム'
    #     verbose_name_plural = 'アイテム'