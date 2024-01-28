#%%
import json
import os
import shutil

#%%

def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

semester2code = { "sp":"01", "spr":"01", "spring":"01", "su":"02", "sum":"02", "summer":"02", "fa":"03", "fall":"03"}
thisfilename = os.path.basename(__file__) # should match _ver for version, ideally 3-digit string starting as "000", up to "999"

data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """000""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Predicting Political Violence in a Country""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The goal of this project is to develop a methodology to analyze the socio-economic factors of a country and
            then predict the degree of political violence occuring in it based on those factors. This will help humanitarian
            relief organizations predict which countries they may have to allocate resourcces to.  I want to use demographic
            and economic statistics as well as details about the government of the countries being analyzed from both
            historical sources and the present situation.  I would also like to facilitate making comparisons between countries.
            This project could potentially be applied to all countries.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            Dr. Ryan is going to provide us the data and the location of it. 

            We have a geospatial data for these three cities: Lagos Nigeria, Accra Ghana and Nairobi Kenya. Each city there is a 
            series of covariates at 100m grid cells. There are 166 individual tif files that are aligned to the same grid for 
            the cities. There are approximately 50-60 for each city. These data sets represent infrastructure, social economic 
            status (SES), facilities and services, physical hazards and assets and others. The number of covariates varies by 
            city, but there is a set that is common to all of the cities.  

            For each city we are working on extracting Sentinel 2 imagery (10m spatial resolution) for each city. We are running 
            contextual features for each city. This produces 144 layers from the imagery that map spatial patterns and estimates 
            of vegetation. These features are calculated on the same grid and in such a way that a 10x10 group of pixels matches 
            each 100m grid cell. Imagery is collected from Google Earth Engine (Training and validation Data). For Lagos and Accra
            we have created a training and validation data set at the grid cell level. Training data is Deprived residential,
            Other Built, and non-built. Model Attributes: Want to be able to model deprivation estimate at the 100m grid cell 
            level. Test different models to be able to do this. Also, estimate of degree of deprivation, produce a scale of 
            deprivation so that city governments can set this level themselves and play around with the models.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            This project is going to help agencies to tackle poverty and help countries.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            1. Automate data capturing from Google Earth Engine (Python code in the engine).
            2. Work on the covariate features importance.  
            3. Use covariate features to model degree of poverty (Classical Models).
            4. Use a model developed in on city and apply it to other cities (Transfer Learning)
            5. Combine satellite images with covariate features.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (3 Weeks) Data Automation.  
            - (3 Weeks) Feature Importance  
            - (4 Weeks) Modeling  
            - (2 Weeks) Combine satellite images with covariate features  
            - (1 Weeks) Compiling Results  
            - (1 Weeks) Writing Up a paper and submission
            - (1 Weeks) Final Presentation  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            For this project maximum 4 students can work on it.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            The challenge is on data analysis part , find a good features and train a decent model.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Dr. Ryan Engstrom",
        "Proposed by email": "rengstro@gwu.edu",
        "instructor": "Amir Jafari",
        "instructor_email": "ajafari@gmail.com",
        "github_repo": "https://github.com/amir-jafari/Capstone",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
