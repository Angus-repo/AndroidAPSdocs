# Accu Chek Combo 幫浦

**This software is part of a DIY solution and is not a product, but requires YOU to read, learn and understand the system including how to use it. It is not something that does all your diabetes management for you, but allows you to improve your diabetes and your quality of life if you're willing to put in the time required. Don't rush into it, but allow yourself time to learn. You alone are responsible for what you do with it.**

(Accu-Chek-Combo-Pump-hardware-requirements)=

## 硬體需求

- 任何版本的 Roche Accu-Chek Combo（任何韌體版本皆支援）
- A Smartpix or Realtyme device together with the 360 Configuration Software to configure the pump. (Roche sends out Smartpix devices and the configuration software free of charge to their customers upon request.)
- 一部相容的手機：Android 手機，需安裝 LineageOS 14.1（前稱 CyanogenMod）或至少 Android 8.1（Oreo）。 從 AAPS 3.0 開始，Android 9 是必須的。 詳情請見[版本說明](https://androidaps.readthedocs.io/en/latest/Installing-AndroidAPS/Releasenotes.html#android-version-and-aaps-version)。 As of AAPS 3.0 Android 9 is mandatory. See [release notes](https://androidaps.readthedocs.io/en/latest/Installing-AndroidAPS/Releasenotes.html#android-version-and-aaps-version) for details.
- 使用 LineageOS 14.1 時，手機必須是 2017 年 6 月以後的版本，因為只有那時的改變才允許配對 Combo 幫浦。
- 可以在[AAPS 手機列表](https://docs.google.com/spreadsheets/d/1gZAsN6f0gv6tkgy9EBsYl0BQNhna0RDqA9QGycAqCQc/edit)文件中找到相容手機。
- Please be aware that this is not complete list and reflects personal user experience. You are encouraged to also enter your experience and thereby help others (these projects are all about paying it forward).
- 請注意，儘管 Android 8.1 允許與 Combo 通訊，但 AAPS 在 8.1 上仍有問題。
- For advanced users, it is possible to perform the pairing on a rooted phone and transfer it to another rooted phone to use with ruffy/AAPS, which must also be rooted. This allows using phones with Android < 8.1 but has not been widely tested: https://github.com/gregorybel/combo-pairing/blob/master/README.md

## 限制

- 不支援延長注射和多波段注射（請參閱[延長碳水化合物](../Usage/Extended-Carbs.md)）。
- Only one basal profile is supported.
- Setting a basal profile other than 1 on the pump or delivering extended boluses or multiwave boluses from the pump interferes with TBRs and forces the loop into low-suspend only mode for 6 hours as the the loop can't run safely under these conditions.
- 目前無法設置幫浦的時間和日期，因此[夏令時間變更](Timezone-traveling-accu-chek-combo)需要手動進行（你可以在晚上停用手機的自動時鐘更新，然後與幫浦時鐘一起在早上重新調整，以避免夜間警報）。
- Currently only basal rates in the range of 0.05 to 10 U/h are supported. This also applies when modifying a profile, e.g. when increasing to 200%, the highest basal rate must not exceed 5 U/h since it will be doubled. Similarly, when reducing to 50%, the lowest basal rate must be at least 0.10 U/h.
- If the loop requests a running TBR to be cancelled the Combo will set a TBR of 90% or 110% for 15 minutes instead. This is because cancelling a TBR causes an alert on the pump which causes a lot of vibrations.
- 偶爾（大約每幾天），AAPS 可能無法自動取消 TBR 警報，用戶需要處理此問題（按下 AAPS 的重新整理按鈕以將警告傳送至 AAPS 或在幫浦上確認警報）。
- Bluetooth connection stability varies with different phones, causing "pump unreachable" alerts, where no connection to the pump is established anymore.
- 如果發生此錯誤，請確認藍牙已啟用，按下 Combo 標籤中的重新整理按鈕以檢查是否是臨時問題，如果仍無法建立連線，重啟手機，這通常能解決問題。
- There is another issue were a restart doesn't help but a button on the pump must be pressed (which resets the pump's Bluetooth), before the pump accepts connections from the phone again.
- There is very little that can be done to remedy either of those issues at this point. 目前對這些問題幾乎無法解決。 因此，如果你經常看到這些錯誤，目前唯一的選擇是換一部已知與 AAPS 和 Combo 幫浦相容的手機（請參閱上文）。
- Issuing a bolus from the pump will not always be detected in time (checked for whenever AAPS connects to the pump), and might take up to 20 minutes in the worst case.
- Boluses on the pump are always checked before a high TBR or a bolus issued by AAPS but due to the limitations AAPS will then refuse to issue the TBR/Bolus as it was calculated under false premises. (-> Don't bolus from the Pump! See chapter [Usage](Accu-Chek-Combo-Pump-usage) below)
- Setting a TBR on the pump is to be avoided since the loop assumes control of TBRs. 避免在幫浦上設定 TBR，因為循環控制 TBR。 在幫浦上偵測到新的 TBR 可能需要長達 20 分鐘，並且 TBR 的效果僅從偵測時開始計算，因此最壞情況下可能有 20 分鐘的 TBR 沒有反映在 IOB 中。

## 設定

- Configure the pump using 360 config software.
- If you do not have the software, please contact your Accu-Chek hotline. They usually send registered users a CD with the "360° Pump Configuration Software" and a SmartPix USB-infrared connection device (the Realtyme device also works if you have that).
- **必要設定**（在螢幕截圖中以綠色標示）：

  - Set/leave the menu configuration as "Standard", this will show only the supported menus/actions on the pump and hide those which are unsupported (extended/multiwave bolus, multiple basal rates), which cause the loop functionality to be restricted when used because it's not possible to run the loop in a safe manner when used.
  - Verify the _Quick Info Text_ is set to "QUICK INFO" (without the quotes, found under _Insulin Pump Options_).
  - 將 TBR _最大調整_ 設為 500%
  - Disable _Signal End of Temporary Basal Rate_
  - 將 TBR _持續時間增量_ 設定為 15 分鐘
  - 啟用藍牙
- **建議設定**（在螢幕截圖中以藍色標示）

  - 根據你的需求設置低匣警報
  - 配置一個適合你治療的最大注射量，以防軟體中的錯誤
  - Similarly, configure maximum TBR duration as a safeguard. Allow at least 3 hours, since the option to disconnect the pump for 3 hours sets a 0% for 3 hours.
  - Enable key lock on the pump to prevent bolusing from the pump, esp. when the pump was used before and quick bolusing was a habit.
  - Set display timeout and menu timeout to the minimum of 5.5 and 5 respectively. This allows the AAPS to recover more quickly from error situations and reduces the amount of vibrations that can occur during such errors

![用戶選單設定的截圖](../images/combo/combo-menu-settings.png)

![TBR 設定的截圖](../images/combo/combo-tbr-settings.png)

![注射設定的截圖](../images/combo/combo-bolus-settings.png)

![胰島素匣設定的截圖](../images/combo/combo-insulin-settings.png)

- 按照[AAPS wiki](https://androidaps.readthedocs.io/)中的描述安裝 AAPS
- 請務必閱讀 wiki 以了解如何設定 AAPS。
- 此時在 AAPS 中選擇 MDI 外掛，而非 Combo 外掛，以避免 Combo 外掛在配對過程中干擾 ruffy。
- 透過 git 從 [MilosKozak/ruffy](https://github.com/MilosKozak/ruffy) 進行 ruffy 的複製。 目前主要分支是 `combo` 分支，如果遇到問題，你也可以嘗試 'pairing' 分支（見下文）。 At the moment, the primary branch is the `combo` branch, in case of problems you might also try the 'pairing' branch (see below).
- Build and install ruffy and use it to pair the pump. If it doesn't work after multiple attempts, switch to the `pairing` branch, pair the pump and then switch back the original branch.
  If the pump is already paired and can be controlled via ruffy, installing the `combo` branch is sufficient.
  Note that the pairing processing is somewhat fragile (but only has to be done once)
  and may need a few attempts; quickly acknowledge prompts and when starting over, remove the pump device
  from the Bluetooth settings beforehand. Another option to try is to go to the Bluetooth menu after
  initiating the pairing process (this keeps the phone's Bluetooth discoverable as long as the menu is displayed)
  and switch back to ruffy after confirming the pairing on the pump, when the pump displays the authorization code.
  If you're unsuccessful in pairing the pump (say after 10 attempts), try waiting up to 10s before confirming the pairing on the pump (when the name of the phone is displayed on the pump). If you have configured the menu timeout to be 5s above, you need to increase it again. Some users reported they needed to do this. Lastly, consider moving from one room to another in case of local radio interference. At least one user immediately overcame pairing problems by simply changing rooms.
- 當 AAPS 使用 ruffy 時，ruffy 應用程式將無法使用。 最簡單的方式是 在配對過程後重啟手機，然後讓 AAPS 在背景中啟動 ruffy。 現在在手機上啟動 ruffy。 你可以按下重置！ 並移除舊的連線。 然後點擊**連線！**
- If the pump is completely new, you need to do one bolus on the pump, so the pump creates a first history entry.
- Before enabling the Combo plugin in AAPS make sure your profile is set up
  correctly and activated(!) and your basal profile is up to date as AAPS will sync the basal profile
  to the pump. Then activate the Combo plugin. Press the _Refresh_ button on the Combo tab to initialize the
  pump.
- To verify your setup, with the pump **disconnected**, use AAPS to set a TBR of 500% for 15 min and issue a bolus. The pump should now have a TBR running and the bolus in the history. AAPS should also show the active TBR and delivered bolus.

(Accu-Chek-Combo-Pump-why-pairing-with-the-pump-does-not-work-with-the-app-ruffy)=

## Why pairing with the pump does not work with the app "ruffy"?

There are serveral possible reasons. Try the following steps:

1. Insert a **fresh or full battery** into the pump. Look at the battery section for details. Make sure that the pump is very close to the smartphone.

![將 Combo 放在手機旁邊](../images/Combo_next_to_Phone.png)

2. 關閉或移除任何其他藍牙裝置，以防它們在配對過程中與手機建立連線。 任何平行的藍牙通訊或連線提示都可能干擾配對過程。 Any parallel bluetooth communication or prompt to establish connections might disturb the pairing process.

3. Delete already connected devices in the Bluetooth menu of the pump: **BLUETOOTH SETTINGS / CONNECTION / REMOVE** until
   **NO DEVICE** is shown.

4. 在手機的設定 / 藍牙中，刪除與手機已配對的幫浦裝置：移除配對的裝置 "**SpiritCombo**"

5. 確保 AAPS 不在背景執行循環。 停用 AAPS 中的循環。 在 AAPS 中啟用 Combo 外掛之前，請確保你的個人資料已正確設定並啟動（！），並且基礎率設定檔已更新，因為 AAPS 將會同步基礎率設定檔到幫浦上。 然後啟用 Combo 外掛。 按下 Combo 標籤上的_重新整理_按鈕以初始化 幫浦。

6. 嘗試使用[MilosKozak/ruffy](https://github.com/MilosKozak/ruffy/tree/pairing) 倉庫中的 '**pairing**' 分支來建立連線。

7. Now start ruffy on the phone. You may press Reset! and remove the old connection. Then hit **Connect!**.

8. In the Bluetooth menu of the pump, go to **ADD DEVICE / ADD CONNECTION**. Press _CONNECT!_\*
   - The next three steps are timing-sensitive, so you might need to try different pauses/speed if pairing fails. Read the full sequence before trying it.

9. Now the Pump should show up the BT Name of phone to select for pairing. Here it is importand to wait at least 5s
   before you hit the select button on Pump. Otherwise the Pumpe will not send the Paring request to the Phone proberly.

   - If Combo Pump is set to 5s Screentime out, you may test it with 40s (original setting). From experiance the time
     between pump is showing up in phone until select phone is around 5-10s. In many other cases pairing just times out
     without successfully pair. Later you should set it back to 5s, to meet AAPS Combo settings and speed up connections.
   - If the pump does not show the phone as a pairing device at all, your phone's Bluetooth stack is probably not
     compatible with the pump. Make sure you are running a new **LineageOS ≥ 14.1** or **Android ≥ 8.1 (Oreo)**. If
     possible, try another smartphone. 對於進階使用者，可以在已 root 的手機上進行配對，然後將其轉移到另一部已 root 的手機上使用 ruffy/AAPS，這兩部手機都需要 root。 這使得使用 Android 版本低於 8.1 的手機成為可能，但尚未廣泛測試：https://github.com/gregorybel/combo-pairing/blob/master/README.md

10. Sometimes the phone asks for a (typically 4 digit) bluetooth PIN number that is not related to the 10 digit PIN later shown on the pump. Usually, ruffy will set this PIN automatically, but due to timing issues, this does not always work. If a request for a Bluetooth pairing PIN appears on the phone before any code is shown on the pump, you need to enter **}gZ='GD?gj2r|B}>** as the PIN. This is easiest done if you copy this 16 character text into the clipboard before starting the pairing sequence and just paste it in the dialog at this step. See related [Github issue](https://github.com/MilosKozak/ruffy/issues/14) for details.

11. At next the pump should show up a 10 digit security code. And Ruffy shold show a screen to enter it. So enter the code in Ruffy and you
    should be ready to go.

12. If pairing was not successful and you got a timeout on the pump, you will need to restart the process from scratch.

13. If you have used the 'Pairing' branch to build the ruffy app, now install the version build from the 'combo' branch on top of it. Make sure that you have used the same keys when signing the two versions of the app to be able to keep all setting and data, as they also contain the connection properties.

14. 重啟手機。

15. 現在你可以重新啟動 AAPS 循環。

(Accu-Chek-Combo-Pump)=

## 使用說明

- 請記住，這不是一個產品，特別是 剛開始時，用戶需要監控並理解系統、其限制以及它如何可能失效。 強烈建議當使用者無法完全理解系統時，不要使用此系統。 It is strongly advised NOT to use this system when the person
  using it is not able to fully understand the system.
- 閱讀 OpenAPS 文件 https://openaps.org 以理解 AAPS 所基於的循環演算法 。
- 閱讀線上文件以學習和理解 AAPS https://androidaps.readthedocs.io/
- This integration uses the same functionality which the meter provides that comes with the Combo.
  The meter allows to mirror the pump screen and forwards button presses to the pump. The connection
  to the pump and this forwarding is what the ruffy app does. A `scripter` component reads the screen
  and automates entering boluses, TBRs etc and making sure inputs are processed correctly.
  AAPS then interacts with the scripter to apply loop commands and to administer boluses.
  This mode has some restrictions: it's comparatively slow (but well fast enough for what it is used for),
  and setting a TBR or giving a bolus causes the pump to vibrate.
- The integration of the Combo with AAPS is designed with the assumption that all inputs are
  made via AAPS. Boluses entered on the pump directly will be detected by AAPS, but it can take
  up to 20 min before AAPS becomes aware of such a bolus. Reading boluses delivered directly on
  the pump is a safety feature and not meant to be regularly used (the loop requires knowledge of carbs
  consumed, which can't be entered on the pump, which is another reason why all inputs should be done
  in AAPS).
- Don't set or cancel a TBR on the pump. The loop assumes control of TBR and cannot work reliably otherwise, since it's not possible to determine the start time of a TBR that was set by the user on the pump.
- The pump's first basal rate profile is read on application start and is updated by AAPS.
  The basal rate should not be manually changed on the pump, but will be detected and corrected as a safety
  measure (don't rely on safety measures by default, this is meant to detect an unintended change on the pump).
- It's recommended to enable key lock on the pump to prevent bolusing from the pump, esp. when the
  pump was used before and using the "quick bolus" feature was a habit.
  Also, with keylock enabled, accidentally pressing a key will NOT interrupt active communication
  between AAPS and pump.
- When a BOLUS/TBR CANCELLED alert starts on the pump during bolusing or setting a TBR, this is
  caused by a disconnect between pump and phone, which happens from time to time. AAPS will try to reconnect and confirm the alert
  and then retry the last action (boluses are NOT retried for safety reasons). Therefore,
  such an alarm can be ignored as AAPS will confirm it automatically, usually within 30s (cancelling it is not problem, but will lead to the currently
  active action to have to wait till the pump's display turns off before it can reconnect to the
  pump). If the pump's alarm continues, automatic corfirmation failed, in which case the user
  needs to confirm the alarm manually.
- When a low cartridge or low battery alarm is raised during a bolus, they are confirmed and shown
  as a notification in AAPS. If they occur while no connection is open to the pump, going to the
  Combo tab and hitting the Refresh button will take over those alerts by confirming them and
  show a notification in AAPS.
- 當 AAPS 無法確認 '臨時基礎率取消' 警報，或因其他原因觸發該警報時，在 Combo 頁籤按下重新整理會重新建立連線，確認警報，並在 AAPS 顯示通知。 這樣做是安全的，因為這些警報是無害的——在下次循環時會再次設定適當的臨時基礎率（TBR）。 This can safely be done, since those alerts are benign - an
  appropriate TBR will be set again during the next loop iteration.
- For all other alerts raised by the pump: connecting to the pump will show the alert message in
  the Combo tab, e.g. "State: E4: Occlusion" as well as showing a notification on the main screen.
  An error will raise an urgent notification. AAPS never confirms serious errors on the pump,
  but let's the pump vibrate and ring to make sure the user is informed of a critical situation
  that needs action.
- 配對後，不應直接使用 ruffy（AAPS 會在需要時於背景啟動），因為同時使用 ruffy 和 AAPS 是不支援的。
- If AAPS crashes (or is stopped from the debugger) while AAPS and the pump were communicating (using
  ruffy), it might be necessary to force close ruffy. 如果 AAPS 當機（或被調試器停止）時 AAPS 正在與幫浦連線（使用 ruffy），可能需要強制關閉 ruffy。 重新啟動 AAPS 會再次啟動 ruffy。 如果你不知道如何強制關閉應用程式，重新啟動手機也是解決這個問題的簡單方法。
  Restarting the phone is also an easy way to resolve this if you don't know how to force kill
  an app.
- Don't press any buttons on the pump while AAPS communicates with the pump (Bluetooth logo is
  shown on the pump).
