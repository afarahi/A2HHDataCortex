import numpy as np
import sys


def learningPipeline():

    import sys; import numpy as np
    import numpy.random as npr 
    import matplotlib.pylab as plt
    from sklearn.cross_validation import train_test_split
    import scipy.io as scio
    import pandas as pd    
    npr.seed(1000)

    print( "READY" )

  
"""

    if stepNum == 0:
        # look into catalogs
        #data = pd.read_csv('./data/lead_parcel_data_train.csv')
        data = pd.read_csv('./data/sentinel_test_data.csv')
        #print data.columns
        #print data[:3]
        #data['Lead (ppb)'] += 1.
        #data['Lead (ppb)'] = data['Lead (ppb)'].apply(np.log10)
        #print data['Year Built'].unique()
        #print data['Longitude'].unique()
        #print data['Prop Class'].unique()
        print data['Lead (ppb)'][data['Lead (ppb)'] > 400]
        print len(data)

    if stepNum == 1:
 
       from bayesianPipeline import bayesian_pipeline
       bp = bayesian_pipeline()
       M = bp.run_mcmc()
       #bp.class_stats(M)
       bp.save_model(M)

    if stepNum == 2:
 
       from mixtureModelAnalysisPipeline import mixtureModelAnalysisPipeline

       mma = mixtureModelAnalysisPipeline()
       #mma.classification_detail()
       mma.stats_pipeline()


cols = [ u'Sample Number', u'Date Submitted', u'Lead (ppb)', u'Copper (ppb)',
         u'Street #', u'Street Name', u'City', u'Zip Code', u'Best Address',
         u'PID Dash', u'PID no Dash', u'Property Address', u'Property Zip Code',
         u'Owner Type', u'Owner Name', u'Owner Address', u'Owner Zip Code',
         u'Owner City', u'Owner State', u'Owner Country', u'Tax Payer Name',
         u'Tax Payer Address', u'Tax Payer State', u'Tax Payer Zip Code',
         u'Homestead', u'Homestead Percent', u'HomeSEV', u'Land Value',
         u'Land Improvements Value', u'Residential Building Value',
         u'Residential Building Style', u'Commercial Building Value',
         u'Building Storeys', u'Parcel Acres', u'Rental', u'Use Type',
         u'Prop Class', u'Old Prop class', u'Year Built', u'USPS Vacancy',
         u'Zoning', u'Future Landuse', u'DRAFT Zone', u'Housing Condition 2012',
         u'Housing Condition 2014', u'Commercial Condition 2013', u'Latitude',
         u'Longitude', u'Hydrant Type' ]





"""


