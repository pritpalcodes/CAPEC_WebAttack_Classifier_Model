# MULTILABELCAPECCLASSIFICATIONOFWEBATTACKS

This machine learning (ML) project focuses on the identification and classification of web attacks by leveraging advanced multilabel machine learning algorithms. The primary objective is to categorize web attacks into Common Attack Pattern Enumeration and Classification (CAPEC) categories, providing a comprehensive understanding of the threats posed to web applications. The project employs a diverse set of multilabel machine learning algorithms, including but not limited to Binary Relevance, Random Forest, Label Powerset, Multi-Output Classifier, and LightGBM. These algorithms are selected for their ability to handle the complex and interconnected nature of web attack patterns, allowing for a more nuanced and accurate classification of threats.

## About the Project

The project's goal is to develop a robust model for classifying web attacks based on the CAPEC framework. By employing various multilabel machine learning algorithms, the project aims to accurately categorize different types of web attacks, providing valuable insights for enhancing web application security.

## Control Flow
![image](https://github.com/pritpalcodes/webAttack_Classifier_ML-Model/assets/90276050/805bbaec-8604-4701-bc41-52b90a9c4714)



## Demo
Run the file on streamlit server to see the following output:

### Classifying a "normal" url
![image](https://github.com/pritpalcodes/webAttack_Classifier_ML-Model/assets/90276050/cf635c5a-3777-46ae-ba8b-53b24dfaf32c)
[request classified as normal(=1)]
### Classifying a "malicious URL"
![image](https://github.com/pritpalcodes/webAttack_Classifier_ML-Model/assets/90276050/000d6795-ea50-4b19-a42c-fb966384b7b1)
[request classified as not normal(=0), protocol manipulation and path traversal attacks identified]

## Setting it Up

To set up the project, follow these steps:

1. **Importing the dataset:** Obtain the dataset containing web attack samples and corresponding CAPEC labels.
2. **EDA:** Perform exploratory data analysis to understand the dataset's characteristics and distributions.
3. ![image](https://github.com/pritpalcodes/webAttack_Classifier_ML-Model/assets/90276050/7891bccf-9250-4f20-bdc8-fd9b0c172a7b)
4. **Plotting to gain inferences:** Visualize the data to identify patterns and correlations.
   carefully selecting only the relevant features using plotting and EDA
   ![image](https://github.com/pritpalcodes/webAttack_Classifier_ML-Model/assets/90276050/9c1acf40-ef21-4e05-9106-66deb5c92e2d)
   ![image](https://github.com/pritpalcodes/webAttack_Classifier_ML-Model/assets/90276050/d0c811d3-80b2-413a-a865-e9fda8044172)
5. **PreProcessing:** Prepare the data for model training by handling missing values, scaling features, etc.
6. **Encoding:** Encode categorical variables and preprocess text data if applicable.
7. **Model Training:** Train multilabel machine learning models using algorithms such as Binary Relevance, Random Forest, etc. 
8. **Performance Analysis:** Evaluate the models' performance using appropriate metrics and fine-tune them as necessary.
9. **Pipelining:** Construct a pipeline for seamless data preprocessing and model training.
 ![image](https://github.com/pritpalcodes/webAttack_Classifier_ML-Model/assets/90276050/ce3b9cb6-2a4e-494c-bd3e-c293e2e52dce)


## Results

The project aims to achieve accurate classification of web attacks into CAPEC categories, providing insights into the types of threats encountered by web applications.

Results include model performance metrics, such as accuracy, precision, recall, and F1-score, along with insights gained from the classification process.

![image](https://github.com/pritpalcodes/webAttack_Classifier_ML-Model/assets/90276050/3b93f3cb-dd3e-422f-b80e-4d92249b6921)
![image](https://github.com/pritpalcodes/webAttack_Classifier_ML-Model/assets/90276050/2c6513ef-d55c-4dc1-a2cd-3eccf8c806c0)
![image](https://github.com/pritpalcodes/webAttack_Classifier_ML-Model/assets/90276050/2593c64a-6ca3-43ac-a971-1df2dfefed19)


## Contributors

- [Pritpal Singh](https://github.com/pritpalcodes)
- [Aibad Khan](link to their GitHub profile)
  
## Literature and References
 [1] Antunes, N., Vieira, M., 2015. On the metrics for benchmarking vulnerability detection tools.
 In: 2015 45th Annual IEEE/IFIP International Conference on Dependable Systems and
 Networks, pp. 505–516. doi:10.1109/DSN.2015.30.
 [2] Auxilia, M., Tamilselvan, D., 2010. Anomaly detection using a negative security model
 in Web application. In: 2010 International Conference on Computer Information
 Systems and Industrial Management Applications (CISIM), pp. 481–486. doi:10.
 1109/CISIM.2010.5643461.
 [3] Bermejo Higuera, J.R., 2013. Metodología de evaluación de herramientas de
 análisis automático de seguridad de aplicaciones web para su adaptación
 en el ciclo de vida de desarrollo. Universidad Nacional Educación a
 Distancia (UNED). http://e-spacio.uned.es/fez/eserv/tesisuned:IngInd-Jrbermejo/
 BERMEJO_HIGUERA_Juan_Ramon_Tesis.pdf.
 [4] Breiman, L., Friedman, J.H., Olshen, R.A., Stone, C.J., 1984. Classification and
 regression trees.(the wadsworth statistics/probability series), belmont. CA:
 Wadsworth.

