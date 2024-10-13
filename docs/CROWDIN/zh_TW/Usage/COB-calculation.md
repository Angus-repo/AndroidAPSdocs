# COB 計算

## AAPS 如何計算 COB 值？

如果「治療」標籤中碳水化合物和胰島素顯示在同一行，對 **IOB** 數值也應一起檢查。 檢查並記住 **COB** 和 **IOB** 的實際數值，可以在 **AAPS** 的主畫面上看到。 The rate of absorption depends on the carb’s sensitivity factor (**’CSF**”). 當使用者在用餐項目或碳水化合物校正中輸入碳水化合物時，**AAPS** 會將此計算添加到目前的碳水化合物儲量中 (**COB**)。 **AAPS** 接著會根據的使用者**血糖**變化，計算出使用者的碳水化合物吸收。 吸收的速度取決於碳水化合物的敏感性因子 (**’CSF**”)。 這不是使用者**設定檔**中的功能，而是由**AAPS** 根據**ISF/I:C** 的設置來計算，根據1克碳水化合物會使使用者**血糖** 上升多少mg/dl來決定。

## 碳水化合物敏感性因子

**AAPS** 採用的公式為：

- absorbed_carbs = deviation \* ic / isf.

使用者的**設定檔**帶來的影響是：

- _增加_ **IC** —透過增加「每5分鐘碳水化合物的吸收」，來縮短總吸收時間；

- _增加_ **ISF** —透過減少「每5分鐘吸收的碳水化合物」，來延長總吸收時間；以及

- _更改_ **設定檔百分比** —將會同時增加/減少IC、ISF這兩個值，所以對碳水化合物吸收時間沒有影響。

For example, if the user’s  **Profile**  **ISF** is 100 and the **I:C** is 5, the user’s Carb Sensitivity Factor would be 20. For every 20 mg/dl the user’ **BG** goes up and 1g of carbs will be calculated as absorbed by **AAPS**. Positive **IOB** also affects the **COB** calculation. 例如，如果使用者**設定檔**的**ISF** 是100，**I:C** 是5，則使用者的碳水化合物敏感性因子將為20。 當使用者的**血糖** 上升20 mg/dl，**AAPS** 就會計算出1克碳水化合物被吸收。 正向的**IOB** 也會影響**COB** 的計算。 因此，若**AAPS** 預測使用者的**血糖** 會因**IOB** 而下降20 mg/dl，但實際上保持不變，**AAPS** 也會計算出1克碳水化合物已被吸收。

碳水化合物也將通過下述方法進行吸收，具體方式取決於使用者的**AAPS** 中選擇的敏感性演算法。

## 碳水化合物敏感因子 - Oref1

未吸收的碳水化合物將在指定時間後將被切斷:

![Oref1](../images/cob_oref0_orange_II.png)![截圖 2024-10-05 161009](https://github.com/user-attachments/assets/e4eb93b2-bc93-462d-b4d6-854bb9264953)

## 碳水化合物敏感因子 - 加權平均

在指定時間後<0>COB</0> 將被歸0：

![AAPS, 加權平均](../images/cob_aaps2_orange_II.png)

如果使用最小碳水化合物吸收值（min_5m_carbimpact）而不是從**血糖**變化計算出的值，**COB** 圖上將出現一個橙色圓點。

## 偵測錯誤的 COB 值

假如演算法偵測到目前的 **COB** 計算不正確，**AAPS**  會在使用者準備進行注射時發出警告，這裡的 **COB** 是指之前吃東西輸入的碳水。 在這種情況下，系統會在使用者使用注射嚮導後，於確認畫面上出現額外的提示 In this case it will give the user an additional hint on the confirmation screen after usage of bolus wizard.

### AAPS 如何偵測錯誤的 COB 值？

Ordinarily **AAPS** detects carb absorption through **BG** deviations. 通常 **AAPS** 會透過 **血糖** 變化來偵測碳水化合物的吸收狀況。 如果使用者輸入了碳水化合物，但 **AAPS** 無法透過 **血糖** 變化偵測到預估的吸收量，系統會改用 [min_5m_carbimpact](../Configuration/Config-Builder.md?highlight=min_5m_carbimpact#absorption-settings) 這個方法來計算吸收量（這稱為「備用」計算方式）。 但因為這個方法只會計算最低的碳水化合物吸收量，而不考慮 **血糖** 的變化，所以也可能會導致 <0>COB</0> 數值不正確。 As this method calculates only the minimal carb absorption without considering **BG** deviations, it might lead to incorrect COB values.

![錯誤 COB 值的提示](../images/Calculator_SlowCarbAbsorption.png)

在上面的截圖中，有 41% 的時間是用 <1>min_5m_carbimpact</1> 來計算碳水化合物的吸收量，而不是透過變動來偵測的數值。 這表示使用者實際上的 **COB** ，可能比演算法計算出來的還要少。 This indicates that the user may have had less **COB** than calculated by the algorithm.

### 如何處理這個警告？

- 考慮取消這次治療—按「取消」而不是「確認」。
- Calculate your upcoming meal again with bolus wizard leaving **COB** unticked.
- If you need a correction bolus, enter it manually.
- Be careful not to overdose or insulin stacking!

### 為什麼演算法無法正確偵測 COB？

可能的原因如下：

- 使用者在輸入碳水化合物時，可能預估量過高，或輸入了碳水化合物，但剩下過多餐點沒有吃完。
- 先前餐點後的活動/運動.
- I:C 需要調整.
- min_5m_carbimpact 的數值不正確（建議使用 SMB 時是 8，使用 AMA 時是3）。

## 手動修正輸入的碳水化合物

如果碳水化合物輸入過多或過少，可以透過「治療」選單進行更正，具體步驟如 [這裡](Screenshots-carb-correction) 所述。

## 碳水化合物更正—如何從「治療」中刪除碳水化合物的項目

The ‘Treatments’ tab can be used to correct a faulty carb entry by deleting the entry in Treatments. This may be because the user over or underestimated the carb entry:

![COB\_Screenshot 2024-10-05 170124](https://github.com/user-attachments/assets/e123d85d-907e-4545-bf1b-09fee4d42555)

1. Check and remember actual **COB** and **IOB** on the **AAPS'** homescreen.
2. Depending on the pump, the carbs in the Treatments tab might show together with insulin in one line or as a separate entry (i.e. with Dana RS).
3. Remove the entry by firstly 'ticking' the waste bin on the top right corner (see above photo, step 1). Then 'tick' the faulty carb amount (see above photo, step 2). Then 'tick' the ‘waste bin’ on the top right corner (step 1 again).
4. 確保碳水化合物已成功移除，請再次檢查 **AAPS** 主畫面上的 **COB**。
5. Do the same for **IOB** if there is just one line in the Treatment tab including carbs and insulin.
6. 如果碳水化合物未按預期移除，並且如本節所講的，增加了額外的碳水化合物，**COB** 項目會過高，這可能導致 **AAPS** 輸入過量的胰島素。
7. 透過 **AAPS** 主畫面上的碳水化合物按鈕輸入正確的碳水化合物數量，並設定正確的事件時間。
8. If there is just one line in Treatment tab including carbs and insulin the user should add also the amount of insulin. Make sure to set the correct event time and check **IOB** on homescreen after confirming the new entry.
