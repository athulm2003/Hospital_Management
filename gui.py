import streamlit as st
from patientviews import HsptlManager

patient_instance=HsptlManager()
tab1,tab2=st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add New Patient")
    name=st.text_input("Enter Patient Name")
    place=st.text_input("Enter Place")
    mobile=st.text_input("Enter Mobile Number")
    dr_name=st.text_input("Enter Doctor's Name")
    admission_date=st.date_input("Enter Admission Date(yyyy/mm/dd)")
    if st.button("Add New Patient"):
        patient_instance.post(name=name,place=place,mobile=mobile,dr_name=dr_name,admission_date=admission_date)
        st.success("New Patient Added Successfully...!")

with tab2:
    st.title("View Patient Details")
    records=patient_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No Records Found...!")