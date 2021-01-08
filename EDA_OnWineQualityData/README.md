# EDA On Wine Quality Dataset
#### Problem Statement: 
It is very difficult to assess the quality of wine just by reading the label. Quality is assessed best by tasting. but as we have dataset which contains different ingredient of wine and also we have Quality of Wine column. So based on that we will try to find out what should be level of various ingredients to get the best quality of wine.


![](https://raw.githubusercontent.com/DhirajAmbure/MachineLearningProjects/main/images/90866256-hello-winter-mulled-wine-vector-illustration.jpg)



------------


#### Dataset:
- This dataset provides information about **wine's** ingredient like citric acid, chlorides, sulfur dioxide, density, PH, alcohol etc.
- There are total 6497 rows & 12 columns in given data
- There are 11 columns with float data-type and 1 column with int data-type

| Column Name  | Description  |
| :------------: | :------------: |
| fixed acidity | most acids involved with wine or fixed or nonvolatile (do not evaporate readily). |
| volatile acidity | the amount of acetic acid in wine, which at too high of levels can lead to an unpleasant, vinegar taste. |
| citric acid | found in small quantities, citric acid can add ‘freshness’ and flavor to wines. |
| residual sugar  | the amount of sugar remaining after fermentation stops, it’s rare to find wines with less than 1 gram/liter and wines with greater than 45 grams/liter are considered sweet. |
| chlorides | the amount of salt in the wine. |
| free sulfur dioxide | free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion; it prevents microbial growth and the oxidation of wine. |
| total sulfur dioxide | amount of free and bound forms of S02; in low concentrations, SO2 is mostly undetectable in wine, but at free SO2 concentrations over 50 ppm, SO2 becomes evident in the nose and taste of wine. |
| density | the density of water is close to that of water depending on the percent alcohol and sugar content. |
| pH | describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic); most wines are between 3-4 on the pH scale. |
| sulphates | a wine additive which can contribute to sulfur dioxide gas (S02) levels, wich acts as an antimicrobial andantioxidant. |
| alcohol | the percent alcohol content of the wine. |
| quality  | score between 0 to 10. |



------------



#### Basic Wine Characteristics
1. **Sweetness**:
	- Bone Dry: < 1 g/L
	- Dry: 1-10 g/L
	- Off-Dry: 10-35 g/L
	- Sweet: 35-120 g/L
	- Very Sweet: 120-220 g/L

2. **Acidity**:
	- The three prevalent acids in wine are tartaric, citric and malic
	- pH is the measure of acidity in wine on a logarithmic scale (Mostlt between 2.5 and 4.5)
	- pH and acidity have a negative correlation

3. **Tannin**:
	- More the Tannins, Dryer the Wine

4. **Body**:
	- Light-Bodied: 8-10% Alcohol
	- Medium-Bodied: 10-12% Alcohol
	- Full-Bodied: 12-15% Alcohol

