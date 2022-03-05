# make a bar chart of the results

basketball_results = [1.03,1.02,1.04]
golf_results = [1.01,0.98,0.85] # outlier 0.85 as we can see in the scatter graph
yogaball_results = [1.01,0.98,1.03]
tabletennis_ball_results = [1.00,0.99,1.04]
paper_results = [4.28,4.30,4.27]
poolball_results = [1.00,0.99,0.97]

import matplotlib.pyplot as plt

# make a dictionary of all the lists
results = {
    'basketball': basketball_results,
    'golf': golf_results,
    'yogaball': yogaball_results,
    'tabletennis': tabletennis_ball_results,
    'paper': paper_results,
    'poolball': poolball_results
}

def scatter_graph(results):
    plt.style.use('ggplot')
    plt.style.use('dark_background')
    # set the scale to higher
    # plt.xlim(1,1)
    # plt.ylim(1,1)
    for name, results_list in results.items():
        for value in results_list:
            plt.scatter(name,value,label=name+str(results_list.index(value)+1))
            print(value, name)
    plt.legend()
    plt.title('Results scatter graph')
    plt.xlabel('Items')
    plt.ylabel('Average time to fall')
    plt.show()

def bar_graph(results, title):
    # set the background color of the plot to black
    plt.style.use('ggplot')
    plt.style.use('dark_background')
    for name, results_list in results.items():
        average_result = sum(results_list)/len(results_list)
        print(average_result, name)
        # create a bar with the average and add a lebel of the name of the result_list
        plt.bar(name,average_result,label=name)
        # create a ledger with the color the name and the average
        plt.legend()
        # set the title of the plot
        plt.title(title)
        # set the x and y labels of the plot
        plt.xlabel('Items')
        plt.ylabel('Average time to fall')
    plt.show()


scatter_graph(results)

choice = input("Do you want to remove outliers? (y/n): ")
if choice == 'n':
    bar_graph(results, 'Graph with outliers')
elif choice == 'y':
    # remove outliers based on the scatter graph
    # golf_ball outlier 0.85 as we can see in the scatter graph so we remove it
    golf_results.remove(0.85)
    # remove also the paper because it is affected by air resistance
    results.pop('paper')
    bar_graph(results, 'Graph without outliers')
else:
    print("You have to make a choice (y/n)")