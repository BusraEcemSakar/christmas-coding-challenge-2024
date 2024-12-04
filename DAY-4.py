#Question:Remove duplicate email entries from a DataFrame. Retain only the row with the smallest id for each unique email. Modify the DataFrame in place.

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:

# Sort by id to ensure the smallest id is retained for each email
    person.sort_values(by="id", inplace=True)

    # Drop duplicates based on the email column
    person.drop_duplicates(subset="email", keep="first", inplace=True)
