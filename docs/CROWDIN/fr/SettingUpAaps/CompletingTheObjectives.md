# Compléter les objectifs

**AAPS** has a series of **Objectives** required to be completed to help the user progress from basic open looping to hybrid closed looping and full **AAPS** functionality. Completing the **Objectives** aims to ensure you have:

- Configured everything correctly in your **AAPS** setup;
- Learned about the essential features of **AAPS**; and
- A basic understanding of what your system can do, in order to help instill confidence when using **AAPS**.

When **AAPS** is installed for the first time, each objective must be completed before moving on to the next one. New features will gradually be unlocked as progress is made through each **Objective**.

**Objectives 1 to 8** will guide you from configuring **AAPS** on your smartphone to “basic” hybrid closed looping. This will take about 6 weeks to complete. You can proceed up to **Objective 5** using a virtual pump (and using some other method of insulin delivery in the meantime). **Objectives 9 to 11** are designed to test more advanced **AAPS** features with the aim of better control of your diabetes, and will take up to 3 months to complete, possibly longer. Further details on an estimated breakdown of time can be obtained here: [How long will it take?](../Getting-Started/PreparingForAaps.md#how-long-will-it-take-to-set-everything-up)

As well as progressing through the **Objectives**, if required, you can also remove your progress and [go back to an earlier objective](#go-back-in-objectives).

### Backup your settings

```{admonition} Note
:class: note

Exporting your **AAPS** settings is recommended after completing each **Objective**!
```

It is strongly recommended that you [export your settings](../Maintenance/ExportImportSettings.md) after completing each objective to avoid losing any progress made in **AAPS**. This exporting process creates a **settings file** (.json) which should be backed-up in one or more safe places (e.g. Google Drive, hard disk, email attachment _etc._). This ensures that any progress made in **AAPS** is saved. If your phone is lost or if you accidentally delete your progress, the json file can be re-loaded to **AAPS** by importing a recent settings file. Having a backup **settings file** is also required if a new **AAPS** smartphone is required for any reason (upgrading/lost/broken phone _etc._)

The **settings** file will save not only your progress through the **Objectives**, but also all your **AAPS** settings such as **max bolus** _etc._

The **Objectives** will need to be restarted from the beginning should you fail to have a backup of your settings and anything happens to your **AAPS** smartphone. Progressing through the **Objectives** takes time, and having to re-complete them again because for example you lost your smartphone, is a situation to be best avoided.

## Objective 1: Setting up visualization and monitoring, analyzing basals and ratios

**Objective 1** requires the user to set up their basic technical setup in **AAPS**. No progress can be made until this step has been completed.

- Select the correct CGM/FGM in [Config Builder](../SettingUpAaps/ConfigBuilder.md#bg-source). See [BG Source](../Getting-Started/CompatiblesCgms.md) for more information.
- Select the correct Pump in [Config Builder](../SettingUpAaps/ConfigBuilder.md) to ensure your pump can communicate with **AAPS**. Select **virtual pump** if you are using a pump model with no **AAPS** driver for looping, or if you want to work through the early **Objectives** while using another system for insulin delivery. See [insulin pump](../Getting-Started/CompatiblePumps.md) for more information.
- If using Nightscout:
  - Follow instructions in [Nightscout](../SettingUpAaps/Nightscout.md) page to ensure **Nightscout** can receive and display **AAPS** data.
  - Note that URL in **NSClient** must be **_without_ "/api/v1/"** at the end - see [Preferences > NSClient](../SettingUpAaps/Preferences.md#NSClient).
- If using Tidepool:
  - Follow instructions in [Tidepool](../SettingUpAaps/Tidepool.md) page to ensure **Tidepool** can receive and display **AAPS** data.

Note : _Vous devrez peut-être attendre la prochaine lecture de glycémie avant qu'elle n'arrive dans **AAPS**._

## Objectif 2 : Apprendre à contrôler AAPS

**Objective 2** requires several ‘tasks’ to be actioned as shown in the screenshot below
Click on the orange text "Not completed yet" to access the to-dos.
Des liens vous sont donnés pour vous guider si vous n'êtes pas encore familier avec une tâche particulière.

![Screenshot objective 2](../images/Objective2_V2_5.png)

Les tâches à terminer dans l'**Objectif 2** sont :

- Set your **Profile** to 90% for a duration of 10 min.
  - _Hint_: Long press your Profile name on the OVERVIEW screen. More information in [Profile switch & Profile Percentage](../DailyLifeWithAaps/ProfileSwitch-ProfilePercentage.md).
  - _Note_: **AAPS** does not accept basal rates below 0.05U/hr. If your **Profile** includes rates 0.06U/hr or lower you will need to create a temporary **Profile** with higher basal rates before completing this task. Switch back to your normal **Profile** after completing this task.
- Simulate "taking a shower" by [disconnecting your pump](../DailyLifeWithAaps/AapsScreens.md#section-c---bg--loop-status) in **AAPS** for a duration of 1h.
  - _Hint_: press the loop icon on the OVERVIEW screen to open the Loop dialogue.
- End "taking a shower" by reconnecting your pump.
  - _Hint_: press the "disconnected"-icon to open the loop dialog.
- Set a custom [**Temporary Target**](../DailyLifeWithAaps/TempTargets.md) with a duration of 10 min.
  - _Hint_: press the target bar on the OVERVIEW screen to bring up the temporary target dialog.
- Activate the **Actions** plugin in [**Config Builder**](../SettingUpAaps/ConfigBuilder.md) to make it appear on the top scrollable menu bar.
  - _Hint_: Go to **Config Builder** and scroll down to General.
- Display the **Loop** plugin's content.
- [Scale the BG-Chart](../DailyLifeWithAaps/AapsScreens.md#section-f---main-graph) to be able to look at larger or smaller time frames: toggling between 6h, 12h, 18h 24h of past data.
  - _Hint_: Long press on the chart or use the arrow at the top right.

## Objectif 3 : Prouver ses connaissances

**Objective 3** requires the user to pass a multiple-choice exam which is designed to test your **AAPS** knowledge.

Certains utilisateurs trouvent que l'**Objectif 3** est le plus difficile à compléter. Please read the **AAPS** documents in conjunction with the questions. If you are genuinely stuck after researching the **AAPS** documents, please search the [Facebook](https://www.facebook.com/groups/AndroidAPSUsers) or [Discord](https://discord.gg/4fQUWHZ4Mw) group for "Objective 3" (because it is likely that your question has been asked before - and answered by the group). Ces groupes peuvent fournir des indices en toute bienveillance, ou vous rediriger vers la partie appropriée de la documentation **AAPS**.

In the meantime :

- To reduce the number of notifications / decisions you are asked to make (temporary basal rates) while in Open Loop, set a wide target range in your **Profile** _e.g._ 90 - 150 mg/dl or 5.0 - 8.5 mmol/l.
- Vous pouvez même augmenter encore la limite supérieure, ou même désactiver la Boucle ouverte, pendant la nuit.

Pour avancer dans l'**Objectif 3**, cliquez sur le texte orange "**Pas encore complété**" pour accéder à la question en cours. Veuillez lire attentivement chaque question et sélectionner votre(s) réponse(s).

Pour chaque question, il peut y avoir une ou plusieurs réponses correctes ! If an incorrect answer is selected, the question will be time-locked for 1 hour before you can go back and answer the question again. Notez que l'ordre des propositions peut changer lorsque vous essayez de répondre à nouveau ; ceci pour faire en sorte que vous lisiez attentivement et réfléchissiez vraiment à la validité (ou non) de chaque proposition.

```{admonition} __What happens if new question(s) are added to an Objective when I update to a newer version of AAPS?__
:class: Note
From time to time, new features are added to **AAPS** which may require a new question to be added to the **Objectives**, particularly **Objective 3**. As a result, any new question added to **Objective 3** will be marked as “incomplete” because **AAPS** will require you to action this. Do not worry, as each **Objective** is independent, you will **not lose the existing functionality of AAPS**, providing the other **Objectives** remain completed.
```

## Objectif 4 : Démarrage de la boucle ouverte

The purpose of **Objective 4** is to recognise how often **AAPS** will evaluate the user's basal rate against glucose levels, and recommend temporary basal rate adjustments. As part of this **Objective**, you will activate open looping for the first time, and will accept 20 proposed temporary basal rate changes, and if required, apply these manually on your pump. You will also observe the impact of [**Temporary Targets**](../DailyLifeWithAaps/TempTargets.md). If you are not familiar with setting a temporary basal rate change in **AAPS** yet, please refer to the [**Actions** tab](../DailyLifeWithAaps/AapsScreens.md#action-tab).

The minimal time to complete this objective: **7 days**. Vous serez obligé d'attendre que ce temps soit écoulé. It is not possible to proceed to the next **Objective**, even if all basal rate changes were enacted already.

- Select Open Loop either from the [Preferences > OpenAPS](../SettingUpAaps/Preferences.md#aps-mode) menu or by pressing and holding the Loop icon on the top left of the **Overview** screen.
- Acceptez manuellement au moins 20 suggestions de débits de base temporaires sur une période de 7 jours; entrez-les dans votre pompe (réelle) et confirmez dans AAPS que vous les avez acceptés. Ensure these basal rate adjustments show up in **AAPS** and **Nightscout**.
- Use [**Temp Targets**](../DailyLifeWithAaps/TempTargets.md) when necessary. After treating a hypo, use the predefined "hypo temp target" to prevent the system from overcorrecting upon the bounce back.

To reduce the number of proposed basal rate changes while in Open Loop, you can still use the tips described in [**Objective 3**](#objective-3-prove-your-knowledge).
Additionally, you can change the minimum percentage for recommended basal rate changes. The higher the value, the fewer change notifications you will receive.

![Open Loop minimal request change](../images/OpenLoop_MinimalRequestChange2.png)

```{admonition} Note
:class: Note

You don't need to action each and every system recommendation!
```

## Objectif 5 : Compréhension de la Boucle Ouverte, y compris les propositions de débits Basal temporaires

Dans le cadre de l'**Objectif 5**, vous allez commencer à comprendre comment les recommandations de basal temporaire sont calculées. This includes the [determination of basal logic](https://openaps.readthedocs.io/en/latest/docs/While%20You%20Wait%20For%20Gear/Understand-determine-basal.html), analyzing the impact by observing [prediction lines in **AAPS Overview**](../DailyLifeWithAaps/AapsScreens.md#prediction-lines) (or Nightscout) and looking at detailed calculations shown on your **OpenAPS** tab.

Temps estimé pour terminer cet objectif : **7 jours**.

This **Objective** requires you to determine and set your “Max U/h a temp basal can be set to” (max-basal) value as described in [OpenAPS-features](../DailyLifeWithAaps/KeyAapsFeatures.md#max-uh-a-temp-basal-can-be-set-to-openaps-max-basal). This value can be set in [Preferences > OpenAPS](../SettingUpAaps/Preferences.md#max-uh-a-temp-basal-can-be-set-to).
If you are still using a virtual pump, make sure this safety setting is set in both **AAPS** and your insulin pump.

You might wish to set your [**Profile** BG target](../SettingUpAaps/YourAapsProfile.md#glucose-targets) higher than usual until you are comfortable with **AAPS**' calculations and settings. You may wish to experiment with adjusting your **BG target** in your **Profile** being in a tighter range (say, 1 or less mmol/l [20 mg/dl or less] wide) and observe the resulting behavior.

![Stop sign](../images/sign_stop.png)

```{admonition} If you have been using a virtual pump, change to a real insulin pump now!
:class: note

If you are open looping with a virtual pump **stop here**. Only click verify at the end of this **Objective** once you have changed to using a "real" pump which delivers insulin.

```

![blank](../images/blank.png)

## Objectif 6 : Démarrage de la boucle fermée avec le système AGB ( Arrêt pour Glycémie Basse )

![Warning sign](../images/sign_warning.png)

```{admonition} Closed loop will not correct high **BG** values in **Objective 6** as it is limited to **Low Glucose Suspend** only!
:class: Note
Vous devrez toujours corriger les glycémies élevées vous-même (manuellement avec des corrections par pompe ou stylo) !
```

As part of **Objective 6** you will close the loop and activate its **Low Glucose Suspend** (LGS) mode while [max IOB](../DailyLifeWithAaps/KeyAapsFeatures.md#maximum-total-iob-openaps-cant-go-over-openaps-max-iob) is set to zero. You have to remain in LGS mode for 5 days to complete this **objective**. You should use this time to check if your **Profile** settings are accurate and LGS events are not triggered too often.

Minimal time to complete this objective: **5 days**. Vous serez obligé d'attendre que ce temps soit écoulé. You cannot proceed to the next **Objective** before this time is up.

It is crucial that your current **Profile** (basal, ISF, IC) have been well tested before you close your loop in **LGS** mode. Incorrect **Profile** settings might force you into hypo situations which have to be treated manually. An accurate **Profile** will help reduce the need for low glucose treatments during the 5 days period.

**If you still observe frequent or severe low glucose episodes consider refining your DIA, basal, ISF and carb ratios.** Please refer to the [Facebook](https://www.facebook.com/groups/AndroidAPSUsers) or [Discord](https://discord.gg/4fQUWHZ4Mw) group which has much discussion on this.

During **Objective 6**, **AAPS** will override the maxIOB setting to zero. **This override will end when moving to Objective 7.**

This means that when you are on **Objective 6**, if sensor glucose levels are dropping, **AAPS** will reduce your basal insulin delivery for you. But, if sensor glucose levels are rising, **AAPS** will  increase the basal rate above your **Profile** value only if **basal IOB** is negative as a result of  a previous **LGS**. Sinon, **AAPS** n'augmentera pas le basal au-dessus de la valeur définie dans votre profil, même si la glycémie augmente. Cette précaution vise à éviter les hypos pendant que vous apprenez à utiliser **AAPS**.

**Par conséquent, vous devez gérer les glycémies élevées avec des bolus de correction manuels.**

- If your basal IOB is negative (see screenshot below) a temporary basal rate (TBR) > 100% can be triggered in **Objective 6**.

![Example negative IOB](../images/Objective6_negIOB.png)

- Définissez votre cible légèrement plus haute que d'habitude, par pure précaution et pour avoir un peu plus de marge de sécurité.
- Enable 'Low Glucose Suspend' mode by pressing and holding the Loop icon in the top right corner of the OVERVIEW screen and selecting the Loop - LGS mode icon.
- Vous pouvez voir le basal temporaire actif sur l'écran d'accueil grâce au texte de basal turquoise, et en voir l'historique avec la courbe de basal turquoise du graphique.
- Vous pouvez subir temporairement des pics de glycémie à la suite d'hypos sans pouvoir augmenter le débit de base sur le rebond.

## Objectif 7 : Réglage de la Boucle Fermée, augmentation de l'IA (Insuline Active) maximale au dessus de 0 et abaissement progressif des cibles glycémiques

To complete **Objective 7** you have to close your loop and raise your [maxIOB](../DailyLifeWithAaps/KeyAapsFeatures.md#maximum-total-iob-openaps-cant-go-over-openaps-max-iob). **maxIOB** was zeroed out automatically in **Objective 6**. Ce n'est plus le cas. **AAPS** va commencer à utiliser la valeur max-IA telle que définie pour corriger les valeurs de glycémie élevées.

Minimal time to complete this objective: **1 day**. Vous serez obligé d'attendre que ce temps soit écoulé. It is not possible to proceed to the next **Objective** until this period of time has expired.

- Select **Closed Loop** either from [Preferences > OpenAPS](../SettingUpAaps/Preferences.md) or by pressing and holding the Loop icon in the top right corner of the **Overview** screen. Stay in **Closed Loop** over a period of 1 day.

- Slowly raise your 'Maximum total IOB OpenAPS can’t go over' (in OpenAPS called 'max-iob') above 0, until you find the settings that work best for you.

The default recommendation for this setting is “**average meal bolus + 3x max daily basal**”, where “max daily basal” is the maximum hourly value in any time segment of the day.

![max daily basal](../images/MaxDailyBasal2.png)

Cette recommandation doit être considérée comme un point de départ. If you use this rule but are experiencing AAPS delivering too much insulin as glucose levels rise, you may need to :

- lower the "Maximum total IOB OpenAPS can’t go over" value;
- review your **Profile** settings, only making one adjustment at a time.

Alternatively, if you are very insulin resistant, raise the **maxIOB** value very cautiously.

Once confident on how much **maxIOB** suits your looping patterns, lower your **BG targets** to your desired level.

## Objective 8: Adjust basals and ratios if needed, and then enable Autosens

As part of this **objective**, you will revisit your **Profile**'s performance and will use [Autosens](../DailyLifeWithAaps/KeyAapsFeatures.md#autosens) functionality as an indicator for wrong settings.

Minimal time to complete this objective: **7 days**. Vous serez obligé d'attendre que ce temps soit écoulé. It is not possible to proceed to the next **Objective** until this period of time has expired.

Enable [Autosens](../DailyLifeWithAaps/KeyAapsFeatures.md) over a period of 7 days and watch [**Overview**'s graph white line](../DailyLifeWithAaps/AapsScreens.md#section-g---additional-graphs) showing your insulin sensitivity rising or falling due to exercise or hormones etc. Keep an eye on the OpenAPS report tab which shows **AAPS** adjusting the sensitivity, basals and targets accordingly.

Additionally, you can use [Autotune](https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/autotune.html) as a one off to check your basals remain accurate or do a traditional basal test.

## Objectif 9 : Activation de fonctionnalités supplémentaires pour l'utilisation en journée, telles que la fonction SMB

In **Objective 9**, you will tackle and use **"Super Micro Bolus (SMB)"** as one core functionality. After working through the mandatory readings you will have a good understanding of what SMBs are, how these work, and why basal is set to zero temporarily after SMBs are given (zero-temping).

Minimal time to complete this objective: **28 days**. Vous serez obligé d'attendre que ce temps soit écoulé. You can’t proceed to the next Objective before this time is up.

- The [SMB section in this documentation](../DailyLifeWithAaps/KeyAapsFeatures.md#super-micro-bolus-smb) and [oref1 coverage in the openAPS docs](https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/oref1.html) are must-reads to understand **SMB** and the concept of **zero-temping**.
- Once done, you can [raise maxIOB](../DailyLifeWithAaps/KeyAapsFeatures.md#maximum-total-iob-openaps-cant-go-over-openaps-max-iob) to get **SMBs** working more effectively. maxIOB now includes all **IOB**, not just accumulated basal. This threshold pauses **SMBs** until IOB drops below this value (_e.g._ **maxIOB** is set to 7U and a bolus of 8U is given to cover a meal: SMBs will be paused and not given unless **IOB** drops below 7U).
  A good start is setting **maxIOB** = **average meal bolus + 3x max daily basal** where "max daily basal" is the maximum hourly value in any time segment of the day. See [objective 7](#objective-7-tuning-the-closed-loop-raising-maxiob-above-0-and-gradually-lowering-bg-targets) as reference.
- Evaluate your carb absorption rate and consider changing the “min_5m_carbimpact”-parameter in [Preferences > Absorption settings > min_5m_carbimpact](../SettingUpAaps/Preferences.md#min_5m_carbimpact) if you find it too slow or too fast.

## Objectif 10: Automatisation

**Automations** become available when **Objective 10** is started.

Minimal time to complete this objective: **28 days**. Vous serez obligé d'attendre que ce temps soit écoulé. You can’t proceed to the next Objective before this time is up.

Read the documentation page [Automation](../DailyLifeWithAaps/Automations.md) first.

Set-up the most basic automation rule; for example trigger an Android notification in a few minutes:

- Sélectionnez l'onglet des automatisations
- Dans le menu 3 points en haut à droite, sélectionnez Ajouter une règle
- Entez un nom de tâche comme "Ma première notification automatique"
- "Éditer" l'"État" (la condition de déclenchement)
  - cliquez sur le symbole "+" pour ajouter le premier déclencheur
  - sélectionnez "Heure" & "OK", cela créera une entrée par défaut à la date et heure actuelles
  - cliquez sur la partie MINUTE et modifiez l'heure de telle sorte qu'elle se déclenche dans quelques minutes. Puis cliquez sur OK pour fermer
  - cliquez sur OK pour fermer l'écran des déclencheurs
- Cliquez sur "Ajout" d'une "Action"
  - sélectionnez "Notification", "OK"
  - click "Notification" to edit the message, enter something like "My first automation"
- Wait until the time triggers the notification (note that depending on your phone, it can be a few minutes late)

You can then experiment with setting up a more useful **Automation**.
The documentation page gives a few examples, and you can search for "Automation" screenshots on the [Facebook](https://www.facebook.com/groups/AndroidAPSUsers) group. There is also a dedicated channel in the [Discord](https://discord.gg/4fQUWHZ4Mw) community.

For example, if you eat the same thing for breakfast at the same time every morning before school/work, you can create an **Automation** such as "before-breakfast-target" to set a slightly lower **Temporary Target** 30 minutes before having breakfast. Dans ce cas, votre déclencheur utilisera probablement "Période répétitive" qui permet de sélectionner des jours spécifiques de la semaine (Lundi, Mardi, Mercredi, Jeudi, Vendredi) et une heure précise (06h30). The action will consist of "Start temp target" with a lower than usual target value and a 30 minutes duration.

## Objective 11: Enabling additional features for daytime use, such as Dynamic Sensitivity plugin (DynISF).

Minimal time to complete this **Objective**: **28 days**. Vous serez obligé d'attendre que ce temps soit écoulé. It is not possible to proceed to the next **Objective** until this period of time has expired.

- Ensure that **SMB** is functioning properly
- Read the documentation concerning **Dynamic ISF** [here](../DailyLifeWithAaps/DynamicISF.md)
- Search the [Facebook](https://www.facebook.com/groups/AndroidAPSUsers) and [Discord](https://discord.gg/4fQUWHZ4Mw) groups for discussions around **Dynamic ISF** and read about other users' experiences and recommendations.
- Activez le **plugin SI Dynamique** et travaillez à la recherche de paramètres adaptés à votre propre corps. Il est conseillé de commencer avec une valeur inférieure à 100% pour des raisons de sécurité.

### Retour arrière dans les Objectifs

If you wish to go back in the **Objectives** for whatever reason you can do so by clicking at "clear finished".

![Go back in objectives](../images/Objective_ClearFinished.png)