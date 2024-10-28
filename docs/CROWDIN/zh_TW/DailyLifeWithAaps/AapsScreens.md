# AAPS 螢幕畫面

```{contents} 目錄 :depth: 2

    <br />## 主畫面
    
    ![主畫面 V2.7](../images/Home2020_Homescreen.png)
    
    這是您開啟 **AAPS** 時首先會看到的畫面，裡面包含了您日常所需的大部分資訊。
    
    ### 區域 A - 標籤
    
    * 在不同的 **AAPS** 模組之間瀏覽。
    * 您也可以透過向左或向右滑動來切換螢幕。
    * 顯示的標籤可以在 [設定建構器](../SettingUpAaps/ConfigBuilder.md#tab-or-hamburger-menu) 中選擇。
    
    ### 區域 B - 設定檔與目標
    
    #### 當前設定檔
    
    當前的設定檔顯示在左側的工具列中。 
    
    點一下設定檔欄位查看設定檔詳細資訊. 長按設定檔工具列以 [切換不同的設定檔](../DailyLifeWithAaps/ProfileSwitch-ProfilePercentage.md#profile-switch--profile-percentage)。
    
    ![設定檔切換剩餘時間](../images/Home2020_ProfileSwitch.png)
    
    1. 常規顯示標準的設定檔激活。
    2. 設定檔切換剩餘時間為 59 分鐘。
    3. 設定檔切換特定百分比為 120%。
    4. 設定檔切換特定百分比為 80% 且剩餘時間為 59 分鐘。
    5. 設定檔切換時區偏移為 -1 小時。
    6. 設定檔切換特定百分比為 120%、時區偏移 1 小時，剩餘時間為 59 分鐘。
    
    #### 目標
    
    ![臨時目標剩餘時間](../images/Home2020_TT.png)
    
    當前的目標血糖水平顯示在右側工具列中。
    
    輕按目標工具列以設定 **[臨時目標](../DailyLifeWithAaps/TempTargets.md)**。
    
    如果設定了臨時目標，工具列將變為黃色，並會在括號中顯示剩餘時間（以分鐘為單位）。
    
    #### 動態目標調整的視覺化
    
    ![動態目標調整的視覺化](../images/Home2020_DynamicTargetAdjustment.png)
    
    使用 [SMB 演算法](../SettingUpAaps/ConfigBuilder.md#aps) 和 [Autosens](../DailyLifeWithAaps/KeyAapsFeatures.md#autosens) 功能時，**AAPS** 可以根據敏感性動態調整您的目標。 
    
    在 [偏好設定 > OpenAPS SMB 設定](../SettingUpAaps/Preferences.md#openaps-smb-settings) 中啟用以下一個或兩個選項：
    
       * “敏感性提高目標” 和/或 
       * “抗性降低目標” 
    
    如果 **AAPS** 偵測到抗性或敏感性，目標將會變更為設定檔中設定的值。 當它變更目標血糖時，背景顏色會變為綠色。
    
    ### 區域 C - 血糖與循環狀態
    
    #### 當前血糖
    來自 CGM 的最新血糖讀取值顯示在左側。
    
    血糖數值的顏色反映了與設定的 [範圍](../SettingUpAaps/Preferences.md#range-for-visualization) 相比的狀態。
    
       * 綠色 = 在範圍內
       * 紅色 = 低於範圍
       * 黃色 = 超出範圍 
    
    中間的灰色區塊顯示自上次讀取以來的分鐘數以及在最近 15 和 40 分鐘內的變化。
    
    #### 循環狀態
    
    ![循環狀態](../images/Home2020_LoopStatus.png)
    
    在右側，圖示顯示循環狀態：
    
    * 綠色圓圈 = 循環運行中
    * 帶虛線的綠色圓圈 = [低血糖暫停 (LGS)](../SettingUpAaps/CompletingTheObjectives.md#objective-6-starting-to-close-the-loop-with-low-glucose-suspend)
    * 紅色圓圈 = 循環禁用（永久不工作）
    * 黃色圓圈 = 循環暫停（暫時停止，但基礎胰島素將會給予）- 下方圖示顯示剩餘時間
    * 灰色圓圈 = 幫浦已中斷連線（暫時沒有任何胰島素劑量）- 下方圖示顯示剩餘時間
    * 橙色圓圈 = 超量注射運行中 - 下方圖示顯示剩餘時間
    * 帶虛線的藍色圓圈 = 開放循環
    
    輕按或長按圖示以開啟循環對話框以切換循環模式（關閉、低血糖暫停、開放或禁用），暫停/重新啟用循環或中斷/重新連線幫浦。
    
       * 如果輕按循環圖示，則在選擇循環對話框後需要進行驗證
    
       ![循環狀態選單](../images/Home2020_Loop_Dialog.png)
    
    #### 血糖警告標誌
    
    如果 **AAPS** 接收到的血糖讀取值出現任何問題，您會在主畫面上的血糖數字下方收到警告信號。
    
    ##### 紅色警告標誌：重複的血糖數據
    
    紅色警告標誌提醒您立即行動：您正在接收 **重複的血糖數據**，這會妨礙循環的正常運作。 因此，您的循環將會被禁用，直到問題解決。
    
    ```{admonition} 您的循環未運行
    :class: note
    在解決此問題之前，您的循環不會運行！
    

