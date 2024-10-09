import os
import pandas as pd

import minsearch


DATA_PATH = './data/data_chunked_5s.csv'    # use this when on cloud



def load_index(data_path=DATA_PATH):
    df = pd.read_csv(data_path)
    
    documents = df.to_dict(orient="records")

    index = minsearch.Index(
        text_fields=[
            
            "content",
        ],
        keyword_fields=[],
    )

    index.fit(documents)
    return index