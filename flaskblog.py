from flask import Flask, escape, request,render_template,url_for
	
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['DEBUG']=True

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'touristplaces'

mysql = MySQL(app)

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
###### helper functions. Use them when needed #######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
##################################################

##Step 1: Read CSV File
df = pd.read_csv("C:/Users/Pravin Swamy/Favorites/Desktop/final_year_project/tourist_pura_1000.csv")
#print df.columns
##Step 2: Select Features

features = ['category','location']
##Step 3: Create a column in DF which combines all selected features
for feature in features:
	df[feature] = df[feature].fillna('')

def combine_features(row):
	try:
		return row['category'] +" "+row['location']
	except:
		print ("Error:", row)	

df["combined_features"] = df.apply(combine_features,axis=1)



app.config['SECRET_KEY']='383ff39566b2e647a0e9e5e93ffd84d1'

posts=[
	{
		'author':'prava',
		'content':'my first blog'
	},
	{
		'author':'pravinkumar',
		'content':'my second blog'
	}
]
@app.route('/')
#@app.route('/home')

def main():
    #name = request.args.get("name", "World")
    #cur=mysql.connection.cursor()
    #location1=request.form['location']
    #cur.execute("select category from places where location='location1' ")
    #data=cur.fetchall()
    #cur.close()
    return render_template('index.html')


@app.route('/select',methods=['POST'])
#@app.route('/home')

def select():
    #name = request.args.get("name", "World")
    cur=mysql.connection.cursor()
    cur_title=mysql.connection.cursor()
    cur_index=mysql.connection.cursor()
    location1=request.form['location']
    #print(location1)
    cur.execute("select image_url from places where location=%s",(location1,))
    cur_title.execute("select title from places where location=%s",(location1,))
    cur_index.execute("select id from places where location=%s",(location1,))
    data0=cur.fetchall()
    print(data0)
    data00=cur_title.fetchall()
    data000=cur_index.fetchall()
    #print(data00)
    #print(data)
    #print(data00)
    l1=list(map(list, data00))
    data01 = [j for sub in l1 for j in sub]    
    data1=list(data0)   
    print(data1)
    #data01=list(data00)
    data001=list(data000)


    data1=data1[3:11]
    data01=data01[3:11]
    data001=data001[3:11]
    #print(data1)
    #print(data01)
    #print(data001)
    #data000=zip(data1,data01)
    #print(data000)
    cur.close()
    cur_title.close()
    cur_index.close()
    return render_template('layout1.html',places=data1,places01=data01,places001=data001)





@app.route('/register')
def register():
    #name = request.args.get("name", "World")
    form=RegistrationForm()
    return render_template('register.html',title='register',form=form)

#@app.route('/final',methods=['POST'])
#def final():
    #name = request.args.get("name", "World")
    #form=LoginForm()
    #return render_template('login.html',title='login',form=form)
    #check=request.form.getlist("chkbox")
    #print(check)
    
    #check1=request.form.getlist("ratings1")
    
    #while("" in check1) : 
    #    check1.remove("")
    #print(type(check1))
    
    #l3=[check[0],check[1],check[2]]
    #l4=[check1[0],check1[1],check1[2]]
    #l2=list(map(float, l4))
    #print(type(list_2))
    
    #place_lover = [(l3[0],l2[0]),(l3[1],l2[1]),(l3[2],l2[2])]
    
    
    #similar_places = pd.DataFrame()
    #for place,rating in place_lover:
    #    similar_places = similar_places.append(get_similar(place,rating),ignore_index = True)
    #print(similar_places)
    #print(similar_places.head(10))
    #l10=[]
    #l10=similar_places.sum().sort_values(ascending=False).head(20)
    #print(similar_places.sum().sort_values(ascending=False).head(20))
    #print(similar_places.columns)
    #res1 = " ".join(str(l10))
    #print(res1)
    
    #return (res1)




