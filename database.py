from deta import Deta
# import os
# from dotenv import load_dotenv

# load_dotenv(".env")
# DETA_KEY = os.getenv("DETA_KEY")
DETA_KEY = st.secrets["DETA_KEY"]

deta = Deta(DETA_KEY)



db = deta.Base("pepmine_mvp")

db_pep =deta.Base("pepmine_peptide")

def insert_user(username,name,password):
    init_pep_nft = {}
    return db.put({"key":username,"name":name,"password":password,"token":0,"pep_nft":init_pep_nft})

def insert_peptide(sequence):
    return db_pep.put({"key":sequence,"fund_now":0,"fund_target":1000000,"funder":{}})


# insert_user("tutu","Wenqiang Tu","twq999")

def fetch_all_users():
    res = db.fetch()
    return res.items

def fetch_all_peps():
    res = db_pep.fetch()
    return res.items


def get_user(username):
    """If not found, the function will return None"""
    return db.get(username)

def get_pep(sequence):
    return db_pep.get(sequence)

def update_user(username, updates):
    """If the item is updated, returns None. Otherwise, an exception is raised"""
    return db.update(updates, username)

def update_pep(sequence, updates):
    """If the item is updated, returns None. Otherwise, an exception is raised"""
    return db_pep.update(updates,sequence)


def delete_user(username):
    """Always returns None, even if the key does not exist"""
    return db.delete(username)


# print(fetch_all_users())
