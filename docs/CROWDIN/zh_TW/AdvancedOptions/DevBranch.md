## 開發分支

<font color="#FF0000"><strong>注意：</strong></font> 開發分支僅用於 AAPS 的進一步開發。 應在另一台手機上用於測試，<font color="#FF0000"><strong>而不是實際循環！</p> 

<p spaces-before="0">
  AAPS 的最穩定版本是<a href="https://github.com/nightscout/AndroidAPS/tree/master">Master 分支</a>中的版本。  建議在實際循環中保持在 Master 分支。
</p>

<p spaces-before="0">
  AAPS 的開發版本僅適用於能處理堆棧追蹤、查找日誌文件，甚至啟動調試器以生成對開發人員有幫助的錯誤報告的開發者和測試者（簡言之：知道自己在做什麼而不需要協助的人）。 因此，許多未完成的功能都被停用了。 要啟用這些功能，請在 /AAPS/extra 目錄中建立名為<code>engineering_mode</code>的文件，以啟用<strong x-id="1">工程模式</strong>。 啟用工程模式可能會完全破壞循環。
</p>

<p spaces-before="0">
  但是，開發分支是一個不錯的地方，可以查看正在測試的功能，並幫助解決錯誤，並反饋新功能在實際中的效果。  通常人們會在舊手機和幫浦上測試開發分支，直到他們確信他是穩定的——使用他完全是自擔風險。  在測試任何新功能時，請記住你是在選擇測試一個仍在開發中的功能。 請自行承擔風險並謹慎行事以確保安全。
</p>

<p spaces-before="0">
  如果你發現錯誤或認為使用開發分支時發生了問題，請查看<a href="https://github.com/nightscout/AndroidAPS/issues">問題標籤</a>，看看是否有其他人發現，或者如果沒有，請自己添加。  您在這裡分享的資訊越多越好（不要忘記您可能需要分享您的<a href="../GettingHelp/AccessingLogFiles.md">日誌檔案</a>）。  新功能也可以在<a href="https://discord.gg/4fQUWHZ4Mw">Discord</a>上討論。
</p>

<p spaces-before="0">
  開發版本有一個過期日期。 當使用他滿意時，這似乎不便，但他有其作用。 當單一開發版本流傳時，更容易跟踪人們報告的錯誤。 開發人員不希望出現三個開發版本在外流傳，其中一些錯誤在某些版本中已經修復，而其他版本則未修復，而人們仍然繼續報告已經解決的錯誤。
</p>
