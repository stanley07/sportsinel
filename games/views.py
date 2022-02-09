from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages
import numpy as np
import pandas as pd 
import csv
# Create your views here.


def now(request):
	return render(request, 'now.html')



def home_wins(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch.csv")    
    df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score', 'home_team']]
    df1 = df1.set_axis(['Date', 'Country', 'League', 'Home', 'Away','predicted_homescore', 'predicted_awayscore', 'Prediction'], axis=1)
    df1 = df1.round({'predicted_home_score' : 1, 'predicted_away_score':1})
    df1 = df1.sort_values(by=["predicted_homescore"], ascending=False)
    

    df2 = df1.head(30)
    df2 = df2.style.set_precision(2)
    df2 = df2.to_html()    
    #df1 = df1.sort_values(by=["win"], ascending=False)
    home = df2  
    return render(request, 'home_wins.html', {
    	'home': home
    	})
	

def home_loose(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch.csv")     
    df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score', 'away_team']]
    df1 = df1.set_axis(['Date', 'Country', 'League', 'Home', 'Away','Predicted_home_score', 'Predicted_away_score', 'Prediction'], axis=1)
    #df1 = df.rename(columns={'match_datetime': 'Match_Datetime', 'country': 'Country', 'league': 'League', 'home_team': 'Home', 'away_team': 'Away', 'predicted_home_score': 'predicted_home_score', 'predicted_away_score': 'predicted_away_score', 'home_team': 'win' })
    df1 = df1.sort_values(by=["Predicted_home_score"], ascending=False)
    #df1 = df1.drop(['Predicted_home_score', 'Predicted_away_score'], axis = 1)
    
    df2 = df1.tail(30) 
    df2 = df2.style.set_precision(2)   
    df2 = df2.to_html()    
    #df1 = df1.sort_values(by=["win"], ascending=False)
    home1 = df2  
    return render(request, 'home_loose.html', {
    	'home1': home1,
    	})


def away_wins(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch.csv")  
    df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score', 'away_team']]  
    ##df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score', 'away_team']]
    df1 = df1.set_axis(['Match_Datetime', 'Country', 'League', 'Home_team', 'Away_team','Predicted_home_score', 'Predicted_away_score', 'Prediction'], axis=1)
    df1 = df1.sort_values(by=["Predicted_away_score"], ascending=False)    
    df2 = df1.head(30) 
    df2 = df2.style.set_precision(2)   
    df2 = df2.to_html()    
    away = df2  
    return render(request, 'away_wins.html', {
    	'away': away
    	})



def away_loose(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch.csv")  
    df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score', 'away_team']]  
    ##df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score', 'away_team']]
    df1 = df1.set_axis(['Match_Datetime', 'Country', 'League', 'Home_team', 'Away_team','Predicted_home_score', 'Predicted_away_score', 'Prediction'], axis=1)
    df1 = df1.sort_values(by=["Predicted_away_score"], ascending=False)    
    df2 = df1.tail(30) 
    df2 = df2.style.set_precision(2) 
    df2 = df2.to_html()    
    away = df2  
    return render(request, 'away_loose.html', {
        'away': away
        })
    


def raw_predictions(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch.csv")    
    
    df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score']]
    ##df1['predicted'] = np.where((df1['predicted_home_score'] <= df1['predicted_away_score']), df1['away_team'], np.nan)
    ##df1 = df1.drop(['predicted_home_score', 'predicted_away_score'], axis=1)
    ##df1 = df1.dropna()
    #df1 = df1.set_index('match_datetime')
    
    #df1 = df1.style
    
    #df4 = df1.to_html()

    
    ###df1 = df1.round({'predicted_home_score': 1, 'predicted_away_score': 1}) 

    #@df1 = df1.round({'predicted_home_score' : 1, 'predicted_away_score':1})

    #@df1['predicted_goals'] = df1['predicted_home_score'] + df1['predicted_away_score']

    #df1 = df1.rename(columns={'match_datetime': 'Match_Datetime', 'country': 'Country', 'league': 'League', 'home_team': 'Home', 'away_team': 'Away', 'predicted_home_score': 'predicted_home_score', 'predicted_away_score': 'predicted_away_score', 'home_team': 'win' })
       
    #df2 = df2.sort_values(by=["win"], ascending=False)
    #df1 = df1.set_axis(['match_datetime', 'Country', 'League', 'Home_team', 'Away_team','Predicted_home_score', 'Predicted_away_score', 'total_predicted_goals'], axis=1)
    #df1 = df1.sort_values(by=["total_predicted_goals"], ascending= False)
    #df1 = df.loc[['England', 'Germany']]
    df2 = df1.style.set_precision(2)
    
    #df2 = Styler.format(precision=2)
    raw = df2.to_html()

    return render(request, 'raw.html', {
        'raw': raw
        })


 
def over_goals(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch.csv")    
    df = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'home_odds', 'draw_odds', 'away_odds', 'predicted_home_score', 'predicted_away_score']]
    df['total_predicted_goals'] = df['predicted_home_score'] + df['predicted_away_score']
    df = df.set_axis(['Match_Datetime', 'Country', 'League', 'Home_team', 'Away_team','home_odds', 'draw_odds', 'away_odds','Predicted_home_score', 'Predicted_away_score', 'total_predicted_goals'], axis=1)
    df1 = df.sort_values(by=["total_predicted_goals"], ascending= False)
    df1 = df1.drop(['home_odds', 'draw_odds', 'away_odds'], axis=1)
    
    df1 = df1.head(10)
    dt = ['Over 2.5', 'Over 2.5', 'Over 2.5', 'Over 2.5', 'Over 2.5', 'Over 1.5', 'Over 1.5','Over 1.5','Over 1.5','Over 1.5']
    df1['Prediction'] = dt
    df2 = df1.drop(['Predicted_home_score', 'Predicted_away_score', 'total_predicted_goals'], axis=1)
    df2 = df2.style
    goals = df2.to_html()  
    return render(request, 'over_goals.html', {
        'goals': goals
        })
    

def under_goals(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch.csv")    
    df = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'home_odds', 'draw_odds', 'away_odds', 'predicted_home_score', 'predicted_away_score']]
    df['total_predicted_goals'] = df['predicted_home_score'] + df['predicted_away_score']
    df = df.set_axis(['Datetime', 'Country', 'League', 'Home', 'Away','home_odds', 'draw_odds', 'away_odds','Predicted_home_score', 'Predicted_away_score', 'total_predicted_goals'], axis=1)
    df1 = df.sort_values(by=["total_predicted_goals"], ascending=False)
    df1 = df1.drop(['home_odds', 'draw_odds', 'away_odds'], axis=1)
    
    df1 = df1.tail(15)
    
    dt = ['Under 3.5','Under 3.5','Under 3.5','Under 3.5','Under 3.5', 'Under 3.5', 'Under 3.5', 'Under 3.5', 'Under 3.5','Under 2.5', 'Under 2.5', 'Under 2.5', 'Under 2.5', 'Under 2.5','Under2.5'] 
    df1['Prediction'] = dt
    df1 = df1.set_index('Datetime')
    df1 = df1.drop(['Predicted_home_score', 'Predicted_away_score', 'total_predicted_goals'], axis=1)
    df2 = df1.style
    nogoals = df2.to_html()
  
    return render(request, 'under_goals.html', {
        'nogoals': nogoals
        })

    
def to_win(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch.csv")    
    df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score', 'home_team']]
    df1 = df1.set_axis(['Match_Datetime', 'Country', 'League', 'Home_team', 'Away_team','Predicted_home_score', 'Predicted_away_score', 'Prediction'], axis=1)
    #df1 = df.rename(columns={'match_datetime': 'Match_Datetime', 'country': 'Country', 'league': 'League', 'home_team': 'Home', 'away_team': 'Away', 'predicted_home_score': 'predicted_home_score', 'predicted_away_score': 'predicted_away_score', 'home_team': 'win' })
    
    
    df2 = df1.sort_values(by=["Predicted_home_score"], ascending=False)
    
    #df1 = df1.drop(['Predicted_home_score', 'Predicted_away_score'], axis = 1)
    df2 = df2.head(15) 
    df2 = df2.style
    df2 = df2.to_html()
   
       
    #df1 = df1.sort_values(by=["win"], ascending=False)
    home7 = df2
   
    
      
    return render(request, 'to_win.html', {
        'home7': home7
        })   





def now(request):
 #   file = open("media/csv/predictions_with_gridsearch.csv")
  #  csvreader = csv.reader(file)
   # header = next(csvreader)
    
    #rows = []
    #for row in csvreader:
     #   rows.append(row[1])
   

    return render(request, 'now.html')


def top_pick(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch.csv")    
    df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score', 'home_team']]
    df1 = df1.set_axis(['Match_Datetime', 'Country', 'League', 'Home_team', 'Away_team','Predicted_home_score', 'Predicted_away_score', 'Prediction'], axis=1)
    #df1 = df.rename(columns={'match_datetime': 'Match_Datetime', 'country': 'Country', 'league': 'League', 'home_team': 'Home', 'away_team': 'Away', 'predicted_home_score': 'predicted_home_score', 'predicted_away_score': 'predicted_away_score', 'home_team': 'win' })
    
    
    df2 = df1.sort_values(by=["Predicted_home_score"], ascending=False)
    
    #df1 = df1.drop(['Predicted_home_score', 'Predicted_away_score'], axis = 1)
    df2 = df2.head(5) 
    df2 = df2.style   
    df2 = df2.to_html()
   
       
    #df1 = df1.sort_values(by=["win"], ascending=False)
    home5 = df2
   
    
      
    return render(request, 'top_pick.html', {
        'home5': home5
        })    

def vip(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch_selection.csv") 
    df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'selection', 'predicted_result']]
    ##df1 = datch_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score', 'home_team']]
    ##df1 = df1.set_axis(['Match_Datetime', 'Country', 'League', 'Home_team', 'Away_team','Predicted_home_score', 'Predicted_away_score', 'Prediction'], axis=1)
    #df1 = df.rename(columns={'match_datetime': 'Match_Datetime', 'country': 'Country', 'league': 'League', 'home_team': 'Home', 'away_team': 'Away', 'predicted_home_score': 'predicted_home_score', 'predicted_away_score': 'predicted_away_score', 'home_team': 'win' })
    
    #df1 = df1.drop(df1[df1['selection'] == 'N'].index, inplace = True)
    #df1 = df1.set_index('match_datetime')

    #df1 = df1.drop(["N"], inplace = True)
    df1 = df1.dropna()
    df2 = df1[df1.selection != "N"]

    
    df2 = df2.style
    df2 = df2.to_html()    
    
    #df1 = df1.sort_values(by=["win"], ascending=False)
    finish = df2  

    return render(request, 'vip.html', {
        'finish': finish
        })


def gol(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch_selection.csv") 
    df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'selection', 'predicted_result']]
    
    df2 = df1[df1.selection != "N"]
    df2 = df2.style
    df2 = df2.to_html()    
    
    #df1 = df1.sort_values(by=["win"], ascending=False)
    end = df2  


    return render(request, 'gol.html', {
        'end':end
        })


 
def gold(request):
    df = pd.read_csv("media/csv/predictions_with_gridsearch_selection.csv")    
    df = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'home_odds', 'draw_odds', 'away_odds', 'predicted_home_score', 'predicted_away_score']]
    df['total_predicted_goals'] = df['predicted_home_score'] + df['predicted_away_score']
    df = df.set_axis(['Match_Datetime', 'Country', 'League', 'Home_team', 'Away_team','home_odds', 'draw_odds', 'away_odds','Predicted_home_score', 'Predicted_away_score', 'total_predicted_goals'], axis=1)
    df1 = df.sort_values(by=["total_predicted_goals"], ascending=False)
    df1 = df1.drop(['home_odds', 'draw_odds', 'away_odds'], axis=1)
    
    df1 = df1.head(10)
    dt = ['Over 2.5', 'Over 2.5', 'Over 2.5', 'Over 2.5', 'Over 2.5', 'Over 1.5', 'Over 1.5','Over 1.5','Over 1.5','Over 1.5']
    df1['Prediction'] = dt
    df2 = df1.reset_index()
    df2 = df2.style
    gold = df2.to_html()
  
    return render(request, 'gold.html', {
        'gold': gold
        })
    


#def away_wins(request):(extra_to_check by me)
    ####df = pd.read#
    ####df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score']]  
    ##df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score', 'away_team']]
    ##df1 = df1.set_axis(['Match_Datetime', 'Country', 'League', 'Home_team', 'Away_team','Predicted_home_score', 'Predicted_away_score', 'Prediction'], axis=1)
    
    #df1 = df.rename(columns={'match_datetime': 'Match_Datetime', 'country': 'Country', 'league': 'League', 'home_team': 'Home', 'away_team': 'Away', 'predicted_home_score': 'predicted_home_score', 'predicted_away_score': 'predicted_away_score', 'home_team': 'win' })
    

    ####df1['predicted'] = np.where((df1['predicted_home_score'] <= df1['predicted_away_score']), df1['away_team'], np.nan)
    ####df1 = df1.drop(['predicted_home_score', 'predicted_away_score'], axis=1)
    ####df1 = df1.dropna()
    ####df1 = df1.set_index('match_datetime')


    ##df1 = df1.sort_values(by=["Predicted_away_score"], ascending=False)
    ##df1 = df1.drop(['Predicted_home_score', 'Predicted_away_score'], axis = 1)
    ##df2 = df1.head(30)
    ####df1 = df1.style
    ####df2 = df1.to_html() 

    #df1 = df1.sort_values(by=["win"], ascending=False)
    ####away = df2  
    ####return render(request, 'away_wins.html', {
        ####'away': away
        ####})


####def away_loose(request):
    ####df = pd.read_csv("media/csv/predictions_with_gridsearch.csv") 
    ####df1 = df[['match_datetime', 'country', 'league', 'home_team', 'away_team', 'predicted_home_score', 'predicted_away_score']]     
    ####df1['predicted'] = np.where((df1['predicted_home_score'] >= df1['predicted_away_score']), df1['home_team'], np.nan)
    ####df1 = df1.drop(['predicted_home_score', 'predicted_away_score'], axis=1)
    ####df1 = df1.dropna()
    ####df1 = df1.set_index('match_datetime')
    ####df2 = df1.tail(30)
    ####df2 = df2.style
    ####df2 = df2.to_html()    
    ####away = df2  
    ####return render(request, 'away_loose.html', {
        ####'away': away
        ####}