# Importing Libraries
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import pdfkit

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("ReportCardTemplate.html")

# This Function takes a dataframe and find all the Candidate's ID inside it
def get_all_candidate_ID(df):
    List_of_ID = list(set(df['Unnamed: 0'][1::]))
    return List_of_ID


# this Function takes a canditate ID and return a candidate specific dataframe
def get_candidate_df(c_id, df):
    df = df[df['Unnamed: 0'] == c_id]
    df = df.reset_index()
    return df

# this function takes the cadidate data and convert into HTML file and then convert that HTML to candidate specifc PDF
def make_candidate_pdf(candidate_data):
    html_out = template.render(candidate_data)
    htmlFile = open("report.html", 'w')
    htmlFile.write(html_out)
    htmlFile.close()
    options = {
        "enable-local-file-access": None
    }

    pdfkit.from_file("report.html", "PDF_REPORTS/" +
                     candidate_data['CandidateName']+".pdf", options=options)


# main function which calls every other function and find candidate specific data and passes them to make PDF
def main():
    print("This Program is to Make Student's Report Card using Python :\nPlease note :\n1. This Program will only work for Data similar to DummyData.xlsx else it will throw error\n2. The format of PDF generated can be changed by editing 'ReportCardTemplate.html'\n3. The input file should be .xlsx\n4. Candidate Photos will be taken from 'Pics for assignment' folder, Please ensure that candidate photos title is Candidate Name")
    Excel_file_name = input(
        "Please input the Excel file name (eg Studentdata.xlsx): ")
    print("Student Report Card will saved in folder REPORT_CARDS with student name as name of PDF\nPlease wait while PDF's are being Generated")
    main_df = pd.read_excel(Excel_file_name)
    candidate_ids = get_all_candidate_ID(main_df)

    # Runniong a loop over all the available candidate ID
    for c_id in candidate_ids:
        candidate_df = get_candidate_df(c_id, main_df) # get candidate specific data using ID

        # getting all the Details for making PDF
        CandidateName = candidate_df['Unnamed: 4'][1]
        RegistrationNumber = candidate_df['Unnamed: 5'][1]
        Grade = candidate_df['Unnamed: 6'][1]
        NameofSchool = candidate_df['Unnamed: 7'][1]
        Gender = candidate_df['Unnamed: 8'][1]
        Address = candidate_df['Unnamed: 10'][1] + "/"+candidate_df['Unnamed: 12'][1]
        DateofBirth = str(candidate_df['Unnamed: 9'][1]).split()[0]
        DateofTest = candidate_df['Unnamed: 11'][1]
        ScoreData = candidate_df[['Unnamed: 13', 'Unnamed: 14',
                                  'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18']].to_numpy()
        FinalResult = candidate_df['Unnamed: 19'][1]
        PossibleScore = candidate_df['Unnamed: 17'].sum()
        candidate_df['Unnamed: 18'] = pd.to_numeric(
            candidate_df['Unnamed: 18'])
        OverallScore = candidate_df["Unnamed: 18"].sum()

        # making dict and passing to html using jinja
        template_var = {"CandidateName": CandidateName,
                        "RegistrationNumber": RegistrationNumber,
                        "Grade": Grade,
                        "NameofSchool": NameofSchool,
                        "Gender": Gender,
                        "Address": Address,
                        "DateofBirth": DateofBirth,
                        "DateofTest": DateofTest,
                        "FinalResult": FinalResult,
                        "ScoreData": ScoreData,
                        "PossibleScore": PossibleScore,
                        "OverallScore": OverallScore}
                    
        make_candidate_pdf(template_var) # making PDF
    exit_input = input("Press any key to exit")



if __name__ == "__main__":
    main()
