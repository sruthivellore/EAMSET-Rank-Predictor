def to_open_files(files, code, category, branch):
    import csv
    sets = []
    with open(files,'r') as file1:
        line = csv.reader(file1,delimiter = ' ')
        for parts in line:
            if code in parts:
                return check_branch(parts, category, branch)

def check_branch(parts, category, branch):
    branch_check = {"OCCSE" : 1, "BCCSE" : 2, "SCCSE" :3,"STCSE" : 4,"OCECE" : 5,"BCECE" : 6,"SCECE" : 7,"STECE" :8 ,"OCEEE" : 9, "BCEEE" : 10, "SCEEE" : 11,"STEEE" : 12}
    return parts[branch_check[category + branch]]
  
def uppercase(word):
    return word.upper()

def predict_value_of_y(xs,ys):
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib import style
    style.use('ggplot')
    x = np.array(xs,dtype = np.float64)
    y = np.array(ys,dtype = np.float64)
    
    coefficient1 = np.polyfit(x, y, 1)
    coefficient2 = np.polyfit(x, y, 2)
    coefficient3 = np.polyfit(x, y, 3)
    linear_equation = np.poly1d(coefficient1)
    quadratic_equation = np.poly1d(coefficient2)
    cubic_equation = np.poly1d(coefficient3)
    
    xp = np.linspace(2013, 2017)
    plt.xlim(2013,2017)
    
    plt.title('Rank Prediction Graph')
    plt.xlabel('Years')
    plt.ylabel('Cutoff Ranks')
    plt.plot(x,y,'.', xp,linear_equation(xp),'-', xp,quadratic_equation(xp),'.', xp, cubic_equation(xp),'-')
    
    predict_x = 2017
    predict_y1 = int(np.polyval(coefficient1,predict_x))
    predict_y2 = int(np.polyval(coefficient2,predict_x))
    predict_y3 = int(np.polyval(coefficient3,predict_x))
    
    r_squared1 = squared_error(y,[linear_equation(x1) for x1 in x])
    r_squared2 = squared_error(y,[quadratic_equation(x1) for x1 in x])
    r_squared3 = squared_error(y,[cubic_equation(x1) for x1 in x])
    
    if predict_y2 > 0:
        print("Predicted Cutoff For 2017 :", predict_y2)
    elif predict_y1 > 0:
        print("Predicted Cutoff For 2017 :", predict_y1)
    elif predict_y3 > 0:
        print("Predicted Cutoff For 2017 :", predict_y3)
    else:
        print("Could not Predict")
    plt.scatter(predict_x,predict_y1 , color='m')
    plt.scatter(predict_x,predict_y2 , color='m')
    plt.scatter(predict_x,predict_y3 , color='m')
    
    plt.legend(['cutoff ranks','linear fit','quadratic fit','cubic fit'], loc ='upper left')
    plt.show()

def squared_error(x, y):
    from scipy import stats
    import numpy as np
    slope,intercept,r_values,p_values,std_err = stats.linregress(x,y)
    return r_values * r_values


#input
college_code = uppercase(input("Enter College Code :  "))
category = uppercase(input("Category           :  "))
branch = uppercase(input("Branch             :  "))

year2016 = to_open_files("for_year2016.csv",college_code,category,branch)
year2015 = to_open_files("for_year2015.csv",college_code,category,branch)
year2014 = to_open_files("for_year2014.csv",college_code,category,branch)
year2013 = to_open_files("for_year2013.csv",college_code,category,branch)
predict_value_of_y([2013, 2014, 2015 ,2016],[year2013, year2014, year2015, year2016])
