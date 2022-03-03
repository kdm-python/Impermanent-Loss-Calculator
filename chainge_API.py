import requests
import pandas as pd

##############################
### CHAINGE PRICE DATA API ###
##############################

# this URL from the telegram chat returns an empty DF
# used identical code with other API links and it works
# perhaps need to use a different data extractions method, other than CSV

chainge_url = "https://public.chainge.finance/v1/getTotalSupply?symbol=CHNG"
target_csv_path = "chainge_data.csv"

response = requests.get(chainge_url)
response.raise_for_status()    # Check that the request was successful

with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")

chaingeDF = pd.read_csv("chainge_data.csv")
print(type(chaingeDF))
print(len(chaingeDF))
print(chaingeDF)