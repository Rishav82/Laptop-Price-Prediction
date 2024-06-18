import streamlit as st
import pickle
import numpy as np
import pandas
lr1 = pickle.load(open('lr1.pkl', 'rb'))
rf1 = pickle.load(open('rf1.pkl', 'rb'))
bag1 = pickle.load(open('bag1.pkl', 'rb'))
st.title('Laptop Price Pridiction App')
st.header('Fill the Details to generate the Pridicted Laptop Price')
options = st.sidebar.selectbox(
    'select ML Model', ['Lin_Reg', 'Bag_Reg', 'Random_Forest'])
company = st.selectbox('Company', [
                       'Dell', 'Lenovo', 'HP', 'Asus', 'Acer', 'MSI', 'Toshiba', 'Apple', 'Others'])
typename = st.selectbox('Typename', [
                        'Notebook', 'Gaming', 'Ultrabook', '2 in 1 Convertible', 'Workstation', 'Netbook'])
ram = st.selectbox('RAM', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.slider('Weight', 0.69, 4.42)
touchscreen = st.selectbox('Touchscreen', ['Yes', 'No'])
ips = st.selectbox('IPS', ['Yes', 'No'])
cpu_brand = st.selectbox(
    'CPU_brand', ['I7', 'I5', 'I3', 'AMD', 'Other Intel Processor'])
hdd = st.selectbox('HDD', [0, 32, 128, 500, 1000, 2000])
ssd = st.selectbox('SSD', [0, 8, 16, 32, 64, 128,
                   180, 240, 256, 512, 768, 1000, 1024])
os = st.selectbox('OS', ['Win', 'Others', 'Mac'])
gpu_brand = st.selectbox('GPU_brand', ['Intel', 'Nvidia', 'AMD'])
if st.button('Predict'):
    if company == 'Dell':
        company = 3
    elif company == 'Lenovo':
        company = 5
    elif company == 'HP':
        company = 4
    elif company == 'Asus':
        company = 2
    elif company == 'Acer':
        company = 0
    elif company == 'MSI':
        company = 6
    elif company == 'Others':
        company = 7
    elif company == 'Toshiba':
        company = 8
    else:
        company = 1
    if typename == 'Notebook':
        typename = 3
    elif typename == 'Gaming':
        typename = 1
    elif typename == 'Ultrabook':
        typename = 4
    elif typename == '2 in 1 Convertible':
        typename = 0
    elif typename == 'Workstation':
        typename = 5
    else:
        typename = 2
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchsreen = 0
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
    if cpu_brand == 'I7':
        cpu_brand = 3
    elif cpu_brand == 'I5':
        cpu_brand = 2
    elif cpu_brand == 'Other Intel Processor':
        cpu_brand = 4
    elif cpu_brand == 'I3':
        cpu_brand = 1
    else:
        cpu_brand = 0
    if gpu_brand == 'Intel':
        gpu_brand = 1
    elif gpu_brand == 'Nvidia':
        gpu_brand = 2
    else:
        gpu_brand = 0
    if os == 'Win':
        os = 2
    elif os == 'Others':
        os = 1
    else:
        os = 0

    test = np.array([company, typename, ram, weight, touchsreen,
                    ips, cpu_brand, hdd, ssd, os, gpu_brand])
    test = test.reshape(1, 11)
    if options == 'Lin_Reg':
        st.success(lr1.predict(test)[0])
    elif options == 'Bag_Reg':
        st.success(bag1.predict(test)[0])
    else:
        st.success(rf1.predict(test)[0])
