import pandas as pd
hospital = pd.read_csv('/Users/wendyarias/Documents/GitHub/data-enrichment/data_files/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015-2.csv')
hospital
adi = pd.read_csv('/Users/wendyarias/Documents/GitHub/data-enrichment/data_files/NY_2015_ADI_Census Block Group_v3.1.csv')
adi
adi.columns
hospital.columns

### clean up for hospital columns
hospital.columns =  hospital.columns.str.replace('[^A-Za-z0-9]+', '_')
list(hospital.columns)
hospital.columns = hospital.columns.str.lower()
hospital.columns

### clean up for adi 
adi.columns = adi.columns.str.replace('[^A-Za-z0-9]+', '_')
adi.columns = adi.columns.str.lower()
adi.columns

###merge hospital and adi 
df_hospital_small= hospital[['hospital_county', 'facility_id', 'facility_name','zip_code_3_digits']]
print(df_hospital_small.sample(80).to_markdown())
df_adi_small = adi[['state', 'fips']]
print(df_adi_small.sample(80).to_markdown())
combined_df = df_hospital_small.merge(df_adi_small, how='left', left_on='facility_id', right_on='state')
combined_df
combined_df.to_csv('/Users/wendyarias/Documents/GitHub/data-enrichment/data_files/combined_df.csv')