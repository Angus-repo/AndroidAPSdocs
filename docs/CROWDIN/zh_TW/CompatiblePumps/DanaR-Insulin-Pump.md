# DanaR Pump

_這些說明適用於配置該應用程式與 DanaR 幫浦。  如果您擁有 2017 年推出的 DanaRS，請訪問[DanaRS 胰島素幫浦](./DanaRS-Insulin-Pump.md)。_

* In the pump go to Main Menu > Setting > User Option
* Turn on "8. Extended Bolus"

![DanaR pump](../images/danar1.png)

* 進入主選單 > 設置 > 探索
* 在手機設置中進入藍牙，掃描附近的設備，選擇你的 DanaR 序列號，並輸入你的密碼（配對密碼為 0000）。  如果 DanaR 未出現在掃描中，請重新啟動手機並將 DanaR 電池取出，重新安裝，然後再次開始這兩個步驟。

* 在 AAPS 中進入組態建置工具並選擇你擁有的 DanaR 型號（DanaR、DanaR 韓國版、DanaRv2）。
* 點擊右上角的三個點選擇選單。 選擇偏好設定。
* 選擇 DanaR 藍牙設備，然後點擊你的 DanaR 序列號。
* 選擇幫浦密碼，並輸入你的密碼。 （預設密碼為 1234）
* 如果你希望 AAPS 允許基礎速率超過 200%，啟用使用超過 200% 的延時注射。 注意，這意味著在使用延時注射進行用餐時，你無法使用高 TBR 循環。
* In Preferences under DanaR pump settings you can change the default bolus speed used (12sec per 1u, 30sec per 1u or 60sec per 1u).
* Set basal step on pump to 0.01 U/h
* Set bolus step on pump to 0.1 U/h
* Enable extended boluses on pump

## Timezone traveling with Dana R pump

For information on traveling across time zones see section [Timezone traveling with pumps](../DailyLifeWithAaps/TimezoneTraveling-DaylightSavingTime.md#danarv2-danars).
