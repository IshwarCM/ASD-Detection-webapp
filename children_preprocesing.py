def create_country_dict(country_of_res):
    # List of all possible country keys
    countries = [
        'contry_of_res_Afghanistan', 'contry_of_res_Argentina',
        'contry_of_res_Armenia', 'contry_of_res_Australia',
        'contry_of_res_Bahrain', 'contry_of_res_Bangladesh',
        'contry_of_res_Bhutan', 'contry_of_res_Brazil',
        'contry_of_res_Bulgaria', 'contry_of_res_Canada', 'contry_of_res_China',
        'contry_of_res_Costa Rica', 'contry_of_res_Egypt',
        'contry_of_res_Europe', 'contry_of_res_Germany', 'contry_of_res_Ghana',
        'contry_of_res_India', 'contry_of_res_Iraq', 'contry_of_res_Ireland',
        'contry_of_res_Isle of Man', 'contry_of_res_Italy',
        'contry_of_res_Japan', 'contry_of_res_Jordan', 'contry_of_res_Kuwait',
        'contry_of_res_Latvia', 'contry_of_res_Libya', 'contry_of_res_Malaysia',
        'contry_of_res_Malta', 'contry_of_res_Nepal',
        'contry_of_res_Netherlands', 'contry_of_res_New Zealand',
        'contry_of_res_Nigeria', 'contry_of_res_Oman',
        'contry_of_res_Philippines', 'contry_of_res_Qatar',
        'contry_of_res_Romania', 'contry_of_res_Russia',
        'contry_of_res_Saudi Arabia', 'contry_of_res_South Africa',
        'contry_of_res_South Korea', 'contry_of_res_Sweden',
        'contry_of_res_Syria', 'contry_of_res_Turkey',
        'contry_of_res_U.S. Outlying Islands',
        'contry_of_res_United Arab Emirates', 'contry_of_res_United States'
    ]
    
    # Create a dictionary with all keys set to 0
    country_dict = {country: 0 for country in countries}
    
    # If the input is a valid country, set its value to 1
    if country_of_res in country_dict:
        country_dict[country_of_res] = 1
    
    return country_dict


def create_ethnicity_dict(ethnicity):
    # List of all possible ethnicity keys
    ethnicities = [
        'ethnicity_Black', 'ethnicity_Hispanic',
       'ethnicity_Latino', 'ethnicity_Middle Eastern ', 'ethnicity_Others',
       'ethnicity_South Asian', 'ethnicity_Turkish',
       'ethnicity_White-European'
    ]
    
    # Create a dictionary with all keys set to 0
    ethnicity_dict = {group: 0 for group in ethnicities}
    
    # If the input is a valid ethnicity, set its value to 1
    if ethnicity in ethnicity_dict:
        ethnicity_dict[ethnicity] = 1
    
    return ethnicity_dict


def create_gender_dict(gender):
    # List of all possible gender keys
    genders = ['gender_f', 'gender_m']
    
    # Create a dictionary with all keys set to 0
    gender_dict = {g: 0 for g in genders}
    
    # If the input is a valid gender, set its value to 1
    if gender in gender_dict:
        gender_dict[gender] = 1
    
    return gender_dict


def create_relation_dict(relation):
    # List of all possible relation keys
    relations = [
        'relation_Health care professional', 'relation_Parent', 
        'relation_Relative', 'relation_Self'
    ]
    
    # Create a dictionary with all keys set to 0
    relation_dict = {rel: 0 for rel in relations}
    
    # If the input is a valid relation, set its value to 1
    if relation in relation_dict:
        relation_dict[relation] = 1
    
    return relation_dict

def create_autism_dict(autism):
    # List of all possible autism keys
    autism_keys = ['austim_no', 'austim_yes']
    
    # Create a dictionary with all keys set to 0
    autism_dict = {key: 0 for key in autism_keys}
    
    # If the input is a valid autism key, set its value to 1
    if autism in autism_dict:
        autism_dict[autism] = 1
    
    return autism_dict

def create_score_dict(A1_Score, A2_Score, A3_Score, A4_Score, A5_Score,
                      A6_Score, A7_Score, A8_Score, A9_Score, A10_Score):
    # Create a dictionary from the provided parameters
    scores_dict = {
        "A1_Score": A1_Score,
        "A2_Score": A2_Score,
        "A3_Score": A3_Score,
        "A4_Score": A4_Score,
        "A5_Score": A5_Score,
        "A6_Score": A6_Score,
        "A7_Score": A7_Score,
        "A8_Score": A8_Score,
        "A9_Score": A9_Score,
        "A10_Score": A10_Score
    }
    
    return scores_dict



def minmax_scaling(age, result):
    # Define min and max values for age and result
    age_min, age_max = 48, 132
    result_min, result_max = 0, 10

    # Apply Min-Max scaling for age
    scaled_age = (age - age_min) / (age_max - age_min)

    # Apply Min-Max scaling for result
    scaled_result = (result - result_min) / (result_max - result_min)

    # Return dictionary with scaled values
    return {'Age_Mons': scaled_age, 'result': scaled_result}