![紅色血糖警告](../images/bg_warn_red.png)

你需要找出為什麼會收到重複的血糖資料：

* 您的 Nightscout 網站上是否啟用了 Dexcom 橋接？ 通過進入 Nightscout 實例的管理面板，編輯 "enable" 變數並刪除其中的 "bridge" 部分來禁用橋接。 （有關 heroku 的[詳細資訊可以在此找到](https://nightscout.github.io/troubleshoot/troublehoot/#heroku-settings)。）
* 是否有多個來源將您的血糖上傳到 Nightscout？ 如果您使用 BYODA 應用程式，請在 **AAPS** 中啟用上傳，但不要在 xDrip+ 中啟用。
* 您是否有任何可能會接收您的血糖並再次上傳到您的 Nightscout 網站的追蹤者？
* 最後的手段：在 **AAPS** 中，請前往 [偏好設定 > NSClient](../SettingUpAaps/Preferences.md#nsclient)，選擇同步設定並禁用 "接受來自 NS 的 CGM 數據" 選項。

要立即移除警告並重新啟動循環，您需要手動刪除 Dexter/xDrip+ 標籤中的幾個條目。

然而，當有很多重複項目時，可能更容易

* [備份您的設定](../Maintenance/ExportImportSettings.md)，
* 在維護選單中重置你的資料庫，然後
* [再次匯入您的設定](../Maintenance/ExportImportSettings.md)

##### 黃色警告標誌

黃色警告信號表示您的血糖數據抵達的不規則時間間隔或某些血糖數據缺失。 按壓標誌時，訊息顯示「使用了重新計算的數據」。

![黃色血糖警告](../images/bg_warn_yellow.png)

通常你不需要採取任何行動。 閉環會繼續運作！

由於感測器更換會中斷血糖數據的連續流動，因此在感測器更換後出現黃色警告標誌是正常的，無需擔心。

Libre 使用者的特殊注意事項：

* 每個 Libre 感應器每隔幾小時都會慢個一兩分鐘，這意味著你永遠無法獲得完美的定期血糖間隔。
* 此外，波動的讀取值會中斷連續流動。
* 因此，對於 Libre 使用者來說，黃色警告標誌將「始終開啟」。

*注意*: 在 **AAPS** 計算中，最多考慮 30 小時的數據。 因此，即使你解決了問題，黃三角標誌可能會在最後一次不規則間隔發生後大約 30 小時內消失。

### D 區 - 胰島素、碳水化合物、基礎率與自動敏感性

![D 區](../images/Home2020_TBR.png)

**注射器**: 體內的胰島素量 (IOB) - 你身體內活性胰島素的數量

* 如果僅運作標準基礎率，且沒有先前注射的胰島素剩餘，則 IOB 為零。 
* 如果最近有減少的基礎率，IOB 可能為負值。
* 按圖示可查看注射胰島素與基礎胰島素的分配情況。

* **碳水化合物**: [體內碳水化合物 (COB)](CobCalculation) - 你之前吃但尚未吸收的碳水化合物 如果需要碳水化合物，圖示呈紅色閃爍（請參閱[下方](#carbs-required)）

* **紫色線**: 當前的基礎率。 圖示會根據基礎率的臨時變化而改變（維持在 100%） 
   * 按圖示可查看基礎基礎率和任何臨時基礎率的詳細資訊（包括剩餘時間）。
* **上下箭頭**: 表示實際的 [自動感測](KeyAapsFeatures#autosens) 狀態（啟用或停用），數值顯示在圖示下方

#### 需要碳水化合物

![需要碳水化合物](../images/Home2020_CarbsRequired.png)

當系統偵測到需要碳水化合物時，會提供碳水化合物建議。

當 oref 演算法認為無法透過零基礎補救時，你需要碳水化合物來修正。

碳水化合物的通知會比注射計算機的通知更為精準。 你可能會看到碳水化合物建議，而注射計算機未顯示缺少的碳水化合物。

如果有需要，碳水化合物需求通知可以推送到 Nightscout，屆時會顯示並廣播公告。

### E 區 - 狀態指示燈

![E 區](../images/Home2020_StatusLights.png)

狀態指示燈為以下情況提供視覺警告：

* 輸注針頭的使用時間
* 胰島素的使用時間（儲液罐使用的天數）
* 儲液罐的剩餘容量（單位）
* 傳感器使用時間
* 電池使用時間及電量（百分比）

如果超過警告門檻值，數值將顯示為黃色。

如果超過危急門檻值警告，數值將顯示為紅色。

可以在 [偏好設定 > 總覽 > 狀態燈](../SettingUpAaps/Preferences.md#status-lights) 中更改設置。

根據你使用的幫浦，你可能不會擁有所有這些圖示。

### F 區 - 主圖表

![F 區](../images/Home2020_MainGraph.png)

圖表顯示你的血糖 (BG)，從你的血糖傳感器 (CGM) 讀取。

在操作標籤中輸入的筆記（如手指校準和碳水化合物輸入）以及設定檔切換也會顯示在此處。

長按圖表可更改時間尺度。 你可以選擇 6、12、18 或 24 小時。

綠色區域反應你的目標範圍。

藍色三角形顯示 [微量注射 (SMB)](KeyAapsFeatures#super-micro-bolus-smb) - 如果在 [偏好設定 > OpenAPS SMB](../SettingUpAaps/Preferences.md#openaps-smb-settings) 中啟用。

#### 啟用可選資訊

在主圖表上，你可以開啟這些可選資訊：

* 預測
* 基礎率
* 活動 - 胰島素活動曲線

要顯示這些資訊，請點擊主圖表右側的三角形。 對於主圖表，只有位於 "\---\---- 圖表 1 \---\----" 以上的三個選項可用。

    ![主圖表設定](../images/Home2020_MainGraphSetting.png)
    

#### 預測線

* **橘色**線: [碳水化合物在體內 (COB)](CobCalculation)（顏色一般用於代表 COB 和碳水化合物）
   
   此預測線顯示你的血糖 (BG) 將會如何變化，該變化是根據當前**設定檔**設定推測的，假設由碳水化合物吸收導致的偏差保持不變。 此線僅在有已知的 COB 時出現。

* **深藍色**線: IOB（顏色一般用於代表 IOB 和胰島素）
   
   此預測線顯示在僅受胰島素影響下會發生什麼。 例如，如果你調整了一些胰島素，然後沒有吃任何碳水化合物。

* **淺藍色**線：零基礎率（如果設置了 0% 的臨時基礎率，預測血糖會怎麼變化）
   
   此預測線顯示如果幫浦停止所有胰島素輸送（0% TBR），血糖軌跡線將如何改變。
   
   *這條線僅在使用[SMB](../SettingUpAaps/ConfigBuilder.md#aps)算法時顯示。*

* **深黃色**線: [未公告餐 (UAM)](../DailyLifeWithAaps/SensitivityDetectionAndCob.md#sensitivity-oref1)
   
   未輸入的餐點(UAM)表示偵測到由於用餐、腎上腺素或其他影響導致的血糖顯著上升。 預測線類似於**橘色的 COB 線**，但它假設偏差會以恆定速率減少（延長當前減少的速率）。
   
   *這條線僅在使用[SMB](../SettingUpAaps/ConfigBuilder.md#aps)算法時顯示。*

* **深橙色**線：aCOB（加速碳水化合物吸收）
   
   類似於 COB，但假設碳水化合物吸收率為每 5 分鐘 10 mg/dL（-0.555 mmol/l/5 分鐘）。 已棄用，實用性有限。
   
   *這條線僅在使用較舊的[AMA](../SettingUpAaps/ConfigBuilder.md#aps)算法時顯示。*

通常你的實際血糖曲線最終會位於這些線之間，或接近最符合你情況的假設。

#### 基礎率

一條**實心藍色**線顯示你的幫浦基礎胰島素輸送，並反應實際的輸送時間。

一條**虛線藍色**線顯示如果沒有暫時的基礎率調整（TBR），基礎率會是什麼。

當提供標準基礎率時，曲線下方的區域以深藍色顯示。 當基礎率臨時調整（增加或減少）時，曲線下方的區域會以淺藍色顯示。

#### 活動

一條**細黃色**線顯示胰島素的活動。

他基於胰島素在系統中的預期血糖降低，如果沒有其他因素（如碳水化合物）存在。

### G 區 - 其他圖表

你可以在主圖表下啟用最多四個其他圖表。

要開啟額外圖表的設定，點擊[主圖表](#section-f---main-graph)右側的三角形並向下滾動。

![其他圖表設置](../images/Home2020_AdditionalGraphSetting.png)

要添加另一個圖表，請勾選其名稱左側的方框（例如：\---\---- 圖表 1 \---\----）。

大多數使用者發現以下附加圖表配置足夠：

* 圖表 1 包含 IOB、COB、敏感度
* 圖表 2 包含偏差和 BGI。

#### 絕對胰島素

活動中的胰島素，包括注射**和基礎率**。

#### 活性胰島素(IOB)

顯示你體內的胰島素（= 體內的活動胰島素）。 包括注射胰島素和臨時的基礎率（**但不包括你設定檔中的基礎率**）。

如果在DIA期間沒有任何[SMB](KeyAapsFeatures#super-micro-bolus-smb)、沒有注射和沒有TBR，則這將為零。

如果沒有剩餘注射且長時間設置為零/低基礎率，IOB 可能為負值。

衰減取決於您的[DIA和胰島素設定檔](../SettingUpAaps/YourAapsProfile.md)。

#### 活性碳水化合物(COB)

顯示你體內的碳水化合物（= 活動中的，但尚未衰減的碳水化合物）。

衰減取決於 [演算法檢測的偏差](../DailyLifeWithAaps/CobCalculation.md)。

如果他偵測到碳水化合物吸收率高於預期，將注射胰島素，這將增加 IOB（多或少，取決於你的安全設置）。

#### 敏感性

顯示[自動感知](KeyAapsFeatures#autosens)檢測到的敏感度。

敏感性是運動、荷爾蒙等導致的對胰島素的敏感性計算結果。

#### 心率

使用 [Garmin 智慧手錶](../UsefulLinks/WearOsSmartwatch.md#garmin) 時，該資料可能可用。

#### 偏差

* **灰色**條顯示因碳水化合物引起的偏差。 
* **綠色**條顯示血糖高於演算法預期的範圍。 綠色條用來增加[自動感知](KeyAapsFeatures#autosens)的抵抗力。
* **紅色**條顯示血糖低於演算法預期的範圍。 紅色條用來增加[自動感知](KeyAapsFeatures#autosens)的敏感度。
* **黃色**條顯示因用餐而引起的偏差。
* **黑色**條顯示未考慮敏感度的小偏差

#### 血糖變化率

這條線顯示基於胰島素活動，血糖應該上升或下降的程度。

![主畫面按鈕](../images/Screenshots_DEV_BGI.png)

將此線與偏差條一起顯示是一個很好的組合。 它們共享相同的尺度，但與其他可選資料的尺度不同，因此最好將它們顯示在單獨的圖表上，如上所示。 比較 BGI 線和偏差條是了解**血糖**波動的另一種方式。 在標記**1**的時間，此時偏差條大於 BGI 線，顯示血糖正在上升。 稍後，在標記**2**的時間，BGI 和 DEV 幾乎一致，顯示血糖穩定。

### H 區 - 按鈕

![主畫面按鈕](../images/Home2020_Buttons.png)

胰島素、碳水化合物和計算機的按鈕幾乎總是可見的。 如果與幫浦的連線中斷，胰島素按鈕將不會顯示。

其他按鈕可以在 [偏好設定 > 總覽 > 按鈕](../SettingUpAaps/Preferences.md#buttons) 中設定。

關於使用胰島素、碳水化合物和計算機按鈕：如果在 [偏好設定 > 總覽](../SettingUpAaps/Preferences.md#show-notes-field-in-treatments-dialogs) 中啟用，**註記**欄位允許你輸入將顯示在主圖表上的文本，並可能根據你的 NS 客戶端設定上傳到 Nightscout。

#### 胰島素

![注射按鈕](../images/Home2020_ButtonInsulin.png)

要在不使用[注射計算器](#bolus-wizard)的情況下給予特定的胰島素量。

透過勾選 **起始餐前 TT**方框，你可以自動啟動你的 [即將進餐的臨時目標](../DailyLifeWithAaps/TempTargets.md#eating-soon-temp-target)。

如果你不想透過幫浦注射，但想記錄一次胰島素注射（例如：使用筆注射的胰島素），請勾選相應的方框。 勾選此方框時，你將獲得一個額外欄位「時間偏移」，可用來記錄過去進行的胰島素注射。

您可以使用按鈕快速增加胰島素的量。 增量值可以在 [偏好設定 > 總覽 > 按鈕](../SettingUpAaps/Preferences.md#buttons) 中更改。

#### 碳水化合物

![碳水化合物按鈕](../images/Home2020_ButtonCarbs.png)

記錄碳水化合物而不進行注射。

某些[預設的臨時目標](../DailyLifeWithAaps/TempTargets.md#hypo-temp-target)可以直接通過勾選框來設置。

**時間偏移**: 您何時/曾經吃過碳水化合物（以分鐘計）。

**持續時間**: 用於 [“延長碳水化合物”](ExtendedCarbs)

您可以使用按鈕快速增加碳水化合物的量。 增量值可以在 [偏好設定 > 總覽 > 按鈕](../SettingUpAaps/Preferences.md#buttons) 中更改。

#### 計算機

請參閱注射嚮導 [下方章節](#bolus-wizard)。

#### 校準

發送校準至 xDrip+ 或打開 Dexcom 校準對話框。

必須在 [偏好設定 > 總覽 > 按鈕](../SettingUpAaps/Preferences.md#buttons) 中註冊。

#### CGM

開啟 xDrip+。

返回按鈕將返回到 **AAPS**。

必須在 [偏好設定 > 總覽 > 按鈕](../SettingUpAaps/Preferences.md#buttons) 中註冊。

#### 快速嚮導

輕鬆輸入碳水化合物數量並設置計算基礎。

詳細信息在 [偏好設定 > 總覽 > 快速嚮導設定](../SettingUpAaps/Preferences.md#quick-wizard) 中設置。

## 注射嚮導

![注射嚮導](../images/Home2020_BolusWizard_v2.png)

當您想要進行餐前注射時，通常會從此處發起。

### I 區

顯示計算出的注射劑量。

如果活性胰島素（IOB）的量已超過計算出的注射劑量，那麼他只會顯示仍然需要的碳水化合物數量。

### J 區

血糖 欄位通常會自動填充最新的 CGM 讀取值。 如果你沒有使用中的 CGM，則該欄位將保持空白。

在 **碳水化合物** 欄位中，您可以添加您估算的碳水化合物數量或等效值，以進行注射。

如果您想基於某些理由修改最終劑量，請使用 **Corr** 欄位。

**碳水化合物時間** 欄位用於預注射，讓系統知道在預期碳水化合物之前會有延遲。 如果你是為之前的碳水化合物進行注射，你可以在此欄位中輸入負數。

**進食提醒** : 對於未來的碳水化合物，可以選擇啟用警報 checkbox（當未來時間被輸入時預設啟用），以便您可以在給定的時間受到提醒，提醒您進食已輸入到**AAPS**中的碳水化合物。

![帶有用餐提醒的注射嚮導](../images/Home2021_BolusWizard_EatingReminder.png)

### K 區

**設定檔** 允許您選擇與當前不同的設定檔，以計算所需的胰島素。 此設定檔的選擇僅適用於當前的注射，不會變更設定檔。

**超注射** 是指將未來兩小時的基礎胰島素加到即時的注射中，並在接下來的兩小時內發出零臨時基礎率來回收額外的胰島素。 該選項僅在「啟用超注射於嚮導中」在 [偏好設定 > 總覽 > 高級設定](../SettingUpAaps/Preferences.md#advanced-settings-overview) 中設置時顯示。 其目的是更快地注射胰島素，希望減少血糖高峰。

詳情請查看[diabetesnet.com](https://www.diabetesnet.com/diabetes-technology/blue-skying/super-bolus/)。

### L 區

嚮導的注射計算詳細信息。

您可以取消選擇不想包括的項目，但通常您不會這樣做。

出於安全原因，**TT 盒必須手動勾選**，如果您想讓注射嚮導根據現有的臨時目標進行計算。

#### COB 和 IOB 的組合及其含義

* 出於安全原因，當 COB 盒已勾選時，無法取消勾選 IOB 盒，因為這樣可能會導致胰島素過多，因為 **AAPS** 不會考慮已經給予的胰島素。
* 如果您同時勾選 COB 和 IOB，未被胰島素覆蓋的碳水化合物 + 所有作為臨時基礎率或微量注射給予的胰島素都會被考慮在內。
* 如果您勾選 IOB 而不勾選 COB，**AAPS** 將考慮已給予的胰島素，但不會將其抵消任何仍需吸收的碳水化合物。 這會導致“缺少碳水化合物”的提示。
* 如果你在餐後注射胰島素後，為了**額外食物**（如額外的甜點）再進行注射，最好取消勾選所有選項。 這樣只會加入新增的碳水化合物，因為主餐不一定會立刻被吸收，因此餐後的 IOB 和 COB 不會馬上精確匹配。

![注射嚮導與詳細信息](../images/Home2021_BolusWizard_Details.png)

眼睛旁邊的框允許您在詳細視圖（每個項目進行計算的數字）和簡單視圖（圖示）之間進行選擇。 按一下圖示將啟用/禁用該條目從計算中。

#### 錯誤的 COB 偵測

![碳水化合物吸收緩慢](../images/Calculator_SlowCarbAbsorption.png)

如果您在使用注射嚮導後看到上述警告，**AAPS** 已檢測到計算的 COB 值可能是錯誤的。 因此，如果您想在之前進食後再次注射 COB，您應該注意過量注射！

有關詳細信息，請參見[COB計算頁面](CobCalculation#detection-of-wrong-cob-values)上的提示。

## 操作標籤

![操作標籤](../images/Home2021_Action.png)

### 操作 - M 區

按鈕**[設定檔切換](../DailyLifeWithAaps/ProfileSwitch-ProfilePercentage.md#profile-switch--profile-percentage)**作為按壓[主畫面當前設定檔](#section-b---profile--target)的替代項。

按鈕**[臨時目標](../DailyLifeWithAaps/TempTargets.md)**作為按壓[主畫面當前目標](#section-b---profile--target)的替代項。

啟動或取消臨時基礎率的按鈕。 請注意，當設置了臨時基礎率時，按鈕將從“TEMPBASAL”變為“CANCEL x%”。

儘管[延長注射](ExtendedCarbs#extended-bolus-and-why-they-wont-work-in-closed-loop-environment)在封閉循環環境中實際上無法運作，但有些人還是要求提供使用延長注射的選項。

* 此選項僅適用於 Dana RS 和 Insight 幫浦。 
   * 閉環將自動停止並切換為開環模式，以運作延長注射。
   * 在使用此選項之前，務必閱讀[詳細資訊](ExtendedCarbs)。

### 護理入口 - N 區

顯示以下資訊:

    * 感測器年齡 & 水準（電池百分比）
    * 胰島素年齡 & 水準（單位）
    * 輸管年齡
    * 幫浦電池年齡 & 水準（百分比）
    

如果使用**低解析度外觀**，將顯示較少資訊（[偏好設定 > 一般 > 外觀](../SettingUpAaps/Preferences.md#skin)）。

#### 傳感器電量（電池）

適用於具有額外發射器的 CGM，例如 MiaoMiao 2。 （技術上，傳感器必須將電量資訊傳送至 xDrip+。）

門檻值可以在 [偏好設定 > 總覽 > 狀態燈](../SettingUpAaps/Preferences.md#status-lights) 中設置。

如果感測器水準與手機電池水準相同，則您的 xDrip+ 版本可能過舊且需要更新。 (需要 xDrip+ 每日版本 2020年12月10日或更新版本。） 這將使您能夠回溯 **AAPS** 的歷史紀錄。

    ![感測器等於手機電池電量](../images/Home2021_ActionSensorBat.png)
    

### 護理入口 - O 區

BG檢查、預備/填充、傳感器插入和幫浦電池更換是[N部分](#careportal---section-n)中顯示資料的基礎。

填充/注入允許你記錄幫浦部位和胰島素筒的更換。

O 區反應了 Nightscout 的護理入口功能。 因此，運動、公告和問題是特別的筆記形式。

### 工具 - P 區

#### 歷史瀏覽器

允許您回溯在 **AAPS** 中的歷史記錄。

#### 每日總劑量(TDD)

每日總劑量 = 每日的注射量 + 基礎率

一些醫生（尤其是新使用幫浦者）使用 50:50 的基礎-注射比例。

因此，比例計算為 TDD / 2 * TBB（總基礎胰島素 = 24小時內基礎速率之和）。

其他人則更喜歡 TDD 的 32% 至 37% 範圍作為 TBB。

如同大多數此類經驗法則，這種方法的實際有效性有限。 注意：每個人的糖尿病狀況都不同！

![歷史瀏覽器 + TDD](../images/Home2021_Action_HB_TDD.png)

## 胰島素設定檔

![胰島素設定檔](../images/Screenshot_insulin_profile.png)

這顯示您在[組態設置工具](../SettingUpAaps/ConfigBuilder.md#insulin)中選擇的胰島素的活動特徵。

**紫色** 線顯示在注射後胰島素量隨時間衰減的情況，**藍色** 線顯示其活性狀態。 需要注意的重要點是衰減具有**長尾巴**。 如果您習慣手動注射，可能已經習慣認為胰島素的衰減大約需要 3.5 小時。 然而，當您在迴路中時，長尾巴的關鍵在於計算非常精確，這些小數量在 **AAPS** 算法進行遞迴計算時都會累加。

有關不同類型的胰島素、他們的活性設定檔以及為什麼這些很重要的更多詳細討論，你可以閱讀這篇文章[暸解基於指數活性曲線的新 IOB 曲線](https://openaps.readthedocs.io/en/latest/docs/While%20You%20Wait%20For%20Gear/understanding-insulin-on-board-calculations.html#understanding-the-new-iob-curves-based-on-exponential-activity-curves)

你還可以在這裡閱讀一篇出色的部落格文章：[我們經常在使用的胰島素作用時間（DIA）上出錯的原因以及為什麼這很重要...](https://www.diabettech.com/insulin/why-we-are-regularly-wrong-in-the-duration-of-insulin-action-dia-times-we-use-and-why-it-matters/)

更多資訊請查看：[指數胰島素曲線 + Fiasp](https://web.archive.org/web/20220630154425/http://seemycgm.com/2017/10/21/exponential-insulin-curves-fiasp/)

## 幫浦狀態

![幫浦狀態](../images/Screenshot_PumpStatus.png)

* 顯示幫浦狀態的不同資訊。 顯示的資訊取決於你的幫浦型號。
* 詳情請參見[幫浦頁面](../Getting-Started/CompatiblePumps.md)。

## 閉環、AMA / SMB

這些選項卡顯示有關算法計算的詳細信息，以及**AAPS** 為何這樣運作。

每次系統從 CGM 獲取新讀取值時，計算都會運行。

有關更多詳細資訊，請參見[組態設置工具頁面的APS部分](../SettingUpAaps/ConfigBuilder.md#aps)。

## 設定檔

![設定檔](../images/Screenshots_Profile.png)

設定檔包含有關你個人糖尿病設定的資訊：

    * DIA（胰島素作用持續時間）
    * IC 或 I:C: 胰島素與碳水化合物比例
    * ISF: 胰島素敏感性係數
    * 基礎速率
    * 目標: 您希望<strong>AAPS</strong> 針對的血糖水準
    

請參閱詳細的 **[設定檔](../SettingUpAaps/YourAapsProfile.md)** 頁面以獲取更多資訊。

## 自動化

請參閱專門的頁面 [這裡](../DailyLifeWithAaps/Automations.md)。

## NSClient

![NSClient](../images/Screenshots_NSClient.png)

此頁面顯示與您的 Nightscout 網站的連線狀態。

設定可以在 [偏好設定 > NS 客戶端](../SettingUpAaps/Preferences.md#nsclient) 中進行更改。

如遇故障，請參考此[頁面](../GettingHelp/TroubleshootingNsClient.md)。

## 血糖來源 - xDrip+、BYODA...

![血糖資料來源標籤 - 這裡是 Nightscout](../images/Screenshots_BGSource.png)

根據您的 BG 資料來源設定，此標籤的名稱會有所不同。

顯示 CGM 讀取的歷史紀錄並提供選項刪除失敗（例如：壓縮低）或重複讀取情況下的值。

## 治療

可以通過按下選單右側的 3 個點來訪問此視圖，然後選擇「治療」。 無法通過 Config Builder 在主選單中顯示它。 在此視圖中，您可以查看和修改以下治療的歷史紀錄：

* 注射與碳水化合物
* [延長注射](../DailyLifeWithAaps/ExtendedCarbs.md#extended-bolus-and-switch-to-open-loop---dana-and-insight-pump-only)
* 臨時基礎率
* [臨時目標](../DailyLifeWithAaps/TempTargets.md)
* [設定檔切換](../DailyLifeWithAaps/ProfileSwitch-ProfilePercentage.md)
* 照護入口：通過動作標籤輸入的筆記和對話中的筆記
* 用戶輸入：其他未發送至 Nightscout 的筆記

在最後一欄中，每行的資料來源以藍色顯示。 它可以是：

* NS 表示 Nightscout：資料來自或已記錄到 Nightscout
* PH 表示幫浦歷史：資料已由幫浦處理

### 注射與碳水化合物

![碳水化合物與注射](../images/TreatmentsView1.png)

在此標籤中，您可以查看注射和碳水化合物的紀錄。 每次注射（第**1**行和**4**行）在胰島素數量旁邊顯示相關的剩餘 IOB。 注射的來源可以是：

* 餐前（通過胰島素、快速嚮導或注射嚮導按鈕手動輸入）
* 當使用 SMB 功能時的 SMB

碳水化合物（第**2**行）僅存儲在 Nightscout 中。 如果您使用 [注射嚮導](#bolus-wizard) 計算胰島素劑量，您可以按下「計算」文字（第**3**行）以顯示注射計算的詳細信息。

根據使用的幫浦，胰島素和碳水化合物可以顯示在一行中，或者會導致多行顯示：一行顯示計算詳細信息，一行顯示碳水化合物，一行顯示注射本身。

治療標籤可以用來修正錯誤的碳水化合物輸入（例如：您高估或低估了碳水化合物）。 請注意，無法編輯現有的輸入，您需要遵循以下過程：

1. 在主畫面檢查並記住實際的 COB 和 IOB。
2. 根據幫浦的不同，在治療標籤中碳水化合物可能與胰島素一起顯示在同一行，或作為單獨的項目顯示（如 Dana RS）。
3. 移除碳水化合物數量錯誤的項目。 (最新版本在治療螢幕上有垃圾桶圖示。 按一下垃圾桶圖示，選擇要刪除的行，然後再次按垃圾桶圖示以完成刪除。)
4. 再次檢查主畫面上的 COB 以確保成功移除了碳水化合物。
5. 如果治療標籤中包含碳水化合物和胰島素的條目是單行的，請對 IOB 執行相同操作。
   
   → 如果碳水化合物未按照預期移除，並且您如這裡所述（6.）添加額外碳水化合物，COB 將過高，這可能導致胰島素給藥過量。

6. 透過主畫面的碳水化合物按鈕輸入正確的碳水化合物數量，並確保設置正確的事件時間。

7. 如果治療標籤中包含碳水化合物和胰島素的條目是單行的，你還必須添加胰島素的數量。 確保設置正確的事件時間，並在確認新條目後檢查主畫面上的 IOB。

### 臨時基礎速率

![臨時基礎速率](../images/TreatmentsView2.png)

循環應用的 **臨時基礎** 在此顯示。 當某個輸入的 IOB 仍有影響時，資訊會以綠色顯示。 它可以是：

* 正 IOB 如果臨時基礎高於設定檔中的基礎（第**2**行）
* 負 IOB 針對零臨時或如果臨時基礎低於設定檔中的基礎（第 **1**行）

刪除輸入僅影響您在 Nightscout 的報告，並可能影響您的實際 IOB - 不建議這樣做。

在行的左側，紅色 S 代表「暫停」：當基礎目前未給藥時會發生。 這在更換藥囊過程中是一個正常情況，例如。

### 臨時目標

![臨時目標](../images/TreatmentsView3.png)

臨時目標的歷史可以在這裡查看。

### 設定檔切換

![設定檔切換](../images/TreatmentsView4.png)

設定檔切換的歷史可以在這裡查看。 每次切換設定檔時，您可能會看到多條條目：第**1**行，存儲在 Nightscout 中但不在幫浦歷史中，對應於用戶進行的設定檔切換請求。 第**2**行，存儲在 NS 和 PH 中，對應於實際切換。

刪除輸入僅影響您在 Nightscout 的報告，永遠不會實際更改當前的設定檔。

### 照護入口

![照護入口](../images/TreatmentsView5.png)

此標籤顯示所有在 Nightscout 中記錄的筆記和警報。

## 歷史瀏覽器

可以通過按下選單右側的 3 個點然後選擇「歷史」來訪問此視圖。 無法通過 Config Builder 在主選單中放入它。 還可以通過 [動作標籤](#action-tab) 底部的一個按鈕訪問。

允許您回溯在 **AAPS** 中的歷史記錄。

## 設定檔助手

此視圖可以通過按下選單右側的 3 個點然後選擇「設定檔助手」來訪問。 無法通過 Config Builder 在主選單中放入它。 [設定檔助手](../SettingUpAaps/ProfileHelper.md) 可以幫助您：

* 從零開始為小孩建立設定檔
* 比較兩個設定檔
* 複製一份設定檔