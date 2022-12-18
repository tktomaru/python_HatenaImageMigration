# HatenaImageMigration
画像ファイルの対比

# 使用方法

Migration.pyを開きます。

以下のファイルパスを適切に変更します。

RenameFileList = glob.glob("C:/Users/tktomaru/Desktop/blog-new-rename/*")
OldFileList = glob.glob("C:/Users/tktomaru/Desktop/blog/*")

ただ画像を比較した結果、一致したファイルを一行でスペースで区切って表示します。
比較元１ファイルにつき、比較先パスで全画像検索しているので時間がかかります。


# サンプル実行結果

D:\github\HatenaImageMigration>python Migration.py
Image Search Start!!
=== Callled : __init__ ===
C:/Users/tktomaru/Desktop/blog-new-rename\20191005143644.jpg   C:/Users/tktomaru/Desktop/blog\20171230222012.jpg
C:/Users/tktomaru/Desktop/blog-new-rename\20191005143647.jpg   C:/Users/tktomaru/Desktop/blog\20171230235325.jpg
C:/Users/tktomaru/Desktop/blog-new-rename\20191005143650.png   C:/Users/tktomaru/Desktop/blog\20180108215416.png


