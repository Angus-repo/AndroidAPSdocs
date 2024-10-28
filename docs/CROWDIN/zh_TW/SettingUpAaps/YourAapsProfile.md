# 您的 **AAPS** 設定檔

您的 **AAPS** 設定檔是一組五個關鍵參數，定義了 **AAPS** 應如何根據您的感測器血糖水平提供胰島素。 **AAPS** 具備幾個可修改的 _額外_ 參數（例如 SMB 設定），但良好地使用這些參數依賴於您底層的 **AAPS** 設定檔是正確的。 **AAPS** 設定檔包括：

- [胰島素作用持續時間](#duration-of-insulin-action-dia) (DIA)，
- [血糖目標](#glucose-targets)，
- [基礎率](#basal-rates) (BR)，
- [胰島素敏感性因子](#insulin-sensitivity-factor-isf) (ISF) 以及
- [胰島素與碳水化合物比](#insulin-to-carb-ratio-icr) (IC 或 ICR)。

最後四個參數的值可以在 24 小時內按需設置為不同的值，隨時間改變。 請注意，下方範例設定檔顯示了大量的時間點。 當您剛開始使用 **AAPS** 時，您的設定檔可能會更簡單。

```{admonition} Your diabetes may vary
:class: information
設定檔在不同人之間差異很大。

對於最後三個參數，即基礎率 (BR)、胰島素敏感性因子 (ISF) 和胰島素與碳水化合物比 (IC 或 ICR)，您的胰島素需求的絕對值和趨勢因個人的生理、性別、年齡、健身水平等因素，以及較短期的因素如疾病和近期運動，差異可能很大。對於這方面的更多指導，Adam Brown 的書籍 [「Brights Spots and Landmines」](https://brightspotsandlandmines.org/Bright_Spots_and_Landmines_by_Adam_Brown.pdf) 是一本值得一讀的好書。

```

以下顯示 **AAPS** 的 _範例_ 設定檔的截圖。

## 胰島素作用持續時間（DIA）

在 **AAPS** 中，胰島素作用持續時間是設置為單一值，因為您的幫浦將不斷注入相同類型的胰島素。

結合[胰島素類型](../SettingUpAaps/ConfigBuilder.md#insulin)，這將導致[胰島素設定檔](../DailyLifeWithAaps/AapsScreens.md#insulin-profile)。 請在那裡閱讀以幫助您定義適當的 DIA。

## 血糖目標

**下方圖示**顯示了在 **AAPS** 設定檔中 DIA 和血糖目標如何設置的範例。

![24-07-23，設定檔基礎 - DIA 和目標](../images/f3904cc3-3d9e-497e-a3b6-3a49650053e6.png)

您的 **BG 目標** 是一個核心值，所有的 **AAPS** 計算都是基於它。 它不同於您通常希望將您的血糖值保持在的目標範圍：

- 血糖目標，特別是如果它只是短期（少於 4 小時的持續時間），並不需要是您預期或希望您的血糖水平達到的_實際值_，而是一個良好的方式來告訴 **AAPS** 需要更具侵略性或不那麼侵略性，同時仍保持您的血糖水平在範圍內。
- 如果您的目標範圍非常寬（比方說，3 或更多 mmol/l [50 mg/dl 或更多]），您通常會發現 **AAPS** 的行動很少。 這是因為 **BG** 水平預測位於那個寬範圍內，因此很少建議進行臨時基礎率的改變。
- 當您剛開始使用 **AAPS**，特別是在進行[第一個目標](../SettingUpAaps/CompletingTheObjectives.md)時，使用寬範圍的目標可以是一個不錯的選擇，同時您學習 **AAPS** 的行為並調整您的 **設定檔**。
- 稍後，您可能會發現更合適的是減小範圍，直到您為每天的每個時段（_低_ 目標 = _高_ 目標）設定一個單一目標，以確保 **AAPS** 迅速對 **BG** 的波動做出反應。

目標可以在這些邊界內定義：

|    | _低_ 目標                | 高血糖目標                 |
| -- | --------------------- | --------------------- |
| 最小 | 4 mmol/l 或 72 mg/dL   | 5 mmol/l 或 90 mg/dL   |
| 最大 | 10 mmol/l 或 180 mg/dL | 15 mmol/l 或 225 mg/dL |

血糖目標根據你的個人偏好設定。 例如，如果你擔心夜間低血糖，你可以將目標設定為稍高的 117 mg/dL（6.5 mmol/L），從晚上 9 點到早上 7 點。 如果你希望在早餐前有充足的胰島素儲備，你可以將早上 7 點到 8 點的目標設定為較低的 81 mg/dL（4.5 mmol/L）。

## 基礎率

你的胰島素基礎率（單位/小時）提供背景胰島素，在沒有食物或運動的情況下保持血糖穩定。

精準的基礎率能讓你在醒來時保持血糖在範圍內，並在一天中可以提前或延後進餐，而不會引起血糖過高或過低。 胰島素幫浦每幾分鐘會輸送少量速效胰島素，以防止肝臟釋放過多的葡萄糖，並將葡萄糖輸送到體細胞中。 基礎胰島素通常占你每日總劑量（TDD）的 40-50%，取決於你的飲食，並且通常遵循日夜節律，在 24 小時內有一個高峰和一個低谷。 關於更多資訊，Gary Scheiner 的[《Think like a Pancreas》](https://amzn.eu/d/iVU0RGe) 的第 23 章非常有用。

大多數 1 型糖尿病教育者（以及 1 型糖尿病患者！） 都同意，你應該先確保基礎率正確，然後再嘗試優化 ISF 和 ICR。

## 胰島素敏感度因子（ISF）

胰島素敏感性係數（有時稱為修正係數）是衡量 1 單位胰島素會降低血糖的程度。

\*\*以 mg/dL 為單位：\*\*如果你的 ISF 為 40，則每單位胰島素將使血糖降低約 40 mg/dL（例如，你的血糖將從 140 mg/dL 降至 100 mg/dL）。

\*\*以 mmol/L 為單位：\*\*如果你的 ISF 為 1.5，則每單位胰島素將使血糖降低約 1.5 mmol/L（例如從 8 mmol/L 降至 6.5 mmol/L）。

從這些範例中，你可以看到 ISF 值越小，你對胰島素的敏感性越低。 因此，如果你將胰島素敏感度因子（ISF）從 40 降至 35（mg/dl）或從 1.5 降至 1.3（mmol/L），這通常被稱為強化你的胰島素敏感度因子（ISF）。 相反，將 ISF 值從 40 增加到 45（mg/dl）或從 1.5 增加到 1.8（mmol/L）稱為削弱 ISF。

如果你的 ISF 過強（值較小），會導致低血糖；如果 ISF 過弱（值較大），則會導致高血糖。

確定你白天 ISF 的基本起點是基於你的每日總劑量（TDD），使用 1,700（94）規則。 更多詳情請參閱 Gary Scheiner 的[《Think like a Pancreas》](https://amzn.eu/d/iVU0RGe) 的第 7 章。

1700（若以 mg/dl 為單位）或 94（mmol/L）/ TDD = 大約 ISF。

範例：TDD = 40 U大約 ISF（mg/dl）= 1700/40 = 43大約 ISF（mmol/L）= 94/40 = 2.4

請參閱下方的**圖示**以獲得如何在**AAPS**設定檔中設置基礎率和胰島素敏感度因子的範例。

![24-07-23，設定檔基礎 - 基礎率和 ISF](../images/55c8ed24-e24e-4caa-9c17-294fa93cb84a.png)

## 胰島素與碳水化合物的比例（ICR）

ICR 是衡量每單位胰島素覆蓋多少克碳水化合物的指標。

有些人也使用 I:C 作為 ICR 的縮寫，或稱之為碳水化合物比率（CR）。

例如，1:10 的胰島素與碳水化合物比率表示你每攝入 10 克碳水化合物需要注射 1 單位的胰島素。 一餐包含 25 克碳水化合物需要 2.5 單位的胰島素。

如果你的 ICR 較弱，可能是 1:20，那麼你只需 0.5 單位的胰島素來覆蓋 10 克碳水化合物。 一餐包含 25 克碳水化合物需要 25/20 = 1.25 單位的胰島素。

由於荷爾蒙水平和體力活動，ICR 在一天中的不同時間可能會有所不同。 許多人發現，他們的 ICR 在早餐時間最低。 例如，你的 ICR 可能在早餐時為 1:8，午餐時為 1:10，晚餐時為 1:10，但這些模式並非普遍適用，某些人在晚餐時間對胰島素的抵抗力較高，因此需要更強/較小的 ICR。

如下方的**圖示**所示，當將這些數值輸入到**AAPS**設定檔中時，我們只需輸入比例的最後部分，因此胰島素與碳水化合物的比例 1:3.5 僅輸入「3.5」。

![24-07-23，設定檔基礎 - ICR](../images/7741eefb-cae5-45c5-a9e5-8eae5ead3f48.png)

## 關於正確設置你的設定檔的重要性

**為什麼我應該努力設置我的設定檔？** 難道循環系統不可以自動處理嗎？\*\*

混合閉環_可以_嘗試調整胰島素輸送，以最大限度減少由於設定檔值不正確而導致的血糖控制不良。 它可以這樣做，例如如果你將要低血糖，它會暫停胰島素的輸送。 然而，若你的設定檔參數已經接近你身體所需的值，你將能夠實現更好的血糖控制。 這是**AAPS**使用階段性目標逐步從開放循環幫浦過渡到混合閉環的一個原因。 此外，有時你需要開放環路（例如傳感器加熱期間、傳感器故障等），有時甚至在夜間發生，你會希望在這些情況下擁有正確的設定。

如果你在使用其他開放或閉環幫浦系統後開始使用**AAPS**，那麼你已經對基礎率（BR）、胰島素敏感度因子（ISF）和胰島素與碳水化合物比例（IC 或 ICR）要使用的數值有一個合理的了解。

如果你是從注射（MDI）轉到**AAPS**，那麼最好先了解如何從 MDI 轉換到幫浦，並與你的糖尿病團隊進行謹慎的計劃和轉換。 John Walsh 和 Ruth Roberts 的[《Pumping insulin》](https://amzn.eu/d/iaCsFa2) 以及 Gary Scheiner 的[《Think like a Pancreas》](https://amzn.eu/d/iVU0RGe) 非常有用。

## 設定檔助手

[設定檔助手](../SettingUpAaps/ProfileHelper.md) 可以幫助您：

- 從零開始為小孩建立設定檔
- 比較兩個設定檔
- 複製一份設定檔