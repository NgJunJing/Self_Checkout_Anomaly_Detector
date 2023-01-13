from pycaret.classification import load_model, predict_model
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from PIL import Image
import base64

# load the Classifier
lmodel = load_model('s2_best')

def DisplayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    st.markdown(pdf_display, unsafe_allow_html=True)

def predict(model, inputs):
    pred_df = predict_model(model, data=inputs)
    pred = pred_df['Label'][0]
    return pred

st.markdown ("## :orange[Self-checkout Transaction Anomaly Detector]")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Documentation", "Online Anomaly Detector", "Batch Anomaly Detector"],
        icons=["house","book","search","file-spreadsheet"],
        menu_icon="cursor",
        default_index=0,
        styles={
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {
                "font-size": "20px",
                "text-align": "left",
                "margin": "2px",
                "--hover-color": "#eee",
            },
        },
    )


if selected == 'Home':

    st.write('---')
    st.markdown('''
    ##### Self-checkout Transaction Anomaly Detector is a web application that allows user to perform anomaly detection using self-checkout transactions data

    **This web application consists of:**

    ##### **:orange[Documentation]**

    Contains the **User Manual** for this app, the **Dataset** used to build the supervised anomaly detection model, and the **Exploratory Data Analysis** of the dataset used 
    
    ##### **:orange[Online Anomaly Detector]**

    Based on the input from user for the required fields, the app generates a prediction

    ##### **:orange[Batch Anomaly Detector]**

    User upload a **csv file containing the variables required**. Then, the app will label every data in the file and return a labelled DataFrame. User has the option to download the DataFrame. User can also use the app to generate Exploratory Data Analysis based on the uploaded data.

    ''')
    
    st.write('---')


if selected == 'Documentation':

    st.header("Documentation")
    st.write('---')

    st.header('**Dataset**')
    data = pd.read_csv("train.csv")
    st.markdown('''
    Dataset used to train the self-checkout transaction anomaly detecion model is obtained from the [Data Mining Cup 2019](https://www.data-mining-cup.com/reviews/dmc-2019/) competition

    Following are the variables description:

    1. ***trustLevel*** : Trust Level of a customer, from lowest (1) to highest (6) 

    2. ***totalScanTimeInSeconds*** : Total time(secs) between the first and last product scanned 

    3. ***grandTotal*** : The total amount to be paid for the scanned items 

    4. ***lineItemVoids*** : The number of scanned but cancelled items 

    5. ***scansWithoutRegistration*** : The number of times a customer tried to trigger the scanner without scanning anything 

    6. ***quantityModification*** : The number of times a customer modified the quantities for any of the scanned products 

    7. ***scannedLineItemsPerSecond*** : Number of scanned products in one second 

    8. ***valuePerSecond*** : Total value of scanned products in one second 
 
    9. ***lineItemVoidsPerPosition*** : The ratio of item voids to the total number of scanned and not cancelled products 

    10. ***fraud*** : Label, fraud (1), not fraud (0) 

    ''')
    st.write(data)

    st.write('---')
    
    st.header('**Exploratory Data Analysis of Dataset Used**')
    # Add some description here
    if st.button('Generate EDA Report'):
        EDAdataset = ProfileReport(data, explorative=True)
        st_profile_report(EDAdataset)

    st.write('---')
    
    st.header('**User Manual**')
    st.markdown('This is the user manual for using the two anomaly detector function in this app')
    st.markdown('''
    #### Online Anomaly Detector

    1. Select “Online Anomaly Detector” in the “Main Menu”.

    ''')
    um1 = Image.open('UM1.png')
    st.image(um1)
    st.markdown('''

    2. Then, you will land on this page.

    ''')
    um2 = Image.open('UM2.png')
    st.image(um2)
    st.markdown('''

    3. Now, input every field here on the page.

    ''')
    um3 = Image.open('UM3.png')
    st.image(um3)
    st.markdown('''

    4. Click on “Check” button at the bottom.

    ''')
    um4 = Image.open('UM4.png')
    st.image(um4)
    st.markdown('''

    5. View result generated.

    ''')
    um5 = Image.open('UM5.png')
    st.image(um5)
    st.write('---')
    st.markdown('''
    #### Batch Anomaly Detector

    1. Select "Batch" Anomaly Detector” in the “Main Menu”.

    ''')
    um6 = Image.open('UM6.png')
    st.image(um6)
    st.markdown('''

    2. Then, you will land on this page.

    ''')
    um7 = Image.open('UM7.png')
    st.image(um7)
    st.markdown('''

    3. Upload a csv containing the variables stated.

    ''')
    um8 = Image.open('UM8.png')
    st.image(um8)
    st.markdown('''

    4. The result DataFrame with the labelled data will be displayed below and can be downloaded after clicking the “Download Labelled Data” button.

    ''')
    um9 = Image.open('UM9.png')
    st.image(um9)
    st.markdown('''

    5. The Exploratory Data Analysis report for the Labelled DataFrame is generated below it.

    ''')
    um10 = Image.open('UM10.png')
    st.image(um10)

    st.write('---')
    

