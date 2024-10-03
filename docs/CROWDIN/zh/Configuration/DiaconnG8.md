# Diaconn G8 胰島素幫浦

## Insulin Pump Bluetooth Pairing

- Click on the hamburger menu in the top left corner.

![圖像](../images/DiaconnG8/DiaconnG8_01.jpg)

- Click on Config Builder.

![圖像](../images/DiaconnG8/DiaconnG8_02.jpg)

- After selecting the Diaconn G8 Pump click on the Settings icon (cog wheel).

![圖像](../images/DiaconnG8/DiaconnG8_03.jpg)

- Choose Selected pump.

![圖像](../images/DiaconnG8/DiaconnG8_04.jpg)

- Select your insulin pump’s model number once it appears in the list.

![圖像](../images/DiaconnG8/DiaconnG8_05.jpg)

- 有兩種方法來檢查您的型號：

1. 幫浦背面的 SN 編號的最後五位數字。
2. Click on O button > Information > BLE > Last 5 digits.

![圖像](../images/DiaconnG8/DiaconnG8_06.jpg)

- Once you select your pump, a window appears asking for a pin code. Enter the pin number displayed on your pump to complete the connection.

![圖像](../images/DiaconnG8/DiaconnG8_07.jpg)

## Pump status check and log synchronization

- Once your pump is connected, click on the Bluetooth symbol to check the status and to synchronize logs.

![圖像](../images/DiaconnG8/DiaconnG8_08.jpg)

## 藍牙疑難排解

**What to do in the case of an unstable Bluetooth connection with the pump.**

### Method 1 ) Check the pump again after AAPS application is completed.

- Click on the 3 dots button on the top right.

![圖像](../images/DiaconnG8/DiaconnG8_09.jpg)

- Click on Exit.

![圖像](../images/DiaconnG8/DiaconnG8_10.jpg)

### 方法 2) 如果第一種方法無效，中斷藍牙然後重新連線。

- 按住頂部的藍牙按鈕約 3 秒鐘。

![圖像](../images/DiaconnG8/DiaconnG8_11.jpg)

- Click on the Setting button on the paired Diaconn G8 Insulin pump.

![圖像](../images/DiaconnG8/DiaconnG8_12.jpg)

- Unpair.

![圖像](../images/DiaconnG8/DiaconnG8_13.jpg)

- Repeat the Bluetooth pairing process for the pump (see above).

## 更多資訊

### Diaconn G8 胰島素幫浦選項設定

- 設定管理器 > 幫浦 > Diaconn G8 > 設定
- DIACONN G8 在頂部> 右上角三點按鈕 > Diaconn G8 偏好設定

![Diaconn G8 幫浦選項](../images/DiaconnG8/DiaconnG8_14.jpg)

- If the **Log reservoir change** option is activated, the relevant details are automatically uploaded to the careportal when an “Insulin Change” event occurs.
- If the **Log needle change** option is activated, the relevant details are automatically uploaded to the careportal when a “Site Change” event occurs.
- If the **Log tube change** option is activated, the relevant details are automatically uploaded to the careportal when a “Tube Change” event occurs.
- If the **Log battery change** option is activated, the relevant details are automatically uploaded to the careportal when a “Battery Change” event occurs, and the PUMP BATTERY CHANGE button in the ACTION tab is deactivated. (Note: To change the battery, please stop all in-progress injection functions before proceeding.)

![Diaconn G8 操作選單](../images/DiaconnG8/DiaconnG8_15.jpg)

### 延長注射功能

- If you use extended bolus it will disable closed loop.
- 請參閱[本頁](Extended-Carbs-why-extended-boluses-won-t-work-in-a-closed-loop-environment)了解為何延長注射功能無法在循環模式下運作的詳情。
