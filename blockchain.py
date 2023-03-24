from hashlib import *
import time
import pickle
from pathlib import Path
from ethereum import Blockchain, transaction, Block
import ethereum


########## Streamlit App ############# 



chain = Blockchain()

chain.addGenesis()


import streamlit as st
import streamlit_authenticator as stauth

st.title("Smart Transactions with Ethereum Ξ ♦")

names = ["Poornika"]
usernames = ["poornika123"]

file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {
    "usernames":{
        usernames[0]:{
            "name":names[0],
            "password":hashed_passwords[0]
        }
    }
}


authenticator = stauth.Authenticate(credentials, 
                "my-DashBoard" , "abcdef", cookie_expiry_days=30)

name, authentication_status, usernames = authenticator.login("Login" , "main")




if authentication_status == True:
    authenticator.logout("Logout" , "sidebar")


    add_selectbox = st.sidebar.selectbox(
        "What would you like to do?",
        ("Home Page" , "Create New ID", "Add Transaction" , "Add Transaction Information" , "View Transaction Chain" , "View Information Chain")
    )

    st.sidebar.title('Developer\'s Contact')
    st.sidebar.markdown('[![]'
                    '(https://img.shields.io/badge/Author-Poornika-brightgreen)]'
                    '(https://www.linkedin.com/in/poornika-m-9002a11b2/)') 

    st.sidebar.success("BlockChain Project")

    if add_selectbox == "Home Page":
        st.image("EthereumUniversal.webp")
        st.write("""
                This Streamlit app is designed to visualize the workings of a basic smart transaction using the Ethereum blockchain, which has been implemented from scratch. 
                The app has two main features:

        1. Peer-to-peer transaction: This allows users to send and receive Ethereum between themselves through the app.

        2. Additional transaction information: This feature enables users to add extra information to their transactions, such as notes or comments, which will be recorded on the blockchain along with the transaction data.

        Overall, this app provides a user-friendly way to interact with the Ethereum blockchain and gain a better understanding of how smart transactions work.
        Check the out all the features in the side bar of left side 🤏.
        """)

    elif add_selectbox == "Create New ID":
        st.subheader("Create a new peer in the chain 👨")
      

        form = st.form(key="user-creation")
        c1, c2 = st.columns(2)
        with c1:
            Name = form.text_input("Enter the name of user")
        with c2:
            Id_new = form.text_input("Enter an unique ID")


        submit = form.form_submit_button("click here to add the user")


        if submit == True:
            ethereum.blockNames.append(Name)
            ethereum.BlockIds.append(Id_new)
            st.success(f"New peer with Id : {Id_new} added to chain")


    elif add_selectbox == "Add Transaction":
        
        st.subheader("Make Smart transactions 💰")
        st.image("trans.png")

        form = st.form(key="user-trans")
        c1, c2, c3 = st.columns(3)
        with c1:
            fromUser = form.text_input("Enter the 'from username' ")
        with c2:
            toUser = form.text_input("Enter the 'to username' ")
        with c3:
            Amount = form.number_input("Enter the transaction amount")

        submit = form.form_submit_button("click here to add the user")

        if submit == True:
            if fromUser in ethereum.BlockIds and toUser in ethereum.BlockIds:
                transaction_ID = transaction(fromUser,toUser,Amount)
                st.write(transaction_ID)
                st.success("Transaction Successfully made")
                st.caption("Please check your chain information of the transaction")
            else:
                st.warning("Id's doesn't exits in the database!!")

    
    elif add_selectbox == "View Transaction Chain":
        st.subheader("View your complete transaction chain")
        st.image("chain.jpeg")
        st.write(Blockchain.pendingtrans)

    elif add_selectbox == "View Information Chain":
        st.subheader("View your complete Information chain")
        st.image("info.jpeg")
    
        st.write(chain.displayChain())

    elif add_selectbox == "Add Transaction Information":
        st.subheader("Add any personal transactional information")
        form = st.form(key="user-trans")
        c1, c2 = st.columns(2)
        with c1:
            UserId = form.text_input("Enter the the userId")
        with c2:
            Data = form.text_input("Enter the information to store ")
       

        submit = form.form_submit_button("click here to add the information")

        if submit == True:
            Blockinfo = Block(time.time(), Data)
            st.write(Blockinfo)
            chain.addBlock(Blockinfo)
            st.success("Information added successfully!")



    


else:
    st.warning("Username/password Incorrect!")