@app.route('/final1',methods=['POST'])
def final1():
    check=request.form.get("chkbox")
    print(check)
    
    cv = CountVectorizer()

    count_matrix = cv.fit_transform(df["combined_features"])

    ##Step 5: Compute the Cosine Similarity based on the count_matrix
    cosine_sim = cosine_similarity(count_matrix) 
    user_likes = check

    ## Step 6: Get index of this movie from its title
    place_index = get_index_from_title(user_likes)

    similar_places =  list(enumerate(cosine_sim[place_index]))

    ## Step 7: Get a list of similar movies in descending order of similarity score
    sorted_similar_places = sorted(similar_places,key=lambda x:x[1],reverse=True)
    #print(sorted_similar_places)
    #l10=[]
    #l10=similar_places.sum().sort_values(ascending=False).head(20)
    #print(similar_places.sum().sort_values(ascending=False).head(20))
    #print(similar_places.columns)
    #res1 = " ".join(str(l10))
    #print(res1)
    l10=[]
    i=0
    for element in sorted_similar_places:
        l10.append(get_title_from_index(element[0]))
        print (get_title_from_index(element[0]))
        i=i+1
        if i>8:
            break

    print(l10)
    cur_1=mysql.connection.cursor()
    cur_2=mysql.connection.cursor()
    cur_3=mysql.connection.cursor()
    cur_4=mysql.connection.cursor()
    cur_5=mysql.connection.cursor()
    cur_6=mysql.connection.cursor()
    cur_7=mysql.connection.cursor()
    cur_8=mysql.connection.cursor()
    img_1=l10[0]
    img_2=l10[1]
    img_3=l10[2]
    img_4=l10[3]
    img_5=l10[4]
    img_6=l10[5]
    img_7=l10[6]
    img_8=l10[7]
    
    cur_1.execute("select image_url from places where title=%s",(img_1,))
    cur_2.execute("select image_url from places where title=%s",(img_2,))
    cur_3.execute("select image_url from places where title=%s",(img_3,))
    cur_4.execute("select image_url from places where title=%s",(img_4,))
    cur_5.execute("select image_url from places where title=%s",(img_5,))
    cur_6.execute("select image_url from places where title=%s",(img_6,))
    cur_7.execute("select image_url from places where title=%s",(img_7,))
    cur_8.execute("select image_url from places where title=%s",(img_8,))
    img_url_1=cur_1.fetchall()
    img_url_2=cur_2.fetchall()
    img_url_3=cur_3.fetchall()
    img_url_4=cur_4.fetchall()
    img_url_5=cur_5.fetchall()
    img_url_6=cur_6.fetchall()
    img_url_7=cur_7.fetchall()
    img_url_8=cur_8.fetchall()
    img_url_10=list(sum(img_url_1, ()))
    img_url_20=list(sum(img_url_2, ()))
    img_url_30=list(sum(img_url_3, ()))
    img_url_40=list(sum(img_url_4, ()))
    img_url_50=list(sum(img_url_5, ()))
    img_url_60=list(sum(img_url_6, ()))
    img_url_70=list(sum(img_url_7, ()))
    img_url_80=list(sum(img_url_8, ()))
    
    print(img_url_1)
    print(img_url_2)
    print(img_url_3)
    print(img_url_4)
    print(img_url_5)
    print(img_url_10)
    print(img_url_20)
    print(img_url_30)
    print(img_url_40)
    print(img_url_50)

    img_url_list=[]
    img_url_list.append(img_url_10)
    img_url_list.append(img_url_20)
    img_url_list.append(img_url_30)
    img_url_list.append(img_url_40)
    img_url_list.append(img_url_50)
    img_url_list.append(img_url_60)
    img_url_list.append(img_url_70)
    img_url_list.append(img_url_80)
    img_url_flatten_list = [j for sub in img_url_list for j in sub]
    print(img_url_flatten_list)
    print(img_url_flatten_list[0])
    cur_1.close()
    cur_2.close()
    cur_3.close()
    cur_4.close()
    cur_5.close()
    cur_6.close()
    cur_7.close()
    cur_8.close()
    
    return render_template('layout2.html',place_url=img_url_flatten_list,place_title=l10)



if __name__=='__main__':
	app.run(debug=True)