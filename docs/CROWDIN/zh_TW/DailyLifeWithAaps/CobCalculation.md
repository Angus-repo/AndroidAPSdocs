# COB 計算

## AAPS 如何計算 COB 值？

當使用者在用餐項目或碳水化合物校正中輸入碳水化合物時，**AAPS** 會將此計算添加到目前的碳水化合物儲量中 (**COB**)。 **AAPS** 接著會根據的使用者**血糖**變化，計算出使用者的碳水化合物吸收。 吸收的速度取決於碳水化合物的敏感性因子 (**’CSF**”)。 這不是使用者**設定檔**中的功能，而是由**AAPS** 根據**ISF/I:C** 的設置來計算，根據1克碳水化合物會使使用者**血糖** 上升多少mg/dl來決定。

## 碳水化合物敏感性因子

**AAPS** 採用的公式為：

- absorbed_carbs = deviation * ic / isf.

使用者的**設定檔**帶來的影響是：

- _增加_ **IC** —透過增加「每5分鐘碳水化合物的吸收」，來縮短總吸收時間；

- _增加_ **ISF** —透過減少「每5分鐘吸收的碳水化合物」，來延長總吸收時間；以及

- _更改_ **設定檔百分比** —將會同時增加/減少IC、ISF這兩個值，所以對碳水化合物吸收時間沒有影響。

例如，如果使用者**設定檔**的**ISF** 是100，**I:C** 是5，則使用者的碳水化合物敏感性因子將為20。 當使用者的**血糖** 上升20 mg/dl，**AAPS** 就會計算出1克碳水化合物被吸收。 正向的**IOB** 也會影響**COB** 的計算。 因此，若**AAPS** 預測使用者的**血糖** 會因**IOB** 而下降20 mg/dl，但實際上保持不變，**AAPS** 也會計算出1克碳水化合物已被吸收。

碳水化合物也將通過下述方法進行吸收，具體方式取決於使用者的**AAPS** 中選擇的敏感性演算法。

## 碳水化合物敏感因子 - Oref1

未吸收的碳水化合物將在指定時間後將被切斷:

![Oref1](../images/cob_oref0_orange_II.png)

![Screenshot 2024-10-05 161009](../images/cob_oref0_orange_I.png)


## 碳水化合物敏感因子 - 加權平均

Absorption is calculated to have COB = 0 after specified time:

![AAPS, WheitedAverage](../images/cob_aaps2_orange_II.png)

If minimal carbs absorption (min_5m_carbimpact) is used instead of value calculated from **BG** deviations, an orange dot appears on the **COB** graph.

(CobCalculation-detection-of-wrong-cob-values)=
## 偵測錯誤的 COB 值

**AAPS**  will warn the user if they are about to bolus with **COB** from a previous meal if the algorithm detects current **COB** calculation as incorrect. In this case it will give the user an additional hint on the confirmation screen after usage of bolus wizard.

### AAPS 如何偵測錯誤的 COB 值？

Ordinarily __AAPS__ detects carb absorption through **BG** deviations. Incase the user has entered carbs but **AAPS** cannot detect their estimated absorption through **BG** deviations, it will use the [min_5m_carbimpact](#Preferences-min_5m_carbimpact) method to calculate the absorption instead (so called ‘fallback’). As this method calculates only the minimal carb absorption without considering **BG** deviations, it might lead to incorrect COB values.

![Hint on wrong COB value](../images/Calculator_SlowCarbAbsorption.png)

In the screenshot above, 41% of time the carb absorption was calculated by the min_5m_carbimpact instead of the value detected from deviations. This indicates that the user may have had less **COB** than calculated by the algorithm.

### 如何處理這個警告？

- 考慮取消這次治療—按「取消」而不是「確認」。
- 用注射嚮導重新計算你即將吃的餐點，並且不要勾選 **COB**。
- 如果需要修正注射，請手動輸入劑量。
- 小心不要打太多，或者胰島素累積過多！


### 為什麼演算法無法正確偵測 COB？

This could be because:
- 使用者在輸入碳水化合物時，可能預估量過高，或輸入了碳水化合物，但剩下過多餐點沒有吃完。
- 先前餐點後的活動/運動.
- I:C 需要調整.
- min_5m_carbimpact 的數值不正確（建議使用 SMB 時是 8，使用 AMA 時是3）。


## 手動修正輸入的碳水化合物

If carbs are over or underestimated carbs this can be corrected through the Treatments tab and actions tab / menu as described [here](#screens-bolus-carbs).


## 碳水化合物更正—如何從「治療」中刪除碳水化合物的項目


The ‘Treatments’ tab can be used to correct a faulty carb entry by deleting the entry in Treatments. This may be because the user over or underestimated the carb entry:

![COB_Screenshot 2024-10-05 170124](https://github.com/user-attachments/assets/e123d85d-907e-4545-bf1b-09fee4d42555)

1. 檢查並記住 **COB** 和 **IOB** 的實際數值，可以在 **AAPS** 的主畫面上看到。
2. 根據不同的幫浦，「治療」標籤中的碳水化合物和胰島素可能會顯示在同一行，也可能是分開的項目（例如在 Dana RS 中）。
3. 要刪除該項目，首先在右上角點選垃圾桶圖示（參見上方圖片，第 1 步）。 接著勾選錯誤的碳水化合物（參見上方圖片，第 2 步）。 最後再次點選右上角的垃圾桶圖示（再次執行第 1 步）。
4. 確保碳水化合物已成功移除，請再次檢查 **AAPS** 主畫面上的 **COB**。
5. 如果「治療」標籤中碳水化合物和胰島素顯示在同一行，對 **IOB** 數值也應一起檢查。
6. 如果碳水化合物未按預期移除，並且如本節所講的，增加了額外的碳水化合物，**COB** 項目會過高，這可能導致 **AAPS** 輸入過量的胰島素。
7. 透過 **AAPS** 主畫面上的碳水化合物按鈕輸入正確的碳水化合物數量，並設定正確的事件時間。
8. 如果「治療」標籤中碳水化合物和胰島素顯示在同一行，使用者也應該輸入正確的胰島素劑量。 請確保設定正確的事件時間，並在確認新增項目後，檢查主畫面上的 **IOB**。

