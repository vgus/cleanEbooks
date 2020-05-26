from ExtracFunction import extract, extractOther
import os

mydir = os.path.abspath(os.path.dirname(__file__))
ruta2 = os.path.join(mydir, '../1995StaffordBeer/OEBPS/')

'''
extractOther(['i'],ruta2,"0_1", "IntroStaffordBeer")
'''
extract(['ix','x','xi'],ruta2,"0_6", "IntroPreface")
'''
extractOther(['iii'],ruta2,"0_2", "IntroCover",nombreClase='center')
extractOther(['iv'],ruta2,"0_3", "IntroDataBook",nombreClase='nonindent')
extractOther(['v'],ruta2,"0_4", "IntroDedication",nombreClase='nonindent')
extractOther(['vii','viii',],ruta2,"0_5", "IntroContent",nombreClase='nonindent')


extract(range(1,3),ruta2,"1_0", "TheNatureOfOperationResearch")
extract(range(3, 17), ruta2, '1_1', 'AnInitialPosture')
extract(range(17, 33), ruta2, '1_2', 'OnFixingBelief')
extract(range(33, 47), ruta2, '1_3', 'SomeDangerousPrecedents')
extract(range(47, 69), ruta2, '1_4', 'TheWedgedBear')
extract(range(69,93), ruta2, '1_5', 'TheNewLook')

extract(range(93,95),ruta2,"2_0", "TheActivityofOperationalResearch")
extract(range(95, 120), ruta2, '2_6', 'AboutModels')
extract(range(120,142), ruta2, '2_7', 'ModelsinAspic')
extract(range(142,172), ruta2, '2_8', 'TheFormalLanguages')
extract(range(172,204), ruta2, '2_9', 'AWalkintheRamifiedSystem')
extract(range(204,239), ruta2, '2_10', 'ApolloSGift')

extract(range(239,241),ruta2,"3_0", "TheRelevanceofCybernetics")
extract(range(241,270),ruta2,"3_11", "AboutSystems")
extract(range(270,299),ruta2,"3_12", "CopingwithComplexity")
extract(range(299,345),ruta2,"3_13", "ControllingOperations")
extract(range(345,370),ruta2,"3_14", "SelfOrganizingSystems")
extract(range(370,399),ruta2,"3_15", "ControllingEnterprises")

extract(range(399,401),ruta2,"4_0", "Outcomes")
extract(range(401,432),ruta2,"4_16", "OutcomeforIndustry")
extract(range(432,461),ruta2,"4_17", "InformationandAutomation")
extract(range(461,496),ruta2,"4_18", "TheOutcomeforGovernment")
extract(range(496,525),ruta2,"4_19", "TheOutcomeforManagementScience")
extract(range(525,551),ruta2,"4_20", "OnPracticability")
'''

#extractOther(range(551,556),ruta2,"5_0", "Index ",nombreClase='subject_index')
