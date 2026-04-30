import pandas as pd
import numpy as np
exam_data = {'name':["Jim", "Mike", "Sam", "Dave", "Matt", "Hal", "Chris", "John"],
             'score':[94, 79, 90, 83, 68, 71, 97, np.nan],
             'attempts':[2, 3, 1, 1, 3, 1, 2, 1],
             'quilify':["yes", "no", "yes", "yes", "no", "no", "yes", "no"]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h"]
df = pd.DataFrame(exam_data, index = labels)
print("Summery of the basic information about the data frame and its data: ")
print(df.info())