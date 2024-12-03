#Question:
#Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:
#The scores should be ranked from the highest to the lowest.
#If there is a tie between two scores, both should have the same ranking.
#After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
#Return the result table ordered by score in descending order.

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Sort scores in descending order
    scores = scores.sort_values(by='score', ascending=False)
    
    # Calculate the rank using a groupby operation
    scores['rank'] = (scores['score']
                      .rank(method='dense', ascending=False)
                      .astype(int))
    
    # Select the required columns
    result = scores[['score', 'rank']]
    
    return result