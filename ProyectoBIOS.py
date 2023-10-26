import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier

'''
Age : Age of the patient
Sex : Sex of the patient
exang: exercise induced angina (1 = yes; 0 = no)
ca: number of major vessels (0-3)
cp : Chest Pain type chest pain type
    Value 1: typical angina
    Value 2: atypical angina
    Value 3: non-anginal pain
    Value 4: asymptomatic
trtbps : resting blood pressure (in mm Hg)
chol : cholestoral in mg/dl fetched via BMI sensor
fbs : (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
rest_ecg : resting electrocardiographic results
Value 0: normal
Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
thalach : maximum heart rate achieved
target : 0= less chance of heart attack 1= more chance of heart attack
'''
PC = 0.85
PM = 0.1

columnas = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa',
            'thall', 'output']
configuration = []
firstGeneration = {}
sonsGeneration = {}


def knn(X, Y, Individual):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    bin = tuple(Individual)
    accuracy = float(accuracy_score(y_test, y_pred))

    return {bin: accuracy}


def top10(Population):
    maximos = []
    accs = list(Population.items())
    ordenados = sorted(accs, key=lambda conteo: conteo[1], reverse=True)

    for k in range(0, 10):
        maximos.append(ordenados[k])

    tenMost = maximos
    # printDataframe(accs)
    dataframe = printDataframe(maximos)

    return tenMost, dataframe


def printDataframe(Box):
    df = pd.DataFrame(Box, columns=['Bin', 'Accuracy'])
    print(df)
    print("================================================")
    return df


def selTournament(Population):
    parents = random.choices(Population, k=3)
    parents = sorted(parents, key=lambda x: x[1], reverse=True)

    p1 = parents[0]
    p2 = parents[1]
    indP1 = population.index(p1)
    indP2 = population.index(p2)
    #print(indP1,indP2)
    return parents[0], parents[1], indP1, indP2


def crosses(Parent1, Parent2):
    crossPoint = np.random.randint(13)
    #print("el punto de cruza es: ", crossPoint)
    sonC1 = np.zeros(13, int)
    sonC2 = np.zeros(13, int)
    #print("el padre 1 es:", parent1)
    #print("el padre 2 es:", parent2)

    for k in range(0, len(Parent1)):

        sonC1[k] = Parent1[k]
        sonC2[k] = Parent2[k]

        if k > crossPoint:
            sonC1[k] = Parent2[k]
            sonC2[k] = Parent1[k]

    return sonC1, sonC2


def mutation(Son1, Son2):
    mut1 = []
    mut2 = []
    # print(son1,son2)
    for i in range(0, 13):
        mut1.append(random.random())
        mut2.append(random.random())
        # print(son1[i])
        # print("i es:",i)
        if mut1[i] < PM:  # Si el numero para el gen es menor que la probabilidad de mutacion, se muta
            if Son1[i] == 1:
                Son1[i] = 0

            else:
                Son1[i] = 1
        # print("===================")
        # print(son1[i])
        if mut2[i] < PM:  # Si el numero para el gen es menor que la probabilidad de mutacion, se muta
            if Son2[i] == 1:
                Son2[i] = 0
            else:
                Son2[i] = 1
    #print(mut1,mut2)
    return son1, son2

def fitnessGen (Cromosome):
    config = []
    pos = 0
    for i in Cromosome:
        if i == 1:
            # print(pos,j, columnas[pos])
            config.append(columnas[pos])
        pos += 1
    X = dataset[config]
    y = dataset.iloc[:, -1]
    individualn = knn(X, y, Cromosome)
    return individualn


## KNN1
dataset = pd.read_csv('C:/Users/jerem/Desktop/heart.csv')
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]
ni = array = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# print(ni)
individual1 = knn(X, y, ni)
firstGeneration.update(individual1)

## POBLACION INICIAL
population = np.random.randint(0, 2, [10, 13])
for cromosome in population:
    gen = fitnessGen(cromosome)
    firstGeneration.update(gen)

population, representationStart = top10(firstGeneration)
# print(representationStart)

best2=[]
## GENERACIONES de cruza = 5
for g in range(100):
    print("--------------------------------------------------")
    print("Generacion numero ", g + 1, "de la cruza y mutacion:")
    # Seleccionamos 2 individuos
    parent1, parent2, indexP1, indexP2 = selTournament(population)
    #print(parent1, parent2)
    #print(indexP1,indexP2)
    # Cruza de padres
    crossPr = random.random()
    #print("La probabilidad de cruza es: ", crossPr)
    if crossPr < PC:
        son1, son2 = crosses(parent1[0], parent2[0])
    elif crossPr >= PC:
        son1 = parent1[0]
        son2 = parent2[0]
    #print("los hijos resultantes son: ", son1, son2)
    # Mutacion de hijos
    mutson1, mutson2 = mutation(list(son1), list(son2))
    #print("Los hijos mutados son: ", mutson1, mutson2)
    sonF1 = fitnessGen(mutson1)
    sonF2 = fitnessGen(mutson2)
    sonF1 = list(sonF1.items())
    sonF2 = list(sonF2.items())

    population.pop(indexP1)
    population.insert(indexP1,(sonF1[0][0],sonF1[0][1]))
    population.pop(indexP2)
    population.insert(indexP2,(sonF2[0][0],sonF2[0][1]))

    ordenados = sorted(population, key=lambda conteo: conteo[1], reverse=True)
    dataframe = printDataframe(ordenados)