#First Function: Online User Input
if selected == 'Online Anomaly Detector':

    st.header("Online Anomaly Detector")

    # Defining the inputs
    #input1 = trustLevel                : Trust Level of a customer, from lowest(1) to highest(6)
    #input2 = totalScanTimeInSeconds    : Total time(secs) between the first and last product scanned
    #input3 = grandTotal                : The total amount to be paid 
    #input4 = lineItemVoids             : The number of scanned but cancelled items
    #input5 = scansWithoutRegistration  : The number of times a customer attempted to activate the scanner w/out actually scanning anything
    #input6 = quantityModification      : The number of times a customer modified the quantities for one of the scanned products
    #input7 = scannedLineItemsPerSecond : Average number of scanned products per second
    #input8 = valuePerSecond            : Average total value of scanned products per second
    #input9 = lineItemVoidsPerPosition  : Average numer of item voids per total number of scanned and not cancelled products
    #'_This_ is some **Markdown***'
    '**The Total Number of Items Scanned (1-50 Items)**'
    temp_input1 = st.number_input('The Total Number of Items Scanned (1-50)', min_value=1, max_value=50, value=1, step=1, label_visibility="collapsed")
    '**The Total Time Taken in Seconds between The Fisrt and The Last Product Scanned (1-3600secs for more than 1 item)**'
    input2 = st.number_input('The Total Time Taken in Seconds between The Fisrt and The Last Product Scanned (1-3600secs for more than 1 item)', 0, 3600, value=0, step=1, label_visibility="collapsed")
    '**The Grand Total of Product Scanned (RM)**'
    input3 = st.number_input('The Grand Total of Product Scanned (RM)', 0.00, 1000.00, step=0.01, value=0.00, format="%0.2f", label_visibility="collapsed")
    '**The Number of Scanned but Cancelled Items**'
    input4 = st.number_input('The Number of Scanned but Cancelled Items', min_value=0, max_value=temp_input1, step=1, value=0, label_visibility="collapsed")
    '**The Number of Attempts to Activate The Scanner Without Actually Scanning Anything**'
    input5 = st.number_input('The Number of Attempts to Activate The Scanner Without Actually Scanning Anything', min_value=0, max_value=50, step=1, value=0, label_visibility="collapsed")
    '**The Number of Times The Customer Modified The Quantities for One of The Scanned Products**'
    input6 = st.number_input('The Number of Times The Customer Modified The Quantities for One of The Scanned Products', min_value=0, max_value=100, step=1, value=0, label_visibility="collapsed")
    '**Customer Trust Level (Lowest(1) to Highest(6))**'
    input1 = st.selectbox('Customer Trust Level',[1,2,3,4,5,6], label_visibility="collapsed")
    if input2 == 0:
        input7 = 0
        input8 = 0
    else:
        input7 = temp_input1/input2
        input8 = input3/input2
    input9 = input4/(temp_input1-input4)

    input_listing = {'trustLevel': input1, 'totalScanTimeInSeconds': input2, 'grandTotal': input3, 'lineItemVoids': input4,
    'scansWithoutRegistration': input5, 'quantityModifications': input6, 'scannedLineItemsPerSecond': input7,
    'valuePerSecond': input8, 'lineItemVoidsPerPosition': input9}
    input_df = pd.DataFrame([input_listing])
    
    normal_img = Image.open('Normal.png')
    anomalous_img = Image.open('Anomalous.png')
    
    # Make Prediction
    if st.button("Check"):
        output = predict(model=lmodel, inputs=input_df)
        st.markdown('#### According to our anomaly detection model, this transaction is')
        if output == 1:
            st.image(anomalous_img)
        else:
            st.image(normal_img)


if selected == 'Batch Anomaly Detector':
    
    st.header("Batch Anomaly Detector")

    # Let user upload csv data file
    file_upload = st.file_uploader("Upload csv file for self-checkout transactions anomaly detection", type=["csv"])

    # Make predictions and Display the output dataframe
    if file_upload is not None:
        @st.cache
        def load_csv():
            data = pd.read_csv(file_upload)
            return data
        preds = predict_model(lmodel, load_csv())
        preds = preds.rename(columns={"Label": "Anomalous"})
        EDAreport = ProfileReport(preds, explorative=True)
        
        def df_to_csv(df):
            return df.to_csv(index=False).encode('utf-8')

        st.header('**Labelled DataFrame**')
        st.write(preds)
        st.download_button(
        "Download Labelled Data",
        df_to_csv(preds),
        "labelled_data.csv",
        "text/csv",
        key='download-data'
        )
        st.write('---')

        st.header('**Exploratory Data Analysis Report**')
        st_profile_report(EDAreport)
        st.write('---')

        


    else:
        st.info('Awaiting for CSV file to be uploaded')

        



