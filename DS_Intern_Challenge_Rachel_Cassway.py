"""
    Rachel Cassway
    Tue May 10 14:32:05 2022
    Shopify Fall 2022 Data Science Intern Challenge
"""
# import statements
import pandas as pd
import matplotlib.pyplot as plt

# universal variables
FILENAME = "2019_Winter_Data_Science_Intern_Challenge_Data_Set.csv"

def get_item_distr(df):
    '''
    function: get_item_distribution
    parameters: df, pandas dataframe holding Shopify sneaker data
    returns: total_item_distr, dictionary with total items in order as keys, 
        and frequency of total item occurances as values
    '''
    total_item_distr = {}
    for i in range(len(df)):
        items = df.loc[i, "total_items"]
        if items in total_item_distr.keys():
            total_item_distr[items] += 1
        else:
            total_item_distr[items] = 1
    return total_item_distr
    
def main():
    # read in provided sneaker data to pandas dataframe
    df = pd.read_csv(FILENAME)
    
    # get the distribution of total items in orders
    total_item_distr = get_item_distr(df)
    print('TOTAL ITEM DISTRIBUTION:', total_item_distr)
    # plot the total items in order distribution to identify any outliers
    plt.scatter(total_item_distr.keys(), total_item_distr.values())
    
    # averaging all order totals for AOV
    avg_order_amt = df['order_amount'].mean() 
    print('ALL ORDERS - AVG ORDER VALUE: $', round(avg_order_amt, 2), sep="")
    
    # new df for orders with 100 items or less - avg order total for AOV
    small_df = df.loc[(df['total_items'] < 100)]
    small_aov = small_df['order_amount'].mean()
    print('SMALL ORDERS (<100 ITEMS) - AVG ORDER VALUE: $', 
          round(small_aov, 2), sep="")
    
    # new df for orders with 2000 items - avg order total for AOV
    large_df = df.loc[(df['total_items'] >= 100)]
    large_aov = large_df['order_amount'].mean()
    print('LARGE ORDERS (≥100 ITEMS) - AVG ORDER VALUE: $', 
          round(large_aov, 2), sep="")
    
if __name__ == '__main__':
    main()