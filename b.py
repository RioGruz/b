import streamlit as st 
import pandas as pd
import numpy as np
from deta import Deta
from datetime import datetime

def main():

    st.header("Demo web aplikacija")

    username = st.text_input("Korisničko ime")

    if username == "Agencija A" or username == "Agencija B":
        pass
    else:
        st.write("greška")
    
    password = st.text_input("Password", type='password')

    if password != "1234":
        st.stop()
    else: 
        st.success("Uspješan login! Dobrodošli, {}".format(username))

    meni = ["Rezervacija", "Cjenik", "Pravila ponašanja", "Kontakt"]
    izbor = st.sidebar.selectbox("Izbor", meni)

    if izbor == "Rezervacija":

        with st.form("form"):
            lokacija = st.selectbox("Molimo odaberite željenu lokaciju:", ("", "Lovrjenac", "Sv.Ivan", "Bokar"))
            vrsta = st.selectbox("Molimo odaberite vrstu događaja:", ("", "Večera", "Koktel", "Ostalo"))
            datum = st.text_input("Molimo unesite datum rezervacije (u formatu dd.mm.gggg.)")
            opcija = st.selectbox("Molimo unesite vrstu rezervacije:", ("", "PRELIMINARNA rezervacija", "KONAČNA rezervacija"))
            submitted = st.form_submit_button("Spremi") 

        deta = Deta("a0p63srh_XBUhFhrF6SsZDNqXpF4fS3ZAj627V6uV")


        db = deta.Base("example-db")


        if submitted:
            db.put({"naziv_agencije": username, "lokacija":lokacija, "vrsta":vrsta, "datum": datum, "vrsta rezervacije": opcija})

        "Rezervacije:"
        db_content = db.fetch().items
        #st.write(db_content)
        df = pd.DataFrame(list(db_content))
        st.write(df[["datum", "lokacija", "vrsta","naziv_agencije", "vrsta rezervacije"]])
 
    elif izbor == "Cjenik":
        st.text("U izradi...")

    elif izbor == "Pravila ponašanja":
        st.text("U izradi...")

    else: 
        izbor == "Kontakt"
        st.text("U izradi...")

if __name__ == '__main__':
	main()