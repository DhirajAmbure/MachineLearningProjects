
## Machine Learning Foundation Project

------------


#### Problem Statement:
- What types of machine learning models perform best on this dataset?
- Which features are most indicative of a poisonous mushroom?

![Mushroom](https://raw.githubusercontent.com/DhirajAmbure/MachineLearningProjects/main/images/Vintage-Brown.jpg "Mushroom")

#### Dataset:
- There are total 8124 rows & 23 columns in given data
- All the 23 columns are of Object/String data-type

| Column Name | Description  |
| :------------: | :------------: |
| class  | edible=e, poisonous=p  |
| cap-shape  | bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s.  |
| cap-surface  | fibrous=f, grooves=g, scaly=y, smooth=s  |
| cap-color  | 	brown=n, buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y  |
| bruises  | bruises=t, no=f  |
| odor  | almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s  |
| gill-attachment  | attached=a, free=f  |
| gill-spacing  | close=c, crowded=w |
| gill-size  | 	broad=b, narrow=n  |
| gill-color  | black=k, brown=n, buff=b, chocolate=h, gray=g, green=r, orange=o, pink=p, purple=u, red=e, white=w, yellow=y  |
| stalk-shape  | enlarging=e, tapering=t  |
| stalk-root  | bulbous=b, club=c, equal=e, rhizomorphs=z, rooted=r  |
| stalk-surface-above-ring  | fibrous=f, scaly=y, silky=k, smooth=s  |
| stalk-surface-below-ring  | fibrous=f, scaly=y, silky=k, smooth=s  |
| stalk-color-above-ring  | brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y  |
| stalk-color-below-ring  | brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y  |
| veil-type  | partial=p  |
| veil-color  | brown=n, orange=o, white=w, yellow=y  |
| ring-number  | none=n, one=o, two=t  |
| ring-type  | 	evanescent=e, flaring=f, large=l, none=n, pendant=p  |
| spore-print-color  | black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y  |
| population  | abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y  |
| habitat  | grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d  |

- There is a Class column which segregates the mushrooms in 2 types, **Edible** and **Poisonous**
- Mushrooms basically have 5 physical properties such as, **Cap**, **Gill**, **Stalk**, **Veil** & **Ring**


------------


### Machine Learning Models Used:
1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. Decision Tree with GridSearch
5. Random Forest with RandomizedSearch

#### Model Evaluation Technique
1. Accuracy Score
2. Confusion Matrix
3. Precision Score
4. Recall Score
5. AUC-ROC Curve


------------

## Conclusions

1. *The important features of mushrooms to identify that it is safe to eat are as follows*:-
	- **Odor** – None, Almond & Anise are edible and creosote, foul, musty, pungent, spicy and fishy are poisonous.
	- **Gill Size** – Narrow are Poisonous.
	- **Rings** – Whether large or absent.
	- **Spore print colour** – Brown and Black are mostly edible & White, Chocolate are poisonous
	- **Population** – Available in several places.
	- **Habitat** – Grown on grasses, leaves, woods, path and urban.\

2. *From the comparison between scores of different evaluation metrics, we can say that following ML algorithms are best fit*
	- Decision Tree using GridSearchCV for Hyper-Parameter Tuning
	- Random Forest with RandomizedSearchCV for Hyper-Parameter Tuning
