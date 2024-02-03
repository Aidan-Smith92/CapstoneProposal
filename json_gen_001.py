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
            I will be using
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            This will help agencies and schools attempt to determine how to best help produce satisfactory educational outcomes
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.   

            -Create a single dataset
            -Make training set
            -Train algorithm using training set
            -Test accuracy of algorithm
            -Try to improve accuracy
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (2 Weeks) Creating a single dataset
            - (2 Weeks) Make training set
            - (3 Weeks) Train algorithm
            - (2 Weeks) Test accuracy of algorithm
            - (3 Weeks) Try to improve accuracy of algorithm
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
