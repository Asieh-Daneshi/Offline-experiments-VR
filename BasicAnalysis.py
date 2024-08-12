# read the data file ==========================================================
import pandas as pd  
df = pd.read_csv("Asi.csv") 
#==============================================================================
# Column1 :> SessionInd; 	// if index==1, it is practice session, else, it is test session
# Column2 :> catchInd; 	// it is 1 if it is a catch. Otherwise, it is zero
# Column3 :> threshold; 	// yellow:0.6; blue:0.4
# Column4 :> numberOfAgents; 			// number of responding agents
# Column5 :> agents' raise hand: left:2; right:1; missed:0
# Column6 :> participant's raised hand. right(blue):1; left(yellow):2
# Column7 :> participant's response time
# Column8 :> congruencyFactor: congruent:1; incongruent:2
# Column9 :> time passed since beginning of the experiment
# in this experiment, always participant's right hand was blue, and left hand yellow
# Therefore,if column6=1, participant response was blue, and if column6=0, yellow!
#==============================================================================
Threshold=df.iloc[:,3]
mainTrials=df[Threshold==6]     # in main trials, the ration of blue to yellow pixels is 50-50

df.iloc[:,]

# Analyzing catch trials to remove outliers -----------------------------------
CatchTrials=df[df.iloc[:,1]==1]
Correct=((CatchTrials.iloc[:,2]==0.6) & (CatchTrials.iloc[:,5]==1)) | ((CatchTrials.iloc[:,2]==0.4) & (CatchTrials.iloc[:,5]==2))

PercentCorrect=sum(Correct.astype(int))/len(CatchTrials)    # just catch trials
