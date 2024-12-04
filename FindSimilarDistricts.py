import pandas as pd

def compare_districts(list1, list2):
    # Ensure both lists are of the same length
    if len(list1) != len(list2):
        print("Error: Lists are of different lengths.")
        return False

    ranges = [0.30, 0.2, 0.25, 0.2, 0.4]
    reasons= ["Total population" , "hispanic%" , "mean h" , 
            "high school+", "bachelor degree+"]
    # Iterate through both lists and compare each element
    results = []
    for i, (a, b, r) in enumerate(zip(list1, list2, ranges)):
        # Check if the first element is within 90% and 110% of the second element
        if (1-r) * float(b) <= float(a) <= (1+r) * float(b):
            results.append(True)
        #    print(True)
        else:
            results.append(False)
            # print(reasons[i])
            #print(f"{(1-RANGE) * float(b)} <= {float(a)} <= {(1+RANGE) * float(b)}")
        #    print(False)
    return False if False in results else True


# Function to process a single CSV file
def process_csv(file):
    # Read the CSV file
    df = pd.read_csv(file)
    # Skip the first two columns
    columns_to_process = df.columns[3:]

    florida27 = [754619.0, 551539.0/754619.0, 124442.0, 86.5, 44.0]
    #florida27 = [754619.0, 551539.0/754619.0, 346779.0, 75323.0, 124442.0, 12.6, 86.5, 44.0]
    # Iterate through each column
    for col in columns_to_process:
        # Get values from rows 
        try:
            values = [df[col].iloc[i] for i in [0, 29, 200, 240, 241]]
            #values = [df[col].iloc[i] for i in [0, 29, 36, 199, 200, 217, 240, 241]]
            
            # values = [float(x.replace(",", "")) for x in values]
            if '+' not in values[0]:
                values = [float(x.replace(",", "")) for x in values]
                values[1] = values[1]/values[0]
                # print(f"Column '{col}' in file '{file}'")
                # print("FINAL "+ str(compare_districts(values, florida27)))
                if compare_districts(values, florida27):
                    print(values)
                    print()
                    print(f"Column '{col}' in file '{file}'")
                    print("\t Total population {:,} -vs- {:,}: {:.2%}".format(values[0], florida27[0], values[0]/florida27[0]))
                    print("\t hispanic/ latino {:,} -vs- {:,}: {:.2%}".format(values[1], florida27[1], values[1]/florida27[1]))
                    # print("\t Native           {:,} -vs- {:,}".format(values[2], florida27[2]))
                    #print("\t median h income  {:,} -vs- {:,}".format(values[3], florida27[3]))
                    print("\t mean h income    {:,} -vs- {:,}: {:.2%}".format(values[2], florida27[2], values[2]/florida27[2]))
                    # print("\t poor all people  {:,} -vs- {:,}".format(values[5], florida27[5]))
                    print("\t high school+     {:,} -vs- {:,}: {:.2%}".format(values[3], florida27[3], values[3]/florida27[3]))
                    print("\t bachelor degree+ {:,} -vs- {:,}: {:.2%}".format(values[4], florida27[4], values[4]/florida27[4]))
                    print()
                    print(compare_districts(values, florida27))

        except IndexError:
            print(f"Column '{col}' in file '{file}' has fewer than 23 rows.")
        
# File paths of the CSV files
files = ['Florida_District_all.csv', 'Illinois_District_all.csv', 
         'Georgia_District_all.csv', 'California_District_all.csv', 
         'Louisiana_District_all.csv', 'Mississippi_District_all.csv',
         'Texas_District_all.csv', 'New_Mexico_District_all.csv',
         'South_Carolina_District_all.csv', 'Arizona_District_all.csv']

# Process each file
for file in files:
    process_csv(file)
