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
            """001""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Predicting Educational Outcomes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            I want to proedict educational outcome based on demographic information, socio-economic factors, and educational history.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            I will be using https://nces.ed.gov/.  I will also be using https://www.census.gov/data.html.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            This predictive model aims to assist agencies and schools in identifying effective strategies to enhance satisfactory educational outcomes. By understanding the key factors influencing success, tailored interventions can be implemented.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            1. Data Collection and Cleaning:
            - Retrieve relevant data from specified sources and conduct thorough cleaning to address missing values, outliers, and inconsistencies.
            
            2. Feature Engineering and Selection:
            - Perform exploratory data analysis and consider creating new features and employ techniques for selecting the most impactful variables.
            
            3. Data Integration:
            - Merge the datasets together into one file, ensuring alignment of key variables and coherent representation.
            
            4. Training Set Development:
            - Construct a representative training data set.
            
            5. Model Selection and Iterative Development:
            - Experiment with different machine learning algorithms, emphasizing iterative development for optimal model selection.
            
            6. Cross-Validation and Hyperparameter Tuning:
            - Implement cross-validation techniques to ensure model generalization, and fine-tune hyperparameters for optimal performance.
            
            7. Performance Metrics and Model Interpretability:
            - Utilize model performance metrics for accurate evaluation and ensure the interpretability of the model for insights into predictive factors.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (2 Weeks) Data Collection and Cleaning
            - (2 Weeks) Feature Engineering and Selection
            - (3 Weeks) Data Integration and Training Set Formation
            - (2 Weeks) Model Selection and Iterative Development
            - (3 Weeks) Cross-Validation, Hyperparameter Tuning, and Evaluation
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            For this project maximum 4 students can work on it.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            The challenge is improving the accuracy of the algorithm.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Aidan Smith",
        "Proposed by email": "aidansmith@gwmail.gwu.edu",
        "instructor": "Edwin Lo",
        "instructor_email": "edwinlo@email.gwu.edu",
        "github_repo": "https://github.com/Aidan-Smith92/CapstoneProposal",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
