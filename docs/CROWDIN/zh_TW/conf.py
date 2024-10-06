import os

exec (open("../../shared.conf.py").read())

# 指定語言代碼
language = 'zh-TW'

# 語言檔案路徑
locale_dirs = ['docs/CROWDIN/']  # 你的翻譯檔案所在的目錄
gettext_compact = False    # 確保每個文件都有單獨的翻譯檔案